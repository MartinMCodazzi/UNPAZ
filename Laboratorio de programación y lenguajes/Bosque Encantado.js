//Martìn Muñoz Codazzi 02/04/2025

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

class Duende extends Criatura {
    // Según internet, no es necesario llamar al constructor de la clase padre si la clase hija no difiere
    calcularAtaque() {
        return super.calcularAtaque() * 1.1; // Los duendes tienen un 10% màs de ataque
    };
    getEsAstuta() {
        //Los duendes nunca son astutos.
        return false;
    };
}

class Hada extends Criatura {
    constructor(rol, edad = 1, poderMagico = 1, astucia = 1) {
        //Cuando nacen todas las hadas pueden volar 2 kilometros
        super(rol, edad, poderMagico, astucia);
        this.kmQuePuedeVolar = 2;
    }
    getEsAstuta() {
        //Un hada se considera astuta si su astucia es mayor a 50. 
        return this.astucia > 50
    };
    sumarKmQuePuedeVolar() {
        //Con el tiempo pueder ir aumentando paulatinamente la cantidad de kilometros hasta una máximo de 25.
        this.kmQuePuedeVolar = this.kmQuePuedeVolar < 25 ? this.kmQuePuedeVolar + 1 : 25;
    }
    getEsFormidable() {
        //Además de tener un rol extraordinario las Hada necesitan una condicion adicional que puedan volar mas de 10 kilometros.
        return super.getEsFormidable() && this.kmQuePuedeVolar > 10;
    }
}

class Rol {
    calcularExtraAtaque() {
        throw new Error("Método no implementado en la clase Rol");
    };
    cambiarRol() {
        throw new Error("Método no implementado en la clase Rol");
    };
    getEsExtraordinario(criatura) {
        throw new Error("Método no implementado en la clase Rol");
    }
}

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
        throw new Error("Método no implementado en la clase Domador");
    };
    getEsExtraordinario(criatura) {
        //Es extraorinario si el poder mágico de la criatura es mayor o igual a 15, y si todas sus mascotas mágicas son veteranas. 
        return ((criatura >= 15) && (this.mascotas.every(mascota => mascota.esVeterana())));
    }
}

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

class Mascota {
    constructor(edad = 1, cuernos = false) {
        this.edad = edad;
        this.cuernos = cuernos;
    };
    esVeterana() {
        return this.edad >= 10
    }
    tieneCuernos() {
        return this.cuernos;
    }
}

class Colonia {
    constructor(area, criaturas = []) {
        this.area = area;
        this.criaturas = criaturas;
    }
    getPoderOfensivo() {
        return this.criaturas.reduce((acumulador, criatura) =>
            acumulador + criatura.calcularAtaque(), 0);
    }
    getPoderDefensivo() {
        return this.area.gerPoderDefensivo(this);
    }
    atacar(coloniaQueDefiende) { // No sé si debería atacar un area o a otra colonia
        /* Si el poder ofensivo de la colonia invasora supera al poder defensivo del área, el área es usurpada por la colonia invasora,es decir, comienza a habitarla. 
        Y si, en cambio, el área resultara vencedora, la conquista no tiene éxito; la colonia defensora mantiene el control, y todos los integrantes de la colonia invasora pierden el 15% de su poder mágico. */
        if (coloniaQueDefiende.getPoderDefensivo() < this.getPoderOfensivo()) {
            this.area = coloniaQueDefiende.area;
            coloniaQueDefiende.area = undefined;
        } else {
            this.criaturas.forEach(criatura => criatura.poderMagico *= 0.85);
        }
    }
}

class Area {
    getPoderDefensivo(colonia) {
        throw new Error("Método no implementado en la clase Area");
    }
}

class Castillo extends Area {
    getPoderDefensivo(colonia) {
        //el poder defensivo de un castillo es igual a 200 unidades por cada criatura formidable de la colonia que lo habita.
        const criaturasFormidables = colonia.criaturas.reduce((acumulador, criatura) =>
            acumulador + (criatura.getEsFormidable() ? 1 : 0), 0);
        return criaturasFormidables * 200;
    }
}

class Claro extends Area {
    //el poder defensivo es 100 unidades adicionales al poder ofensivo de la colonia que lo habita.
    getPoderDefensivo(colonia) {
        return colonia.criaturas.reduce((acumulador, criatura) =>
            acumulador + criatura.calcularAtaque(), 0) + 100;
    }
}
//Te debo las pruebas :]