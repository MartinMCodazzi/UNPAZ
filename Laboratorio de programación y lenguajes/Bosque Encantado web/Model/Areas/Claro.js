// Martin Muñoz Codazzi 3/5/2025

const Area = require("./Area");

class Claro extends Area {
    //el poder defensivo es 100 unidades adicionales al poder ofensivo de la colonia que lo habita.
    getPoderDefensivo(colonia) {
        return colonia.criaturas.reduce((acumulador, criatura) =>
            acumulador + criatura.calcularAtaque(), 0) + 100;
    }
}

module.exports = { Claro };