import unittest
import requests
from main import parseUserQuery

from event import event, data

class TestFunctions(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.event = event
        cls.data = data
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_1(self):
        self.assertEqual(1, 1)
        response = requests.post(
            'http://192.168.29.196:8080/',
            json = {
                'event' : self.event,
                'data' : self.data
            }
        )
        
        print(response.reason, response.text)
        
        
if __name__ == '__main__':
    unittest.main()
        
        
