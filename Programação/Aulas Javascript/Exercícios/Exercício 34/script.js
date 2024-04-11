let calculadora = {
    somar: function (a, b) {
        return a + b;
    },
    subtrair: function (a, b) {
        return a - b;
    },
    multiplicar: function (a, b) {
        return a * b;
    },
    dividir: function (a, b) {
        return a / b;
    }
}

console.log(calculadora.somar(4, 2));
console.log(calculadora.subtrair(4, 2));
console.log(calculadora.multiplicar(4, 2));
console.log(calculadora.dividir(4, 2));