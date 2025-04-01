//Martín Muñoz Codazzi 01/04/2025
export class Tarea {
    constructor(identificador, duracion, tareas = [], complejidad = new ComplejidadMinima()) {
        this.identificador = identificador;
        this.duracion = duracion;
        this.incluye = tareas;
        this.complejidad = complejidad;
    }
    agregar(tarea) {
        this.incluye.push(tarea);
    }
    getDuracion() {
        return this.incluye.reduce((acumulador, tarea) => acumulador + tarea.getDuracion(), this.duracion);
        //En Tareas simples, esto último devuelve sólo la duracion propia
    }
    getSubtotal() {
        return this.incluye.reduce(
            (acumulador, elemento) => acumulador + (elemento.getDuracion() <= 5 ? 100 : 200),
            this.getDuracion() <= 5 ? 100 : 200);
    }
    getCosto() {
        //Incluir complejidad
        const subtotal = this.complejidad.modificadorComplejidad(this) + this.getSubtotal();
        //Overhead
        const total = this.incluye.length > 3 ? subtotal * 1.04 : subtotal
        return total;
    }
    bajarDificultad() {
        this.complejidad = this.complejidad.bajarDificultad();
    }
    subirDificultad() {
        this.complejidad = this.complejidad.subirDificultad();
    }
}

export class Complejidad {
    modificadorComplejidad(tarea) { }
    bajarDificultad() { return this }
    subirDificultad() { return this }
}

/* Complejidad mínima: no agrega porcentaje extra. */
export class ComplejidadMinima extends Complejidad {
    modificadorComplejidad(tarea) {
        return 0
    }
    subirDificultad() { return new ComplejidadMedia() }
}

/* Complejidad media: agrega un 5% extra */
export class ComplejidadMedia extends Complejidad {
    modificadorComplejidad(tarea) {
        return tarea.getSubtotal() * 0.05 //Retorna el 5% del total de la tarea
    }
    bajarDificultad() { return new ComplejidadMinima() }
    subirDificultad() { return new ComplejidadMaxima() }
}

/* - Complejidad máxima:
  - Si el tiempo es menor o igual a 10 unidades entonces agrega un extra del 7%
  - Si el tiempo es mayor a 10 unidades entonces agrega un extra 
  del 7% más $1000 por cada día que la tarea exceda las 10 unidades. */
export class ComplejidadMaxima extends Complejidad {
    modificadorComplejidad(tarea) {
        const subtotal = tarea.getSubtotal();
        if (tarea.getDuracion() <= 10) {
            return subtotal * 0.07;
        } else {
            return (subtotal * 0.07) + 1000 * (tarea.getDuracion() - 10);
        }
    }
    bajarDificultad() { return new ComplejidadMedia() }
}