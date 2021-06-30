function arrayToJson_(dataArray, companyIndex) {
	var dataJson = "";
	var rowCount = 0;
	data = [];
	var columnMapping = getColumnMapping_(dataArray[0], companyIndex);
	for (var z = 1; z < dataArray.length; z++) { // Skipping first row which might contain the header row
		var row_str = "";
		// if shape or size or color or clarity or cut is empty then skip that row.
		if (dataArray[z][columnMapping[0]].toString() && dataArray[z][columnMapping[1]].toString() &&
			dataArray[z][columnMapping[2]].toString() && dataArray[z][columnMapping[3]].toString()) {
			var back = dataArrayFn_(dataArray[z], columnMapping[18], true).replace(/ /g, '').replace(/\-/g, '');
			rowCount++;
			var jsonRow = JSON.stringify({
				'Shape': getActualShape_(dataArrayFn_(dataArray[z], columnMapping[0], true)),
				'Size': dataArrayFn_(dataArray[z], columnMapping[1], false),
				'Color': dataArrayFn_(dataArray[z], columnMapping[2], true),
				'Clarity': dataArrayFn_(dataArray[z], columnMapping[3], true),
				'Cut': dataArrayFn_(dataArray[z], columnMapping[4], true),
				'Polish': dataArrayFn_(dataArray[z], columnMapping[5], true),
				'Sym': dataArrayFn_(dataArray[z], columnMapping[6], true),
				'Flour': getActualFlour_(dataArrayFn_(dataArray[z], columnMapping[7], true)),
				'M1': getBreath_(dataArrayFn_(dataArray[z], columnMapping[8], true)),
				'M2': getWidth_(dataArrayFn_(dataArray[z], columnMapping[9], true)),
				'M3': getHeight_(dataArrayFn_(dataArray[z], columnMapping[10], true)),
				'Depth': dataArrayFn_(dataArray[z], columnMapping[11], false),
				'Table': dataArrayFn_(dataArray[z], columnMapping[12], false),
				'Ref': dataArrayFn_(dataArray[z], columnMapping[13], true),
				'CertNo': dataArrayFn_(dataArray[z], columnMapping[14], true),
				'Detail': dataArrayFn_(dataArray[z], columnMapping[15], true),
				'cert': dataArrayFn_(dataArray[z], columnMapping[16], true),
				'RapRate': dataArrayFn_(dataArray[z], columnMapping[17], false),
				'Back': back,
				'Rate_US': dataArrayFn_(dataArray[z], columnMapping[19], false),
				'ReportNo': dataArrayFn_(dataArray[z], columnMapping[20], true),
				'CompanyCode': companyCode[companyIndex]
			});
			data.push(jsonRow);
		} else {
			for (var i = 0; i < dataArray[z].length; i++) {
				row_str += ", " + dataArray[z][i];
			}
			Logger.log("Error in arrayToJson(): Field count:" + dataArray[z].length + " Row #" + z + " And Value:" + row_str);
		}
	}
	if (dryRun) {
		Logger.log("Row Count #" + rowCount);
	}
	return data.join("\n");
}

function dataArrayFn_(dataArray, columnIndex, convString) {
	if (columnIndex >= 0) {
		if (!convString) {
			return dataArray[columnIndex];
		}
		return dataArray[columnIndex].toString();
	}
	return 0;
}




// Diamond Entity Values:
//List of standard Color values
var colorsG = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
var clarityG = ['FL', 'IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1', 'I2', 'I3']; //List of standard Clarity values
var polishG = ['EX', 'VG', 'G']; //List of standard Polish values
var symG = ['EX', 'VG', 'G']; //List of standard Symmetry values
var cutG = ['EX', 'VG', 'G', 'F', 'IDEAL']; //List of standard Cut values
var flourG = ['NONE', 'FAINT', 'MEDIUM', 'STRONG', 'VERY STRONG']; //List of standard Flour values
var shapeG = ["ROUND", "MARQUISE", "PRINCESS", "PEAR", "OVAL", "HEART", "CUSHION MODIFIED", "CUSHION", "ASHCHER", "RADIANT"]; //List of standard Shape values
var certG = ['GIA', 'HRD', 'IGI', 'FM']; //List of standard Certificate values

