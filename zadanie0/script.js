let secretNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;
let maxAttempts = 5;

function checkGuess() {
    let guess = parseInt(document.getElementById('guessInput').value);
    let message = document.getElementById('message');

    attempts++;

    if (guess < secretNumber) {
        message.textContent = "Слишком маленькое число. Попробуйте снова.";
    } else if (guess > secretNumber) {
        message.textContent = "Слишком большое число. Попробуйте снова.";
    } else {
        message.textContent = `Поздравляем! Вы угадали число за ${attempts} попыток.`;
        document.getElementById('guessInput').disabled = true;
    }

    if (attempts >= maxAttempts) {
        message.textContent = `К сожалению, вы исчерпали все попытки. Загаданное число было: ${secretNumber}.`;
        document.getElementById('guessInput').disabled = true;
    }
}
