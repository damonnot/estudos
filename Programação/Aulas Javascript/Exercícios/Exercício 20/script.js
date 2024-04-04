function print(texto) {
    console.log(texto)
}

function autoescola(idade) {
    if (idade >= 18)
        print(`Com ${idade} anos você já pode dirigir.`);
    else
        print(`Com ${idade} anos você não pode dirigir.`);
}

autoescola(21);
autoescola(12);