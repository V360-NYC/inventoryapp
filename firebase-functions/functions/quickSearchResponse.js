exports.createQuickSearchResponse = function (rows) {
	const quickSearchArray = [];
	const headerRow = ['color', 'clarity', 'carat'];
	const colorVal = ['D E F', 'G H', 'I J', 'K L M N'];
	const clarityVal = ['IF', 'VVS', 'VS', 'SI', 'I'];
	const caratVal = ['0.18 to 0.45', '0.46 to 0.95', '0.96 to 1.45', '1.46 to 10.0'];

	const colorValSearch = ['D  F', 'G H', 'I J', 'K N'];
	const clarityValSearch = ['FL IF ', 'VVS1 VVS2', 'VS1 VS2', 'SI1 SI2', 'I1 I3'];
	const caratValSearch = ['0.18 0.45', '0.46 0.95', '0.96 1.45', '1.46  10.0'];

	const caratActualVal = [0.18, 0.46, 0.96, 10.0];

	quickSearchArray.push(headerRow);
	quickSearchArray.push(colorVal);
	quickSearchArray.push(clarityVal);
	quickSearchArray.push(caratVal);
	quickSearchArray.push(colorValSearch);
	quickSearchArray.push(clarityValSearch);
	quickSearchArray.push(caratValSearch);

	var a3d = new Array(colorVal.length);
	for (var i = 0; i < colorVal.length; i++) {
		a3d[i] = new Array(clarityVal.length);
		for (var j = 0; j < clarityVal.length; j++) {
			a3d[i][j] = new Array(caratActualVal.length);
			for (var k = 0; k < caratActualVal.length; k++) {
				a3d[i][j][k] = [0, 1000000, 0];
			}
		}
	}
	console.log("Quick Search Row Count:" + rows.length);

	rows.forEach((row) => {
		var classifyObj = classifyRow_(row);
		var c1 = classifyObj.color;
		var c2 = classifyObj.clarity;
		var c3 = classifyObj.carat;
		a3d[c1][c2][c3][0] = a3d[c1][c2][c3][0] + row['Count'];
		if (row['Min_Price'] < a3d[c1][c2][c3][1] && row['Min_Price'] > 10) {
			a3d[c1][c2][c3][1] = row['Min_Price'];
		}
		if (row['Max_Price'] > a3d[c1][c2][c3][2]) {
			a3d[c1][c2][c3][2] = row['Max_Price'];
		}
	});

	return {
		quickSearchArray: quickSearchArray,
		stats: a3d
	};
}

const colorMap = {
	D: 0,
	E: 0,
	F: 0,
	G: 1,
	H: 1,
	I: 2,
	J: 2,
	K: 3,
	L: 3,
	M: 3,
	N: 3,
	FANCY: 3
};

const clarityMap = {
	FL: 0,
	IF: 0,
	VVS1: 1,
	VVS2: 1,
	VS1: 2,
	VS2: 2,
	SI1: 3,
	SI2: 3,
	I1: 4,
	I2: 4,
	I3: 4
};

function classifyRow_(row) {
	var color = row['Color'];
	var clarity = row['Clarity'];
	var carat = row['Carat'];

	var colorIdx = 3;
	if (colorMap[color] != undefined) {
		colorIdx = colorMap[color];
	}

	var clarityIdx = 4;
	if (clarityMap[clarity] != undefined) {
		clarityIdx = clarityMap[clarity];
	}

	var caratIdx = 0;
	if (carat < 0.46) {
		caratIdx = 0;
	} else if (carat < 0.96) {
		caratIdx = 1;
	} else if (carat < 1.46) {
		caratIdx = 2;
	} else {
		caratIdx = 3;
	}

	return {
		color: colorIdx,
		clarity: clarityIdx,
		carat: caratIdx
	};
}