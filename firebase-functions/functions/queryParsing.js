// Replace this value with the project ID listed in the Google
// Developers Console project.
const projectId = 'cloudstoragehelloworld';

// GLOBALS
// Name of the label which will be applied after processing the mail message
const labelName = 'AddedToBigQuery';
const dryRun = false;
const datasetId2 = 'dharam_test';

const companyDir = ['dharam', 'kiran', 'rk', 'srk'];
const dharamIndex = 0;
const kiranIndex = 1;
const rkIndex = 2;
const srkIndex = 3;
const companydatasetId = ['Dharam_Inv', 'Kiran_Inv', 'RK_Inv', 'SRK_Inv'];
const companyCode = ['DHM', 'KIRAN', 'RK', 'SRK'];

const percentRegex = /[\+\-]?[0-9\.]+(%|p)/g;
const percentCharRegex = /[\+\-]?[0-9\.]+\s+(pct|percent)/g;
const pointerRegex = /[0-9\.]+\s+(pointers|ptr|pointer|pt|point)/g;
const numberRegex = /[0-9\.]+/g;

const columnNameC = [
	'Shape', 'Size', 'Color', 'Clarity', 'Cut', 'Polish', 'Sym', 'Flour',
	'Rate_US', 'USDPerCT', 'Back'
];
const hiddenColumnNameC = [
	'ReportNo', 'M1', 'M2', 'M3', 'Depth', 'Table', 'Ref', 'CertNo', 'Detail',
	'cert', 'CompanyCode'
];

// Diamond Entity Values:
// Value count = 14
const colorRange = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']; //, 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
// Value count = 11
const clarityRange = ['fl', 'if', 'vvs1', 'vvs2', 'vs1', 'vs2', 'si1', 'si2', 'i1', 'i2', 'i3'];
// Value count 3
const polishRange = ['ex', 'vg'];
// Value count = 3
const symRange = ['ex', 'vg'];
// Value count = 3
const cutRange = ['ex', 'vg'];
// Value count = 5
const flourRange = ['none', 'faint', 'medium', 'strong', 'very strong'];
// Value count = 10
const shapeRange = ["round", "marquise", "princess", "pear", "oval", "heart", "cushion modified", "cushion", "ashcher", "radiant"];
// Value count = 4
const certRange = ['gia', 'hrd', 'igi', 'fm'];

const userShape = ["round", "rd", "r", "br", "rb", "rbb",
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
];
const actualShape = ["round", "round", "round", "round", "round", "round",
	"marquise", "marquise", "marquise", "marquise",
	"princess", "princess", "princess",
	"pear", "pear", "pear", "pear",
	"oval", "oval",
	"heart", "heart", "heart",
	"cushion modified", "cushion modified", "cushion modified",
	"cushion", "cushion", "cushion",
	"ashcher", "ashcher",
	"radiant", "radiant",
	"emerald", "emerald", "emerald"
];

const userFlour = ["none", "non", "no", "nan",
	"strong", "stg",
	"very strong", "vst", "vstg",
	"medium", "med",
	"faint", "fnt", "faint"
];
const actualFlour = ["none", "none", "none", "none", "none",
	"strong", "strong",
	"very strong", "very strong", "very strong",
	"medium", "medium",
	"faint", "faint", "faint"
];


const sizeKeyword = ['quaters', 'quater', 'quarters', 'quarter', '1/4', 'forth', '4th',
	'thirds', 'third', '1/3', '3rd',
	'3/8',
	'halfs', 'half', '1/2',
	'fifth', 'fifths', '1/5',
	'1/6',
];
const sizeKeywordValue = ['size 0.23 0.27', 'size 0.23 0.27', 'size 0.23 0.27', 'size 0.23 0.27', 'size 0.23 0.27', 'size 0.23 0.27', 'size 0.23 0.27',
	'size 0.32 0.35', 'size 0.32 0.35', 'size 0.32 0.35', 'size 0.32 0.35',
	'size 0.36 0.39',
	'size 0.48 0.52', 'size 0.48 0.52', 'size 0.48 0.52',
	'size 0.19 0.21', 'size 0.19 0.21', 'size 0.19 0.21',
	'size 0.16 0.18',
];

const sizeRange = [0.01, 0.18, 0.23, 0.3, 0.37, 0.45, 0.52, 0.6, 0.66, 0.75, 0.83, 0.96, 1.1,  1.37, 1.7, 2.0, 10.0];

const multiValueKeyword = ['xxx', '3x', '3ex',
	'2x', '2ex', 'xx',
	'3vg', '3vg+'
];
const multiValueKeywordValue = ['cut ex polish ex sym ex', 'cut ex polish ex sym ex', 'cut ex polish ex sym ex',
	'cut ex polish ex', 'cut ex polish ex', 'cut ex polish ex',
	'cut vg polish vg sym vg', 'cut vg polish vg sym vg'
];

