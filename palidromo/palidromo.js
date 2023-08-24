const readline = require('readline')

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

r1.question('Type a word: ', function(answer) {
    if (palidromo(answer)) {
        console.log('The string is a palindrome');
        r1.close()
    }
    else {
        console.log('THe string is not a palindrome')
        r1.close()
    }
}

)
function palidromo(str) {
    let processedStr = str.toLowerCase().replace(/[\W_]/g, '');
    let reverseStr = processedStr.split('').reverse().join('');
    return processedStr === reverseStr
}