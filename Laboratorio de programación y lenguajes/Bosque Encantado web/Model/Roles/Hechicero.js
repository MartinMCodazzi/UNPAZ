// Martin Muñoz Codazzi 3/5/2025

const Rol = require("./Rol");

class Hechicero extends Rol {
    calcularExtraAtaque() {
        //No recibe ningún extra.
        return 0
    };
    cambiarRol() {
        //solo puede pasar al rol guardían.
        return new Guardian();
    };
    getEsExtraordinario() {
        //Siempre es extraordinario.
        return true;
    }
}

module.exports = { Hechicero };