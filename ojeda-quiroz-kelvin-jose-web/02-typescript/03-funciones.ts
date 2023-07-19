//03-funciones.ts
function sumarNumeros(
    numeroInicial: number, // requerido
    ...numerosInfinitos: number[]  // requerido
): number {
    return numeroInicial;
}
function imprimir(
    mensaje?: string  // opcional
): void { // undefined
    console.log('Hola ' + mensaje ? mensaje : 'bienvenido');
}

const arregloNumeros: number[] = [1, 2];
const arregloNumerosDos: Array<number> = [1, 2];
const arregloNumerosTres: (number | string | boolean)[] = [1, 'dos', true, 1, 'dos', true];
const arregloNumerosCuatro: Array<number | string | boolean> = [1, 'dos', true, 1, 'dos', true];
let arregloNumerosCinco: number[] | string[] = [1, 2];
arregloNumerosCinco = ['uno', 'dos'];