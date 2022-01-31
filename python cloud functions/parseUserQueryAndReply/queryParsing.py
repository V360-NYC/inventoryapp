import re
import math

projectId = 'cloudstoragehelloworld'
labelName = 'AddedToBigQuery'
dryRun = False
datasetId2 = 'dharam_test'

companyDir = ['dharam', 'kiran', 'rk', 'srk']
dharamIndex = 0
kiranIndex = 1
rkIndex = 2
srkIndex = 3
companydatasetId = ['Dharam_Inv', 'Kiran_Inv', 'RK_Inv', 'SRK_Inv']
companyCode = ['DHM', 'KIRAN', 'RK', 'SRK']

percentRegex = r"[\+\-]?[0-9\.]+(%|p|percentage)"
percentCharRegex = r"[\+\-]?[0-9\.]+\s+(pct|percent)"
pointerRegex = r"[0-9\.]+\s+(pointers|ptr|pointer|pt|point)"
numberRegex = r"[0-9\.]+"

columnNameC = [
	'Shape', 'Size', 'Color', 'Clarity', 'Cut', 'Polish', 'Sym', 'Flour',
	'Rate_US', 'USDPerCT', 'Back'
]
hiddenColumnNameC = [
	'ReportNo', 'M1', 'M2', 'M3', 'Depth', 'Table', 'Ref', 'CertNo', 'Detail',
	'cert', 'CompanyCode'
]

# Diamond Entity Values:
# Value count = 14
colorRange = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Value count = 11
clarityRange = ['fl', 'if', 'vvs1', 'vvs2', 'vs1', 'vs2', 'si1', 'si2', 'i1', 'i2', 'i3']
# Value count 3
polishRange = ['ex', 'vg']
# Value count = 3
symRange = ['ex', 'vg']
# Value count = 3
cutRange = ['ex', 'vg']
# Value count = 5
flourRange = ['none', 'faint', 'medium', 'strong', 'very strong']
# Value count = 10
shapeRange = ["round", "marquise", "princess", "pear", "oval", "heart", "cushion modified", "cushion", "ashcher", "radiant"]
# Value count = 4
certRange = ['gia', 'hrd', 'igi', 'fm']

userShape = ["round", "rd", "r", "br", "rb", "rbb",
	"marquise", "mr", "mq", "mar",
	"princess", "pr", "pc",
	"pear", "paer", "per", "ps",
	"oval", "ov",
	"heart", "hrt", "love",
	"cushion modified", "cmb", "cm",
	"cushion", "cus", "cu",
	"ashcher", "as",
	"radiant", "rad",
	"emerald", "em", "emrd"
]
actualShape = {'round': 'round', 'rd': 'round', 'r': 'round', 'br': 'round', 'rb': 'round', 'rbb': 'round', 'marquise': 'marquise', 'mr': 'marquise', 'mq': 'marquise', 'mar': 'marquise', 'princess': 'princess', 'pr': 'princess', 'pc': 'princess', 'pear': 'pear', 'paer': 'pear', 'per': 'pear', 'ps': 'pear', 'oval': 'oval', 'ov': 'oval', 'heart': 'heart', 'hrt': 'heart', 'love': 'heart', 'cushion modified': 'cushion modified', 'cmb': 'cushion modified', 'cm': 'cushion modified', 'cushion': 'cushion', 'cus': 'cushion', 'cu': 'cushion', 'ashcher': 'ashcher', 'as': 'ashcher', 'radiant': 'radiant', 'rad': 'radiant', 'emerald': 'emerald', 'em': 'emerald', 'emrd': 'emerald'}

userFlour = ["none", "non", "no", "nan",
	"strong", "stg",
	"very strong", "vst", "vstg",
	"medium", "med",
	"faint", "fnt", "faint"
]
actualFlour = {'none': 'none', 'non': 'none', 'no': 'none', 'nan': 'none', 'strong': 'strong', 'stg': 'strong', 'very strong': 'very strong', 'vst': 'very strong', 'vstg': 'very strong', 'medium': 'medium', 'med': 'medium', 'faint': 'faint', 'fnt': 'faint'}


sizeKeyword = ['quaters', 'quater', 'quarters', 'quarter', '1/4', 'forth', '4th',
	'thirds', 'third', '1/3', '3rd',
	'3/8',
	'halfs', 'half', '1/2',
	'fifth', 'fifths', '1/5',
	'1/6',
]
sizeKeywordValue = {'quaters': 'size 0.23 0.27', 'quater': 'size 0.23 0.27', 'quarters': 'size 0.23 0.27', 'quarter': 'size 0.23 0.27', '1/4': 'size 0.23 0.27', 'forth': 'size 0.23 0.27', '4th': 'size 0.23 0.27', 'thirds': 'size 0.32 0.35', 'third': 'size 0.32 0.35', '1/3': 'size 0.32 0.35', '3rd': 'size 0.32 0.35', '3/8': 'size 0.36 0.39', 'halfs': 'size 0.48 0.52', 'half': 'size 0.48 0.52', '1/2': 'size 0.48 0.52', 'fifth': 'size 0.19 0.21', 'fifths': 'size 0.19 0.21', '1/5': 'size 0.19 0.21', '1/6': 'size 0.16 0.18'}

sizeRange = [0.01, 0.18, 0.23, 0.3, 0.37, 0.45, 0.52, 0.6, 0.66, 0.75, 0.83, 0.96, 1.1,  1.37, 1.7, 2.0, 10.0]

