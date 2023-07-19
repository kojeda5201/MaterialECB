let nombre: string = 'Adrian' // primitivo
let nombre2: String = 'Adrian2' // Clase String
 // compilar tsc ./01-variables.ts --target es3 --ignoreDeprecations 5.0
// transpilo a javascript

let edad: number = 32
let casado: boolean = false
let fecha: Date = new Date()
let sueldo: number
sueldo = 12.4

//Duck typing
let apellido = 'Ojeda'
//apellido = 1
apellido = 'ojeda'
apellido.toUpperCase()

let anyVariable: any = 2
anyVariable ='2'
anyVariable= true
anyVariable = () => '2'

let anyLimitVariable: number | string | Date = '2'
anyLimitVariable = '2'
anyLimitVariable = 'dos'
anyLimitVariable = new Date()
anyLimitVariable = 222
let numeroUnico: number = 1 // para igualar a otros se castea
numeroUnico = numeroUnico + Math.pow((anyLimitVariable as number), 2)