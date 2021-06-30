/*
 * Given a results from big query in form of rows (each row being JSON object), it
 * parse and return html table that can be represented in email. 
 */
exports.CreateHtmlTableFromResultArray = function(rows) {
	if (rows.length > 0) {
		// Append the results.
		var data = []; //new Array(rows.length + 1);

		var firstRow = rows[0];
		var headerRow = [];
		for (var j = 0; j < firstRow.length; j++) {
			headerRow.push(firstRow[j]);
		}
		data.push(headerRow);

		for (var i = 1; i < rows.length; i++) {
			var row = rows[i];
			var values = [];
			for (var j = 0; j < row.length; j++) {
				if (headerRow[j] == 'ReportNo') {
					values.push("<a href='https://www.gia.edu/report-check?reportno=" +
						row[j] + "' target='_blank' >" + row[j] + "</a>");
				} else {
					values.push(row[j]);
				}
			}
			data.push(values);
		}

		return MakeTableHTML(data);
	}
	return 'No result match your criteria ';
}

// makeTableHTML_ takes the 2D array and return the properly formatted HTML table.
function MakeTableHTML(myArray) {
	var result = "<table border=1 style='font-family: arial,sans-serif; color:#111111; border-collapse: collapse; width: 100%;'>";
	var rowStyle = "style='border: 1px solid #dddddd; text-align: left; padding: 8px;";
	for (var i = 0; i < myArray.length; i++) {
		result += "<tr>";
		var backgroundSyle = "'";
		if (i % 2 != 0) {
			backgroundSyle = "background-color: #dddddd;'";
		}
		for (var j = 0; j < myArray[i].length; j++) {
			if (i == 0) {
				result += "<th " + rowStyle + backgroundSyle + ">" + myArray[0][j] + "</th>";
			} else {
				result += "<td " + rowStyle + backgroundSyle + ">" + myArray[i][j] + "</td>";
			}
		}
		result += "</tr>";
	}
	result += "</table>";

	return result;
}

exports.ParseBQResultAndCreateArray = function(rows, shownColumnName) {
	var data = [];
	if (rows.length > 0) {
		var headerRow = shownColumnName;
		data.push(headerRow);

		rows.forEach((row) => {
			var values = [];
			for (var i = 0; i < headerRow.length; i++) {
				if (row[headerRow[i]]) {
					values.push(row[headerRow[i]]);
				} else {
					values.push('NA');
				}
			}
			data.push(values);
		});
	}
	return data;
};

/*
 * Change the Rate_US column value as per percent mentioned. Also update "back" and
 * USD per carat for all the rows in that table.
 */
exports.ChangeRateUS = function(rows, percent, constDollar) {
	var rateMultiplier = 1.0 + (percent) / 100;
	if (rows.length > 0) {
		rows.forEach((row) => { // Change value here
			if (row['Rate_US']) {
				if (!isNaN(row['Rate_US'])) {
					row['Rate_US'] = (row['Rate_US'] * rateMultiplier + constDollar).toFixed(0);
					row['Back'] = (100 - rateMultiplier * (100 - row['Back'])).toFixed(2); // Need to also consider const for back calculation.
					row['USDPerCT'] = (row['Rate_US'] / row['Size']).toFixed(0);
				}
			}
		});
	}
	return rows;
};

