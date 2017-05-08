var memorizedValue = null;
var startNewInput = true;
var displayedValue = '0';
document.querySelector('p').textContent = displayedValue;

for (var i = 0; i < 10; i++) {
    var digitButton = document.getElementById(i);
    digitButton.addEventListener('click', function(e) {
        if (startNewInput == true) {
            displayedValue = e.target.id;
            if (displayedValue != '0') {
                startNewInput = false;
            }
        } else {
            displayedValue += e.target.id;
        }
        document.querySelector('p').textContent = displayedValue;
    });
}

clearButton = document.getElementById('clear');
clearButton.addEventListener('click', function(e) {
    displayedValue = '0';
    document.querySelector('p').textContent = displayedValue;
});


plusButton = document.getElementById('+');
plusButton.addEventListener('click', function(e) {
    memorizedValue = displayedValue;
    startNewInput = true;
});


equalButton = document.getElementById('=');
equalButton.addEventListener('click', function(e) {
    if (memorizedValue != null) {
        var result = parseInt(displayedValue) + parseInt(memorizedValue);
        memorizedValue = null;
        displayedValue = result;
        document.querySelector('p').textContent = displayedValue;
    }
});