const priceKeyword = ['1 grand', '2 grand', '3 grand', '4 grand', '5 grand',
	'6 grand', '7 grand', '8 grand', '9 grand', '10 grand',
];
const priceKeywordValue = ['1000', '2000', '3000', '4000', '5000',
	'6000', '7000', '8000', '9000', '10000'
];

const cutKeyword = ['quarter'];
const cutKeywordValue = ['0.23 0.25'];

const polishKeyword = ['quarter'];
const polishKeywordValue = ['0.23 0.25'];

const clarityKeyword = [
	'eye clean', 'eyeclean',
	'vvs', 'vs', 'si',
	'pk', 'pique'
];
const clarityKeywordValue = [
	'clarity vs1', 'clarity vs1',
	'clarity vvs1 vvs2', 'clarity vs2 vs1', 'clarity si1 si2',
	'i1 i2 i3', 'i1 i2 i3'
];

const QueryMode = {
	// table mode
	remove: 'hide',
	delete: 'hide',
	hide: 'hide',
	add: 'show',
	unhide: 'show',
	show: 'show',
	sort: 'sort',
	order: 'sort',
	limit: 'limit',
	rows: 'limit',
	rows: 'limit',
	count: 'limit',
	more: 'more',
	next: 'more',
	email: 'email',
	mail: 'email',
	csv: 'csv',
	attach: 'csv',
	attachment: 'csv',
	image: 'image',
	video: 'video',
	// Query Mode
	exact: 'exact',
	match: 'exact',
	exat: 'exact',
	same: 'exact',
	specific: 'exact',
	ditto: 'exact',
	equal: 'exact',
	like: 'exact',
	qs: 'quick-search',
	fs: 'quick-search',
	quickSearch: 'quick-search',
	fastSearch: 'quick-search'
};

const columnName = {
	shape: 'Shape',
	size: 'Size',
	color: 'Color',
	clarity: 'Clarity',
	cut: 'Cut',
	polish: 'Polish',
	sym: 'Sym',
	flour: 'Flour',
	m1: 'M1',
	m2: 'M2',
	m3: 'M3',
	depth: 'Depth',
	table: 'Table',
	ref: 'Ref',
	certno: 'CertNo',
	detail: 'Detail',
	cert: 'cert',
	raprate: 'RapRate',
	back: 'Back',
	rate_us: 'Rate_US',
	USDPerCT: 'USDPerCT',
	reportno: 'ReportNo',
	companyCode: 'CompanyCode',
};

const getActualShape = function(inputShape) {
	for (var j = 0; j < userShape.length; j++) {
		if ( userShape[j] == inputShape.trim()) {
			return  actualShape[j];
		}
	}
	return null;
};

const getActualFlour = function(inputFlour) {
	for (var j = 0; j <  userFlour.length; j++) {
		if ( userFlour[j] == inputFlour.trim()) {
			return actualFlour[j];
		}
	}
	return null;
};



// Typos: ***********************************************************************************************
// Typo generated using: http://tools.seobook.com/spelling/keywords-typos.cgi

