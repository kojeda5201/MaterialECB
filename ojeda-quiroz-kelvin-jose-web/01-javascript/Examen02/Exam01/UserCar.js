import inquirer from 'inquirer'
import Persona from './Persona.js'
import Carro from "./Carro.js";
import {
    saveDataPriviousData,
    saveDataDelete,
    readData
} from "./fileGesture.js";


async function eliminarPersona(idUsuario) {
    try {
        const personas = await readData();
        if (personas) {
            const personasActualizadas = personas.filter((persona) => persona.id !== idUsuario);
            await saveDataDelete(personasActualizadas);
            console.log('Usuario eliminado exitosamente');
        } else {
            console.log('No se encontró el listado de usuarios usuario');
        }
    } catch (error) {
        console.error('Error al eliminar el usuario:', error);
    }
}

async function modificarPersona(idPersonaModificar, personaModificar) {
    await eliminarPersona(idPersonaModificar)
    const respuesta = await inquirer.prompt([
        {
            type: 'list',
            name: 'opcionModificar',
            message: 'Seleccione una opción',
            choices: [
                'Modificar nombre',
                'Modificar edad',
                'Modificar estado civil',
                'Modificar id',
                'Salir',
            ],
        }
    ])
    const opcion = respuesta.opcionModificar
    switch (opcion) {
        case 'Modificar nombre':
            const modificarNombre = await inquirer.prompt([
                {
                    type: 'input',
                    name: 'nombre',
                    message: 'Ingrese el nombre de la persona: ',
                }

            ])
            personaModificar.nombre = modificarNombre.nombre
            break
        case 'Modificar edad':
            const modificarEdad = await inquirer.prompt([
                {
                    type: 'input',
                    name: 'edad',
                    message: 'Ingrese la edad de la persona: ',
                }

            ])
            personaModificar.edad = modificarEdad.edad
            break
        case 'Modificar estado civil':
            const modificarEstadoCivil = await inquirer.prompt([
                {
                    type: 'confirm',
                    name: 'estadoCivil',
                    message: 'Está casado?',
                }

            ])
            personaModificar.estadoCivil = (modificarEstadoCivil.estadoCivil) ? 'casado' : 'soltero'
            break
        default:
            console.log('Opción Inválida')
            break
    }
    saveDataPriviousData(personaModificar)
}

async function menuPrincipal() {
    const respuesta = await inquirer.prompt([
        {
            type: 'list',
            name: 'opcion',
            message: 'Seleccione una opción',
            choices: [
                'Añadir usuario',
                'Buscar usuario',
                'Eliminar usuario',
                'Modificar información de usuario',
                'Listar carros',
                'Ir menu carros',
                'Salir'
            ],
        },
    ])

    const opcion = respuesta.opcion
    switch (opcion) {
        case 'Añadir usuario':
            await anadirCarroUsuario()
            break
        case 'Buscar usuario':
            const idPersonaBuscar = await ingresarIdPersona()
            const personaBuscar = await buscarUsuario(idPersonaBuscar)
            if (personaBuscar !== undefined) {
                console.log(personaBuscar)
            } else {
                console.log("Persona no existe")
            }
            break
        case 'Eliminar usuario':
            const idPersonaEliminar = await ingresarIdPersona()
            const personaEliminar = await buscarUsuario(idPersonaEliminar)
            if (personaEliminar !== undefined) {
                await eliminarPersona(idPersonaEliminar)
            } else {
                console.log("Persona no existe")
            }

            break
        case 'Modificar información de usuario':
            const idPersonaModificar = await ingresarIdPersona()
            const personaModificar = await buscarUsuario(idPersonaModificar)
            if (personaModificar !== undefined) {
                await modificarPersona(idPersonaModificar, personaModificar)
            } else {
                console.log("Persona no existe")
            }
            break
        case 'Listar carros':
            const idPersonaCarro = await ingresarIdPersona()
            const personaCarro = await buscarUsuario(idPersonaCarro)
            if (personaCarro !== undefined) {
                console.log(personaCarro.carros)
            } else {
                console.log("Persona no existe")
            }
            break
        case 'Ir menu carros':
            const idPersonaMenuCarro = await ingresarIdPersona()
            const personaMenuCarro = await buscarUsuario(idPersonaMenuCarro)
            if (personaMenuCarro !== undefined) {
                await irMenuCarroRecursivo(personaMenuCarro)
            } else {
                console.log("Persona no existe")
            }
            break
        case 'Salir':
            process.exit
            break
        default:
            console.log('Opción Inválida')
            break

    }

}

