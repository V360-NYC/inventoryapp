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