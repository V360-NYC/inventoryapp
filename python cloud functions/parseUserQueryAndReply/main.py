import tempfile
import os
from google.cloud import storage
import pandas as pd
import openpyxl
import uuid
import firebase_admin
from datetime import datetime 
from firebase_admin import credentials, firestore
import math
import time
import fnmatch
import pickle
import tempfile
import re
import numpy as np
from queryParsing import *
from utils import *
from columnMapping import columnMapping
from quickSearch import createQSR
from pandasql import sqldf
import json

tempdir = tempfile.mkdtemp()
client = storage.Client(project="kp-assist")
cred = credentials.ApplicationDefault()

firebase_admin.initialize_app(cred,{
    'project_id':'kp-assist-4b13d9b7e9e5'
})

db = firestore.client()

DEFAULTS = {
    'color' : ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'fc', 'n', 'd-','e-', 'f-', 'g-', 'h-', 'h+', 'e+', 'f+', 'g+', 'i+', 'i-', 'j-','j+', 'k+', 'k-', 'm+', 'l-', 'n+'],
    'shape' : ['round','pear','oval','emerald','heart','princess','marquise','cushion','radiant','asscher','cushion br'],
    'polish' : ['ex', 'vg', 'g'],
    'cut' : ['ex', 'vg', 'g', '-'],
    'symn' : ['ex', 'vg', 'g'],
    'fluor': ['none', 'faint', 'medium', 'strong', 'very strong'],
    'purity' : ['if', 'vvs1', 'vvs2', 'vs1', 'vs2', 'si1', 'si2', 'i1', 'fl', 'if-', 'vvs1-', 'vvs1+', 'vvs2-', 'vvs2+', 'vs1+', 'vs1-', 'vs2-', 'vs2+', 'si1+', 'si1-', 'si2+', 'si2-'],
    'cert' : ['gia', 'gia-hk', 'gia-mum', 'gia-isr', 'gia-nyk', 'gia-lab'],
    'branch' : ['hk', 'be', 'us', 'in', 'du'],
    'size' : [0, 1e15],
    'originCountry' : ['russia', 'botswana sort', 'angola', 'mixed', 'south africa','botswana', 'canada', 'namibia', 'hke', 'muc', 'usc', 'bec', 'hkc','kol', 'b', 'a', 'h', 'duc', 'botswana star']
}

CATEGORICAL_COLUMNS = [
    'color',
    'shape',
    'polish',
    'cut',
    'symn',
    'fluor',
    'purity',
    'cert',
    'branch',
    'originCountry',
]

def get_master_file_path():
    return 'master.xlsx'

def downloadFromBucket(bucketName, path, filepath):
    bucket = client.get_bucket(bucketName)
    blob = bucket.blob(path)
    doesFileExist = blob.exists()
    
    if not doesFileExist:
      raise Exception('remote file not present')
  
    blob.download_to_filename(filepath)
    
def uploadToBucket(bucketName, path, filepath):
    bucket = client.get_bucket(bucketName)

    blob = bucket.blob(path)
    
    with open(filepath, 'rb') as file:
        blob.upload_from_file(file)

    blob.make_public()     
  
def getCondition(line):
    line = re.sub(r'\s', r':', line)
    
    filters = dict()
    
    matches = re.findall(r'[\w]+',line)
    
    for i in range(0,len(matches), 2):
      filters[matches[i]] = matches[i + 1]
    return filters    
    
def addReplyToFirestore(collectionPath, doc):
    collection_ref = db.collection(collectionPath)
    
    collection_ref.add(doc)
def updateFirestore(uidd,dc1):
      doc_ref=db.collection('lastResInfo').document(uidd)
      doc_ref.set(dc1)

def getLatestTable(uidd):
    doc_ref=db.collection('lastResInfo').document(uidd)
    return doc_ref.get().to_dict()
#suppose a=getLatestTable(uidd)
#for retriving searchResult searchResultfetched=a['searchResult']

def extractConditions(textInput):
    return json.loads(textInput)

def getFilteredData(df, conditions):
    color = conditions.get('color', DEFAULTS['color'])
    shape = conditions.get('shape', DEFAULTS['shape'])
    polish = conditions.get('polish', DEFAULTS['polish'])
    cut = conditions.get('cut', DEFAULTS['cut'])
    symn = conditions.get('sym', DEFAULTS['symn'])
    cert = conditions.get('cert', DEFAULTS['cert'])
    fluor = conditions.get('flour', DEFAULTS['fluor'])
    purity = conditions.get('clarity', DEFAULTS['purity'])
    size = conditions.get('size', DEFAULTS['size'])
   
    if df['Size'].dtype != np.float64 :
        df['Size'] = df['Size'].apply(lambda cell : float(cell.split(' ')[0]))
    
    return df[
        df['Color'].str.lower().isin(color) &
        df['Shape'].str.lower().isin(shape) &
        df['Polish'].str.lower().isin(polish) &
        df['Cut'].str.lower().isin(cut) &
        df['Symn'].str.lower().isin(symn) &
        df['Cert'].str.lower().isin(cert) &
        df['Fluor'].str.lower().isin(fluor) &
        df['Purity'].str.lower().isin(purity) &
        df['Weight'].between(size[0], size[1])
    ]   

