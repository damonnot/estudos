function negPos(x){
    if (x < 0) {
        return(Math.abs(x))
    }
    else if (x >= 0)
    return(x)
}
    console.log(negPos(-20))