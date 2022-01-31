import unittest
# import requests
import pandas as pd
import numpy as np
import openpyxl
import pickle
import tempfile
import os
from maintestcode import parseUserQuery,tempdir
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
    
    # def test_1(self):
    #     if self.master['Size'].dtype != np.float64 : 
    #         self.master['Size'] = self.master['Size'].apply(lambda cell : float(cell.split(' ')[0]))
            
    #     current = self.master[
    #         self.master['Color'].str.lower().isin(['d','e','f']) &
    #         self.master['Shape'].str.lower().isin(['round', 'oval']) 
    #     ]
        
    #     self.data['value']['fields']['text']['stringValue'] = 'rd oval d e f'
        
    #     result = parseUserQuery(self.data, self.event)
        
    #     self.assertEqual(len(current.index), len(result.index))
    
    def test_1(self):
        current={}
        current['shape']=['rd','ov']
        self.data['value']['fields']['text']['stringValue'] = 'rd oval'
        res=parseUserQuery(self.data,self.event)
        self.assertEqual(current,res['conditions'])
    def test_2(self):
        current={}
        current['shape']=['rd','ov']
        current['fluor']=['n']
        self.data['value']['fields']['text']['stringValue'] = 'rd oval NAN'
        res=parseUserQuery(self.data,self.event)
        self.assertEqual(current,res['conditions'])
    def test_3(self):
        current={}
        

        current['clarity']=['vs1']
        current['shape']=['rd','ov']
        current['fluor']=['n']
        self.data['value']['fields']['text']['stringValue'] = 'rd oval NAN VS1'
        res=parseUserQuery(self.data,self.event)
        
        a=[at for at in current['clarity']]
        b=[t for t in res['conditions']['clarity']]
        self.assertEqual(a,b)
        self.assertEqual(current['shape'],res['conditions']['shape'])
        self.assertEqual(current['fluor'],res['conditions']['fluor'])        
    def test_4(self):
        current={}
        

        current['clarity']=['vs1']
        current['shape']=['rd','ov']
        current['fluor']=['n']
        current['color']=['d']
        self.data['value']['fields']['text']['stringValue'] = 'rd oval NAN VS1 D+'
        res=parseUserQuery(self.data,self.event)
        
        a=[at for at in current['clarity']]
        b=[t for t in res['conditions']['clarity']]
        c=[at for at in current['color']]
        d=[t for t in res['conditions']['color']]
        self.assertEqual(a,b)
        self.assertEqual(current['shape'],res['conditions']['shape'])
        self.assertEqual(current['fluor'],res['conditions']['fluor'])   
        self.assertEqual(c,d)    
    def test_4(self):
        current={}
        

        current['clarity']=['vs1']
        current['shape']=['rd','ov']
        current['fluor']=['n']
        current['color']=['d']
        self.data['value']['fields']['text']['stringValue'] = 'rd oval NAN VS1 D+'
        res=parseUserQuery(self.data,self.event)
        
        a=[at for at in current['clarity']]
        b=[t for t in res['conditions']['clarity']]
        c=[at for at in current['color']]
        d=[t for t in res['conditions']['color']]
        self.assertEqual(a,b)
        self.assertEqual(current['shape'],res['conditions']['shape'])
        self.assertEqual(current['fluor'],res['conditions']['fluor'])   
        self.assertEqual(c,d)    
    def test_5(self):
        current={}
        
        current['cut']=['ex']
        current['clarity']=['vs1']
        current['shape']=['rd','ov']
        current['fluor']=['n']
        current['color']=['d']
        self.data['value']['fields']['text']['stringValue'] = 'rd oval NAN VS1 D ex'
        res=parseUserQuery(self.data,self.event)
        
        a=[at for at in current['clarity']]
        b=[t for t in res['conditions']['clarity']]
        c=[at for at in current['color']]
        d=[t for t in res['conditions']['color']]
        e=[at for at in current['cut']]
        f=[t for t in res['conditions']['cut']]
        print(res['conditions'])
        self.assertEqual(a,b)
        self.assertEqual(current['shape'],res['conditions']['shape'])
        self.assertEqual(current['fluor'],res['conditions']['fluor'])   
        self.assertEqual(c,d)  
        self.assertEqual(e,f)      
    def test_6(self):
        current={}
        current['polish']=['ex']
        current['cut']=['ex']
        current['clarity']=['vs1']
        current['shape']=['rd','ov']
        current['fluor']=['n']
        current['color']=['d']
        self.data['value']['fields']['text']['stringValue'] = 'rd oval NAN VS1 D ex ex'
        res=parseUserQuery(self.data,self.event)
        
        a=[at for at in current['clarity']]
        b=[t for t in res['conditions']['clarity']]
        c=[at for at in current['color']]
        d=[t for t in res['conditions']['color']]
        e=[at for at in current['cut']]
        f=[t for t in res['conditions']['cut']]
        g=[at for at in current['polish']]
        h=[t for t in res['conditions']['polish']]
        print(res['conditions'])
        self.assertEqual(a,b)
        self.assertEqual(current['shape'],res['conditions']['shape'])
        self.assertEqual(current['fluor'],res['conditions']['fluor'])   
        self.assertEqual(c,d)  
        self.assertEqual(e,f)
        self.assertEqual(g,h)
    def test_7(self):
        current={}
        current['polish']=['ex']
        current['cut']=['ex']
        current['clarity']=['vs1']
        current['shape']=['rd','ov']
        current['fluor']=['n']
        current['color']=['d']
        current['sym']=['ex']
        current['size']=[0.2,0.3]
        self.data['value']['fields']['text']['stringValue'] = 'rd oval NAN VS1 D 3x 0.2 0.3'
        res=parseUserQuery(self.data,self.event)
        
        a=[at for at in current['clarity']]
        b=[t for t in res['conditions']['clarity']]
        c=[at for at in current['color']]
        d=[t for t in res['conditions']['color']]
        e=[at for at in current['cut']]
        f=[t for t in res['conditions']['cut']]
        g=[at for at in current['polish']]
        h=[t for t in res['conditions']['polish']]
        i=[at for at in current['sym']]
        j=[t for t in res['conditions']['sym']]
        k=[at for at in current['size']]
        l=[t for t in res['conditions']['size']]
        print(res['conditions'])
        self.assertEqual(a,b)
        self.assertEqual(current['shape'],res['conditions']['shape'])
        self.assertEqual(current['fluor'],res['conditions']['fluor'])   
        self.assertEqual(c,d)  
        self.assertEqual(e,f)
        self.assertEqual(g,h)
        self.assertEqual(i,j)
        self.assertEqual(k,l)
            
if __name__ == '__main__':
    unittest.main()
        

# Rate US
# PURITY
# ORIGINCOUNTRY       




