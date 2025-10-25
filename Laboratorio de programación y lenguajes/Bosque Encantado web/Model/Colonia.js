// Martin Muñoz Codazzi 3/5/2025

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

module.exports = { Colonia };