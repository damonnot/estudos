// O que acontece dentro de uma função fica separado do escopo global

let y = 10;

function imprimir() {
    let y = 150;
    console.log(y)
}

imprimir();

console.log(y);
