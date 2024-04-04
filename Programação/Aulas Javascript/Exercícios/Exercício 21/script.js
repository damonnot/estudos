function verificardado (dado) {
    if (typeof dado === "number") {
        console.log("Número")

    } else if (typeof dado === "boolean") {
        console.log("Booleano")

    } else if (typeof dado === "string") {
        console.log("String")
    }
}

    verificardado("ola")