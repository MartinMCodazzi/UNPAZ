const { Router } = require ('express');

const route = Router(); // bàsicamente, lo mismo que app()
const users = require("../../data/users.json"); // Rquiero el listado de usuarios

route.get('/', (request, response) => {
    response.status(200).json(users) //devuelvo el listado de usuarios
});

// Hago un push a un array QUE ESTÀ EN MEMORIA, NO PERSISTE!
route.post("/", (req, res) => {
    const body = req.body;
    const id = Math.max(...users.map((u)=> u.id)) + 1
    const nuevo = {id, ...body};
    users.push(nuevo);
    res.status(201).json(nuevo);
  
})

module.exports = route; // Y exporto el listado de rutas que creè