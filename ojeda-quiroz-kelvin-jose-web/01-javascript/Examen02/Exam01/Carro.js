class Carro {
    constructor(placa, recorrido, numeroPuertas) {
        this.placa = placa;
        this.recorrido = recorrido;
        this.numeroPuertas = numeroPuertas;
        this.esNuevo = recorrido === 0;
        this.inicialPlaca = placa.split("")[0];
    }
}

export default Carro