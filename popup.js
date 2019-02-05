window.onload = function() {
    var note = document.getElementById("note");
    var xhr = new XMLHttpRequest();

    xhr.addEventListener("error", function(event) {
        alert('Failed to update.');
    })
    xhr.open('GET', '', false);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send();
    var texts = JSON.parse(xhr.response).valueRanges[0].values;
    note.innerText = decodeURI(texts[texts.length - 1]);
    
    var save = document.getElementById("save");

    save.addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("error", function(event) {
            alert('Failed to save.');
        })
        xhr.open('POST', '', false);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send();
    })
}
