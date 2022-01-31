import unittest
import util
class TestFunctions(unittest.TestCase):
    def test_getActualShape(self):
        current='RD'
        data='r'
        result=util.getActualShape(data)
        self.assertEqual(result,current)

    def test_getActualColor(self):
        current='D'
        data='D+'
        result=util.getActualColor(data)
        self.assertEqual(result,current)

    def test_getActualFluor(self):
        current='N'
        data='none'
        result=util.getActualFluor(data)
        self.assertEqual(result,current)

    def test_getActualClarity(self):
        current='I2'
        data='i2+'
        result=util.getActualClarity(data,'FL')
        self.assertEqual(result,current)

    #deafult value for all shapes other than round is VG
    def test_getActualCut(self):
        current='X'
        data='Excellent'
        result=util.getActualCut(data,'VG','RD')
        self.assertEqual(result,current)

    def test_getActualPolish(self):
        current='X'
        data='Excellent'
        result=util.getActualPolish(data,'VG')
        self.assertEqual(result,current)

    def test_getActualSym(self):
        current='X'
        data='Excellent'
        result=util.getActualSym(data,'VG')
        self.assertEqual(result,current)

    def test_get_d360_weight(self):
        current='0.23'
        data='0.10'
        result=util.get_d360_weight(data)
        self.assertEqual(result,current)
    
    def test_getActualShapeHeading(self):
        current='SHAPE'
        data='shp'
        result=util.getActualShapeHeading(data)
        self.assertEqual(result,current)

    def test_getActualColorHeading(self):
        current='COLOR'
        data='clr'
        result=util.getActualColorHeading(data)
        self.assertEqual(result,current)

    def test_getActualFluorHeading(self):
        current='FLUORESCENCE'
        data='FLUOR'
        result=util.getActualFluorHeading(data)
        self.assertEqual(result,current)

    def test_getActualClarityHeading(self):
        current='CLARITY'
        data='clr'
        result=util.getActualClarityHeading(data)
        self.assertEqual(result,current)

    #deafult value for all shapes other than round is VG
    def test_getActualCutHeading(self):
        current='CUT'
        data='cut grade'
        result=util.getActualCutHeading(data)
        self.assertEqual(result,current)

    def test_getActualPolishHeading(self):
        current='POLISH'
        data='pol'
        result=util.getActualPolishHeading(data)
        self.assertEqual(result,current)

    def test_getActualSymHeading(self):
        current='SYMMETRY'
        data='sym'
        result=util.getActualSymHeading(data)
        self.assertEqual(result,current)
if __name__ == '__main__':
    unittest.main()