var displayedValue = '0';
document.querySelector('p').textContent = displayedValue;

for (var i = 0; i < 10; i++) {
    var digitButton = document.getElementById(i);
    digitButton.addEventListener('click', function(e) {
        if (displayedValue == '0') {
            displayedValue = e.target.id;
        } else {
            displayedValue += e.target.id;
        }
        document.querySelector('p').textContent = displayedValue;
    });
}

clearButton = document.getElementById('clear')
clearButton.addEventListener('click', function(e) {
    displayedValue = '0';
    document.querySelector('p').textContent = displayedValue;
});