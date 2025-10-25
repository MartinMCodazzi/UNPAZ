// Martin Muñoz Codazzi 3/5/2025

const Area = require("./Area")

class Castillo extends Area {
    getPoderDefensivo(colonia) {
        //el poder defensivo de un castillo es igual a 200 unidades por cada criatura formidable de la colonia que lo habita.
        const criaturasFormidables = colonia.criaturas.reduce((acumulador, criatura) =>
            acumulador + (criatura.getEsFormidable() ? 1 : 0), 0);
        return criaturasFormidables * 200;
    }
}

module.exports = { Castillo };