const sizeTypo = ['size', 'weight', 'weigh', 'wieght', 'wiegh', 'ize', 'sz', 'sioze', 'sized', 'sizse', 'sizes'];
const colorTypo = ['color', 'olor', 'clor', 'coor', 'colr', 'colo', 'ccolor', 'coolor', 'collor', 'coloor', 'colorr', 'oclor', 'cloor', 'coolr', 'colro'];
const clarityTypo = ['clarity', 'larity', 'carity', 'clrity', 'claity', 'clarty', 'clariy', 'clarit', 'cclarity', 'cllarity', 'claarity', 'clarrity', 'clariity', 'claritty', 'clarityy', 'lcarity', 'clarityrange'];
const cutTypo = ['cut', 'ut', 'ct', 'cu', 'ccut', 'cuut', 'cutt', 'uct', 'ctu', 'cyt'];
const polishTypo = ['polish'];
const symTypo = ['sym', 'symmetry', 'symetry', 'simmetry', 'ym', 'sm', 'sy', 'ssym', 'syym', 'symm', 'syymmetry', 'symmmetry', 'symmmetry'];
const flourTypo = ['flour', 'fluor', 'fluorescent', 'lour', 'four', 'flur', 'flor', 'flou', 'fflour', 'fllour', 'flpour'];
const depthTypo = ['depth', 'epth', 'dpth', 'deth', 'deph', 'dept', 'ddepth', 'deepth', 'ddept', 'dedpt', 'dsept', 'despt', 'deopt', 'depot', 'de0pt', 'dep0t', 'delpt', 'deplt', 'deprt', 'deptr', 'dep5t', 'dept5', 'dep6t', 'dept6', 'depyt', 'depty', 'depht', 'depth', 'depgt', 'deptg', 'depft'];
const tableTypo = ['table', 'able', 'tble', 'tale', 'tabe', 'tabl'];
const certTypo = ['cert', 'certificate', 'ert', 'ert', 'crt', 'cerrt', 'cfert', 'cefrt', 'cdert', 'cedrt', 'csert', 'cesrt', 'ceert', 'ceret', 'ce4rt', 'cer4t', 'ce5rt', 'cer5t', 'cetrt', 'certt', 'cegrt', 'cergt', 'cefrt', 'cerft', 'cedrt', 'cerdt', 'cerrt', 'certr', 'cer5t', 'cert5', 'cer6t', 'cert6', 'ceryt', 'certy', 'cerht', 'certh', 'cergt', 'certrange', 'cerft', 'certf', 'ertificate', 'crtificate', 'cetificate', 'cerificate', 'certficate', 'certiicate', 'certifcate', 'certifiate', 'certificte', 'certificae', 'certificat', 'ccertificate', 'ceertificate', 'cerrtificate', 'certtificate', 'certiificate', 'certifficate', 'certifiicate', 'certificcate', 'certificaate', 'certificatte', 'certificatee', 'ecrtificate', 'cretificate', 'cetrificate', 'ceritficate', 'certfiicate', 'certiifcate', 'certifciate', 'certifiacte', 'certifictae', 'certificaet', 'xertificate', 'dertificate', 'fertificate', 'vertificate', 'cwrtificate', 'certeficated', 'certeficatse', 'certeficates'];
const rapRateTypo = ['raprate', 'aprate', 'aprate', 'rprate', 'rarate', 'rapate', 'raprte', 'raprae', 'rates', 'rate'];
const backTypo = ['back', 'discount', 'off', '%', 'ack', 'ack', 'bck', 'bak'];
const rate_usTypo = ['rate_us', 'price', 'prise', 'value', 'cost', 'dollar', 'rate', 'rate us', 'raste us', 'rxate us', 'raxte us', 'rzate us', 'razte us', 'rarte us', 'ratre us', 'ra5te us', 'rat5e us', 'ra6te us', 'rat6e us', 'rayte us', 'ratye us', 'rahte us', 'rathe us', 'ragte us', 'ratge us', 'rafte us', 'ratfe us', 'ratwe us', 'ratew us', 'rat3e us', 'rate3 us', 'rat4e us', 'rate4 us', 'ratre us', 'rater us', 'ratfe us', 'ratef us', 'ratde us', 'rated us', 'ratse us', 'rates us', 'price', 'rice', 'pice', 'prce', 'prie', 'pric', 'pprice', 'dollar', 'dopllar', 'dlollar', 'dolllar', 'dkollar', 'dokllar', 'dokllar', 'dolklar', 'doollar', 'dololar', 'dopllar', 'dolplar', 'dolklar', 'dollkar', 'dololar', 'dolloar', 'dolplar', 'dollpar', 'dollqar', 'dollaqr', 'dollwar', 'dollawr', 'dollsar', 'dollasr', 'dollxar', 'dollaxr', 'dollzar', 'dollazr', 'dollaer', 'dollare', 'dolla4r', 'dollar4', 'dolla5r', 'dollar5', 'dollatr', 'dollart', 'dollagr', 'dollarg', 'dollafr', 'dollarf', 'dolladr', 'dollard', 'value', 'valued', 'valuse', 'values'];
const reportNoTypo = ['reportno'];
const shapeTypo = ["shape", "shepe", "shapw"];

// Typos: ***********************************************************************************************

 const helpStr = 'How To:\n\n' +
 'Search:\n You can input search string ' +
 'by specifying values of 4Cs of diamond ' +
 'you are looking for seperated by space.\n' +
 'On top of that you can also add different ' +
 'values for fluorescence, price in USD, one or more ' +
 'GIA report number.\n' +
 ' Some of the example queries are:\n' +
 '"rd 6k xxx E F 1.0"\n' +
 '"si1 vs1 0.98 1.05 D H 3x none rd"\n' +
 '"Round Princess xxx  si 1/2  I 3x medium 3000 4000"\n' +
 '"I2 pk 75 pointer D H 3vg medium 2.7k"\n' +
 'Note: Each of the Diamond result shown will have parameter ' +
 'either equal or better than what you asked for in search.\n' +
 'If you looking for exact search, you can add "exact" keyword to search query.\n' +
 'Example: "exact vvs1 g h rd"\n\n' +
 'Quick-Search:\n You can also do quick search messaging "quick-search" or just "qs"\n' +
 'It will show you table with broad catagories and corresponding count for \n' +
 'each stone as well as minimum price and maximum price for that category.\n\n' +
 'Show/Hide Columns:\n On quick-search table you can click on any cell to perform corresponding search.\n' +
 'Once you get search result in table you add show/hide additional column. \n' +
 'Example: "show m1 m2 m3" (this will show additional columns with measurements for stone)\n' +
 'Similarly you can hide column by specifying column names.\n\n' +
 'Change Price:\n You just specify percentage after the search result, and it will add/decreae \n' +
 'that percent from USD rate and update the back and cost per carat column\n' +
 'Example: "5%" or "-2%"\n\n' +
 'Email:\n' +
 'Just enter any email address and it will send last search result in email.\n' +
 'Example: "sales@anikadiamond.com" \n';


