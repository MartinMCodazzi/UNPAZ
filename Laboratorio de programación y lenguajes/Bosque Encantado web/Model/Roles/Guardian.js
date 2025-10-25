// Martin Muñoz Codazzi 3/5/2025

const Rol = require("./Rol");

class Guardian extends Rol {
    calcularExtraAtaque() {
        //Siempre recibe un extra de 100.
        return 100;
    };
    cambiarRol() {
        //unicamente puede pasar a rol domador con una nueva mascota mítologica de 1 año de edad y sin cuernos.
        const mascota1 = new Mascota(1, false);
        return new Domador([mascota1]);
    };
    getEsExtraordinario(criatura) {
        //Es extraordinario si el poder mágico de la criatura es mayor a 50.
        return criatura.poderMagico > 50;
    }
}

module.exports = { Guardian };