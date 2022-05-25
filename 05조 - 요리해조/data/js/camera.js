var loadFile = function(event) {
    var output = document.getElementById('pictureFromCamera');
    var outputr = document.getElementById('pictureFromCamera-r');
    output.src = URL.createObjectURL(event.target.files[0]);
    outputr.src = URL.createObjectURL(event.target.files[0]);
};