// Este archivo contiene las diferentes clases de armas
class Arma {
    constructor(nombre, danio) {
        this.nombre = nombre;
        this.danio = danio
    }
    getTipo(){
        return this.nombre
    }
    getDanio() {
        return this.danio
    }
}

class ArmaDeFilo extends Arma {
    constructor(nombre, filo, longitud) {
        super(nombre, filo * longitud);
    }
}

class ArmaContundente extends Arma {
    constructor(nombre, peso) {
        super(nombre, peso);
    }
}

