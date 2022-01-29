import unittest
# import requests
import pandas as pd
import numpy as np
import openpyxl
import pickle
import tempfile
import os
from main import parseUserQuery, db, tempdir, downloadFromBucket, get_master_file_path
import firebase_admin
from firebase_admin import credentials, firestore
from event import event, data

class TestFunctions(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.event = event
        cls.data = data
        masterFilePath = None
        try:
            # masterFilePath = get_master_file_path(data['value']['fields']['uid']['stringValue'])
            
            # assert masterFilePath is not None
    
            # masterFilePath = masterFilePath.split('.')[0]+'.pickle'
            # localPath = os.path.join(tempdir,'master.pickle')
            try :
                # downloadFromBucket('dinsight-master-files-test',masterFilePath,localPath)
                # with open(os.path.join(tempdir,'master.pickle'),'rb') as pickleFile:
                #    cls.master = pickle.load(pickleFile)
                with open('master.pickle','rb') as pickleFile:
                    cls.master = pickle.load(pickleFile)
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
    
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_1(self):
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
            
        current = self.master[
            self.master['Color'].str.lower().isin(['d','e','f']) &
            self.master['Shape'].str.lower().isin(['round', 'oval']) 
        ]
        
        self.data['value']['fields']['text']['stringValue'] = "G H I3 0.96 1.45 3282 5248"
        
        result = parseUserQuery(self.data, self.event)
        
        self.assertEqual(len(current.index), len(result.index))
        
    
    def test_2(self):
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
            
        current = self.master[
            self.master['Color'].str.lower().isin(['j','e','f']) &
            self.master['Shape'].str.lower().isin(['round', 'oval']) &
            self.master['Size'].between(0.499, 1.501)
        ]
        
        self.data['value']['fields']['text']['stringValue'] = 'rd oval j e f 0.5 1.5'
        
        result = parseUserQuery(self.data, self.event)
        
        self.assertEqual(len(current.index), len(result.index))
   
    def test_3(self):
    # For XXX rd
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
            
        current = self.master[
        self.master['Cut'].str.lower().isin(['ex']) &
        self.master['Symn'].str.lower().isin(['ex']) &
        self.master['Polish'].str.lower().isin(['ex']) &
        self.master['Shape'].str.lower().isin(['round'])
        
    ]

    def test_4(self):
        # For XXX rd
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
            
        current = self.master[
       
        self.master['Shape'].str.lower().isin(['round']) &
        self.master['Size'].between(0.5,0.5,inclusive='both')        
    ]
   
        
        self.data['value']['fields']['text']['stringValue'] = '0.5 rd'
        
        result = parseUserQuery(self.data, self.event)
        
        self.assertEqual(len(current.index), len(result.index))


    def test_5(self):
        # For xxx rd 1.0 1.1 none
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
            
        current = self.master[
       
        self.master['Fluor'].str.lower().isin(['none']) &
        self.master['Shape'].str.lower().isin(['round']) &
        self.master['Size'].between(1.0,1.1,inclusive='both') & 
        self.master['Cut'].str.lower().isin(['ex']) &
        self.master['Symn'].str.lower().isin(['ex']) &
        self.master['Polish'].str.lower().isin(['ex']) 
    ]
   
        
        self.data['value']['fields']['text']['stringValue'] = 'xxx rd 1.0 1.1 none'
        
        result = parseUserQuery(self.data, self.event)
        self.assertEqual(len(current.index), len(result.index))

    def test_6(self):
        # For  rd xxx E F 1.0
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
        print(self.master['Symn'].unique())    
        current = self.master[

        self.master['Color'].str.lower().isin(['e','f']) & 
        self.master['Shape'].str.lower().isin(['round']) &
        self.master['Size'].between(1.0,1.0,inclusive='both') & 
        self.master['Cut'].str.lower().isin(['ex']) &
        self.master['Symn'].str.lower().isin(['ex']) &
        self.master['Polish'].str.lower().isin(['ex']) 
    ]
        self.data['value']['fields']['text']['stringValue'] = 'xxx 1.0 rd e f'
        
        result = parseUserQuery(self.data, self.event)
        self.assertEqual(len(current.index), len(result.index))

    def test_7(self):
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
        print(self.master['Symn'].unique())    
        current = self.master[
        
        self.master['Fluor'].str.lower().isin(['none']) & 
        self.master['Color'].str.lower().isin(['d','h']) & 
        self.master['Shape'].str.lower().isin(['round']) &
        self.master['Size'].between(0.98,1.05,inclusive='both') & 
        self.master['Cut'].str.lower().isin(['ex']) &
        self.master['Symn'].str.lower().isin(['ex']) &
        self.master['Polish'].str.lower().isin(['ex']) 
    ]
        self.data['value']['fields']['text']['stringValue'] = 'xxx rd 0.98 1.05 D H none'
        
        result = parseUserQuery(self.data, self.event)
        self.assertEqual(len(current.index), len(result.index))

    def test_8(self):
        # For  rd xxx E F 1.0
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
        print(self.master['Symn'].unique())    
        current = self.master[
        
        self.master['Fluor'].str.lower().isin(['medium']) & 
        self.master['Color'].str.lower().isin(['i']) & 
        self.master['Shape'].str.lower().isin(['round','princess']) &
        self.master['Size'].between(0.48,0.52,inclusive='both') & 
        self.master['Cut'].str.lower().isin(['ex']) &
        self.master['Symn'].str.lower().isin(['ex']) &
        self.master['Polish'].str.lower().isin(['ex']) 
    ]
        
        self.data['value']['fields']['text']['stringValue'] = 'Round Princess xxx I 3x medium 0.48 0.52'
        
        result = parseUserQuery(self.data, self.event)
        self.assertEqual(len(current.index), len(result.index))
    def test_9(self):
        # For  rd xxx E F 1.0
        if self.master['Size'].dtype != np.float64 : 
            self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
        print(self.master['Symn'].unique())    
        current = self.master[
        self.master['Purity'].str.lower().isin(['si1']) &
        self.master['Fluor'].str.lower().isin(['medium']) & 
        self.master['Color'].str.lower().isin(['i']) & 
        self.master['Shape'].str.lower().isin(['round','princess']) &
 
        self.master['Cut'].str.lower().isin(['ex']) &
        self.master['Symn'].str.lower().isin(['ex']) &
        self.master['Polish'].str.lower().isin(['ex']) 
    ]
        
        self.data['value']['fields']['text']['stringValue'] = 'Round Princess xxx si1 I 3x medium'
        
        result = parseUserQuery(self.data, self.event)
        print(len(current.index))
        self.assertEqual(len(current.index), len(result.index))

if __name__ == '__main__':
    unittest.main()
        

# Rate US
# PURITY
# ORIGINCOUNTRY       
