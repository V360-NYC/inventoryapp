import tempfile
import os
from google.cloud import storage
import pandas as pd
import numpy as np
import fnmatch
import openpyxl
import time
import math
import Mapping_util as util
import firebase_admin
from firebase_admin import credentials, firestore

def exportDataFrameToExcel(dataframe, path):
    dataframe.to_excel(path)

def read_excel(filename):
    assert filename.split('.')[-1] in ['xlsx', 'xls'] ,'Not a excel file'
    return pd.concat(pd.read_excel(filename,sheet_name=None,header=None),ignore_index=True)

def isfloat(input_str):
    try:
        float(input_str)
    except ValueError:
        return False
    return True

def map(row):
    if math.isnan(row['PRICE/CTS_x']):
        return 'New'
    if row['PRICE/CTS_x'] == row['PRICE/CTS_y']:
        return 'Same'
    if row['PRICE/CTS_x'] < row['PRICE/CTS_y']:
        return 'Increase'
    if row['PRICE/CTS_x'] > row['PRICE/CTS_y']:
        return 'Decrease'
    print(row['PRICE/CTS_x'] ,row['PRICE/CTS_y'])
    return 'Error'
    
def generate_summary_file(master, inventory):
    summary = master.merge(inventory, how='right',on='REPORTNO', indicator=True)
    summary['SUMMARY'] = summary.apply(lambda row : map(row), axis = 1)
    summary = summary[[column for column in summary.columns if '_y' in column] + ['REPORTNO', 'SUMMARY']]
    summary = summary.rename(columns={column:column.replace("_y", "") for column in summary.columns})
    
    return summary

def generate_master_file(master, inventory):
    return pd.concat([master, inventory]).drop_duplicates(subset=['ReportNo'], keep = 'last')

def get_master_file_path(uid):
   pass

def mapping(filePath):
    fileValue = read_excel(filePath)
    # print(fileValue)
    fileValue_df,total_rows_skip = util.skip_to(fileValue)
    fileValue_df = pd.DataFrame(fileValue_df)
    # print(fileValue_df)
    fileValue_df=util.getActualLink(filePath,fileValue_df,total_rows_skip)
    new_heading=[]
    for heading in fileValue_df.columns:
        new_heading.append(util.getActualHeading(heading).upper())
    fileValue_df.columns=new_heading
    print("mapping col ",fileValue_df.columns)    
    new_heading=fileValue_df.columns
    print("new heading",new_heading)
    additional_column_heading_list=[]
    additional_column_list=[]

    for heading in new_heading:
        if 'ABC' in heading:
            additional_column_heading_list.append(heading)

    print("additional_column_heading_list",additional_column_heading_list)

    for index,row in fileValue_df.iterrows():
        dicti={}
        for heading in additional_column_heading_list:
            dicti[heading[:-3]]=row[heading]
        additional_column_list.append(dicti)

    fileValue_df["ADDITIONAL_COLUMN"]=additional_column_list
    print("additional_column_list",additional_column_list[:5])

    # summary=fileValue_df[column for column in summary.columns if 'abc' in column]
    fileValue_df.drop(columns=additional_column_heading_list,axis=0,inplace=True)

    # if('NOT_REQUIRED' in new_heading):
    #     fileValue_df.drop(columns="NOT_REQUIRED",axis=0,inplace=True)
    #     new_heading=fileValue_df.columns

    new_heading=fileValue_df.columns
    fileValue_df.apply(lambda x: x.astype(str).str.upper().str.strip())
    fileValue_df.replace('',np.NaN,inplace=True)
    print(fileValue_df.columns)

    for heading in new_heading: 
        if heading == "MES1" and not fileValue_df["MES1"].empty:
            if not isfloat(str(fileValue_df["MES1"][2])):
                fileValue_df["MES1"],fileValue_df["MES2"],fileValue_df["MES3"]=util.getActualMeasurement(fileValue_df["MES1"])
        fileValue_df[heading]=util.getActualValue(heading,fileValue_df[heading],filePath,total_rows_skip)
    return(fileValue_df)
    
    # fileValue_df.to_excel("Output.xlsx")

# data_df=pd.DataFrame(data)
# inventory_path='/home/github6_v360/inventoryapp/python cloud functions/columnMapping/Company-6-DISONS.xls'
# inventory_df=mapping(inventory_path)
# inventory_df.to_excel("Company6_output.xlsx")
# print("Inventory File DONE")
# master_path="/home/github6_v360/inventoryapp/python cloud functions/columnMapping/DHARM-MASTER.xlsx"
# master=mapping(master_path)
# master.to_excel("master.xlsx")
# print("Mapping File DONE")
# summary = generate_summary_file(master,inventory_df)
# summary.to_excel("summary.xlsx")
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