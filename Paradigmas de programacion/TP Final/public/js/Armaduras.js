// Este archivo contiene las diferentes clases de armaduras
class Armadura {
    constructor(tipo){
        this.tipo = tipo;
    }
    getArmadura() { }
    getTipo(){
        return this.tipo;
    }
}
class Casco extends Armadura {
    constructor(){
        super("Casco");
    }
    getArmadura() {
        return 10
    }
}
class Escudo extends Armadura {
    constructor(){
        super("Escudo");
    }
    getArmadura(gladiador) { // no es lo ideal, porque recibe el objeto completo, pero sirve...
        return 5 + (gladiador.getDestreza() * 0.1);
    }
}