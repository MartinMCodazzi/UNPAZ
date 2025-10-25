// Martín Muñoz Codazzi 03/05/2025

const Criatura = require("./Criatura.js");

class Duende extends Criatura {
    // Según internet, no es necesario llamar al constructor de la clase padre si la clase hija no difiere
    calcularAtaque() {
        return super.calcularAtaque() * 1.1; // Los duendes tienen un 10% màs de ataque
    };
    getEsAstuta() {
        //Los duendes nunca son astutos.
        return false;
    };
}

module.exports = { Duende };