const parseUserRequest = function(userRequest) {
 userRequest = userRequest.toLowerCase().replace(/\s\s+/g, ' ').trim();

 if (userRequest == 'help') {
     return {
         userMessage: helpStr,
         queryMode: 'help',
     };
 }

 if (userRequest == 'cache') {
     return {
         userMessage: 'cache object is',
         queryMode: 'cache',
     };
 }

 if (userRequest == 'quick search' || userRequest == 'fast search' ||
     userRequest == 'quick-search' || userRequest == 'fast-search' ||
     userRequest == 'qs' || userRequest == 'fs') {
     return {
         queryMode: 'quick-search'
     };
 }

 if ((userRequest.indexOf("hide") != -1 || userRequest.indexOf("remove") != -1 || userRequest.indexOf("delete") != -1) ||
     (userRequest.indexOf("show") != -1 || userRequest.indexOf("add") != -1 || userRequest.indexOf("unhide") != -1)) {
     var columnNames = [];
     var splittedUserRequest = userRequest.split(' ');
     for (var i = 0; i < columnNameC.length; i++) {
         if (splittedUserRequest.indexOf(columnNameC[i].toLowerCase()) != -1) {
             columnNames.push(columnNameC[i]);
         }
     }
     for (var i = 0; i < hiddenColumnNameC.length; i++) {
         if (splittedUserRequest.indexOf(hiddenColumnNameC[i].toLowerCase()) != -1) {
             columnNames.push(hiddenColumnNameC[i]);
         }
     }
     if (userRequest.indexOf("show") != -1 || userRequest.indexOf("add") != -1 || userRequest.indexOf("unhide") != -1) {
         return {
             columnNameArray: columnNames,
             queryMode: 'show'
         }
     } else {
         return {
             columnNameArray: columnNames,
             queryMode: 'hide'
         }
     }
 }

 // parsedQuery is object with three fields.
 // 1. userMessage (string query)
 // 2. entityName array.
 // 3. entityValue array. It is an 2D array.
 var parsedQuery = queryParser_(userRequest);
 if (parsedQuery.entityName.length == 0) {
     var emailAddr = userRequest.match(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi);
     if (userRequest.indexOf('mail') != -1 || emailAddr) {
         var userMessage = '';
         if (emailAddr == '') {
             var userMessage = 'Please provide valid email ID';
         }
         return {
             email: emailAddr,
             userMessage: userMessage,
             queryMode: 'email'
         };
     }

     if (parsedQuery.percent) { // Add only dollar value for const addition
         return {
             percent: parsedQuery.percent,
             constUsd: 0,
             queryMode: 'changeRate'
         };
     }

     return {
         userMessage: 'Your Query is invalid, message/search "help" for usage instructions.',
         queryMode: 'help'
     };
 }



 var whereClause = createWhereClause_(parsedQuery);
 var simpleQuery = createSimpleQuery_(whereClause, parsedQuery);
 return {
     condition: parseQueryToText(parsedQuery),
     parsedQuery: parsedQuery,
     query: simpleQuery.query,
     queryMode: 'btQuery'
 };
}

function createSimpleQuery_(whereClause, parsedQuery) {
 // parsedQuery //  (todo:kalpesh) change to add value to rate_us
 var rateMultiplier = 1.0 + (parsedQuery.percent) / 100;
 var limit = parsedQuery.limit;
 parsedQuery.columnName = columnNameC;
 parsedQuery.hiddenColumnName = hiddenColumnNameC;

 var btQueryStr =
     'SELECT ' +
     'Shape, ' +
     'Size,  ' +
     'Color, ' +
     'Clarity, ' +
     'Cut, ' +
     'Polish, ' +
     'Sym, ' +
     'Flour, ' +
     'ROUND(Rate_US*' + rateMultiplier + ') Rate_US, ' +
     'ROUND((Rate_US*' + rateMultiplier + ')/Size)  USDPerCT, ' +
     'SUBSTR(STRING(100 - ' + rateMultiplier + '*(100 - Back)),0, 5) Back, ' +
     'ReportNo, ' +
     'M1, ' +
     'M2, ' +
     'M3, ' +
     'Depth, ' +
     '[Table], ' + // https://stackoverflow.com/questions/18905842/oops-used-a-reserved-word-to-name-a-column
     'Ref, ' +
     'CertNo, ' +
     'Detail, ' +
     'cert, ' +
     'CompanyCode ' +
     'FROM Diamond_Inv.latest ' +
     ' WHERE Rate_US != 0 AND ' +
     whereClause.join(' AND \n') +
     ' ORDER BY USDPerCT ' +
     'LIMIT ' + limit;

 var btQuery = {
     query: btQueryStr
 };
 return btQuery;
}