multiValueKeyword = ['xxx', '3x', '3ex',
	'2x', '2ex', 'xx',
	'3vg', '3vg+'
]
multiValueKeywordValue = {'xxx': 'cut ex polish ex sym ex', '3x': 'cut ex polish ex sym ex', '3ex': 'cut ex polish ex sym ex', '2x': 'cut ex polish ex', '2ex': 'cut ex polish ex', 'xx': 'cut ex polish ex', '3vg': 'cut vg polish vg sym vg', '3vg+': 'cut vg polish vg sym vg'}

priceKeyword = ['1 grand', '2 grand', '3 grand', '4 grand', '5 grand',
	'6 grand', '7 grand', '8 grand', '9 grand', '10 grand',
]
priceKeywordValue = {'1 grand': '1000', '2 grand': '2000', '3 grand': '3000', '4 grand': '4000', '5 grand': '5000', '6 grand': '6000', '7 grand': '7000', '8 grand': '8000', '9 grand': '9000', '10 grand': '10000'}

cutKeyword = ['quarter']
cutKeywordValue = ['0.23 0.25']

polishKeyword = ['quarter']
polishKeywordValue = ['0.23 0.25']

clarityKeyword = [
	'eye clean', 'eyeclean',
	'vvs', 'vs', 'si',
	'pk', 'pique'
]
clarityKeywordValue = {'eye clean': 'clarity vs1', 'eyeclean': 'clarity vs1', 'vvs': 'clarity vvs1 vvs2', 'vs': 'clarity vs2 vs1', 'si': 'clarity si1 si2', 'pk': 'i1 i2 i3', 'pique': 'i1 i2 i3'}

QueryMode = {
	# table mode
	'remove': 'hide',
	'delete': 'hide',
	'hide': 'hide',
	'add': 'show',
	'unhide': 'show',
	'show': 'show',
	'sort': 'sort',
	'order': 'sort',
	'limit': 'limit',
	'rows': 'limit',
	'rows': 'limit',
	'count': 'limit',
	'more': 'more',
	'next': 'more',
	'email': 'email',
	'mail': 'email',
	'csv': 'csv',
	'attach': 'csv',
	'attachment': 'csv',
	'image': 'image',
	'video': 'video',
	# Query Mode
	'exact': 'exact',
	'match': 'exact',
	'exat': 'exact',
	'same': 'exact',
	'specific': 'exact',
	'ditto': 'exact',
	'equal': 'exact',
	'like': 'exact',
	'qs': 'quick-search',
	'fs': 'quick-search',
	'quickSearch': 'quick-search',
	'fastSearch': 'quick-search'
}

columnName = {
	'shape': 'Shape',
	'size': 'Size',
	'color': 'Color',
	'clarity': 'Clarity',
	'cut': 'Cut',
	'polish': 'Polish',
	'sym': 'Sym',
	'flour': 'Flour',
	'm1': 'M1',
	'm2': 'M2',
	'm3': 'M3',
	'depth': 'Depth',
	'table': 'Table',
	'ref': 'Ref',
	'certno': 'CertNo',
	'detail': 'Detail',
	'cert': 'cert',
	'raprate': 'RapRate',
	'back': 'Back',
	'rate_us': 'Rate_US',
	'USDPerCT': 'USDPerCT',
	'reportno': 'ReportNo',
	'companyCode': 'CompanyCode',
}

#Typos: ***********************************************************************************************
#Typo generated using: http://tools.seobook.com/spelling/keywords-typos.cgi

