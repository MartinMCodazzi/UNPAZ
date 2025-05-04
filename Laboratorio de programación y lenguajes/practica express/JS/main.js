const utils = require('./utils')

const express = require('express'); // https://expressjs.com/en/guide/routing.html
const app = express(); 
const cursos = require('./data/cursos.json');
const routerUsers = require("./src/routes/user.routes")

app.use(express.json()); // Habilita a app a leer el body como JSON


app.use("/users", routerUsers); //le digo que /users lo maneja "routerUsers"

app.get('/cursos', (request, response) => {
    response.status(418).json(    // I AM A TEAPOT :D
        cursos
    )
});

app.listen(4001, () => {
    console.log('La aplicacion arrancó en el puerto 4001')
})