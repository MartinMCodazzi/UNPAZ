// Martin Muñoz Codazzi 3/5/2025

const Router = require("express");
const route = Router();

const db = require("../data/querys")

// Estas rutas responderán a /criaturas/
route.get("/", (req, res) => {         
        res.render("criaturas-show",{"criaturas": db.get_todas_criaturas()})
})

route.get("/crear",(req,res)=>{
    res.render("criaturas-create",{
        "roles" : db.get_todos_roles(),
        "colonias" :db.get_todas_colonias(),
        "tipoCriaturas" :db.get_todos_tiposCriatura()
        })
});

route.post("/crear",(req,res)=>{
    console.log(req.body)
    res.status(201).send();
});

module.exports = route;

