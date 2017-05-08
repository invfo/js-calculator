var memorizedValue = null;
var lastOperation = null;
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
    lastOperation = '+'
    startNewInput = true;
});


equalButton = document.getElementById('=');
equalButton.addEventListener('click', function(e) {
    if (memorizedValue != null) {

        var result;

        switch(lastOperation) {
            case '+':
                result = parseInt(displayedValue) + parseInt(memorizedValue);
                break;
            case '*':
                result = parseInt(displayedValue) * parseInt(memorizedValue);
                break;
            case '-':
                result = parseInt(memorizedValue) - parseInt(displayedValue);
                break;
            case '/':
                result = parseInt(memorizedValue) / parseInt(displayedValue);
                result = +result.toFixed(5);
                break;
        }

        if (result == 'Infinity') {
          startNewInput = true;
          displayedValue = 'ERROR';
        } else {
          displayedValue = result;
        }

        if (result == 0) {
            startNewInput = true;
        }
        memorizedValue = null;
        lastOperation = null;
        document.querySelector('p').textContent = displayedValue;
    }
});

multiplyButton = document.getElementById('x');
multiplyButton.addEventListener('click', function(e) {
    memorizedValue = displayedValue;
    lastOperation = '*'
    startNewInput = true;
});

subtractButton = document.getElementById('-');
subtractButton.addEventListener('click', function(e) {
    memorizedValue = displayedValue;
    lastOperation = '-'
    startNewInput = true;
});

divideButton = document.getElementById('/');
divideButton.addEventListener('click', function(e) {
    memorizedValue = displayedValue;
    lastOperation = '/'
    startNewInput = true;
});
