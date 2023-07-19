// 07-Promesas.js
const fs = require('fs')

function promesaEsPar(numero) {
    const miPrimerPromesa = new Promise(
        (resolve, reject) => {
            if (numero % 2 == 0) {
                resolve(numero);
            } else {
                reject(':( no es par');
            }
        }
    )
    return miPrimerPromesa
}

promesaEsPar(4)
    .then(
        (data) => {
            console.log('DATA', data)//4
            return promesaElevarAlCuadrado(data)
        }
    ).then(
    (data) => {
        console.log('DATA', data)//4
        return promesaElevarAlCuadrado(data)
    }
).then(
    (data) => {
        console.log('DATA', data)//4
    }
).catch(
    (error) => {
        console.error('ERROR', error)//string
    }
).finally(
    () => {
        console.log('Finally')
    }
)

function promesaElevarAlCuadrado(numero) {
    return new Promise((res) => res(Math.pow(numero, 2)))
}

/*
* Una funcion que acepte como parametro una variable
* del "path" del archivo y otra variable con el "contenidoArchivo".
* Utilizar el modulo 'fs' para leer el archivo en ese "path" y anadir el
* "contenidoArchivo" a ese archivo.
* */

function leerArchivo(path, contenidoAnterior) {
    return new Promise(
        (res, rej) => {
            fs.readFile(
                path,
                'utf-8',
                (errorLectura, contenido) => {
                    if (errorLectura) {
                        console.error(errorLectura)
                        rej('Error leyendo el archivo')
                    } else {
                        console.log('Escrito contenido')
                        if (contenidoAnterior === undefined) {
                            res(contenido)
                        } else {
                            res(contenidoAnterior + contenido)
                        }

                    }
                }
            )
        }
    )
}

function leerArchivoOriginal(path, contenidoAnterior) {
    return new Promise(
        (res, rej) => {
            fs.readFile(
                path,
                'utf-8',
                (errorLectura, contenido) => {
                    if (errorLectura) {
                        console.error(errorLectura)
                        rej('Error leyendo el archivo')
                    } else {
                        console.log('Escrito contenido')
                        res(contenido)


                    }
                }
            )
        }
    )
}

function escribirArchivo(path, contenido) {
    return new Promise(
        (res, rej) => {
            fs.writeFile(
                path,
                contenido,
                (errorEscritura, errorLectura) => {
                    if (errorEscritura) {
                        console.error(errorEscritura)
                        rej('Error creando el archivo')
                    }
                }
            )
        }
    )
}

const pathLectura1 = './06-ejemplo.txt'
const pathLectura2 = './01-Variable.js'
const pathEscritura = './07-nuevo-archivo.txt'
const pathEscrituraProfe='./07-nuevo-archivo-alternativa-profe.txt'
const pathEscrituraAsync='./07-nuevo-archivo-async.txt'


console.log("\nPromesas\n")
leerArchivo(pathLectura1).then(
    (data) => {
        //console.log('DATA', data)//hola ya me voy
        return leerArchivo(pathLectura2, data)
    }
).then(
    (data) => {
        return escribirArchivo(pathEscritura, data)
    }
)


function concatenarArchivos(path1, path2, path3){
    let contenidoTotal = ''
    leerArchivoOriginal(path1)
        .then(
            (contenidoPrimer)=>{
                contenidoTotal += contenidoPrimer
                return(leerArchivoOriginal(path2))
            }
        ).then(
        (contenidoSegundo)=>{
            contenidoTotal+=contenidoSegundo
            return(escribirArchivo(path3, contenidoTotal))
        }
    )
}

concatenarArchivos(pathLectura1, pathLectura2, pathEscrituraProfe)


async function concatenarArchivosAsync (path1, path2, path3){
    const contenidoArchivo1 = await leerArchivo(path1)
    const contanidoArchivo2 = await leerArchivo(path2)
    const contenidoFinal = contenidoArchivo1 + contanidoArchivo2
    await escribirArchivo(path3, contenidoFinal)
}

concatenarArchivosAsync(pathLectura1, pathLectura2, pathEscrituraAsync)
