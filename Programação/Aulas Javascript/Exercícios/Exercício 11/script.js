
var nome = prompt("Qual o seu nome?")
var idade = prompt("Qual sua idade?")

if (idade >= 18) {
    var temCnh = prompt("Você possui CNH? Reponda sim ou não")
        if (temCnh == "sim"){
        console.log("Parabéns!")
        } else{
        console.log("Seu fudido")
        }
}if (idade < 18) {
    console.log("Tem nem pelo no sacokkkj")
}