def parseUserQuery(data, context):
    if data['value']['fields']['botReply']['booleanValue']:
        return 

    parsedResponse=parseUserRequest(data['value']['fields']['text']['stringValue'])
    # print(parsedResponse['parsedQuery']['entityName'], parsedResponse['parsedQuery']['entityValue'])
    
    if parsedResponse['queryMode'] == 'help':
        response = {
            'botReply' : True,
            'timeStamp' : int(time.time()*1000),
            'name' : 'message from system',
            'photoUrl' : '/images/logo.png',
            'text' : parsedResponse['userMessage'],
            'queryMode':'help'
        }
        #uid =data['value']['fields']['uid']['stringValue']

        addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), response)
    
    if parsedResponse['queryMode'] == 'quick-search':
        #add alll of errors lyk not finding master, giving the ack, no master, and finding the file and the pandasql query
        text = 'quick search'
        
        ack = {
            'botReply' : True,
            'timeStamp' : int(time.time()*1000),
            'name' : 'message from system',
            'photoUrl' : '/images/logo.png',
            'text' : 'Please wait. We are fetching results for \\n{}'.format(text)
        }
            
        addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), ack)
        
        masterFilePath = None
        try:
            masterFilePath = get_master_file_path()
        except Exception as e:
            print(e)
            queryResult = {
                'botReply' : True,
                'timeStamp' : int(time.time()*1000),
                'name' : 'message from system',
                'photoUrl' : '/images/logo.png',
                'text' : 'No Master File to query.'
            }
            
            addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
        
        assert masterFilePath is not None
        
        masterFilePath = masterFilePath.split('.')[0]+'.pickle'
        
        localPath = os.path.join(tempdir,'master.pickle')
        try:
            downloadFromBucket('dinsight-master-files-test',masterFilePath,localPath)
        except Exception as e:
            print(e)
            queryResult = {
                'botReply' : True,
                'timeStamp' : int(time.time()*1000),
                'name' : 'message from system',
                'photoUrl' : '/images/logo.png',
                'text' : 'No Master File to query.'
            }
            
            addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
        
        df1 = None
        with open(os.path.join(tempdir, 'master.pickle'),'rb') as pickleFile:
            df1=pickle.load(pickleFile)
            
        # with open('master.pickle','rb') as pickleFile:
        #     dfTemp=pickle.load(pickleFile)
            
        assert df1 is not None
        
        output=sqldf("SELECT Color,Purity, Round(Weight,2) Carat,cast(ROUND(Max(Total),0) as int) Max_price, cast(ROUND(Min(Total)) as int) Min_price,  Round(Avg(Total)) Avg_price, count(*) count from df1 GROUP BY Color,Purity,Carat ORDER BY Color,Purity,Carat")
        qsrAns=createQSR(output)
        #end it all here 
        response = {
            'botReply' : True,
            'timeStamp' : int(time.time()*1000),
            'name' : 'message from system',
            'photoUrl' : '/images/logo.png',
            'quickSearch' : qsrAns['quickSearchArray'],
            'stats': qsrAns['stats'],
            'queryMode':'quick-search',
            'text':''
        }
        
        addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), response)
    
    elif parsedResponse['queryMode'] == 'btQuery':
        attrs = parsedResponse['parsedQuery']['entityName']
        values = parsedResponse['parsedQuery']['entityValue']
        for i in range(len(values)):
            if type(values[i]) is not list:
                values[i] = [values[i]]
        assert len(attrs) == len(values)

        conditions = {key:values[i] for i,key in enumerate(attrs)}
        
        if 'shape' in conditions.keys():
            conditions['shape'] = [columnMapping.getActualShape_(shape).lower() for shape in conditions['shape']]
            
        if 'flour' in conditions.keys():
            conditions['flour'] = [columnMapping.getActualFlour_(flour).lower() for flour in conditions['flour']]
        if 'size' in conditions.keys():
            if len(conditions['size'])==1:
                temp=conditions['size'][0]
                conditions['size']=[temp,temp]
            else:
                men=min(conditions['size'][0],conditions['size'][1])
                mex=max(conditions['size'][0],conditions['size'][1])
                conditions['size'][0]=men
                conditions['size'][1]=mex

        print(conditions)
        
        # conditions = extractConditions(data['value']['fields']['text']['stringValue'])

        text = '\\n'.join(['{0} = {1}'.format(key,', '.join([str(item) for item in value])) for key,value in conditions.items()])
        
        ack = {
            'botReply' : True,
            'timeStamp' : int(time.time()*1000),
            'name' : 'message from system',
            'photoUrl' : '/images/logo.png',
            'text' : 'Please wait. We are fetching results for \\n{}'.format(text)
        }
            
        addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), ack)
        
        masterFilePath = None
        try:
            masterFilePath = get_master_file_path()
        except Exception as e:
            print(e)
            queryResult = {
                'botReply' : True,
                'timeStamp' : int(time.time()*1000),
                'name' : 'message from system',
                'photoUrl' : '/images/logo.png',
                'text' : 'No Master File to query.'
            }
            
            addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
        
        assert masterFilePath is not None
        
        masterFilePath = masterFilePath.split('.')[0]+'.pickle'
        
        localPath = os.path.join(tempdir,'master.pickle')
        try:
            downloadFromBucket('dinsight-master-files-test',masterFilePath,localPath)
        except Exception as e:
            print(e)
            queryResult = {
                'botReply' : True,
                'timeStamp' : int(time.time()*1000),
                'name' : 'message from system',
                'photoUrl' : '/images/logo.png',
                'text' : 'No Master File to query.'
            }
            
            addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
        
        dfTemp = None
        with open(os.path.join(tempdir, 'master.pickle'),'rb') as pickleFile:
            dfTemp=pickle.load(pickleFile)
            
        # with open('master.pickle','rb') as pickleFile:
        #     dfTemp=pickle.load(pickleFile)
            
        assert dfTemp is not None
        
        if dfTemp['Size'].dtype != np.float64:
            dfTemp['Size'] = dfTemp['Size'].apply(lambda cell : float(cell.split(' ')[0]))

        print(1)
        result = getFilteredData(dfTemp, conditions)
        # return result
        print(2)
        columnNames = np.array([dfTemp.columns.tolist()])
        cols=dfTemp.columns.tolist()
        print('columnNames',type(columnNames))
        print('cols',type(cols))
        rows=result.iloc[:100].to_numpy()
        emptyArray=np.concatenate((columnNames,rows),axis=0)
        print(3)
        searchResult = dict()
        
        for i in range(emptyArray.shape[0]):
            searchResult[str(i)] = emptyArray[i].tolist()
            
        hiddenColumnNames=[]    
        # print(result.shape)
        queryResult = {
            'botReply' : True,
            'timeStamp' : int(time.time()*1000),
            'name' : 'message from system',
            'photoUrl' : '/images/logo.png',
            'searchResult': searchResult,
            'columnNames': cols,
            'hiddenColumnNames':hiddenColumnNames,
            'text' : 'This is a preview of Original Result.\n We have retrieved {} rows'.format(result.shape[0])
        }

        print(4)
        
        addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
        updateFirestore(data['value']['fields']['uid']['stringValue'],queryResult)
        doc_temp=getLatestTable(data['value']['fields']['uid']['stringValue'])
        print(type(doc_temp['searchResult']))
        tempSR=doc_temp['searchResult']
        tempdfSR=dict2df(tempSR)
        
        print(type(tempdfSR))
        print(doc_temp['botReply'])
        # print(5)
        # print(queryResult)
        queryFilePath = os.path.join(tempdir, '{}_master.csv'.format(str(int(time.time()))))
        
        result.to_csv(queryFilePath, index = False)
        
        params=[]
        params.append(data['value']['fields']['uid']['stringValue'])
        params.append('{}_master.csv'.format(str(int(time.time()))))
        masterFilePath = '/'.join(params)
        
        uploadToBucket(
            "dinsight-master-files-test",
            masterFilePath,
            queryFilePath
        )
        
        queryFileDownloadLinkPrompt = {
            'botReply' : True,
            'timeStamp' : int(time.time()*1000),
            'name' : 'message from system',
            'photoUrl' : '/images/logo.png',
            'downloadURL' : '/'.join(['https://storage.googleapis.com','dinsight-master-files-test', masterFilePath]),
            'text' : 'To download the results for following query\\n{}\\n'.format(text),
            'fileAck' : True
        }
        
        addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryFileDownloadLinkPrompt)
    else :
        response = {
            'botReply' : True,
            'timeStamp' : int(time.time()*1000),
            'name' : 'message from system',
            'photoUrl' : '/images/logo.png',
            'searchResult': searchResult,
            'text' : 'Sorry, We are unable to understand your message. Please try again !'
        }
        addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), response)