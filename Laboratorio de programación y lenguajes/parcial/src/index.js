const express = require("express");
const app = express();

const reglas = require('../politica/reglas.js'); // el doble punto me hizo perder mucho tiempoooooo!!!!
const usuarios = require('./data/usuarios.json');

const PORT = process.env.PORT || 3000; // uso linux
app.use(express.json());

const validarContrasena = (password) => {
    return Object.values(reglas).every(regla => regla(password));
};

const usuariosValidos = usuarios.filter(usuario => validarContrasena(usuario.password))
const usuariosInvalidos = usuarios.filter(usuario => !usuariosValidos.includes(usuario));

app.get("/validador", (request, response) => {
    const respuesta = usuariosInvalidos.map(usuario => ({ 'username': usuario.userName, 'email': usuario.email }))
    response.status(200).json(respuesta);
})

app.get('/validador/con-reglas', (request, response) => {
    const respuesta = usuariosInvalidos.map(usuario => {
        let reglasIncumplidas = [];

        reglasIncumplidas = Object.keys(reglas).filter(nombreRegla => 
            !reglas[nombreRegla](usuario.password)
        );
        
        return {
            'username': usuario.userName,
            'email': usuario.email,
            'reglas_incumplidas': reglasIncumplidas
        };
    });
    
    response.status(200).json(respuesta);
});

app.get('/usuarios-correctos', (request, response) => {
    const respuesta = usuariosValidos.map(usuario => ({ 'username': usuario.userName, 'email': usuario.email }))
    response.status(200).json(respuesta);
});

app.listen(PORT, () => {
    console.log('Servidor Node.js corriendo en puerto: ' + PORT)
});