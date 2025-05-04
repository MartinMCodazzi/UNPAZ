//Martìn Muñoz Codazzi 15/04/2025

class Criatura { // Creo que esta serìa una clase abstracta (o una interface?)
    constructor(rol, edad = 1, poderMagico = 1, astucia = 1) {};
    getEdad() {
        throw new Error("Método no implementado en la clase Criatura");
    }
    cambiarRol() {
        throw new Error("Método no implementado en la clase Criatura");
    };
    calcularAtaque() {
        throw new Error("Método no implementado en la clase Criatura");
    };
    getEsAstuta() {
        throw new Error("Método no implementado en la clase Criatura");
    };
    getEsFormidable() {
        throw new Error("Método no implementado en la clase Criatura"); 
    }
}

class Duende extends Criatura {
    // Según internet, no es necesario llamar al constructor de la clase padre si la clase hija no difiere en nada
    calcularAtaque() {
        throw new Error("Método no implementado en la clase Duende"); // Los duendes tienen un 10% màs de ataque
    };
    getEsAstuta() {
        //Los duendes nunca son astutos.
        throw new Error("Método no implementado en la clase Duende");
    };
}

class Hada extends Criatura {
    constructor(rol, edad = 1, poderMagico = 1, astucia = 1) {
        //Cuando nacen todas las hadas pueden volar 2 kilometros
        throw new Error("Método no implementado en la clase Hada");
    }
    getEsAstuta() {
        //Un hada se considera astuta si su astucia es mayor a 50. 
        throw new Error("Método no implementado en la clase Hada");
    };
    sumarKmQuePuedeVolar() {
        //Con el tiempo pueder ir aumentando paulatinamente la cantidad de kilometros hasta una máximo de 25.
        throw new Error("Método no implementado en la clase Hada");
    }
    getEsFormidable() {
        //Además de tener un rol extraordinario las Hada necesitan una condicion adicional que puedan volar mas de 10 kilometros.
        throw new Error("Método no implementado en la clase Hada");
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
        throw new Error("Método no implementado en la clase Domador");
    }
    calcularExtraAtaque() {
        //Recibe un extra de 150 unidades por cada mascota mitólogica que tiene cuernos.
        throw new Error("Método no implementado en la clase Domador");
    };
    cambiarRol() {
        //puede pasar a Hechicero si tiene al menos una mascota magica con cuernos y en caso contarario se produce un error en el ritual que lo cancela
        throw new Error("Método no implementado en la clase Domador");
    };
    getEsExtraordinario(criatura) {
        //Es extraorinario si el poder mágico de la criatura es mayor o igual a 15, y si todas sus mascotas mágicas son veteranas. 
        throw new Error("Método no implementado en la clase Domador");
    }
}

class Guardian extends Rol {
    calcularExtraAtaque() {
        //Siempre recibe un extra de 100.
        throw new Error("Método no implementado en la clase Guardian");
    };
    cambiarRol() {
        //unicamente puede pasar a rol domador con una nueva mascota mítologica de 1 año de edad y sin cuernos.
        throw new Error("Método no implementado en la clase Guardian");
    };
    getEsExtraordinario(criatura) {
        //Es extraordinario si el poder mágico de la criatura es mayor a 50.
        throw new Error("Método no implementado en la clase Guardian");
    }
}

class Hechicero extends Rol {
    calcularExtraAtaque() {
        //No recibe ningún extra.
        throw new Error("Método no implementado en la clase Hechicero");
    };
    cambiarRol() {
        //solo puede pasar al rol guardían.
        throw new Error("Método no implementado en la clase Hechicero");
    };
    getEsExtraordinario() {
        //Siempre es extraordinario.
        throw new Error("Método no implementado en la clase Hechicero");
    }
}

class Mascota {
    constructor(edad = 1, cuernos = false) {
        throw new Error("Método no implementado en la clase Mascota");
    };
    esVeterana() { //
        throw new Error("Método no implementado en la clase Mascota");
    }
    tieneCuernos() {
        throw new Error("Método no implementado en la clase Mascota");
    }
}

class Colonia {
    constructor(area, criaturas = []) {
        throw new Error("Método no implementado en la clase Mascota");
    }
    getPoderOfensivo() {
        throw new Error("Método no implementado en la clase Mascota");
    }
    getPoderDefensivo() {
        throw new Error("Método no implementado en la clase Mascota");
    }
    atacar(coloniaQueDefiende) { // No sé si debería atacar un area o a otra colonia
        /* Si el poder ofensivo de la colonia invasora supera al poder defensivo del área, el área es usurpada por la colonia invasora,es decir, comienza a habitarla. 
        Y si, en cambio, el área resultara vencedora, la conquista no tiene éxito; la colonia defensora mantiene el control, y todos los integrantes de la colonia invasora pierden el 15% de su poder mágico. */
        throw new Error("Método no implementado en la clase Mascota");
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
        throw new Error("Método no implementado en la clase Castillo");
    }
}

class Claro extends Area {
    //el poder defensivo es 100 unidades adicionales al poder ofensivo de la colonia que lo habita.
    getPoderDefensivo(colonia) {
        throw new Error("Método no implementado en la clase Claro");
    }
}
