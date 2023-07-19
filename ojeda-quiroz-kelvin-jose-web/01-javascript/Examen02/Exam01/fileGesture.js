import fs from 'fs'
import Persona from "./Persona.js";
import Carro from "./Carro.js";

function readData() {
    try {
        const data = fs.readFileSync('01-datos.json', 'utf-8')
        if (data === '') {
            fs.writeFileSync('01-datos.json', JSON.stringify([]))
        } else {
            const parsedData = JSON.parse(data)
            const personas = parsedData.map((item) => {
                const persona = new Persona(
                    item.nombre,
                    item.edad,
                    (item.estadoCivil === 'casado' ? true : false),
                    item.id
                )
                item.carros.forEach((carro) => {
                    const newCar = new Carro(
                        carro.placa,
                        carro.recorrido,
                        carro.numeroPuertas
                    )
                    persona.agregarCarro(newCar)
                })
                return persona
            })
            return personas
        }

    } catch (error) {
        console.error('Error al leer los datos: ', error.message)
    }
}

function saveDataDelete(personas) {
    try {
        fs.writeFileSync('01-datos.json', JSON.stringify(personas))
    } catch (error) {
        console.error('Error al guardar los datos después de delete: ', error);
    }
}


function saveDataPriviousData(persona) {
    try {
        let datosActuales = [];
        if (fs.existsSync('01-datos.json')) {
            const data = fs.readFileSync('01-datos.json', 'utf-8');
            if (data === '') {
                fs.writeFileSync('01-datos.json', JSON.stringify(datosActuales))
            } else {
                datosActuales = JSON.parse(data);
            }
        }
        datosActuales.push(persona);
        fs.writeFileSync('01-datos.json', JSON.stringify(datosActuales));
        console.log('Datos guardados exitosamente');
    } catch (error) {
        console.error('Error al guardar los datos: ', error);
    }
}

export {
    saveDataDelete,
    saveDataPriviousData,
    readData

}