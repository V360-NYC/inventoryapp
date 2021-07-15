import unittest
import requests
import pandas as pd
import numpy as np
import openpyxl
import pickle
from main import parseUserQuery

from event import event, data

class TestFunctions(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.event = event
        cls.data = data
        with open('master.pickle', 'rb') as pickleFile:
            cls.master = pickle.load(pickleFile)
    
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
        
        
