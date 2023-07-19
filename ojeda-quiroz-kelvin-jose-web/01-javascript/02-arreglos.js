// 02-arreglo.js
let arreglo = [6,7,8,9,10]

arreglo = 1
arreglo = true
arreglo = undefined
arreglo = null
arreglo = {}
arreglo = [true, 1, 1.1, "Adrian", 'Vicente', undefined, null, {}, [1,2]]
arreglo = [2,3,4,5,6]

//for of

for(let numero of arreglo){ //Valores
    console.log('numero: ',numero)
}


// for in

for (let indice in arreglo){  //Indice
    console.log('indice: ', indice)
}


// Agregar un elemento al final del arreglo
arreglo.push(11)


//Eliminar al final
arreglo.pop()

// Agregar al inicio del arreglo
arreglo.unshift(4)

//slice(indice donde empenzar, numero elementos elimandos, items agregados)
// ej: arreglo.splice( 0 indice, 3 eliminar 3 elemento, 1,2,3,4 agregar del 1-4 )

arreglo.splice(0, 0, 1,2,3)
console.log(arreglo)

arreglo.splice(0, 1, 1,2,3)
console.log(arreglo)

//Para retornar el número del indice con idexOf
const indiceNueve = arreglo.indexOf(3)
console.log(indiceNueve)