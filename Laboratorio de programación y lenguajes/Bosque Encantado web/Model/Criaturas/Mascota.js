// Martin Muñoz Codazzi 3/5/2025

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

module.exports = { Mascota };