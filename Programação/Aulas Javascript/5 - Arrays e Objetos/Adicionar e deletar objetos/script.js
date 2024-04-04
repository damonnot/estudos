let carro = {
    marca: "VW",
    portas: 4,
    eletrico: "false",
    motor: 1.0,
}
console.log(carro.portas);

//para remover
delete carro.portas;
console.log(carro.portas);

//para adicionar
carro.tetoSolar = true;
console.log(carro.tetoSolar);