//****************************************************************WHERE CLAUSE*****************************************


function testcreateWhereClause_(userMessage) {
 var whereClause = createWhereClause_(queryParser_(userMessage));
}

// createWhereClause_ create the big query from email query.
// parsedQuery is object with three fields.
// 1. userMessage (string query)
// 2. entityName array.
// 3. entityValue array. It is an 2D array.
function createWhereClause_(parsedQuery) {
 var whereClause = [];
 var exactMode = false;
 if (parsedQuery.queryMode == 'exact') {
     exactMode = true;
 }

 for (var i = 0; i < parsedQuery.entityName.length; i++) {
     switch (parsedQuery.entityName[i]) {
         case 'color':
             var clause = getRangeClause_('color', parsedQuery.entityValue[i], colorRange, exactMode);
             whereClause.push(clause);
             break;
         case 'clarity':
             var clause = getRangeClause_('clarity', parsedQuery.entityValue[i], clarityRange, exactMode);
             whereClause.push(clause);
             break;
         case 'polish':
             var clause = getRangeClause_('polish', parsedQuery.entityValue[i], polishRange, exactMode);
             whereClause.push(clause);
             break;
         case 'sym':
             var clause = getRangeClause_('sym', parsedQuery.entityValue[i], symRange, exactMode);
             whereClause.push(clause);
             break;
         case 'cut':
             var clause = getRangeClause_('cut', parsedQuery.entityValue[i], cutRange, exactMode);
             whereClause.push(clause);
             break;
         case 'flour':
             var clause = getRangeClause_('flour', parsedQuery.entityValue[i], flourRange, exactMode);
             whereClause.push(clause);
             break;
         case 'size':
             var sizeClause = getSizeClause_(parsedQuery.entityValue[i]);
             whereClause.push(sizeClause);
             break;
         case 'shape':
             var shapeClause = getShapeClause_(parsedQuery.entityValue[i]);
             whereClause.push(shapeClause);
             break;
         case 'rate_us':
             var rateClause = getRateClause_(parsedQuery.entityValue[i]);
             whereClause.push(rateClause);
             break;
         case 'back':
             var BackClause = getBackClause_(parsedQuery.entityValue[i]);
             whereClause.push(BackClause);
             break;
         case 'reportno':
             var reportNoClause = getReportNoClause_(parsedQuery.entityValue[i]);
             whereClause.push(reportNoClause);
             break;
         default:
             // Nothing for now, but we should log it
     }
 }

 return whereClause;
}

// property examples are color, cut, clarity, etc
// valueArray = ['F', 'H']
// range = ['D', 'E', .... , 'Z']
function getRangeClause_(property, valueArray, range, exactMode) {
 var betterRange = -1;
 var lowerRange = -1;

 for (var j = 0; j < valueArray.length; j++) {
     for (var k = 0; k < range.length; k++) {
         if (valueArray[j] == range[k]) {
             if (betterRange == -1) {
                 betterRange = k;
             } else {
                 lowerRange = k;
             }
             break;
         }
     }
 }
 if (betterRange != -1) {
     retStr = [];
     if (lowerRange == -1) {
         if (exactMode) {
             retStr.push(property + ' = \'' + range[betterRange].toUpperCase() + '\'');
         } else {
             for (var k = 0; k <= betterRange; k++) {
                 retStr.push(property + ' = \'' + range[k].toUpperCase() + '\'');
             }
         }
     } else {
         for (var k = betterRange; k <= lowerRange; k++) {
             retStr.push(property + ' = \'' + range[k].toUpperCase() + '\'');
         }
     }
     return "(" + retStr.join(' OR ') + ") ";
 }

 return '(true)';
}

function getShapeClause_(valueArray) {
 if (valueArray.length > 0) {
     var retStr = [];
     for (var i = 0; i < valueArray.length; i++) {
         var actualShape = getActualShape(valueArray[i]);
         if (actualShape) {
             retStr.push('Shape = \'' + actualShape.toUpperCase() + '\'');
         }
     }
     return '(' + retStr.join(' OR ') + ')';
 }
 return '(true)';
}

function getReportNoClause_(valueArray) {
 if (valueArray.length > 0) {
     var retStr = [];
     for (var i = 0; i < valueArray.length; i++) {
         retStr.push('reportno = \'' + valueArray[i] + '\'');
     }
     return '(' + retStr.join(' OR ') + ')';
 }
 return '(true)';
}

