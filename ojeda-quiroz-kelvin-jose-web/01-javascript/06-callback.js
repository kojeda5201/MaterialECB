const fs = require('fs'); // file system
                          // Importar modulo fs
// 06-ejemplo.txt -> Hola

// 1) Leer archivo:06-ejemplo.txt,
// luego imprimir en consola
// 2) Despues del paso 1, Leer archivo:01-variables.js
// , luego imprimir en consola
// 3) Crear un nuevo archivo llamaddo 06-nuevo-archivo.txt
// con el contenido de los otros dos archivos.


console.log('Primero')
fs.readFile(
    './06-ejemplo.txt',//Nombre del patch del archivo
    'utf-8', //cotificacion
    (errorLecturaPrimerArchivo, contenidoPrimerArchivo) => {
        console.log('Segundo')
        if (errorLecturaPrimerArchivo) {
            console.error("Error leyendo el archivo")
            throw new Error('Error leyendo el archivo')
        } else {
            fs.readFile(
                './01-Variable.js',
                'utf-8',
                (errorLecturaSegundoArchivo, contenidoSegundoArchivo) => {
                    console.log("Tercero")
                    if (errorLecturaSegundoArchivo) {
                        console.error("Error leyendo el segundo archivo")
                        throw new Error('Error leyendo el segundo archivo')
                    } else {
                        fs.writeFile(
                            './06-nuevo-archivo.txt',
                            contenidoPrimerArchivo+contenidoSegundoArchivo,
                            (errorTercerArchivo, contenidoTercerArchivo) => {
                                if(errorTercerArchivo){
                                    console.error("Error creando tercer archivo")
                                    throw new Error('Error creando tercer archivo')
                                }else{
                                    console.log("Sucess")
                                }

                            }
                        )
                    }
                }
            )
        }
    }
)
console.log('Cuarto')