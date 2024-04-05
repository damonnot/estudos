let num = 1
let num2 = 2
let num3 = 3
let num4 = 4

function imprimirNumeros(...args){
    for(let i = 0; i < args.length; i++){
        console.log(args[i])

    }
}

imprimirNumeros(num,num2,num3,num4);
    console.log("pausa");
imprimirNumeros(num2,num4)
    console.log("pausa")
imprimirNumeros(2,4,5,6,78,8,5,3,1);