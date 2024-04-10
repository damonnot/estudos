const cachorro = {
    raca: "Sem raça definida",
    uivar: function() {
        console.log("Auuuuuuuuuu");
    },
    rosnar: function(){
        console.log("Grrrrrrrr");
    },
    setRaca: function(raca) {
        this.raca = raca;
    }
}

console.log(cachorro.raca);

cachorro.setRaca('Pastor Alemão');

console.log(cachorro.raca);