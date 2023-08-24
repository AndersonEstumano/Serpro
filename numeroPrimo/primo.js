function isPrime(number) {
    if (number <= 1) {
        return false;
    }

    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            return false;
        }
    }

    return true;
}

const inputNumber = 10; // Substitua pelo número que deseja verificar

if (isPrime(inputNumber)) {
    console.log(`${inputNumber} é primo.`);
} else {
    console.log(`${inputNumber} não é primo.`);
}
