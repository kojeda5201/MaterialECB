class Persona {
    constructor(nombre, edad, estadoCivil, id) {
        this.nombre = nombre;
        this.edad = edad;
        this.estadoCivil = estadoCivil ? 'casado': 'soltero';
        this.id = id;
        this.carros = [];

    }
    agregarCarro(carro) {
        this.carros.push(carro);
    }
}

export default Persona