sizeTypo = ['size', 'weight', 'weigh', 'wieght', 'wiegh', 'ize', 'sz', 'sioze', 'sized', 'sizse', 'sizes']
colorTypo = ['color', 'olor', 'clor', 'coor', 'colr', 'colo', 'ccolor', 'coolor', 'collor', 'coloor', 'colorr', 'oclor', 'cloor', 'coolr', 'colro']
clarityTypo = ['clarity', 'larity', 'carity', 'clrity', 'claity', 'clarty', 'clariy', 'clarit', 'cclarity', 'cllarity', 'claarity', 'clarrity', 'clariity', 'claritty', 'clarityy', 'lcarity', 'clarityrange']
cutTypo = ['cut', 'ut', 'ct', 'cu', 'ccut', 'cuut', 'cutt', 'uct', 'ctu', 'cyt']
polishTypo = ['polish']
symTypo = ['sym', 'symmetry', 'symetry', 'simmetry', 'ym', 'sm', 'sy', 'ssym', 'syym', 'symm', 'syymmetry', 'symmmetry', 'symmmetry']
flourTypo = ['flour', 'fluor', 'fluorescent', 'lour', 'four', 'flur', 'flor', 'flou', 'fflour', 'fllour', 'flpour']
depthTypo = ['depth', 'epth', 'dpth', 'deth', 'deph', 'dept', 'ddepth', 'deepth', 'ddept', 'dedpt', 'dsept', 'despt', 'deopt', 'depot', 'de0pt', 'dep0t', 'delpt', 'deplt', 'deprt', 'deptr', 'dep5t', 'dept5', 'dep6t', 'dept6', 'depyt', 'depty', 'depht', 'depth', 'depgt', 'deptg', 'depft']
tableTypo = ['table', 'able', 'tble', 'tale', 'tabe', 'tabl']
certTypo = ['cert', 'certificate', 'ert', 'ert', 'crt', 'cerrt', 'cfert', 'cefrt', 'cdert', 'cedrt', 'csert', 'cesrt', 'ceert', 'ceret', 'ce4rt', 'cer4t', 'ce5rt', 'cer5t', 'cetrt', 'certt', 'cegrt', 'cergt', 'cefrt', 'cerft', 'cedrt', 'cerdt', 'cerrt', 'certr', 'cer5t', 'cert5', 'cer6t', 'cert6', 'ceryt', 'certy', 'cerht', 'certh', 'cergt', 'certrange', 'cerft', 'certf', 'ertificate', 'crtificate', 'cetificate', 'cerificate', 'certficate', 'certiicate', 'certifcate', 'certifiate', 'certificte', 'certificae', 'certificat', 'ccertificate', 'ceertificate', 'cerrtificate', 'certtificate', 'certiificate', 'certifficate', 'certifiicate', 'certificcate', 'certificaate', 'certificatte', 'certificatee', 'ecrtificate', 'cretificate', 'cetrificate', 'ceritficate', 'certfiicate', 'certiifcate', 'certifciate', 'certifiacte', 'certifictae', 'certificaet', 'xertificate', 'dertificate', 'fertificate', 'vertificate', 'cwrtificate', 'certeficated', 'certeficatse', 'certeficates']
rapRateTypo = ['raprate', 'aprate', 'aprate', 'rprate', 'rarate', 'rapate', 'raprte', 'raprae', 'rates', 'rate']
backTypo = ['back', 'discount', 'off', '%', 'ack', 'ack', 'bck', 'bak']
rate_usTypo = ['rate_us', 'price', 'prise', 'value', 'cost', 'dollar', 'rate', 'rate us', 'raste us', 'rxate us', 'raxte us', 'rzate us', 'razte us', 'rarte us', 'ratre us', 'ra5te us', 'rat5e us', 'ra6te us', 'rat6e us', 'rayte us', 'ratye us', 'rahte us', 'rathe us', 'ragte us', 'ratge us', 'rafte us', 'ratfe us', 'ratwe us', 'ratew us', 'rat3e us', 'rate3 us', 'rat4e us', 'rate4 us', 'ratre us', 'rater us', 'ratfe us', 'ratef us', 'ratde us', 'rated us', 'ratse us', 'rates us', 'price', 'rice', 'pice', 'prce', 'prie', 'pric', 'pprice', 'dollar', 'dopllar', 'dlollar', 'dolllar', 'dkollar', 'dokllar', 'dokllar', 'dolklar', 'doollar', 'dololar', 'dopllar', 'dolplar', 'dolklar', 'dollkar', 'dololar', 'dolloar', 'dolplar', 'dollpar', 'dollqar', 'dollaqr', 'dollwar', 'dollawr', 'dollsar', 'dollasr', 'dollxar', 'dollaxr', 'dollzar', 'dollazr', 'dollaer', 'dollare', 'dolla4r', 'dollar4', 'dolla5r', 'dollar5', 'dollatr', 'dollart', 'dollagr', 'dollarg', 'dollafr', 'dollarf', 'dolladr', 'dollard', 'value', 'valued', 'valuse', 'values']
reportNoTypo = ['reportno']
shapeTypo = ["shape", "shepe", "shapw"]

#Typos: ***********************************************************************************************

helpStr = 'How To:\n\n' + \
'Search:\n You can input search string ' + \
'by specifying values of 4Cs of diamond ' + \
'you are looking for seperated by space.\n' + \
'On top of that you can also add different ' + \
'values for fluorescence, price in USD, one or more ' + \
'GIA report number.\n' + \
' Some of the example queries are:\n' + \
'"rd 6k xxx E F 1.0"\n' + \
'"si1 vs1 0.98 1.05 D H 3x none rd"\n' + \
'"Round Princess xxx  si 1/2  I 3x medium 3000 4000"\n' + \
'"I2 pk 75 pointer D H 3vg medium 2.7k"\n' + \
'Note: Each of the Diamond result shown will have parameter ' + \
'either equal or better than what you asked for in search.\n' + \
'If you looking for exact search, you can add "exact" keyword to search query.\n' + \
'Example: "exact vvs1 g h rd"\n\n' + \
'Quick-Search:\n You can also do quick search messaging "quick-search" or just "qs"\n' + \
'It will show you table with broad catagories and corresponding count for \n' + \
'each stone as well as minimum price and maximum price for that category.\n\n' + \
'Show/Hide Columns:\n On quick-search table you can click on any cell to perform corresponding search.\n' + \
'Once you get search result in table you add show/hide additional column. \n' + \
'Example: "show m1 m2 m3" (this will show additional columns with measurements for stone)\n' + \
'Similarly you can hide column by specifying column names.\n\n' + \
'Change Price:\n You just specify percentage after the search result, and it will add/decreae \n' + \
'that percent from USD rate and update the back and cost per carat column\n' + \
'Example: "5%" or "-2%"\n\n' + \
'Email:\n' + \
'Just enter any email address and it will send last search result in email.\n' + \
'Example: "sales@anikadiamond.com" \n'

def getActualShape(inputShape):
	"""
	function: it will return the actual shape based on the keyword 
			entered by the user. Eg:- rd -> round

	args:- inputShape of type string
	returns:- it's actual shape

	complexity = o(1) (previous was o(n))
	"""
	if inputShape == None:
		return None
	abc = inputShape.strip().lower()
	if abc in actualShape:
		return actualShape[abc]
	"""for j in range(len(userShape)):
		if userShape[j] == abc:
			return actualShape[j]"""
	return None