// Add keyword like quater, 3rd's, halfs,
function getSizeClause_(valueArray) {
 var firstSize = -1.0;
 var secondSize = -1.0;

 for (var j = 0; j < valueArray.length; j++) {
     if (validDecimal_(valueArray[j])) {
         if (firstSize < 0.0) {
             firstSize = valueArray[j];
         } else {
             secondSize = valueArray[j];
         }
     }
 }
 if (firstSize > 0.0) { //First value is initialize
     if (secondSize < 0.0) { // If second value is not initialize then it should single value.
         return '(Size = ' + firstSize + ')';
     } else { // If both values are initialize then it range.
         if (firstSize > secondSize) {
             return '( Size < ' + firstSize + ' AND size > ' + secondSize + ')';
         } else {
             return ' (Size < ' + secondSize + ' AND size > ' + firstSize + ')';
         }
     }
 }
 return null;
}

// For keyword like ['price','prise','value','cost','dollar','rate','$','dollar',]
function getRateClause_(valueArray) {
 if (valueArray.length == 1) {
     return '(Rate_US <= ' + valueArray[0] + ')';
 } else if (valueArray.length == 2) {
     var firstSize = valueArray[0];
     var secondSize = valueArray[1];
     if (firstSize > secondSize) {
         return '(Rate_US <= ' + firstSize + ' AND Rate_US >= ' + secondSize + ')';
     } else {
         return '(Rate_US <= ' + secondSize + ' AND Rate_US >= ' + firstSize + ')';
     }
 } else {
     return '(true)';
 }
}

// backTypo: ['back','discount','off','%',]
function getBackClause_(valueArray) {
 var firstSize = -1.0;
 var secondSize = -1.0;
 for (var j = 0; j < valueArray.length; j++) {
     if (validDecimal_(valueArray[j])) {
         if (firstSize < 0.0) {
             firstSize = valueArray[j];
         } else {
             secondSize = valueArray[j];
         }
     }
 }
 if (firstSize > 0.0) { //First value is initialize
     if (secondSize < 0.0) { // If second value is not initialize then it should single value.
         return '(Back > ABS(' + firstSize + '))';
     } else { // If both values are initialize then it range.
         if (firstSize > secondSize) {
             return '(Back < ABS(' + firstSize + ') AND Back > ABS(' + secondSize + '))';
         } else {
             return '(Back < ABS(' + secondSize + ') AND Back > ABS(' + firstSize + '))';
         }
     }
 }
 return null;
}

function validDecimal_(value) {
 return !isNaN(parseFloat(value));
}
//****************************************************************WHERE CLAUSE*****************************************

// Function used for testing query parsing
function parseQueryToText(parsedResult) {
 var parsedQuery = '';
 for (var i = 0; i < parsedResult.entityName.length; i++) {
     var entityValue = parsedResult.entityValue[i];
     var entityValueStr = '';
     if (entityValue.length > 0) {
         for (var j = 0; j < entityValue.length; j++) {
             entityValueStr = entityValueStr + entityValue[j] + ' ';
         }
         parsedQuery += "\n" + parsedResult.entityName[i] + " = " + entityValueStr + '\t';
     }
 }
 return parsedQuery;
}

// Parsing the free form query and returning the clause in form "weight = 1.49 1.51"
// or "clarity = VS1" or "cut = ex"
// We still do not parse Depth, Table, and RapRate.
function queryParser_(userMessage) {
 var parsedResult = {
     userMessage: userMessage,
     entityName: [],
     entityValue: [],
     queryMode: '', // Mode like exact match.
     unknown: '',
     percent: 0.0,
     limit: 30, // Number result shown
 };

 console.log('0th parse query is:' + parsedResult.userMessage);
 setQueryMode(parsedResult);

 switch (parsedResult.queryMode) {
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
 }

 parsePointer(parsedResult);
 replaceHotKeyword_(parsedResult, sizeKeyword, sizeKeywordValue);
 replaceHotKeyword_(parsedResult, multiValueKeyword, multiValueKeywordValue);
 replaceHotKeyword_(parsedResult, priceKeyword, priceKeywordValue);
 replaceHotKeyword_(parsedResult, clarityKeyword, clarityKeywordValue);

 // console.log('1st parse query is:' + parsedResult.userMessage);

 replaceHotKeywordSplit_(parsedResult, sizeKeyword, sizeKeywordValue);
 replaceHotKeywordSplit_(parsedResult, multiValueKeyword, multiValueKeywordValue);
 replaceHotKeywordSplit_(parsedResult, priceKeyword, priceKeywordValue);
 replaceHotKeywordSplit_(parsedResult, clarityKeyword, clarityKeywordValue);

 // console.log('2nd parse query is: ' + parsedResult.userMessage);

 // Replacing email clause by different the new line characters.
 // Then replacing all the non (character, equal, number, decimanl point, colon, dash, space) by space.
 parsedResult.userMessage = parsedResult.userMessage
     .replace(/(?:\r\n|\r|\n|<br>)/g, ' ')
     .replace(/\s\s+/g, ' ')
     .replace(/[^a-zA-Z\.0-9\-+%\\ ]/g, " ")
     .replace(/\s\s+/g, ' ');

 // console.log('3rd parse query is:' + parsedResult.userMessage);

 parseEntityKeyword_(parsedResult, shapeTypo, userShape); // TODO: Need to convert user shape to actual shape
 parseEntityKeyword_(parsedResult, clarityTypo, clarityRange);
 parseEntityKeyword_(parsedResult, flourTypo, userFlour);
 parseEntityKeyword_(parsedResult, certTypo, certRange);
 parseEntityKeyword_(parsedResult, colorTypo, colorRange);

 // console.log('5th parse query is:' + parsedResult.userMessage);


 // Here order (cut. polish and sym is important)
 parseCPSKeyword_(parsedResult, cutTypo);
 parseCPSKeyword_(parsedResult, polishTypo);
 parseCPSKeyword_(parsedResult, symTypo);

 // console.log('6th parse query is:' + parsedResult.userMessage);
 parsePercent(parsedResult);

 parseNumberEntityKeyword_(parsedResult, sizeTypo);
 parseNumberEntityKeyword_(parsedResult, rate_usTypo);
 parseNumberEntityKeyword_(parsedResult, backTypo);
 parseNumberEntityKeyword_(parsedResult, reportNoTypo);

 console.log('7th parse query is:' + parsedResult.userMessage);

 return parsedResult;
}

