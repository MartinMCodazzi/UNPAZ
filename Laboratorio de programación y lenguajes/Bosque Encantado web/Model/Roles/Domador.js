// Martin Muñoz Codazzi 3/5/2025

const Rol = require("./Rol");

class Domador extends Rol {
    constructor(mascotas = []) {
        super();
        this.mascotas = mascotas;
    }
    calcularExtraAtaque() {
        //Recibe un extra de 150 unidades por cada mascota mitólogica que tiene cuernos.
        return this.mascotas.reduce((acumulador, mascota) =>
            acumulador + (mascota.tieneCuernos() ? 150 : 0), 0);
    };
    cambiarRol() {
        //puede pasar a Hechicero si tiene al menos una mascota magica con cuernos y en caso contarario se produce un error en el ritual que lo cancela
        if (this.mascotas.some(mascota => mascota.tieneCuernos())) {
            return new Hechicero();
        } else {
            console.error("No fué posible el cambio de rol, no se cumplen los requisitos");
            return this;
        }
    };
    getEsExtraordinario(criatura) {
        //Es extraorinario si el poder mágico de la criatura es mayor o igual a 15, y si todas sus mascotas mágicas son veteranas. 
        return ((criatura >= 15) && (this.mascotas.every(mascota => mascota.esVeterana())));
    }
}

module.exports = { Domador };