def getActualFlour(inputFlour):
	"""
	function: it will return the actual flour based on the keyword 
			entered by the user. Eg:- stg -> strong

	args:- inputFlour of type string
	returns:- it's actual flour

	complexity = o(1) (previous was o(n))
	"""
	if inputFlour == None:
		return None
	abc = inputFlour.strip().lower()
	if abc in actualFlour:
		return actualFlour[abc]
	return None

def indexOf(str1,str2):
	"""
	function: it will return 0 based index of substring from string or of elemnent from list

	args:- str1 = string/list
		   str2 = substring/sub element
	returns:- 0 based index and if it's not present will return -1

	complexity = o(n)
	"""
	if str2 not in str1:
		return -1
	return str1.index(str2)

def setQueryMode(parsedResult):
	"""
	function: it will find type of query from input and update parsedResult

	args:- A dictionary containing all attributes
	returns:- updated parsedResult

	complexity = o(n)
	"""
	userMessage = parsedResult["userMessage"]
	splitQuery = userMessage.split(" ")
	for i in QueryMode:
		idx = indexOf(splitQuery,i)
		if idx != -1:
			splitQuery[idx] = ''
			parsedResult['queryMode'] = QueryMode[i]
			userMessage = ' '.join(splitQuery)
			parsedResult['userMessage'] = userMessage
			break
	return parsedResult

def findall(string,pattern):
	"""
	function: to find all substring satisfying in given pattern

	args:- string = userMessage
		   pattern = re 
	return an array having all sub string satisfying corresponding re

	complexity = o(n)
	"""
	matches = re.finditer(pattern, string)
	x = []
	for matchNum, match in enumerate(matches, start=1):
		x.append(match.group())
	return x

def matchAndReplace(string, pattern):
	# Return array with two string.
	# 1. Str with replaced value
	# 2. Matched string
	results = findall(string,pattern)
	result = ''
	if len(results)>0:
		result = results[0].strip()
		string = string.replace(result, '')
	return [string, result]

def parsePointer(parsedResult):
	"""
	function: to replace pointerRegex and extract value from it

	args:- parsedResult is a dictionary containing all parameters

	return:- updated usermessage
	"""
	strNValue = matchAndReplace(parsedResult["userMessage"], pointerRegex)
	if strNValue[1] != '':
		#Found pointer
		#print('Value:' + strNValue[1])
		numStr = matchAndReplace(strNValue[1], numberRegex)
		if numStr[1] != '':
			try:
				ptrValue = float(numStr[1])
				if ptrValue > 0.9999:
					ptrValue = ptrValue / 100.0
				parsedResult["userMessage"] = strNValue[0] + ' ' + str(ptrValue * 0.97) + ' ' + str(ptrValue * 1.03)
				parsedResult["userMessage"] = parsedResult["userMessage"].strip()
			except:
				print("numStr is not a number")
	return parsedResult

def replaceHotKeywordSplit_(parsedResult, keywordValues):
	"""
	function: to replace keywords with keyword values

	args:- parsedResult is a dictionary containing all parameters
		   keywordValues is a dictionary containing values for specific keywords

	return:- updated usermessage
	"""
	userMessage = parsedResult["userMessage"]
	splitQuery = userMessage.split(' ')
	for i in range(len(splitQuery)):
		if splitQuery[i] in keywordValues:
			splitQuery[i] = keywordValues[splitQuery[i]]
	
	parsedResult["userMessage"] = ' '.join(splitQuery)
	return parsedResult

def parseEntityKeyword_(parsedResult, typoArray, userValues):
	"""
	function: will extract the entityName and entityValue from usermessage

	args:- typoarray is a possible yping mistake of keyboard
		   uservalue consisting of feature like shape round clarity eye clear

	return:- updated parsedResult
	"""
	userMessage = parsedResult["userMessage"]
	keywordReplace = False
	valueReplace = False
	values = []
	for i in range(len(typoArray)):
		typo = typoArray[i]
		if indexOf(userMessage,typo) != -1:
			correctSpell = typoArray[0]
			userMessage = userMessage.replace(typo + '= ',' ')
			userMessage = userMessage.replace(typo + ': ',' ')
			userMessage = userMessage.replace(typo + ' ',' ')
			userMessage = userMessage.strip()
			keywordReplace = True
			break # Assuming each entity (shape, size, color etc) will be present only with single spelling.

	returnClause = ''
	if len(userValues)>0:
		splitQuery = userMessage.split(' ')

		for j in range(len(splitQuery)):
			if splitQuery[j] in userValues:
				values.append(splitQuery[j])
				splitQuery[j] = ' '
				valueReplace = True
	
	if valueReplace:
		parsedResult["userMessage"] = ' '.join(splitQuery)
		parsedResult["userMessage"] = parsedResult["userMessage"].strip()
		parsedResult["entityName"].append(typoArray[0])
		parsedResult["entityValue"].append(values)
	return parsedResult