async function irMenuCarroRecursivo(personaMenuCarro) {
    let respuesta = false
    do {
        await irMenuCarro(personaMenuCarro)
        respuesta = await inquirer.prompt([
            {
                type: 'confirm',
                name: 'recursivoMenuCarro',
                message: 'Quiere visualizar el menu de carro',
            },

        ])
    } while (respuesta.recursivoMenuCarro)
}

async function eliminarCarro(placaCarroEliminar, personaMenuCarro) {
    let carrosActualizados = []
    const carros = personaMenuCarro.carros
    if (carros) {
        carrosActualizados = carros.filter((carro) => carro.placa.toString().toUpperCase() !== placaCarroEliminar.toString().toUpperCase())
    }
    await eliminarPersona(personaMenuCarro.id)
    personaMenuCarro.carros = carrosActualizados
    saveDataPriviousData(personaMenuCarro)


}

async function irMenuCarro(personaMenuCarro) {
    const respuesta = await inquirer.prompt([
        {
            type: 'list',
            name: 'opcion',
            message: 'Seleccione una opción',
            choices: [
                'Añadir carro',
                'Buscar carro',
                'Eliminar carro',
                'Modificar información de carro',
                'Listar carros',
            ],
        },
    ])
    const opcion = respuesta.opcion
    switch (opcion) {
        case 'Añadir carro':
            let carro
            do {
                carro = await anadirCarro()
                if (carro !== undefined) {
                    personaMenuCarro.agregarCarro(carro)
                }
            } while (carro !== undefined)
            await eliminarPersona(personaMenuCarro.id)
            saveDataPriviousData(personaMenuCarro)
            break
        case 'Buscar carro':
            const placaCarro = await ingresarPlacaCarro()
            const buscarCarroBuscar = await buscarCarro(placaCarro, personaMenuCarro)
            if (buscarCarroBuscar !== undefined) {
                console.log(buscarCarroBuscar)
            } else {
                console.log("Carro no existe")
            }
            break
        case 'Eliminar carro':
            const placaCarroEliminar = await ingresarPlacaCarro()
            const buscarCarroEliminar = await buscarCarro(placaCarroEliminar, personaMenuCarro)
            if (buscarCarroEliminar !== undefined) {
                await eliminarCarro(placaCarroEliminar, personaMenuCarro)
            } else {
                console.log("Carro no existe")
            }
            break
        case 'Modificar información de carro':
            const placaCarroModificar = await ingresarPlacaCarro()
            const buscarCarroModificar = await buscarCarro(placaCarroModificar, personaMenuCarro)
            if (buscarCarroModificar !== undefined) {
                await modificarCarro(placaCarroModificar, personaMenuCarro, buscarCarroModificar)
            } else {
                console.log("Carro no existe")
            }
            break
        case 'Listar carros':
            console.log(personaMenuCarro.carros)
    }
}

async function modificarCarro(placaCarroModificar, personaMenuCarro, carroEncontrado) {

    const respuesta = await inquirer.prompt([
        {
            type: 'list',
            name: 'opcionModificarCarro',
            message: 'Seleccione una opción',
            choices: [
                'Modificar recorrido',
                'Modificar el numero de Puertas',
                'Salir',
            ],
        }
    ])
    const opcion = respuesta.opcionModificarCarro
    switch (opcion) {
        case 'Modificar recorrido':
            const modificarRecorrido = await inquirer.prompt([
                {
                    type: 'number',
                    name: 'recorridoCarro',
                    message: 'Ingrese el recorrido del carro: ',
                }

            ])
            carroEncontrado.recorrido = modificarRecorrido.recorridoCarro
            carroEncontrado.esNuevo = (modificarRecorrido.recorridoCarro === 0)
            break
        case 'Modificar el numero de Puertas':
            const modificarNumeroPuertas = await inquirer.prompt([
                {
                    type: 'number',
                    name: 'numeroPuertasCarro',
                    message: 'Ingrese el numero de puertas del carro: ',
                }

            ])
            carroEncontrado.numeroPuertas = modificarNumeroPuertas.numeroPuertasCarro
            break
        case 'Salir':
            break
    }
    await eliminarPersona(personaMenuCarro.id)
    let carrosActualizados = []
    const carros = personaMenuCarro.carros
    if (carros) {
        carrosActualizados = carros.filter((carro) => carro.placa.toString().toUpperCase() !== carroEncontrado.placa.toString().toUpperCase())
    }
    personaMenuCarro.carros = carrosActualizados
    personaMenuCarro.agregarCarro(carroEncontrado)
    saveDataPriviousData(personaMenuCarro)


}

