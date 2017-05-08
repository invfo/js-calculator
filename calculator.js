var memorizedValue = null;
var lastOperation = null;
var startNewInput = true;
var displayedValue = '0';
document.querySelector('p').textContent = displayedValue;

function manageDigitInput(e) {
    var digit = e.target.id;

    if (startNewInput == true) {
        if (digit == '.') {
                displayedValue = '0.';
                startNewInput = false;
        } else {
            displayedValue = digit;
            if (displayedValue != '0') {
                startNewInput = false;
            }
        }
    } else {
        if (! (digit == '.' && displayedValue.includes('.'))) {
            displayedValue += digit;
        }
    }

    document.querySelector('p').textContent = displayedValue;
}

for (var i = 0; i < 10; i++) {
    var digitButton = document.getElementById(i);
    digitButton.addEventListener('click', manageDigitInput);
}

dotButton = document.getElementById('.');
dotButton.addEventListener('click', manageDigitInput);

clearButton = document.getElementById('clear');
clearButton.addEventListener('click', function(e) {
    startNewInput = true;
    displayedValue = '0';
    document.querySelector('p').textContent = displayedValue;
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


var operationButtons = document.getElementsByClassName('operation');
for (var i = 0; i < operationButtons.length; i++) {
    var buttonElt = operationButtons[i];
    buttonElt.addEventListener('click', function(e) {
        memorizedValue = displayedValue;
        lastOperation = e.target.id;
        startNewInput = true;
    })
}

/*

plusButton = document.getElementById('+');
plusButton.addEventListener('click', function(e) {
    memorizedValue = displayedValue;
    lastOperation = '+'
    startNewInput = true;
});

multiplyButton = document.getElementById('*');
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
*/