def parseCPSKeyword_(parsedResult, typoArray):
	"""
	function: will extract the entityName and entityValue of specific type (clarity,sut,sum) from usermessage

	args:- typoarray is a possible yping mistake of keyboard

	return:- updated parsedResult
	"""
	#print("Hello World")
	userValues = ['ex', 'vg', 'g']
	userMessage = parsedResult["userMessage"]
	valueReplace = False
	values = []

	for j in range(len(userValues)):
		for i in range(len(typoArray)):
			typo = typoArray[i]
			if indexOf(userMessage,typo + ' ' + userValues[j]) != -1:
				userMessage = userMessage.replace(typo + ' ' + userValues[j], ' ')
				userMessage = userMessage.strip()
				parsedResult["userMessage"] = userMessage
				parsedResult["entityName"].append(typoArray[0])
				parsedResult["entityValue"].append(userValues[j])
				return parsedResult

	returnClause = ''
	splitQuery = userMessage.split(' ')
	for i in range(len(userValues)):
		if valueReplace:
			break
		userValue = userValues[i]
		for j in range(len(splitQuery)):
			if userValue == splitQuery[j]:
				splitQuery[j] = ' '
				values.append(userValue)
				valueReplace = True
				break

	if valueReplace:
		parsedResult["userMessage"] = ' '.join(splitQuery)
		parsedResult["userMessage"] = parsedResult["userMessage"].strip()
		parsedResult["entityName"].append(typoArray[0])
		parsedResult["entityValue"].append(values)
	return parsedResult

def parsePercent(parsedResult):
	"""
	function: will extract the percentage value from usermessage

	args:- parsedResult a dictionary containing the required features

	return:- updated parsedResult
	"""
	strNValue = matchAndReplace(parsedResult["userMessage"], percentRegex)
	if strNValue[1] == '':
		strNValue = matchAndReplace(parsedResult["userMessage"], percentCharRegex)

	# Found percentage
	if strNValue[1] != '': 
		percentage = float(strNValue[1][0:-1])
		parsedResult["userMessage"] = strNValue[0]
		parsedResult["percent"] = percentage

	return parsedResult

def replaceHotKeyword_(parsedResult, keywordValues):
	"""
	function: to replace keywords with keyword values

	args:- parsedResult is a dictionary containing all parameters
		   keywordValues is a dictionary containing values for specific keywords

	return:- updated usermessage
	"""
	userMessage = parsedResult["userMessage"]
	#var splitQuery = userMessage.split(' ');
	for i in keywordValues:
		if indexOf(userMessage,i) != -1:
			userMessage = userMessage.replace(i, keywordValues[i])
			
	userMessage = userMessage.strip()
	parsedResult["userMessage"] = userMessage
	return parsedResult

def parseNumberEntityKeyword_(parsedResult, typoArray):
	"""
	function: to replace keywords with keyword values

	args:- parsedResult is a dictionary containing all parameters
		   typoarray is a possible yping mistake of keyboard

	return:- updated usermessage
	"""
	userMessage = re.sub(r"\s+"," ",parsedResult["userMessage"])
	keywordReplace = False
	valueReplace = False
	values = []

	splituserMessage = userMessage.split(' ')
	for i in range(len(splituserMessage)):
		strQuery = splituserMessage[i]
		process = re.sub(r"[^0-9\.]+","",strQuery)
		if process == "":
			continue
		parsedNumber = float(process)
		strNum = process + ''
		strNumK = process + 'k'
		strNumZeroK = process + '0k'

		# If number is 0
		if parsedNumber < 0.0001 and parsedNumber > -0.0001:
			continue
		if strQuery == strNumK:
			parsedNumber = parsedNumber * 1000
			userMessage = userMessage.replace("k","")
		elif strQuery == strNumZeroK:
			userMessage = userMessage.replace("0k","")
			parsedNumber = parsedNumber * 1000
		elif strQuery == strNum or strQuery == (strNum + '0') or ('0' + strQuery) == strNum or strQuery == (strNum + '.0') or strQuery == (strNum + '.00'):
			print("to handle decimal number case like 1.0")
			# Do nothing
		else:
			continue

		if typoArray[0] == 'size' and parsedNumber < 15:
			# Assume it is weight
			userMessage = userMessage.replace(strNum, ' ')
			values.append(parsedNumber)
			valueReplace = True

		if typoArray[0] == 'back' and parsedNumber > 15 and parsedNumber < 80:
			#Assume it is back discount
			userMessage = userMessage.replace(strNum, ' ')
			values.append(parsedNumber)
			valueReplace = True

		if typoArray[0] == 'rate_us' and parsedNumber > 200 and parsedNumber < 900000:
			#Assumme it is price
			userMessage = userMessage.replace(strNum, ' ')
			userMessage = userMessage.replace(strNumK, ' ')
			userMessage = userMessage.replace(strNumZeroK, ' ')
			if parsedNumber > 250:
				# Temporary fix for phone number issue
				values.append(parsedNumber)
				valueReplace = True

		if typoArray[0] == 'reportno' and parsedNumber > 100000000 and parsedNumber < 10000000000:
			userMessage = userMessage.replace(strNum, ' ')
			values.append(parsedNumber)
			valueReplace = True
		
		else:
			# Unknown, Cannot parse query, we should log it
			parsedResult["unknown"] = parsedResult["unknown"]+' '+str(parsedNumber)

	if valueReplace:
		for i in range(len(typoArray)):
			typo = typoArray[i]
			if indexOf(userMessage,typo) != -1:
				userMessage = userMessage.replace(typo + ' ', ' ')
				keywordReplace = True
				break # Assuming each entity (shape, size, color etc) will be present only with single spelling.
		userMessage = userMessage.strip()
		parsedResult["userMessage"] = userMessage
		parsedResult["entityName"].append(typoArray[0])
		parsedResult["entityValue"].append(values)
	return parsedResult

