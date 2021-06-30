import tempfile
import os
from google.cloud import storage
import pandas as pd
import numpy as np
import fnmatch
import openpyxl
import time
import math

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred,{
    'project_id':'kp-assist-4b13d9b7e9e5'
})

db = firestore.client()

tempdir = tempfile.mkdtemp()

client = storage.Client(project="dinsightmessenger")

'''
    function to upload file to cloud storage bucket
    bucketName = bucket name where file is to be uploaded,
    path = path inside the bucket
    filepath = location of the file to be uploaded 

    assuming that file to be uploaded is always .xlsx file
'''

def uploadToBucket(bucketName, path, filepath):
    bucket = client.get_bucket(bucketName)

    blob = bucket.blob(path)
    
    with open(filepath, 'rb') as file:
        blob.upload_from_file(file)


def downloadFromBucket(bucketName, path, filepath):
    bucket = client.get_bucket(bucketName)

    blob = bucket.blob(path)
    doesFileExist = blob.exists()

    if not doesFileExist:
        raise Exception('remote file not present')
    
    blob.download_to_filename(filepath)

def exportDataFrameToExcel(dataframe, path):
    dataframe.to_excel(path)

def read_excel(filename):
    assert filename.split('.')[-1] in ['xlsx', 'xls'] ,'Not a excel file'
    return pd.read_excel(filename,engine='openpyxl')

def skip_to(df):
    for index, values in df.iterrows():
        for item in values:
            if item == 'ReportNo':
                return pd.DataFrame(
                    df.iloc[index + 1 : ].to_numpy(), 
                    columns = df.iloc[index])
    raise Exception('header row not found')


def map(row):
    if math.isnan(row['Price/Cts_x']):
        return 'New'
    if row['Price/Cts_x'] == row['Price/Cts_y']:
        return 'Same'
    if row['Price/Cts_x'] < row['Price/Cts_y']:
        return 'Increase'
    if row['Price/Cts_x'] > row['Price/Cts_y']:
        return 'Decrease'
    print(row['Price/Cts_x'] ,row['Price/Cts_y'])
    return 'Error'
    
def generate_summary_file(master, inventory):
    summary = master.merge(inventory, how='right',on='ReportNo', indicator=True)
    summary['summary'] = summary.apply(lambda row : map(row), axis = 1)
    summary = summary[[column for column in summary.columns if '_y' in column] + ['ReportNo', 'summary']]
    summary = summary.rename(columns={column:column.replace("_y", "") for column in summary.columns})
    
    return summary

def generate_master_file(master, inventory):
    return pd.concat([master, inventory]).drop_duplicates(subset=['ReportNo'], keep = 'last')

def get_master_file_path(uid):
   pass

def onInventoryUpload(event, context):
    file = event

    uid = file['name'].split('/')[0]
    
    start_time = time.time()
    downloadFromBucket(
        "dinsight-user-inventory-test",
        file['name'],
        os.path.join(tempdir,'inventory.xlsx')
    )
    print("{} inventory file download time".format(time.time() - start_time))

    print(os.path.join(tempdir,'inventory.xlsx'))

    start_time = time.time()
    inventory = read_excel(os.path.join(tempdir,'inventory.xlsx'))
    inventory = skip_to(inventory)
    print("{} inventory read time time".format(time.time() - start_time))
    print(inventory.head())
    
    start_time = time.time()
    
    masterFilePath = uid + '/master.xlsx';

    try:
        downloadFromBucket(
            "dinsight-master-files-test",
            masterFilePath,
            os.path.join(tempdir, 'master.xlsx')
        )
    except Exception:
        emptyMasterFile = pd.DataFrame(columns = inventory.columns)
        exportDataFrameToExcel(emptyMasterFile, os.path.join(tempdir, 'master.xlsx'))

    master = read_excel(os.path.join(tempdir,'master.xlsx'))

    reportNoIndex = next((index for index, column in enumerate(inventory.columns) if column == 'ReportNo'),None)
    if reportNoIndex is None:
        raise KeyError('ReportNo not found')

    inventory = inventory.dropna(subset = ['ReportNo'])
    inventory['ReportNo'] = inventory['ReportNo'].astype(np.int64)

    summary = generate_summary_file(master, inventory)
    print("{} entire data analysis time".format(time.time() - start_time))

    start_time = time.time()
    exportDataFrameToExcel(summary, os.path.join(tempdir, 'summary.xlsx'))
    summaryFilePath = uid+'/summary.xlsx'
    uploadToBucket(
        "dinsight-summary-files-test",
        summaryFilePath,
        os.path.join(tempdir, 'summary.xlsx')
    )
    print("{} upload summary file to bucket".format(time.time() - start_time))

    start_time = time.time()
    newMaster = generate_master_file(master, inventory)
    exportDataFrameToExcel(newMaster, os.path.join(tempdir, 'master.xlsx'))
    
    uploadToBucket(
        "dinsight-master-files-test",
        masterFilePath,
        os.path.join(tempdir, 'master.xlsx')
    )
    print("{} upload new master file to bucket".format(time.time() - start_time))


    