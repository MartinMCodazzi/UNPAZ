/* Este archivo contiene:
    - Instanciado de armas
    - Instanciado de armaduras
    - Instanciado de gladiadores
    - Asignadores de texto a elementos web
    - Lógicas de pelea
*/

//creacion de armas
let armasDisponibles = [];
function crearArmas() {
    // Acá se agregan armas nuevas
    arma1 = new ArmaDeFilo("gladius", Math.random(), Math.floor(Math.random() * 100));
    arma2 = new ArmaContundente("Mazo", Math.floor(Math.random() * 20) + 10);
    arma3 = new ArmaContundente("Estrella del Alba", Math.floor(Math.random() * 40) + 10);
    arma4 = new ArmaDeFilo("Espada larga", Math.random(), Math.floor(Math.random() * 200));
    armasDisponibles = [arma1, arma2, arma3, arma4];
}
function asignadorArmas(cantidad) {
    let armas = [];
    for (i = 0; i < cantidad; i++) {
        crearArmas(); // Esto lo hago para randomizar cada vez que se vaya a asignar un arma
        armas.push(armasDisponibles[Math.floor(Math.random() * armasDisponibles.length)])
    }
    return armas;
}

//creacion de armaduras
escudo1 = new Escudo();
casco1 = new Casco();

function asignadorArmaduras(){
   if (Math.floor(Math.random()*2 + 1) % 2 == 0){
       return [escudo1, casco1];
   } else return [casco1]
}

//creacion de gladiadores
gladiador1 = new Mirmillon(asignadorArmas(1), asignadorArmaduras());
gladiador2 = new Dimachareus(asignadorArmas(2));

//agregando selectores web
const labelNombreJ1 = document.getElementById("nombreJ1");
const labelNombreJ2 = document.getElementById("nombreJ2");
const labelAtaqueJ1 = document.getElementById("ataqueJ1");
const labelAtaqueJ2 = document.getElementById("ataqueJ2");
const labelDefensaJ1 = document.getElementById("defensaJ1");
const labelDefensaJ2 = document.getElementById("defensaJ2");
const labelBtnJ1 = document.getElementById("btnJ1");
const labelBtnJ2 = document.getElementById("btnJ2");
const detalleAtaqueJ1 = document.getElementById("detalleAtaqueJ1")
const detalleAtaqueJ2 = document.getElementById("detalleAtaqueJ2");
const detalleDefensaJ1 = document.getElementById("detalleDefensaJ1");
const detalleDefensaJ2 = document.getElementById("detalleDefensaJ2");
const arena = document.getElementById("arena");
const btnDentroDeModal = document.getElementById("botonDentroDeModal");

refrescarLabels();
function refrescarLabels() {
    labelNombreJ1.innerText = gladiador1.constructor.name;
    labelNombreJ2.innerText = gladiador2.constructor.name;    
  
    labelBtnJ1.innerText = gladiador1.constructor.name;
    labelBtnJ2.innerText = gladiador2.constructor.name;
    refrescarDetalleAtaque();
    refrescarDetalleDefensa();
}
function refrescarDetalleAtaque() {
    labelAtaqueJ1.innerHTML = gladiador1.atacar().toFixed(2);
    labelAtaqueJ2.innerHTML = gladiador2.atacar().toFixed(2);
    detalleAtaqueJ1.innerHTML = detalleAtaque(gladiador1);
    detalleAtaqueJ2.innerHTML = detalleAtaque(gladiador2);
}
function refrescarDetalleDefensa(){
    labelDefensaJ1.innerHTML = gladiador1.getDefensaTotal().toFixed(2);
    labelDefensaJ2.innerHTML = gladiador2.getDefensaTotal().toFixed(2);
    detalleDefensaJ1.innerHTML = detalleDefensa(gladiador1);
    detalleDefensaJ2.innerHTML = detalleDefensa(gladiador2);
}

//Esta función muestra el modal con el resultado de la batalla
function mostrarArena(jugador, rival) {    
    arena.innerHTML = "<ul>"
    while (gladiador1.getSalud() > 0 && gladiador2.getSalud() > 0) {

        if (document.getElementById('ataquesRandom').checked) {
            ataquesRandom();
        } else {
            ataqueSecuencial(jugador,rival)
        }

        if (gladiador1.getSalud() == 0) {
            arena.innerHTML += "<strong>Es un golpe mortal!</strong>, " + gladiador2.constructor.name + " gana!"
        }
        if (gladiador2.getSalud() == 0) {
            arena.innerHTML += "<strong>Es un golpe mortal!</strong>, " + gladiador1.constructor.name + " gana!"
        }
    }
    arena.innerHTML += "</ul>"

    // texto del boton del modal
    if (jugador.getSalud() == 0) {
        btnDentroDeModal.innerHTML = "Mejor suerte para le próxima";
    } else {
        btnDentroDeModal.innerHTML = "Gracias, me siento con suerte"
    }
    //Reestablecer salud de los gladiadores
    gladiador1.salud = 100;
    gladiador2.salud = 100;

    // Tipos de enfrentamientos
    function ataquesRandom() {
        let randomizador = Math.floor(Math.random() * 1000);
        if (randomizador % 2 == 0) {
            arena.innerHTML += "<li>" + gladiador1.constructor.name + " ataca!</li>"
            arena.innerHTML += "<ul><li>" + gladiador2.defender(gladiador1.atacar()) + "</li></ul>";
        } else {
            arena.innerHTML += "<li>" + gladiador2.constructor.name + " ataca!</li>"
            arena.innerHTML += "<ul><li>" + gladiador1.defender(gladiador2.atacar()) + "</li></ul>";
        }
    }
    function ataqueSecuencial(jugador, rival){
        arena.innerHTML += "<li>" + jugador.constructor.name + " ataca!</li>"
        arena.innerHTML += "<ul><li>" + rival.defender(jugador.atacar()) + "</li></ul>";
        if (rival.getSalud() > 0){
            arena.innerHTML += "<li>" + rival.constructor.name + " ataca!</li>"
            arena.innerHTML += "<ul><li>" + jugador.defender(rival.atacar()) + "</li></ul>";
        } 
    }
};

function detalleAtaque(gladiador) {
    let armas = "<ul>"
    for (let arma of gladiador.getArmas()) {
        armas += "<li>Tipo: " + arma.getTipo() + " - Daño: " + arma.getDanio().toFixed(2) + "</li>"
    }
    armas += "<li>Fuerza del gladiador: " + gladiador.getFuerza().toFixed(2) + "</li>";
    armas += "</ul>"
    return armas
}

function detalleDefensa(gladiador){
    let defensa = "<ul>"; 
    for (let armadura of gladiador.getArmadura()){
        defensa += "<li>Tipo: " + armadura.getTipo() + " - Defensa: " + armadura.getArmadura(gladiador) +"</li>";
    }
    defensa += "<li> Destreza: " + gladiador.getDestreza().toFixed(2) + "</li></ul>"
    return defensa
}

function cambiarArma(gladiador) {
    gladiador.cambiarArma(asignadorArmas(gladiador.getArmas().length))
    refrescarDetalleAtaque()
}
function cambiarArmadura(gladiador){
    gladiador.setArmadura(asignadorArmaduras());
    refrescarDetalleDefensa();
}