RESULT_COUNT = 30
# Parsing the free form query and returning the clause in form "weight = 1.49 1.51"
# or "clarity = VS1" or "cut = ex"
# We still do not parse Depth, Table, and RapRate.
def queryParser_(userMessage):
	parsedResult = {
		"userMessage": userMessage,
		"entityName": [],
		"entityValue": [],
		"queryMode": '',# Mode like exact match.
		"unknown": '',
		"percent": 0.0,
		"limit": RESULT_COUNT, # Number result shown
	}

	print('0th parse query is:' + parsedResult["userMessage"])
	parsedResult = setQueryMode(parsedResult)

	"""switch (parsedResult.queryMode) {
		case 'hide':
			// parse column shown
			break;
		case 'show':
			// show missing column
			break;
		case 'email':
			// find all the shown column to send in email.
			break;
		case 'pdf':
			// Similar to email mode and need to create PDF from HTMl for download.
		case 'image':
			// Need to check if the impage URL is present for the report ID or row number.
			break;
		case 'video':
			// Need to check if the video URL is present for the report ID or row number.
			break;
		case 'quick-search':
			// Need to see what was the user's preference or parse the quick searh query.
			break;
		case 'exact':
			// Exact params to be evaluated.
			break;
		case 'contact':
			// Show contact detail for diamond.
		default:
	}"""

	parsedResult = parsePointer(parsedResult)
	"""parsedResult = replaceHotKeyword_(parsedResult, sizeKeywordValue)
	parsedResult = replaceHotKeyword_(parsedResult, multiValueKeywordValue)
	parsedResult = replaceHotKeyword_(parsedResult, priceKeywordValue)
	parsedResult = replaceHotKeyword_(parsedResult, clarityKeywordValue)"""

	print('1st parse query is: ' + parsedResult["userMessage"])

	parsedResult = replaceHotKeywordSplit_(parsedResult, sizeKeywordValue)
	parsedResult = replaceHotKeywordSplit_(parsedResult, multiValueKeywordValue)
	parsedResult = replaceHotKeywordSplit_(parsedResult, priceKeywordValue)
	parsedResult = replaceHotKeywordSplit_(parsedResult, clarityKeywordValue)

	print('2nd parse query is:' + parsedResult["userMessage"])

	# Replacing email clause by different the new line characters.
	# Then replacing all the non (character, equal, number, decimanl point, colon, dash, space) by space.
	parsedResult['userMessage'] = re.sub(r'(?:\r\n|\r|\n|<br>)', ' ',parsedResult['userMessage'])
	parsedResult['userMessage'] = re.sub(r'\s\s+', ' ',parsedResult['userMessage'])
	parsedResult['userMessage'] = re.sub(r'[^a-zA-Z\.0-9\-+%\\ ]', ' ',parsedResult['userMessage'])
	parsedResult['userMessage'] = re.sub(r'\s\s+', ' ',parsedResult['userMessage'])

	print('3rd parse query is:' + parsedResult["userMessage"])
	parsedResult = parseEntityKeyword_(parsedResult, shapeTypo, userShape) # TODO: Need to convert user shape to actual shape
	parsedResult = parseEntityKeyword_(parsedResult, clarityTypo, clarityRange)
	parsedResult = parseEntityKeyword_(parsedResult, flourTypo, userFlour)
	parsedResult = parseEntityKeyword_(parsedResult, certTypo, certRange)
	parsedResult = parseEntityKeyword_(parsedResult, colorTypo, colorRange)

	print('4th parse query is:' + parsedResult["userMessage"])


	# Here order (cut. polish and sym is important)
	#to be edited from here
	parsedResult = parseCPSKeyword_(parsedResult, cutTypo)
	parsedResult = parseCPSKeyword_(parsedResult, polishTypo)
	parsedResult = parseCPSKeyword_(parsedResult, symTypo)

	print('5th parse query is:' + parsedResult["userMessage"])
	parsedResult = parsePercent(parsedResult)
	print('6th parse query is:' + parsedResult["userMessage"])
	parsedResult = parseNumberEntityKeyword_(parsedResult, sizeTypo)
	parsedResult = parseNumberEntityKeyword_(parsedResult, rate_usTypo)
	parsedResult = parseNumberEntityKeyword_(parsedResult, backTypo)
	parsedResult = parseNumberEntityKeyword_(parsedResult, reportNoTypo)

	print('7th parse query is:' + parsedResult["userMessage"])
	return parsedResult

def createSimpleQuery_(whereClause, parsedQuery):
	#parsedQuery //  (todo:kalpesh) change to add value to rate_us
	rateMultiplier = str(1.0 + parsedQuery["percent"] / 100)
	limit = str(parsedQuery["limit"])
	parsedQuery["columnName"] = columnNameC
	parsedQuery["hiddenColumnName"] = hiddenColumnNameC
	#https://stackoverflow.com/questions/18905842/oops-used-a-reserved-word-to-name-a-column
	btQueryStr = 'SELECT ' + \
	'Shape, ' + \
	'Size,  ' + \
	'Color, ' + \
	'Clarity, ' + \
	'Cut, ' + \
	'Polish, ' + \
	'Sym, ' + \
	'Flour, ' + \
	'ROUND(Rate_US*' + rateMultiplier + ') Rate_US, ' + \
	'ROUND((Rate_US*' + rateMultiplier + ')/Size)  USDPerCT, ' + \
	'SUBSTR(STRING(100 - ' + rateMultiplier + '*(100 - Back)),0, 5) Back, ' + \
	'ReportNo, ' + \
	'M1, ' + \
	'M2, ' + \
	'M3, ' + \
	'Depth, ' + \
	'[Table], ' + \
	'Ref, ' + \
	'CertNo, ' + \
	'Detail, ' + \
	'cert, ' + \
	'CompanyCode ' + \
	'FROM Diamond_Inv.latest ' + \
	' WHERE Rate_US != 0 AND ' + \
	' AND \n'.join(whereClause) + \
	' ORDER BY USDPerCT ' + \
	'LIMIT ' + limit

	btQuery = {"query": btQueryStr}
	return btQuery

