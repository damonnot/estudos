function numAleatorio(num) {
    //Math.floor para arredondar o número pra baixo, Math.random para gerar um número aleatório.
    return Math.floor(Math.random() * num + 1);
}

console.log(numAleatorio(15));