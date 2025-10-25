// Martin Muñoz Codazzi 3/5/2025

class Criatura { // Creo que esta serìa una clase abstracta (o una interface?)
    constructor(rol, edad = 1, poderMagico = 1, astucia = 1) {
        this.edad = edad;
        this.poderMagico = poderMagico;
        this.astucia = astucia;
        this.rol = rol;
    };
    getEdad() {
        return this.edad;
    }
    cambiarRol() {
        this.rol = this.rol.cambiarRol();
    };
    calcularAtaque() {
        return this.poderMagico * 10 + this.rol.calcularExtraAtaque(); // Los duendes tienen un 10% màs de ataque
    };
    getEsAstuta() {
        throw new Error("Método no implementado en la clase Criatura");
    };
    getEsFormidable() {
        return this.getEsAstuta() | this.rol.getEsExtraordinario(this);
    }
}

module.exports = { Criatura };