const express = require('express');
const app = express();

const reglas = require('../reglas/reglas-direcciones.js');
const clientes = require('./data/clientes.json');
//Configuración Puerto configurable por variable de entorno (PORT).
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Función para validar que una direccion cumple todas las reglas
const validarDireccion = (direccion) => {
    return Object.values(reglas).every(regla => regla(direccion));
};

// Función para filtrar clientes con direcciones válidas
const filtrarClientesConDireccionesValidas = () => {
    return clientes.filter(cliente => validarDireccion(cliente.direccion));
};

app.get('/direcciones-validas', (req, res) => {
    const clientesValidos = filtrarClientesConDireccionesValidas();
    let respuesta = clientesValidos.map(cliente => ({ 'nombre': cliente.nombre, 'email': cliente.email }));

    res.json(respuesta);
});

app.get('/direcciones-invalidas', (req, res) => {
    const clientesValidos = filtrarClientesConDireccionesValidas();
    let respuesta = clientes.filter(cliente => !clientesValidos.includes(cliente)).map(cliente => ({ 'nombre': cliente.nombre, 'email': cliente.email }));

    res.json(respuesta);
});

app.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto ${PORT}`);
});