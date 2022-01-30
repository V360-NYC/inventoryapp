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
from queryParsing import queryParsing
import columnMappingL as columnMapping
import json

print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

tempdir = tempfile.mkdtemp()


DEFAULTS = {
    'color' : ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'fc', 'n','d+', 'd-','e-', 'f-', 'g-', 'h-', 'h+', 'e+', 'f+', 'g+', 'i+', 'i-', 'j-','j+', 'k+', 'k-', 'm+', 'l-', 'n+'],
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

   
  
def getCondition(line):
    line = re.sub(r'\s', r':', line)
    
    filters = dict()
    
    matches = re.findall(r'[\w]+',line)
    
    for i in range(0,len(matches), 2):
      filters[matches[i]] = matches[i + 1]
    return filters
    
    
    
    

def getFilteredData(df, conditions):
    color = conditions.get('color', DEFAULTS['color'])
    shape = conditions.get('shape', DEFAULTS['shape'])
    polish = conditions.get('polish', DEFAULTS['polish'])
    cut = conditions.get('cut', DEFAULTS['cut'])
    symn = conditions.get('sym', DEFAULTS['symn'])
    cert = conditions.get('cert', DEFAULTS['cert'])
    fluor = conditions.get('fluor', DEFAULTS['fluor'])
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
        df['Size'].between(size[0], size[1])
    ]
    
    

def parseUserQuery(data, context):
    if data['value']['fields']['botReply']['booleanValue']:
        return 

    parsedResponse=queryParsing.parseUserRequest(data['value']['fields']['text']['stringValue'])
    # print(parsedResponse['parsedQuery']['entityName'], parsedResponse['parsedQuery']['entityValue'])
    
    attrs = parsedResponse['parsedQuery']['entityName']
    values = parsedResponse['parsedQuery']['entityValue']

    assert len(attrs) == len(values)

    conditions = {key:values[i] for i,key in enumerate(attrs)}
    
    if 'shape' in conditions.keys():
        conditions['shape'] = [columnMapping.getActualShape(shape).lower() for shape in conditions['shape']]
        
    if 'fluor' in conditions.keys():
        conditions['fluor'] = [columnMapping.getActualFluor(fluor).lower() for fluor in conditions['fluor']]
    if 'size' in conditions.keys():
        if len(conditions['size'])==1:
            temp=conditions['size'][0]
            conditions['size']=[temp,temp]
        else:
            men=min(conditions['size'][0],conditions['size'][1])
            mex=max(conditions['size'][0],conditions['size'][1])
            conditions['size'][0]=men
            conditions['size'][1]=mex
    if 'color' in conditions.keys():
        conditions['color'] = [columnMapping.getActualColor(color).lower() for color in conditions['color']]
    print(conditions)
    
    # conditions = extractConditions(data['value']['fields']['text']['stringValue'])

    text = '\\n'.join(['{0} = {1}'.format(key,', '.join([str(item) for item in value])) for key,value in conditions.items()])
    
    # ack = {
    #     'botReply' : True,
    #     'timeStamp' : int(time.time()*1000),
    #     'name' : 'message from system',
    #     'photoUrl' : '/images/logo.png',
    #     'text' : 'Please wait. We are fetching results for \\n{}'.format(text)
    # }
        
    # addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), ack)
    
    # masterFilePath = None
    # try:
    #     masterFilePath = get_master_file_path(data['value']['fields']['uid']['stringValue'])
    # except Exception:
    #     print("No master file to query -- main.py")
    #     # queryResult = {
    #     #     'botReply' : True,
    #     #     'timeStamp' : int(time.time()*1000),
    #     #     'name' : 'message from system',
    #     #     'photoUrl' : '/images/logo.png',
    #     #     'text' : 'No Master File to query.'
    #     # }
        
    #     # addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
    
    # assert masterFilePath is not None
    
    # masterFilePath = masterFilePath.split('.')[0]+'.pickle'
    
    # localPath = os.path.join(tempdir,'master.pickle')
    # try:
    #     downloadFromBucket('dinsight-master-files-test',masterFilePath,localPath)
    # except Exception:
    #     print("No master pickle file to query -- main.py")
        # queryResult = {
        #     'botReply' : True,
        #     'timeStamp' : int(time.time()*1000),
        #     'name' : 'message from system',
        #     'photoUrl' : '/images/logo.png',
        #     'text' : 'No Master File to query.'
        # }
        
        # addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
    
    dfTemp = None
    # with open(os.path.join(tempdir, 'master.pickle'),'rb') as pickleFile:
    #     dfTemp=pickle.load(pickleFile)
        
    with open('master.pickle','rb') as pickleFile:
        dfTemp=pickle.load(pickleFile)
        
    assert dfTemp is not None
    
    if dfTemp['Size'].dtype != np.float64:
        print('changing...')
        dfTemp['Size'] = dfTemp['Size'].apply(lambda cell : float(cell.split(' ')[0]))

    # print(1)
    result = getFilteredData(dfTemp, conditions)
    return {
        'result':result,
        'conditions':conditions

        
    }
    # print(2)
    columnNames = np.array([dfTemp.columns.tolist()])
    rows=result.iloc[:5].to_numpy()
    emptyArray=np.concatenate((columnNames,rows),axis=0)
    # print(3)
    searchResult = dict()
    
    for i in range(emptyArray.shape[0]):
        searchResult[str(i)] = emptyArray[i].tolist()
        
        
    print(result.shape)
    # queryResult = {
    #     'botReply' : True,
    #     'timeStamp' : int(time.time()*1000),
    #     'name' : 'message from system',
    #     'photoUrl' : '/images/logo.png',
    #     'searchResult': searchResult,
    #     'text' : 'This is a preview of Original Result.\n We have retrieved {} rows'.format(result.shape[0])
    # }

    # print(4)
    
    # addReplyToFirestore('chats/{}/messages'.format(data['value']['fields']['uid']['stringValue']), queryResult)
    
    # print(5)
    # print(queryResult)
    
    
        

