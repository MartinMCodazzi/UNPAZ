// Martín Muñoz Codazzi 20-03-2025


// Simulador de vehiculo
/* Se solicita modelar oscomponentes necesarios para desarrollar una funcionalidad simple de un software de simulacion de vehiculos
los vehiculos tiene como atributos: cant de combustible (en litros), kilometraje (km recorridos), consumo en km/l velocidad máxima en km/h, tipo de conduccion
Sólo existen 3 tipos de conduccion,  pero se pueden agregar más, de ser necesario. C tipo de conduccion afecta el consumo y la velocidad máxima del auto de la siguente manera:
  1. Ecológica: consumo 16Km/l vel maxima: 120Km/k
  2. Standard: consumo: 10Km/l vel maxima: 150Km/h
  3. Deportiva: consumo 5Km/l vel maxima: 200Km/h

El vehículo puede cambiar el tipo de conducción, pero únicamente con la siguiente secuencia Eco -> Stan -> Depo -> Eco
Avance del vehículo: los vehiculos del simulador siempre inician en modo Eco y con 0 kilometraje, pero se les indica la cantidad de combustible al crearse. 
La simulación es avanzar indicandole una cantidad de km a recorrer
Al avanzar eben restar la cantidad de combustible la cantidad consumida para recorrer la cantidad solicitada
agregar los km recorridos al kilometraje total del vehiculo
Si el combustible no es suficiente para recorrer la distancia solicitada, el vehiculo avanzará hasta donde le alcance el combustible, actualizara sus atributos combustible y kilometraje e informatá un error de que no pudo comp
letar el recorrido solicidado con el siguente mensaje 'Combustible insuficiente, sólo pude recorrer x del total de y km
 */

class tipoConduccion{
    constructor(consumo, velMaxima){
        this.setVelMaxima(velMaxima);
        this.setConsumo(consumo);
    }
    getConsumo(){
        return this.consumo;
    }
    getVelMaxima(){
        return this.velMaxima;
    }
    setConsumo(consumo){
        this.consumo = consumo;
    }
    setVelMaxima(velMaxima){
        this.velMaxima = velMaxima;
    }
    siguiente(){
        return this;
    };
    anterior(){
        return this;
    };
}

class Ecologica extends tipoConduccion{
    constructor(){
        super(16,120);
    }
    siguiente(){
        return new Standard();
    }
}
class Standard extends tipoConduccion{
    constructor(){
        super(10,150);
    }
    siguiente(){
        return new Deportiva();
    }
    anterior(){
        return new Ecologica();
    }
}
class Deportiva extends tipoConduccion{
    constructor(){
        super(5,200);
    }    
    anterior(){
        return new Standard();
    }
}

class Vehiculo {
    constructor(combustible){
        this.combustible = combustible > 0 ? combustible : 0;
        this.kilometraje = 0;
        this.tipoConduccion = new Ecologica();
    }

    avanzar(kilometros){
        const combustibleNecesario = (1/this.tipoConduccion.getConsumo()) * kilometros;
        const kilometrosPosibles = this.combustible / ( 1/ this.tipoConduccion.getConsumo())  

        this.kilomtraje += Math.min(kilometros, kilometrosPosibles);
        this.combustible = Math.max(0, this.combustible - combustibleNecesario);
        
        if (kilometros > kilometrosPosibles){
            console.error('Combustible insuficiente, sólo pude recorrer',kilometrosPosibles,'kilómetros, del total de',kilometros,'km');
        }
    }

    cambiarTipo(){
        this.tipoConduccion = this.tipoConduccion.siguiente();
    }
}

v1 = new Vehiculo(20);
console.log(v1.tipoConduccion.getConsumo());
v1.cambiarTipo();
console.log(v1.tipoConduccion.getConsumo());
v1.avanzar(1000);

