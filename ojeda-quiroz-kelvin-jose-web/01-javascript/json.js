// Stringify y parse
const arregloUsuario =[
    {
        id:1,
        nombre: 'Kelvin'
    }
]

const arregloGuardado = JSON.stringify(arregloUsuario)
const usuario = {
    id:1,
    nombre: 'Adrian'
}

const objectoGuardado = JSON.stringify(usuario)
console.log('arregloGuardado', arregloGuardado)
console.log('TipoArregloGuardado', typeof(arregloGuardado))
console.log('objetoGuardado', objectoGuardado)
console.log('TipoObjetoGuardado', typeof(objectoGuardado))
const arregloRestaurado = JSON.parse(arregloGuardado)
const objectoRestaurado = JSON.parse(objectoGuardado)
console.log('arregloRestaurado', arregloRestaurado)
console.log('TipoArregloRestaurado', typeof arregloRestaurado)
console.log('objetoRestaurado', objectoRestaurado)
console.log('TipoObjetoRestaurado', typeof objectoRestaurado)