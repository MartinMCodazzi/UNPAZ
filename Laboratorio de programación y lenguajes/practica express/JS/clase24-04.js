const {fn1,fn2,fn3} = require('./funciones'); // Importa de a uno
const funciones = require('./funciones'); // <- IMPORTA TODO, COMO UN OBJETO!

console.log(funciones);

const arrayNoPasa = [20,30,35,45,52];
const arrayPasa = [20,30,40,50,60];

const fns = [fn1,fn2,fn3];
const fns2 = Object.values(funciones);

console.log(
    arrayPasa.every((elemento) => fns.every((funcion) => funcion(elemento)))
)
console.log(
    arrayPasa.every((elemento) => fns2.every((funcion) => funcion(elemento)))
)

/* console.log("Para el array que NO debe pasar: " + arrayNoPasa.every((elemento) => 
    fn1(elemento) && fn2(elemento) && fn3(elemento)
))

console.log("Para el array que debe pasar: " + arrayPasa.every((elemento) => 
    fn1(elemento) && fn2(elemento) && fn3(elemento)
)) */
