import { expect } from 'chai';
import { Tarea, ComplejidadMinima, ComplejidadMedia, ComplejidadMaxima } from '../Clase 2 - Tareas.js';

describe('Tarea', function () {
    const tareaSimple = new Tarea('tareaSimple', 100);
    const tareaPadre = new Tarea('Padre', 5, [
        new Tarea('Hija1', 10),
        new Tarea('Hija2', 20),
        new Tarea('Hija3', 30)
    ]);

    it('Debe crear una tarea con lo minimo e indispensable', function () {
        expect(tareaSimple.identificador).to.equal('tareaSimple');
        expect(tareaSimple.duracion).to.equal(100);
        expect(tareaSimple.incluye.length).to.equal(0);
    });

    it('Debe crear tarea con subtareas correctamente ', function () {
        expect(tareaPadre.getDuracion()).to.equal(65);
    });

    it('Debe cambiar de dificultad correctamente', () => {
        tareaSimple.bajarDificultad();
        expect(tareaSimple.complejidad).to.be.instanceOf(ComplejidadMinima);
        tareaSimple.subirDificultad();
        expect(tareaSimple.complejidad).to.be.instanceOf(ComplejidadMedia);
        tareaSimple.subirDificultad();
        expect(tareaSimple.complejidad).to.be.instanceOf(ComplejidadMaxima);
        tareaSimple.subirDificultad();
        expect(tareaSimple.complejidad).to.be.instanceOf(ComplejidadMaxima);
        tareaSimple.complejidad = new ComplejidadMinima();
    })

    it('Calcular el costo correctamente con complejidad mínima sin Overhead', function () {
        const tareaCorta = new Tarea('Corta', 4);
        const tareaLarga = new Tarea('Larga', 10);
        expect(tareaCorta.getCosto()).to.equal(100);
        expect(tareaLarga.getCosto()).to.equal(200);
    });

    it('Calcular el costo correctamente con complejidad media sin Overhead', function () {
        const dificultadMediaCorta = new Tarea('MediaCorta', 2, [], new ComplejidadMedia());
        const dificultadMediaLarga = new Tarea('MediaLarga', 10, [], new ComplejidadMedia());
        expect(dificultadMediaCorta.getCosto()).to.equal(105);
        expect(dificultadMediaLarga.getCosto()).to.equal(210);
    });

    it('Calcular el costo correctamente con complejidad máxima sin Overhead', function () {
        const dificultadMaximaCorta = new Tarea('maximaCorta', 4, [], new ComplejidadMaxima());
        expect(dificultadMaximaCorta.getCosto()).to.equal(107);
        const dificultadMaximaLarga = new Tarea('maximaLarga', 20, [], new ComplejidadMaxima());
        expect(dificultadMaximaLarga.getCosto()).to.equal(10214);
    });

    it('Calcular el costo correctamente con complejidad mínima con Overhead', function () {
        const tareaPadre = new Tarea('Padre', 5, [ //200
            new Tarea('Hija1', 5), //100  
            new Tarea('Hija2', 5), //100 
            new Tarea('Hija3', 5), //100 
            new Tarea('Hija4', 5), //100 
        ]);
        //Da 624 porque getDuración incluye todas las subtareas
        expect(tareaPadre.getCosto()).to.equal(624);
    });

    it('Calcular el costo correctamente con complejidad media con Overhead', function () {
        const tareaPadre = new Tarea('Padre', 5, [ //200
            new Tarea('Hija1', 5), //100
            new Tarea('Hija2', 5), //100
            new Tarea('Hija3', 5), //100
            new Tarea('Hija4', 5), //100
        ], new ComplejidadMedia()); //(600 * 1.05) * 1.04
        expect(tareaPadre.getCosto()).to.equal(655.2);
    });

    it('Calcular el costo correctamente con complejidad máxima con Overhead', function () {
        const tareaPadreCorta = new Tarea('Padre', 1, [ //100
            new Tarea('Hija1', 1), //100
            new Tarea('Hija2', 1), //100
            new Tarea('Hija3', 1), //100
            new Tarea('Hija4', 1), //100
        ], new ComplejidadMaxima()); // (500 * 1.07) * 1.04
        expect(tareaPadreCorta.getCosto()).to.equal(556.4);
        const tareaPadreLarga = new Tarea('Padre', 5, [ //200
            new Tarea('Hija1', 1), //100
            new Tarea('Hija2', 1), //100
            new Tarea('Hija3', 2), //100
            new Tarea('Hija4', 2), //100
        ], new ComplejidadMaxima()); // ((600 * 1.07) + 1000)  * 1.04
        expect(tareaPadreLarga.getCosto()).to.equal(1707.68);
    });

    it('Debe agregar subtareas correctamente', function () {
        const tarea1 = new Tarea('T1', 4);
        const tarea2 = new Tarea('T2', 5);
        tarea1.agregar(tarea2);
        expect(tarea1.incluye).to.include(tarea2);
        expect(tarea1.incluye.length).to.equal(1);
    });
});