function setQueryMode(parsedResult) {
 var userMessage = parsedResult.userMessage;
 for (var mode in QueryMode) {
     if (userMessage.indexOf(mode) != -1) {
         userMessage.replace(mode, '');
         parsedResult.queryMode = QueryMode[mode];
         return;
     }
 }

 return;
}

function parsePercent(parsedResult) {
 var strNValue = matchAndReplace(parsedResult.userMessage, percentRegex);
 if (strNValue[1] == '') {
     strNValue = matchAndReplace(parsedResult.userMessage, percentCharRegex);
 }
 if (strNValue[1] != '') { // Found percentage
     var percentage = Number(strNValue[1].slice(0, -1));
     parsedResult.userMessage = strNValue[0];
     parsedResult.percent = percentage;
 }
}

function parsePointer(parsedResult) {
 var strNValue = matchAndReplace(parsedResult.userMessage, pointerRegex);
 if (strNValue[1] != '') { // Found pointer
     console.log('Value:' + strNValue[1])
     var numStr = matchAndReplace(strNValue[1], numberRegex);
     if (numStr[1] != '') {
         var ptrValue = Number(numStr[1]);
         if (!isNaN(ptrValue)) {
             if (ptrValue > 0.9999) {
                 ptrValue = ptrValue / 100.0;
             }
             parsedResult.userMessage = strNValue[0] + ' ' + (ptrValue * 0.97) + ' ' + (ptrValue * 1.03);
         }
     }
 }
}

// Return array with two string.
// 1. Str with replaced value
// 2. Matched string
function matchAndReplace(str, pattern) {
 var results = str.match(pattern);
 var result = '';
 if (results != null) {
     result = results[0].trim();
     str = str.replace(result, '');
 }
 return [str, result];
}

function replaceHotKeyword_(parsedResult, keywords, keywordValues) {
 var userMessage = parsedResult.userMessage;
 //var splitQuery = userMessage.split(' ');
 for (var i = 0; i < keywords.length; i++) {
     if (userMessage.indexOf(keywords[i]) != -1) {
         userMessage.replace(keywords[i], keywordValues[i]);
     }
 }

 //    parsedResult.userMessage = userMessage;
 return;
}

function replaceHotKeywordSplit_(parsedResult, keywords, keywordValues) {
 var userMessage = parsedResult.userMessage;
 var splitQuery = userMessage.split(' ');
 for (var i = 0; i < keywords.length; i++) {
     for (var j = 0; j < splitQuery.length; j++) {
         if (keywords[i] == splitQuery[j]) {
             splitQuery[j] = keywordValues[i];
         }
     }
 }

 parsedResult.userMessage = splitQuery.join(' ');
 return;
}

function parseEntityKeyword_(parsedResult, typoArray, userValues) {
 var userMessage = parsedResult.userMessage;
 var keywordReplace = false;
 var valueReplace = false;
 var values = [];
 for (var i = 0; i < typoArray.length; i++) {
     var typo = typoArray[i];
     if (userMessage.indexOf(typo) != -1) {
         var correctSpell = typoArray[0];
         userMessage = userMessage.replace(typo + '= ', '');
         userMessage = userMessage.replace(typo + ': ', ' ');
         userMessage = userMessage.replace(typo + ' ', ' ');
         keywordReplace = true;
         break; // Assuming each entity (shape, size, color etc) will be present only with single spelling.
     }
 }

 var returnClause = '';
 if (userValues) {

     var splitQuery = userMessage.split(' ');
     for (var i = 0; i < userValues.length; i++) {
         var userValue = userValues[i];
         for (var j = 0; j < splitQuery.length; j++) {
             if (userValue == splitQuery[j]) {
                 splitQuery[j] = ' ';
                 values.push(userValue);
                 valueReplace = true;
             }
         }
     }
 }

 if (valueReplace) {
     parsedResult.userMessage = splitQuery.join(' ');
     parsedResult.entityName.push(typoArray[0]);
     parsedResult.entityValue.push(values);
 }
 return;
}