def parseUserRequest(userRequest):
	userRequest = userRequest.lower()
	userRequest = re.sub(r'\s\s+', ' ',userRequest)
	userRequest = userRequest.strip()

	if userRequest == 'help':
		return {
			"userMessage" : helpStr,
			"queryMode" : 'help'
		}

	if userRequest == 'cache':
		return {
			"userMessage" : 'cache object is',
			"queryMode" : 'cache'
		}

	if userRequest == 'quick search' or userRequest == 'fast search' or userRequest == 'quick-search' or userRequest == 'fast-search' or userRequest == 'qs' or userRequest == 'fs':
		return {
			"queryMode" : 'quick-search'
		}

	if indexOf(userRequest,"hide") != -1 or indexOf(userRequest,"remove") != -1 or indexOf(userRequest,"delete") != -1 or indexOf(userRequest,"show") != -1 or indexOf(userRequest,"add") != -1 or indexOf(userRequest,"unhide") != -1:
		columnNames = []
		splittedUserRequest = userRequest.split(' ')
		for i in range(len(columnNameC)):
			if indexOf(splittedUserRequest,columnNameC[i].lower()) != -1:
				columnNames.append(columnNameC[i])

		for i in range(len(hiddenColumnNameC)):
			if indexOf(splittedUserRequest,hiddenColumnNameC[i].lower()) != -1:
				columnNames.append(hiddenColumnNameC[i])

		if indexOf(userRequest,"show") != -1 or indexOf(userRequest,"add") != -1 or indexOf(userRequest,"unhide") != -1:
			return{"columnNameArray": columnNames,"queryMode": 'show'}
		else:
			return {
				"columnNameArray": columnNames,
				"queryMode": 'hide'
			}

	

	#parsedQuery is object with three fields.
	#1. userMessage (string query)
	#2. entityName array.
	#3. entityValue array. It is an 2D array.

	parsedQuery = queryParser_(userRequest)
	if len(parsedQuery["entityName"]) == 0:
		p = re.compile(r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)", re.IGNORECASE)
		emailAddr = findall(p,userRequest)
		if indexOf(userRequest,'mail') != -1 or len(emailAddr)>0:
			userMessage = ''
			if emailAddr[0] == '':
				userMessage = 'Please provide valid email ID'
			return {
			 "email": emailAddr[0],
			 "userMessage": userMessage,
			 "queryMode": 'email'
		 	}

		if parsedQuery["percent"]>0.0:
			#Add only dollar value for const addition
			return {
			 "percent": parsedQuery["percent"],
			 "constUsd": 0,
			 "queryMode": 'changeRate'
			}

		return {
			"userMessage": 'Your Query is invalid, message/search "help" for usage instructions.',
			"queryMode": 'help'
		}


	whereClause = createWhereClause_(parsedQuery)
	simpleQuery = createSimpleQuery_(whereClause, parsedQuery)
	return {
	"condition": parseQueryToText(parsedQuery),
	"parsedQuery": parsedQuery,
	"query": simpleQuery["query"],
	"queryMode": 'btQuery'
	}

def testcreateWhereClause_(userMessage):
	whereClause = createWhereClause_(queryParser_(userMessage))

#****************************************************************WHERE CLAUSE*****************************************


# createWhereClause_ create the big query from email query.
# parsedQuery is object with three fields.
# 1. userMessage (string query)
# 2. entityName array.
# 3. entityValue array. It is an 2D array.
def createWhereClause_(parsedQuery):
	whereClause = []
	exactMode = False
	if parsedQuery["queryMode"] == 'exact':
		exactMode = True

	for i in range(len(parsedQuery["entityName"])):
		entityName = parsedQuery["entityName"][i]
		if entityName == "color":
			clause = getRangeClause_('color', parsedQuery["entityValue"][i], colorRange, exactMode)
			whereClause.append(clause)
		elif entityName == 'clarity':
			clause = getRangeClause_('clarity', parsedQuery["entityValue"][i], clarityRange, exactMode)
			whereClause.append(clause)
		elif entityName == 'polish':
			clause = getRangeClause_('polish', parsedQuery["entityValue"][i], polishRange, exactMode)
			whereClause.append(clause)
		elif entityName == 'sym':
			clause = getRangeClause_('sym', parsedQuery["entityValue"][i], symRange, exactMode)
			whereClause.append(clause)
		elif entityName == 'cut':
			clause = getRangeClause_('cut', parsedQuery["entityValue"][i], cutRange, exactMode)
			whereClause.append(clause)
		elif entityName == 'flour':
			clause = getRangeClause_('flour', parsedQuery["entityValue"][i], flourRange, exactMode)
			whereClause.append(clause)
		elif entityName == 'size':
			clause = getSizeClause_(parsedQuery["entityValue"][i])
			whereClause.append(clause)
		elif entityName == 'shape':
			clause = getShapeClause_(parsedQuery["entityValue"][i])
			whereClause.append(clause)
		elif entityName == 'rate_us':
			clause = getRateClause_(parsedQuery["entityValue"][i])
			whereClause.append(clause)
		elif entityName == 'back':
			clause = getBackClause_(parsedQuery["entityValue"][i])
			whereClause.append(clause)
		elif entityName == 'reportno':
			clause = getReportNoClause_(parsedQuery["entityValue"][i])
			whereClause.append(clause)
		else:
			print("createWhereClause_ => entityName loop default condition")

	return whereClause

