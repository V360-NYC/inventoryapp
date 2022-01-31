import unittest
from queryParsing import *

def defineParsedResult(userMessage):
	parsedResult = {
            "userMessage": userMessage,
            "entityName": [],
            "entityValue": [],
            "queryMode": '',# Mode like exact match.
            "unknown": '',
            "percent": 0.0,
            "limit": 30, # Number result shown
	    }
	return parsedResult

class TestCases(unittest.TestCase):

    def test1(self):
        inp = [
            ["round", "rd", "r", "br", "rb", "rbb","Rbb"],
            ["marquise", "mr", "mq", "mar"],
            ["princess", "pr", "pc"],
            ["pear", "paer", "per", "ps"],
            ["oval", "ov"],
            ["heart", "hrt", "love"],
            ["cushion modified", "cmb", "cm"],
            ["cushion", "cus", "cu"],
            ["ashcher", "as"],
            ["radiant", "rad"],
            ["emerald", "em", "emrd"],
            [None,"abc","xyz","por"]
        ]
        for i in inp:
            for j in i:
                self.assertEqual(getActualShape(j),i[0])

    def test2(self):
        inp = [
            ["none", "non", "no", "nan"],
            ["strong", "stg"],
            ["very strong", "vst", "vstg"],
            ["medium", "med"],
            ["faint", "fnt", "faint"],
            [None,"abc","xyz"]
        ]
        for i in inp:
            for j in i:
                self.assertEqual(getActualFlour(j),i[0])

    def test3(self):
        inp = [
            ["abc","abcdef",0],
            ["raj","abcdef",-1],
            ["def",["abc","def","xyz"],1],
            ["raj",["abc","def","xyz"],-1]
        ]
        for i in inp:
           self.assertEqual(indexOf(i[1],i[0]),i[2])

    def test4(self):
        for i in QueryMode:
            self.assertEqual(setQueryMode(defineParsedResult(i))["queryMode"],QueryMode[i])

    def test5(self):
        self.assertEqual(matchAndReplace("19.28 abc",numberRegex)[1],'19.28')
        self.assertEqual(matchAndReplace("19 pt",pointerRegex)[1],'19 pt')

    def test6(self):
        self.assertEqual(parsePointer(defineParsedResult("19 ptr round"))['userMessage'],"round 0.1843 0.1957")

    def test7(self):
        self.assertEqual(replaceHotKeywordSplit_(defineParsedResult("28 quarters"), sizeKeywordValue)['userMessage'],"28 size 0.23 0.27")

    def test8(self):
        self.assertEqual(replaceHotKeyword_(defineParsedResult("28 quarters"),sizeKeywordValue)['userMessage'],"28 size 0.23 0.27")

    def test9(self):
        parsedResult = parseEntityKeyword_(defineParsedResult("shapw: rd 2800"),shapeTypo,userShape)
        self.assertEqual(parsedResult['userMessage'],"2800")
        self.assertEqual(parsedResult["entityName"],["shape"])
        self.assertEqual(parsedResult["entityValue"],[["rd"]])

    def test10(self):
        self.assertEqual(parsePercent(defineParsedResult("28.2%"))["percent"],28.2)

    def test11(self):
        self.assertEqual(parseCPSKeyword_(defineParsedResult("ct ex"),cutTypo)["userMessage"],"")

    def test12(self):
        self.assertEqual(parseNumberEntityKeyword_(defineParsedResult("sioze 0.0018k"),sizeTypo)["userMessage"],"")

    def test13(self):
        self.assertEqual(getShapeClause_(["rd"]),"(Shape = 'ROUND')")

    def test14(self):
        self.assertEqual(getReportNoClause_(["128",156]),"(reportno = '128' OR reportno = '156')")

    def test15(self):
        self.assertEqual(getSizeClause_([125]),"(Size = 125)")

    def test16(self):
        self.assertEqual(getRateClause_([125]),"(Rate_US <= 125)")
        self.assertEqual(getRateClause_([125,126]),"(Rate_US <= 126 AND Rate_US >= 125)")
        self.assertEqual(getRateClause_([125,126,127]),"(true)")

    def test17(self):
        self.assertEqual(getBackClause_([128]),"(Back > ABS(128))")

    def test18(self):
        print(parseUserRequest("D F VVS1 VVS2 0.18 0.45 354 819")) #to be improved
        #second to use G H I3 0.96 1.45 3282 5248
        self.assertEqual(parseUserRequest("remove shape"),{'columnNameArray': ['Shape'], 'queryMode': 'hide'})
        
if __name__ == "__main__":
    unittest.main()