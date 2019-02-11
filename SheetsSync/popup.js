window.onload = function() {
    var table = document.getElementById("box");
    var xhr = new XMLHttpRequest();
    var sheetId = localStorage.getItem('sheetid') || '1xpiQvqm43lilmj5mI8BkbfjIh2BggnQHu-qHnx7Wyqc';
    getData();
    
    function getData () {
        xhr.addEventListener("error", function(event) {
            alert('Failed to update.');
        })
        xhr.open('GET', 'https://sheets.googleapis.com/v4/spreadsheets/'+ sheetId + '/values:batchGet?ranges=A:B&key=AIzaSyAEgRnTTUxzniZcm7G2aivQ01mBmc_Pc8E', false);
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
    
            for (var j=0; j < texts[i].length; j++) {
                var cell = row.insertCell(-1);
                cell.innerHTML = texts[i][j];
                if (isToday)
                    cell.style.backgroundColor = "#e83e3e";
            }
        }
    }

    var btn = document.getElementById("getsheet");
    btn.addEventListener("click", function(event) {
        var url = document.getElementById("urlhere").value;
        var id = '';
        var out = document.getElementById("output");

        try {
            id = url.split('spreadsheets/d/')[1].split('/')[0];
            out.style.color="#25c481";
            out.innerHTML = "Success!";

            localStorage.setItem('sheetid', id);
            location.reload();
        }
        catch(e) {
            out.style.color="#e83e3e";
            out.innerHTML = "Failed!";
            console.log(e);
        }
    })
}