async function buscarCarro(placaCarro, personaMenuCarro) {
    const carros = personaMenuCarro.carros
    if (carros) {
        const carroEncontrado = carros.find((carro) => carro.placa.toString().toUpperCase() === placaCarro.toString().toUpperCase())
        return carroEncontrado
    } else {
        return undefined
    }
}

async function ingresarPlacaCarro() {
    const respuesta = await inquirer.prompt([
        {
            type: 'input',
            name: 'placaCarro',
            message: 'Ingrese la placa del carro: ',
        }
    ])
    return respuesta.placaCarro.toString()
}


async function menuPrincipalRecursivo() {
    let respuesta = false
    do {
        await menuPrincipal()
        respuesta = await inquirer.prompt([
            {
                type: 'confirm',
                name: 'recursivoMenuPrincipal',
                message: 'Quiere visualizar el menu principal',
            },
        ])

    } while (respuesta.recursivoMenuPrincipal === true)
}

async function buscarUsuario(idPersona) {
    const personas = readData()
    if (personas) {
        const usuarioEncontrado = personas.find((persona) => persona.id.toString() === idPersona)
        return usuarioEncontrado
    } else {
        return undefined
    }
}

async function ingresarIdPersona() {
    const respuesta = await inquirer.prompt([
        {
            type: 'input',
            name: 'idUsuario',
            message: 'Ingrese el ID de la persona: ',
        }
    ])
    return respuesta.idUsuario.toString()
}

async function anadirCarroUsuario() {
    const persona = await solicitarDatos()
    let carro
    do {
        carro = await anadirCarro()
        if (carro !== undefined) {
            persona.agregarCarro(carro)
        }
    } while (carro !== undefined)
    saveDataPriviousData(persona)
}

async function anadirCarro() {
    const respuestaAnadir = await inquirer.prompt([
        {
            type: 'confirm',
            name: 'carroAnadir',
            message: 'Desea añadir un carro?',
        },
    ])

    if (respuestaAnadir.carroAnadir) {
        const respuestasCarro = await inquirer.prompt([
            {
                type: 'input',
                name: 'placa',
                message: 'Ingrese la placa del carro: ',
            },
            {
                type: 'number',
                name: 'recorrido',
                message: 'Ingrese el recorrido del carro: ',
            },
            {
                type: 'number',
                name: 'numeroPuertas',
                message: 'Ingrese el número de puertas del carro: ',
            },
        ])
        const carro = new Carro(
            respuestasCarro.placa.toUpperCase(),
            respuestasCarro.recorrido,
            respuestasCarro.numeroPuertas
        )
        return carro
    } else {
        return undefined
    }
}

async function solicitarDatos() {
    const respuestas = await inquirer
        .prompt([
            {
                type: 'input',
                name: 'nombre',
                message: 'Ingrese su nombre:',
            },
            {
                type: 'number',
                name: 'edad',
                message: 'Ingrese su edad:',
            },
            {
                type: 'confirm',
                name: 'estadoCivil',
                message: '¿Está casado/a?',
            },
            {
                type: 'input',
                name: 'id',
                message: 'Ingrese su número de cédula:',
            },
        ])

    const persona = new Persona(
        respuestas.nombre,
        respuestas.edad,
        respuestas.estadoCivil,
        respuestas.id,
    );
    return persona

}

export {
    menuPrincipalRecursivo
};

