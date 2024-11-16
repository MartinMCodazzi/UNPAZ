class Gladiador {
    constructor(destreza, fuerza, arma, armadura) {
        this.salud = 100;
        this.destreza = destreza;
        this.fuerza = fuerza;
        this.arma = arma;
        this.armadura = armadura;
    }
    atacar() { }; // depende de las diferentes implementaciones
    defender(nivelDanio) {   
        /* console.log("nivel ataque: " + nivelDanio)
        console.log("nivel defensa: " + this.getDefensaTotal())    */  
        if (this.getSalud() > 0){
            const danioAplicado = this.getDefensaTotal() - nivelDanio < 0 ? this.getDefensaTotal() - nivelDanio : -5 ; // al menos que sufra algo de daño, evita loops infinitos
            this.salud = this.getSalud() + danioAplicado
            console.log("el " + this.constructor.name + " recibió " + - danioAplicado.toFixed(2) + " de daño total. Salud restante: " + this.getSalud().toFixed(2) + "\n")
        }
    }; 
    cambiarArma(arma) { 
        this.arma = arma;
    };
    getSalud() {
        return this.salud <= 0 ? 0 : this.salud;
    }
    getTotalArmadura() {
        return this.armadura.reduce((acum, armadura) => (
            acum + armadura.getArmadura(this)
        ),0)
    }
    getFuerza() {
        return this.fuerza;
    }
    getDestreza(){
        return this.destreza;
    }
    getDefensaTotal(){}
    getArmas(){
        return this.armas
    }
    
}

/* solo un arma, puede cambiar de armadura. Fuerza variable, destreza siempre 15
Ataque: poder de arma + fuerza
Defensa: puntos de armadura + destreza */
class Mirmillon extends Gladiador {
    constructor(arma, armadura) {
        super(15, Math.random() * 10, arma, armadura);
    }
    atacar() {
        return this.arma.getDanio() + this.getFuerza()
    };
   
    cambiarArmadura(armadura) {
        this.armadura = armadura
    };
    getDefensaTotal(){
        return this.getTotalArmadura() + this.destreza;
    }
}
/* varias armas, no usan armadura, fuerza 10 destreza random
Ataque: fuerza + poder de armas +1 Destreza cada vez
Defensa: 1/2 Destreza */
class Dimachareus extends Gladiador {
    constructor(armas) {
        super(Math.random() * 10, 10, armas, [])
    }
    atacar() {
        this.destreza += 1;
        return this.arma.reduce((acum, armaActual) => (
            acum + armaActual.getDanio()
        ), 0) + this.getFuerza();
    };   
    getDefensaTotal(){
        return this.getDestreza() / 2
    }
}

class Armadura {
    getArmadura() { }
}
class Casco extends Armadura {
    getArmadura() {
        return 10
    }
}
class Escudo extends Armadura {
    getArmadura(gladiador) { // no es lo ideal, porque recibe el objeto completo, pero sirve...
        return 5 + gladiador.destreza * 0.1;
    }
}

//TODO: Crear otros tipos de armadura

class Arma {
    constructor(nombre, danio) {
        this.nombre = nombre;
        this.danio = danio
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

//creacion de armas
arma1 = new ArmaDeFilo("gladius", Math.random() * 10, Math.random() * 20);
arma2 = new ArmaContundente("Mazo", Math.random() * 10);

//creacion de armaduras
escudo1 = new Escudo()
casco1 = new Casco()
armaduras = [escudo1, casco1]

//creacion de gladiadores
gladiador1 = new Mirmillon(arma1, armaduras);
gladiador2 = new Dimachareus([arma1, arma2]);

//Pruebas

//console.log(arma1.getDano()); // esto da 10
//console.log(gladiador1.getTotalArmadura());
//onsole.log(gladiador1.arma);
//console.log(gladiador1.atacar());
//console.log(gladiador2.atacar())
//console.log(gladiador1)
//gladiador2.defender(gladiador1.atacar());
//gladiador1.defender(gladiador2.atacar());

// Pequeña lógica de ataque y defensa
while (gladiador1.getSalud() > 0 && gladiador2.getSalud() > 0 ){
    let randomizador = Math.round(Math.random() * 10000);
    //console.log(randomizador)
    if (randomizador % 2 == 0){
        console.log(gladiador1.constructor.name + " ataca!")
        gladiador2.defender(gladiador1.atacar());
    } else {
        console.log(gladiador2.constructor.name + " ataca!")
        gladiador1.defender(gladiador2.atacar());
    }
    if (gladiador1.getSalud() == 0){
        console.log("Es un golpe mortal!, "+ gladiador2.constructor.name + " gana!")
    }
    if (gladiador2.getSalud() == 0){
        console.log("Es un golpe mortal!, "+ gladiador1.constructor.name + " gana!")
    }

}
