function getColumnMapping_(firstRow, companyIndex) {
	switch (companyIndex) {
		case dharamIndex:
			return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
		case kiranIndex:
			return [2, 3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 20, 19, 1, 10, 26, 10, 12, 13, 15, 42];
		case rkIndex:
			//return [4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 20, 19, 1, 3, 26, 2, 8, 9, 11, 3];
			return [2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 11, 20, 21, 0, 13, 40, 12, 14, 15, 16, 13];
		case srkIndex:
			return [6, 9, 8, 7, 12, 13, 14, 15, 17, 17, 17, 18, 19, 4, 38, 20, 7, -1, 11, -1, 38];
	}
	return null;
}


// Diamond Entity Values:
var colorsG = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']; //, 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
var clarityG = ['FL', 'IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1', 'I2', 'I3'];
var polishG = ['EX', 'VG'];
var symG = ['EX', 'VG'];
var cutG = ['EX', 'VG'];
var flourG = ['NONE', 'FAINT', 'MEDIUM', 'STRONG', 'VERY STRONG'];
var shapeG = ["ROUND", "MARQUISE", "PRINCESS", "PEAR", "OVAL", "HEART", "CUSHION MODIFIED", "CUSHION", "ASHCHER", "RADIANT"];
var certG = ['gia', 'hrd', 'igi', 'fm']


var userShape = ["Round", "RD", "R", "BR", "RB",
	"Marquise", "MR", "MQ", "MAR",
	"Princess", "PR", "PC",
	"Pear", "Paer", "Per", "PS",
	"Oval", "Ov",
	"Heart", "Hrt", "Love",
	"Cushion Modified", "CMB", "CM",
	"Cushion", "Cus", "CU",
	"Ashcher", "AS",
	"Radiant", "RAD",
	"EMERALD", "EM", "EMRD"
];
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


function getActualShape_(inputShape) {
	for (var j = 0; j < userShape.length; j++) {
		if (userShape[j].toLowerCase() == inputShape.trim().toLowerCase()) {
			return actualShape[j];
		}
	}
	return null;
}

var userFlour = ["None", "Non", "N", "NO", "Nan", "strong", "STG", "Very Strong", "VST", "VSTG", "MEDIUM", "MED", "FAINT", "FNT", "FAINT"];
var actualFlour = ["NONE", "NONE", "NONE", "NONE", "NONE", "STRONG", "STRONG", "VERY STRONG", "VERY STRONG", "VERY STRONG", "MEDIUM", "MEDIUM", "FAINT", "FAINT", "FAINT"];

function getActualFlour_(inputFlour) {
	for (var j = 0; j < userFlour.length; j++) {
		if (userFlour[j].toLowerCase() == inputFlour.trim().toLowerCase()) {
			return actualFlour[j];
		}
	}
	return null;
}