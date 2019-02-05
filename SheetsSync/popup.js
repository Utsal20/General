window.onload = function() {
    var table = document.getElementById("box");
    var xhr = new XMLHttpRequest();

    xhr.addEventListener("error", function(event) {
        alert('Failed to update.');
    })
    xhr.open('GET', 'https://sheets.googleapis.com/v4/spreadsheets/{id}/values:batchGet?ranges=A:B&key=AIzaSyAEgRnTTUxzniZcm7G2aivQ01mBmc_Pc8E', false);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send();
    var texts = JSON.parse(xhr.response).valueRanges[0].values;
    //table.innerText =  + " " + texts[texts.length - 1][1];

    var row;
    for (var i=0; i < texts.length; i++) {
        row = table.insertRow(-1);
        for (var j=0; j < 2; j++) {
            var cell = row.insertCell(-1);
            cell.innerHTML = texts[i][j];
        }
    }
}

$(window).on("load resize ", function() {
    var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
    $('.tbl-header').css({'padding-right':scrollWidth});
  }).resize();