# property examples are color, cut, clarity, etc
# valueArray = ['F', 'H']
# range = ['D', 'E', .... , 'Z']
def getRangeClause_(prop, valueArray, ran, exactMode):
	betterRange = -1
	lowerRange = -1

	for j in range(len(valueArray)):
		for k in range(len(ran)):
			if valueArray[j] == ran[k]:
				if betterRange == -1:
					betterRange = k
				else:
					lowerRange = k

	if betterRange != -1:
		retStr = []
		if lowerRange == -1:
			if exactMode:
				retStr.append(prop + ' = \'' + ran[betterRange].upper() + '\'')
			else:
				for k in range(betterRange):
					retStr.append(prop + ' = \'' + ran[k].upper() + '\'')

		else:
			for k in range(betterRange,lowerRange+1):
				retStr.append(prop + ' = \'' + ran[k].upper() + '\'')

		return "(" + ' OR '.join(retStr) + ") "

	return '(true)'

def getShapeClause_(valueArray):
	"""
	function: to convert the entityValue array into sql query

	args:- valueArray is the list containing value of specific feature

	return:- generated or query 
	"""
	if len(valueArray) > 0:
		retStr = []
		for i in range(len(valueArray)):
			actualShape = getActualShape(str(valueArray[i]))
			if actualShape is not None:
				retStr.append('Shape = \'' + actualShape.upper() + '\'')
		return '(' + ' OR '.join(retStr) + ')'
	return '(true)'

def getReportNoClause_(valueArray):
	"""
	function: to convert the entityValue array into sql query

	args:- valueArray is the list containing value of specific feature

	return:- generated or query 
	"""
	if len(valueArray) > 0:
		retStr = []
		for i in range(len(valueArray)):
			retStr.append('reportno = \'' + str(valueArray[i]) + '\'')
		return '(' + ' OR '.join(retStr) + ')'
	return '(true)'

def validDecimal_(value):
	try:
		num = float(value)
		return not math.isnan(num)
	except:
		return False

# Add keyword like quater, 3rd's, halfs,
def getSizeClause_(valueArray):
	"""
	function: to convert the entityValue array into sql query

	args:- valueArray is the list containing value of specific feature

	return:- generated or query 
	"""
	firstSize = -1.0
	secondSize = -1.0

	for j in range(len(valueArray)):
		if validDecimal_(valueArray[j]):
			if firstSize < 0.0:
				firstSize = valueArray[j]
			else:
				secondSize = valueArray[j]
	if firstSize > 0.0:
		#First value is initialize
		if secondSize < 0.0:
			#If second value is not initialize then it should single value.
			return '(Size = ' + str(firstSize) + ')'
		else:
			#If both values are initialize then it range.
			if firstSize > secondSize:
				return '( Size < ' + str(firstSize) + ' AND size > ' + str(secondSize) + ')'
			else:
				return ' (Size < ' + str(secondSize) + ' AND size > ' + str(firstSize) + ')'
	return None

# For keyword like ['price','prise','value','cost','dollar','rate','$','dollar',]
def getRateClause_(valueArray):
	"""
	function: to convert the entityValue array into sql query

	args:- valueArray is the list containing value of specific feature

	return:- generated or query 
	"""
	if len(valueArray) == 1:
		return '(Rate_US <= ' + str(valueArray[0]) + ')'
	elif len(valueArray) == 2:
		firstSize = valueArray[0]
		secondSize = valueArray[1]
		if firstSize > secondSize:
			return '(Rate_US <= ' + str(firstSize) + ' AND Rate_US >= ' + str(secondSize) + ')'
		else:
			return '(Rate_US <= ' + str(secondSize) + ' AND Rate_US >= ' + str(firstSize) + ')'
	else:
		return '(true)'

# backTypo: ['back','discount','off','%',]
def getBackClause_(valueArray):
	"""
	function: to convert the entityValue array into sql query

	args:- valueArray is the list containing value of specific feature

	return:- generated or query 
	"""
	firstSize = -1.0
	secondSize = -1.0
	for j in range(len(valueArray)):
		if validDecimal_(valueArray[j]):
			if firstSize < 0.0:
				firstSize = valueArray[j]
			else:
				secondSize = valueArray[j]

	if firstSize > 0.0:
		# First value is initialize
		if secondSize < 0.0:
			#If second value is not initialize then it should single value.
			return '(Back > ABS(' + str(firstSize) + '))'
		else:
			# If both values are initialize then it range.
			if firstSize > secondSize:
				return '(Back < ABS(' + str(firstSize) + ') AND Back > ABS(' + str(secondSize) + '))'
			else:
				return '(Back < ABS(' + str(secondSize) + ') AND Back > ABS(' + str(firstSize) + '))'
	return None

#****************************************************************WHERE CLAUSE*****************************************

# Function used for testing query parsing
def parseQueryToText(parsedResult):
	parsedQuery = ''
	for i in range(len(parsedResult["entityName"])):
		entityValue = parsedResult["entityValue"][i]
		entityValueStr = ''
		if len(entityValue) > 0:
			for j in range(len(entityValue)):
				entityValueStr = entityValueStr + str(entityValue[j]) + ' '
			parsedQuery += "\n" + parsedResult["entityName"][i] + " = " + entityValueStr + '\t'
	return parsedQuery
	