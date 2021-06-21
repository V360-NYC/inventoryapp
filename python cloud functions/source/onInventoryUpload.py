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
    
    df=pd.read_excel(filepath,engine='openpyxl')
    print(df.head())
    
    headerIndex=0
    flag=0
    for indices,values in df.iterrows():
        for j in range(len(values)):
            if values[j]=='ReportNo':
                headerIndex=indices
                flag=1
                break
        if flag==1:
            break
     
    a=df.iloc[[headerIndex]]
    b=a.values.tolist()
    c=b[0]
    df3=df[headerIndex+1:]
    df3.columns=c
    
    df3.shape
    reportindex=df3.shape
    reportindex=0
    for i in range(len(c)):
        if c[i]=='ReportNo':
            reportindex=i
            
    emptlist=[]
    for indexs,value in df3.iterrows():
        if value[reportindex] is None:
            emptlist.append(df3.index[indexs-1])
    df3=df3.drop(emptlist)
    
    a=df3['ReportNo']
    a=a.values.tolist()

    masterFileBucket = client.get_bucket('dinsight-master-files')
    isMasterFilePresent = masterFileBucket.blob(uid+'/index.xlsx').exists()
    
    masterFilePath = uid + '/index.xlsx';
    
    if not isMasterFilePresent:
        with open(filepath, 'rb') as masterFile:
            masterFileBucket.blob(masterFilePath).upload_from_file(masterFile)
    print(isMasterFilePresent)
    
     #TODO : else generate difference between summary and invenotry file

    df2=pd.read_excel(masterFilePath,engine='openpyxl')
    reportcmntindex=0
    mastercolumns=df2.columns
    mastercolumns=mastercolumns.values.tolist()
    for i in range(len(mastercolumns)):
        if mastercolumns[i]=='ReportCmnt':
            reportcmntindex=i
    reportmasterlist=df2['ReportNo'].values.tolist()
    
    newReportSet=a
    set1={}
    set2={}

    for i in reportmasterlist:
        set1[i]=1
        
    firstSet=set1.keys()
    secondSet=set2.keys()
    
    firstSet=list(firstSet)
    secondSet=list(secondSet)
    
    df3['Total']=df3['Total'].astype('int64')
    df2['Total']=df2['Total'].astype('int64')
    
    df3['ReportNo']=df3['ReportNo'].astype('int64')
    df2['ReportNo']=df2['ReportNo'].astype('int64')
    
    df3['Weight']=df3['Weight'].astype(float)
    df2['Weight']=df2['Weight'].astype(float)
    
    df3['Rap Total']=df3['Rap Total'].astype(float)
    df2['Rap Total']=df2['Rap Total'].astype(float)
    
    df3['Mes1']=df3['Mes1'].astype(float)
    df2['Mes1']=df2['Mes1'].astype(float)
    df3['Mes2']=df3['Mes2'].astype(float)
    df2['Mes2']=df2['Mes2'].astype(float)
    df3['Mes3']=df3['Mes3'].astype(float)
    df2['Mes3']=df2['Mes3'].astype(float)
    
    df3['Table']=df3['Table'].astype(int)
    df2['Table']=df2['Table'].astype(int)
    
    df3['DepthPer']=df3['DepthPer'].astype(float)
    df2['DepthPer']=df2['DepthPer'].astype(float)
    df3['Per']=df3['Per'].astype(float)
    df2['Per']=df2['Per'].astype(float)
    df3['Price/Cts']=df3['Price/Cts'].astype('int64')
    df2['Price/Cts']=df2['Price/Cts'].astype('int64')
    
    columnlist=[]
    for i in range(len(c)):
        columnlist.append(c[i])
    columnlist.append('Summary')
    df5=pd.DataFrame(columns=columnlist)
    df5=df5.append(df3,ignore_index=True)

    df3.set_index('ReportNo', inplace = True)
    df2.set_index('ReportNo', inplace = True)
    
    df4=df2
    
    for i in range(len(df5)):
        tempobj=df5.iloc[[i]]
        indexlocsum=tempobj.index.tolist()
        indexlocsum=indexlocsum[0]
        reportindex2=df5.loc[indexlocsum]['ReportNo']
        if reportindex2 not in set1.keys():
            df5.at[indexlocsum,'Summary']='New'
            
        else:
            
            reportnoindex=df5.loc[indexlocsum]['ReportNo']
            priceold=df4.loc[reportindex]['Price/Cts']
            pricenew=df5.loc[indexlocsum]['Price/Cts']
            if priceold==pricenew:
                df5.at[indexlocsum,'Summary']='Same'
            elif priceold>pricenew:
                df5.at[indexlocsum,'Summary']='Decrease'
            elif priceold<pricenew:
                df5.at[indexlocsum,'Summary']='Increase'
            else:
                df5.at[indexlocsum,'Summary']='Error'
                
    for itr in range(len(df3)):
        emptyobja=df3.iloc[[itr]]
        emptysummaryobj=df3.iloc[[itr]]
        indexloc=emptyobja.index.tolist()
        indexloc=indexloc[0]
        emptyobja=emptyobja.values.tolist()
        emptyobja=emptyobja[0]
        emptyobj2=[]
    
        if indexloc not in set1.keys():
            for i in range(0,reportcmntindex):
                emptyobj2.append(emptyobja[i])
            emptyobj2.append('None')


            for i in range(reportcmntindex,len(emptyobja)):

                    emptyobj2.append(emptyobja[i])
            if 'Video Link' not in c:
                emptyobj2.append('None')
            if 'Cert Link' not in c:
                emptyobj2.append('NA')       
            
            
            df4.loc[indexloc]=emptyobj2
            
    df5.to_excel('master.xlsx')
    
    with open('master.xlsx', 'rb') as newMasterFile:
        masterFileBucket.blob(masterFilePath).upload_from_file(newMasterFile)
        
    
        
     

