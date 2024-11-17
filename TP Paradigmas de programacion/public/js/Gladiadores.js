// Este archivo contiene las diferentes clases de gladadores y sus métodos
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
        if (this.getSalud() > 0){
            const danioAplicado = this.getDefensaTotal() - nivelDanio < 0 ? this.getDefensaTotal() - nivelDanio : -5 ; // al menos que sufra algo de daño, evita loops infinitos
            this.salud = this.getSalud() + danioAplicado
            return "el " + this.constructor.name + " recibió " + - danioAplicado.toFixed(2) + " de daño total. Salud restante: " + this.getSalud().toFixed(2)
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
        return this.arma
    }
    getArmadura(){
        return this.armadura;
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
        return this.arma[0].getDanio() + this.getFuerza()
    };
   
    setArmadura(armadura) {
        this.armadura = armadura
    };

    /* Para un mirmillon, su defensa se calcula como los puntos de su armadura más su destreza*/
    getDefensaTotal(){
        return this.getTotalArmadura() + this.getDestreza();
    }
}
/* varias armas, no usan armadura, fuerza 10 destreza random
Ataque: fuerza + poder de armas +1 Destreza cada vez
Defensa: 1/2 Destreza */
class Dimachareus extends Gladiador {
    constructor(armas) {
        super(Math.random() * 30, 10, armas, [])
    }
    atacar() {
        this.destreza += 1;
        return this.arma.reduce((acum, armaActual) => (
            acum + armaActual.getDanio()
        ), 0) + this.getFuerza();
    };
    /* Para un dimachaerus, su defensa es la mitad de su destreza. */   
    getDefensaTotal(){
        return this.getDestreza() / 2
    }
}