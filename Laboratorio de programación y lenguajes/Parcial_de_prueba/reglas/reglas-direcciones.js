const reglas = {
    //La dirección debe tener entre 20 y 60 caracteres.
    longitud: (direccion) => direccion.length >= 20 && direccion.length <= 60,
    //Debe incluir un número de puerta o apartamento.
    formato: (direccion) => {
        const numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
        return numeros.some(numero => direccion.includes(numero));
    },
    //No puede contener símbolos como ! @ # $ % ^ & * ( ) _ +.
    caracteres_prohibidos: (direccion) => {
        const caracteresProhibidos = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"];
        return !caracteresProhibidos.some((caracter) => direccion.includes(caracter))
    },
    //Debe incluir al menos una de: Calle, Avenida, Bulevar, Pasaje.
    palabras_requeridas: (direccion)=>{
        const palabras = ["Calle", "Avenida", "Bulevar", "Pasaje"];
        return palabras.some((palabra) => direccion.includes(palabra));
    },
    //El código postal (si existe) debe estar al final de la dirección.
    consistencia: (direccion) => {
        const palabras = direccion.split(" ");
        const ultimaPalabra = palabras[palabras.length - 1];
        const numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
        return ultimaPalabra.split("").every(caracter => numeros.includes(caracter)) || palabras.length === 1;
    },
    //Sin abreviaturas: No permite abreviaturas como "Av." (debe ser "Avenida").
    sin_abreviaturas: (direccion) => {
        const abreviaturas = ["Av", "Avda", "Blvr", "Pje"];
        return !abreviaturas.some((abreviatura) => direccion.includes(abreviatura));
    },
    // La primera letra de cada palabra debe ser mayúscula.
    mayusculas:(direccion) => {
        const palabras = direccion.split(" ");
        return palabras.every((palabra) => palabra[0] === palabra[0].toUpperCase());
    }
}

module.exports = reglas;