//List of possible flour values which can user assign
var userShape = ["round", "rd", "r", "br", "rb",
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

//List of standard flour values for user's specified values
var actualShape = ["ROUND", "ROUND", "ROUND", "ROUND", "ROUND",
	"MARQUISE", "MARQUISE", "MARQUISE", "MARQUISE",
	"PRINCESS", "PRINCESS", "PRINCESS",
	"PEAR", "PEAR", "PEAR", "PEAR",
	"OVAL", "OVAL",
	"HEART", "HEART", "HEART",
	"CUSHION MODIFIED", "CUSHION MODIFIED", "CUSHION MODIFIED",
	"CUSHION", "CUSHION", "CUSHION",
	"ASHCHER", "ASHCHER",
	"RADIANT", "RADIANT",
	"EMERALD", "EMERALD", "EMERALD",
];

//List of possible flour values which can user assign
var userFlour = ["none", "non", "n", "no", "nan", "strong", "stg", "very strong", "vst", "vstg", "medium", "med", "faint", "fnt"];
//List of standard flour values for user's specified values
var actualFlour = ["NONE", "NONE", "NONE", "NONE", "NONE", "STRONG", "STRONG", "VERY STRONG", "VERY STRONG", "VERY STRONG", "MEDIUM", "MEDIUM", "FAINT", "FAINT"];

//Create hash map for Shape values
var hashTableForShape = {};
var i;
for (i = 0; i < userShape.length; i++) {
	hashTableForShape[userShape[i]] = actualShape[i];
}

//Create hash map for Flour values
var hashTableForFlour = {};
for (i = 0; i < userFlour.length; i++) {
	hashTableForFlour[userFlour[i]] = actualFlour[i];
}

//get standard value of Shape for user specified different values
function getActualShape_(inputShape) {
	return hashTableForShape[inputShape.trim().toLowerCase()];
}

//get standard value of Flour for user specified different values
function getActualFlour_(inputFlour) {
	return hashTableForFlour[inputFlour.trim().toLowerCase()];
}

exports.arrayToJsonFn = function (dataArray, companyIndex, companyCode) {
	var rowCount = 0;
	data = [];

	var columnMapping = companyIndex;
	for (var z = 1; z < dataArray.length; z++) { // Skipping first row which might contain the header row
		var row_str = "";

		// if shape or size or color or clarity or cut is empty then skip that row.
		if (dataArray[z][columnMapping[0]] != undefined && dataArray[z][columnMapping[1]] != undefined &&
			dataArray[z][columnMapping[2]] != undefined && dataArray[z][columnMapping[3]] != undefined) {
			var back = dataArrayFn_(dataArray[z], columnMapping[18], true, 'No', z).replace(/ /g, '').replace(/\-/g, '');
			rowCount++;
			var jsonRow = JSON.stringify({
				'Shape': getActualShape_(dataArrayFn_(dataArray[z], columnMapping[0], true, 'Shape', z)),
				'Size': dataArrayFn_(dataArray[z], columnMapping[1], false, 'Size', z),
				'Color': dataArrayFn_(dataArray[z], columnMapping[2], true, 'Color', z),
				'Clarity': dataArrayFn_(dataArray[z], columnMapping[3], true, 'Clarity', z),
				'Cut': dataArrayFn_(dataArray[z], columnMapping[4], true, 'Cut', z),
				'Polish': dataArrayFn_(dataArray[z], columnMapping[5], true, 'Polish', z),
				'Sym': dataArrayFn_(dataArray[z], columnMapping[6], true, 'Sym', z),
				'Flour': getActualFlour_(dataArrayFn_(dataArray[z], columnMapping[7], true, 'Flour', z)),
				'Depth': dataArrayFn_(dataArray[z], columnMapping[8], false, 'Depth', z),
				'Table': dataArrayFn_(dataArray[z], columnMapping[9], false, 'Table', z),
				//'M1' : getBreath_(dataArrayFn_(dataArray[z], columnMapping[10], true,'No',z)),
				//'M2' : getWidth_(dataArrayFn_(dataArray[z], columnMapping[11], true,'No',z)),
				//'M3' : getHeight_(dataArrayFn_(dataArray[z], columnMapping[12], true,'No',z)),
				'Ref': dataArrayFn_(dataArray[z], columnMapping[13], true, 'No', z),
				'CertNo': dataArrayFn_(dataArray[z], columnMapping[14], true, 'No', z),
				'Detail': dataArrayFn_(dataArray[z], columnMapping[15], true, 'No', z),
				'cert': dataArrayFn_(dataArray[z], columnMapping[16], true, 'No', z),
				'RapRate': dataArrayFn_(dataArray[z], columnMapping[17], false, 'RapRate', z),
				'Back': back,
				'Rate_US': dataArrayFn_(dataArray[z], columnMapping[19], false, 'Rate_US', z),
				'ReportNo': dataArrayFn_(dataArray[z], columnMapping[20], true, 'No', z),
				'CompanyCode': companyCode
			});
			data.push(jsonRow);
		} else {
			for (var i = 0; i < dataArray[z].length; i++) {
				row_str += ", " + dataArray[z][i];
			}
		}
	}
	return data.join("\n");
}

function dataArrayFn_(dataArray, columnIndex, convString, domainName, rowNumber) {
	if (columnIndex >= 0 && dataArray[columnIndex] != undefined && dataArray[columnIndex].toString().trim().length != 0) {
		validValueOrnot(domainName, dataArray[columnIndex], parseInt(rowNumber) + 1);
		if (!convString) {
			return dataArray[columnIndex];
		}
		return dataArray[columnIndex].toString();
	}
	return 0;
}

//check wheather value for that specified domain is correct or not
function validValueOrnot(domain, value, rowIndex) {
	switch (domain) {
		case 'Shape':
			if (userShape.indexOf(value.toString().toLowerCase()) == -1) {
				throw new Error("Problem in mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Size':
			if (isNaN(value)) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else if (parseFloat(value) > 15 || parseFloat(value) <= 0) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex + ". Not valid value");
			} else {
				return;
			}
			break;

		case 'Color':
			//if multiple values are stored in single cell
			if (value.toString().length > 1) {
				var temp = value.toString();
				for (var i = 0; i < temp.length; i++) {
					if (colorsG.indexOf(temp[i].toUpperCase()) == -1) {
						throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
					}
				}
				return;
			} else {
				if (colorsG.indexOf(value.toString().toUpperCase()) == -1) {
					throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
				} else {
					return;
				}
			}
			break;

		case 'Clarity':
			if (clarityG.indexOf(value.toString().toUpperCase()) == -1) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Polish':
			if (polishG.indexOf(value.toString().toUpperCase()) == -1) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Symm':
			if (symG.indexOf(value.toString().toUpperCase()) == -1) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Cut':
			if (cutG.indexOf(value.toString().toUpperCase()) == -1) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Flour':
			if (userFlour.indexOf(value.toString().toLowerCase()) == -1) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Depth':
			if (isNaN(value)) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Table':
			if (isNaN(value)) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'RapRate':
			if (isNaN(value)) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		case 'Rate_US':
			if (isNaN(value)) {
				throw new Error("Problem with mapping of " + value + " with " + domain + " at row No : " + rowIndex);
			} else {
				return;
			}
			break;

		default:
			return;
	}

}

function getDateInFormat() {
	var today = new Date();
	var dd = today.getDate();
	var mm = today.getMonth() + 1; //January is 0!

	var yyyy = today.getFullYear();
	if (dd < 10) {
		dd = '0' + dd;
	}
	if (mm < 10) {
		mm = '0' + mm;
	}
	var today = yyyy.toString() + mm.toString() + dd.toString();
	return today;
}

exports.TestFunction = function() {
	return 'testFunction';
};