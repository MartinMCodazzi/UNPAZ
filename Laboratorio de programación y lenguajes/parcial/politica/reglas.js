const caracteres = ["!", "#", "$", "%", "&", "="];
const reglas = {
    longitud_minima: (password) => password.length >= 8,

    longitud_maxima: (password) => password.length <= 12,

    sin_espacios: (password) => !password.includes(" "),

    caracteres_requeridos: (password) => {        
        return caracteres.some((caracter) => password.includes(caracter));
    },

    contiene_numero: (password) => {
        //Intenté hacerlo de una forma más elegante, pero no me funcionó
        const numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
        return numeros.some((numero) => password.includes(numero));
    },

    caracter_final_permitido: (password) => {
        return !caracteres.includes(password[password.length - 1]);
    }
}

module.exports = reglas;