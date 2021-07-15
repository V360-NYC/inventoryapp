import unittest
import requests
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
            masterFilePath = get_master_file_path(data['value']['fields']['uid']['stringValue'])
            
            assert masterFilePath is not None
    
            masterFilePath = masterFilePath.split('.')[0]+'.pickle'
            localPath = os.path.join(tempdir,'master.pickle')
            try :
                downloadFromBucket('dinsight-master-files-test',masterFilePath,localPath)
                with open(os.path.join(tempdir, 'master.pickle'),'rb') as pickleFile:
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
        
        self.data['value']['fields']['text']['stringValue'] = 'rd oval d e f'
        
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
        
        
        
if __name__ == '__main__':
    unittest.main()
        
        
