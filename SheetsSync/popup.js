window.onload = function() {
    var table = document.getElementById("box");
    var xhr = new XMLHttpRequest();

    xhr.addEventListener("error", function(event) {
        alert('Failed to update.');
    })
    xhr.open('GET', 'https://sheets.googleapis.com/v4/spreadsheets/1xpiQvqm43lilmj5mI8BkbfjIh2BggnQHu-qHnx7Wyqc/values:batchGet?ranges=A:B&key=AIzaSyAEgRnTTUxzniZcm7G2aivQ01mBmc_Pc8E', false);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send();
    var texts = JSON.parse(xhr.response).valueRanges[0].values;
    //table.innerText =  + " " + texts[texts.length - 1][1];

    var date = new Date();
    var comparableDate = date.toDateString().split(" ");

    var row;
    for (var i=0; i < texts.length; i++) {
        row = table.insertRow(-1);

        var isToday = false;
        var rowDate = texts[i][0].split(" ");
        if ((rowDate[0] == comparableDate[1]) && (parseInt(rowDate[1]) == parseInt(comparableDate[2]))) {
            isToday = true;
        }

        for (var j=0; j < 2; j++) {
            var cell = row.insertCell(-1);
            cell.innerHTML = texts[i][j];
            if (isToday)
                cell.style.backgroundColor = "#e83e3e";
        }
    }
}