// Parsing Cut, Polish and Symmetry from query.
function parseCPSKeyword_(parsedResult, typoArray) {
 var userValues = ['ex', 'vg', 'g'];
 var userMessage = parsedResult.userMessage;
 var valueReplace = false;
 var values = [];

 for (var j = 0; j < userValues.length; j++) {
     for (var i = 0; i < typoArray.length; i++) {
         var typo = typoArray[i];
         if (userMessage.indexOf(typo + ' ' + userValues[j]) != -1) {
             userMessage = userMessage.replace(typo + ' ' + userValues[j], ' ');
             parsedResult.userMessage = userMessage;
             parsedResult.entityName.push(typoArray[0]);
             parsedResult.entityValue.push([userValues[j]]);
             return;
         }
     }
 }

 var returnClause = '';

 var splitQuery = userMessage.split(' ');
 for (var i = 0;
     (i < userValues.length && valueReplace == false); i++) {
     var userValue = userValues[i];
     for (var j = 0; j < splitQuery.length; j++) {
         if (userValue == splitQuery[j]) {
             splitQuery[j] = ' ';
             values.push(userValue);
             valueReplace = true;
             break;
         }
     }
 }

 if (valueReplace) {
     parsedResult.userMessage = splitQuery.join(' ');
     parsedResult.entityName.push(typoArray[0]);
     parsedResult.entityValue.push(values);
 }
 return;
}

function parseNumberEntityKeyword_(parsedResult, typoArray) {
 var userMessage = parsedResult.userMessage.replace(/\s+/g, " ");
 var keywordReplace = false;
 var valueReplace = false;
 var values = [];

 var splituserMessage = userMessage.split(' ');
 for (var i = 0; i < splituserMessage.length; i++) {
     var strQuery = splituserMessage[i];
     var parsedNumber = Number(strQuery.replace(/[^0-9\.]+/g, ""));
     var strNum = parsedNumber + '';
     var strNumK = parsedNumber + 'k';
     var strNumZeroK = parsedNumber + '0k';
     if (parsedNumber < 0.0001 && parsedNumber > -0.0001) { // If number is 0
         continue;
     }

     if (strQuery == strNumK || strQuery == strNumZeroK) {
         parsedNumber = parsedNumber * 1000;
     } else if (strQuery == strNum || strQuery == (strNum + '0') || ('0' + strQuery == strNum) || strQuery == (strNum + '.0') || strQuery == (strNum + '.00')) { // to handle decimal number case like 1.0
         // Do nothing
     } else {
         continue;
     }

     if (typoArray[0] == 'size' && parsedNumber < 15) { // Assume it is weight
         userMessage = userMessage.replace(strNum, ' ');
         values.push(parsedNumber);
         valueReplace = true;
     }
     if (typoArray[0] == 'back' && parsedNumber > 15 && parsedNumber < 80) { // Assume it is back discount
         userMessage = userMessage.replace(strNum, ' ');
         values.push(parsedNumber);
         valueReplace = true;
     }
     if (typoArray[0] == 'rate_us' && parsedNumber > 200 && parsedNumber < 900000) { // Assumme it is price
         userMessage = userMessage.replace(strNum, ' ');
         userMessage = userMessage.replace(strNumK, ' ');
         userMessage = userMessage.replace(strNumZeroK, ' ');
         if (parsedNumber > 250) { // Temporary fix for phone number issue
             values.push(parsedNumber);
             valueReplace = true;
         }
     }
     if (typoArray[0] == 'reportno' && parsedNumber > 100000000 && parsedNumber < 10000000000) {
         userMessage = userMessage.replace(strNum, ' ');
         values.push(parsedNumber);
         valueReplace = true;
     } else { //Unknown, Cannot parse query, we should log it
         parsedResult.unknown += ' ' + parsedNumber;
     }
 }

 if (valueReplace) {
     for (var i = 0; i < typoArray.length; i++) {
         var typo = typoArray[i];
         if (userMessage.indexOf(typo) != -1) {
             userMessage = userMessage.replace(typo + ' ', ' ');
             keywordReplace = true;
             break; // Assuming each entity (shape, size, color etc) will be present only with single spelling.
         }
     }

     parsedResult.userMessage = userMessage;
     parsedResult.entityName.push(typoArray[0]);
     parsedResult.entityValue.push(values);
 }
 return;
}