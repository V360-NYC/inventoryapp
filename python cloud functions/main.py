import tempfile
import os
from google.cloud import storage
import pandas as pd
import numpy as np
import fnmatch
import openpyxl

tempdir = tempfile.gettempdir()

def onInventoryUpload(event, context):
    file = event
    client = storage.Client(project="dinsightmessenger")
    bucket = client.get_bucket("dinsight-user-inventory")
    
    uid = file['name'].split('/')[0]
    filepath = os.path.join(tempdir,file['name'].split('/')[-1])

    print(filepath)

    blob = bucket.get_blob(file['name'])
    blob.download_to_filename(filepath)
    
    # df=pd.read_excel(filepath,engine='openpyxl')
    # print(df.head())
     
    # a=df.iloc[[headerIndex]]
    # b=a.values.tolist()
    # c=b[0]
    # df3=df[headerIndex+1:]
    # df3.columns=c
    
    # df3.shape
    # reportindex=df3.shape
    # reportindex=0
    # for i in range(len(c)):
    #     if c[i]=='ReportNo':
    #         reportindex=i
            
    # emptlist=[]
    # for indexs,value in df3.iterrows():
    #     if value[reportindex] is None:
    #         emptlist.append(df3.index[indexs-1])
    # df3=df3.drop(emptlist)
    
    # a=df3['ReportNo']
    # a=a.values.tolist()

    masterFileBucket = client.get_bucket('dinsight-master-files')
    isMasterFilePresent = masterFileBucket.blob(uid+'/index.xlsx').exists()
    
    if not isMasterFilePresent:
        with open(filepath, 'rb') as masterFile:
            masterFileBucket.blob(uid + '/index.xlsx').upload_from_file(masterFile)
        return
    
     #TODO : else generate difference between summary and invenotry file
