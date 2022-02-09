import tempfile
import os
from google.cloud import storage
import pandas as pd
import numpy as np
import fnmatch
import openpyxl
import time
import math
import util
import firebase_admin
from firebase_admin import credentials, firestore



def exportDataFrameToExcel(dataframe, path):
    dataframe.to_excel(path)

def read_excel(filename):
    assert filename.split('.')[-1] in ['xlsx', 'xls'] ,'Not a excel file'
    return pd.read_excel(filename,engine='openpyxl')


def isfloat(input_str):
    try:
        float(input_str)
    except ValueError:
        return False
    return True

def mapping(filePath):
    fileValue = read_excel(filePath)
    fileValue_df = pd.DataFrame(fileValue)
    fileValue_df=util.skip_to(fileValue_df)
    new_heading=[]
    for heading in fileValue_df.columns:
        new_heading.append(util.getActualHeading(heading).upper())
    fileValue_df.columns=new_heading
    fileValue_df.drop(columns="NOT_REQUIRED",axis=0,inplace=True)
    new_heading=fileValue_df.columns
    fileValue_df.apply(lambda x: x.astype(str).str.upper().str.strip())
    fileValue_df.replace('',np.NaN,inplace=True)
    print(fileValue_df.columns)
    for heading in new_heading: 
        if heading == "MES1" and not isfloat(str(fileValue_df["MES1"][2])):
            fileValue_df["MES1"],fileValue_df["MES2"],fileValue_df["MES3"]=util.getActualMeasurement(fileValue_df["MES1"])
        fileValue_df[heading]=util.getActualValue(heading,fileValue_df[heading],filePath)
    fileValue_df.to_excel("Output.xlsx")

# data_df=pd.DataFrame(data)
mapping('/home/github6_v360/inventoryapp/python cloud functions/columnMapping/Copy of Company4.xlsx')
    # 

    # file = event

    # uid = file['name'].split('/')[0]
    
    # start_time = time.time()
    # downloadFromBucket(
    #     "dinsight-user-inventory-test",
    #     file['name'],
    #     os.path.join(tempdir,'inventory.xlsx')
    # )
    # print("{} inventory file download time".format(time.time() - start_time))

    # print(os.path.join(tempdir,'inventory.xlsx'))

    # start_time = time.time()
    # inventory = read_excel(os.path.join(tempdir,'inventory.xlsx'))
    # inventory = skip_to(inventory)
    # print("{} inventory read time time".format(time.time() - start_time))
    # print(inventory.head())
    
    # start_time = time.time()
    
    # masterFilePath = uid + '/master.xlsx';

    # try:
    #     downloadFromBucket(
    #         "dinsight-master-files-test",
    #         masterFilePath,
    #         os.path.join(tempdir, 'master.xlsx')
    #     )
    # except Exception:
    #     emptyMasterFile = pd.DataFrame(columns = inventory.columns)
    #     exportDataFrameToExcel(emptyMasterFile, os.path.join(tempdir, 'master.xlsx'))

    # master = read_excel(os.path.join(tempdir,'master.xlsx'))

    # reportNoIndex = next((index for index, column in enumerate(inventory.columns) if column == 'ReportNo'),None)
    # if reportNoIndex is None:
    #     raise KeyError('ReportNo not found')

    # inventory = inventory.dropna(subset = ['ReportNo'])
    # inventory['ReportNo'] = inventory['ReportNo'].astype(np.int64)

    # summary = generate_summary_file(master, inventory)
    # print("{} entire data analysis time".format(time.time() - start_time))

    # start_time = time.time()
    # exportDataFrameToExcel(summary, os.path.join(tempdir, 'summary.xlsx'))
    # summaryFilePath = uid+'/summary.xlsx'
    # uploadToBucket(
    #     "dinsight-summary-files-test",
    #     summaryFilePath,
    #     os.path.join(tempdir, 'summary.xlsx')
    # )
    # print("{} upload summary file to bucket".format(time.time() - start_time))

    # start_time = time.time()
    # newMaster = generate_master_file(master, inventory)
    # exportDataFrameToExcel(newMaster, os.path.join(tempdir, 'master.xlsx'))
    
    # uploadToBucket(
    #     "dinsight-master-files-test",
    #     masterFilePath,
    #     os.path.join(tempdir, 'master.xlsx')
    # )
    # print("{} upload new master file to bucket".format(time.time() - start_time))


    