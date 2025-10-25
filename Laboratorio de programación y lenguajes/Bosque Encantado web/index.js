// Martin Muñoz Codazzi 4/5/2025

const express = require("express");
const app = express();
const rutaCriaturas = require("./src/criaturas.routes");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Le digo a Express que use EJS
app.set('view engine', 'ejs');

// Le digo dónde están las vistas
app.set('views', './views');

// Middleware para servir CSS/JS
app.use(express.static('public'));

//ruta a criaturas
app.use('/criaturas', rutaCriaturas);

app.listen(3001);

// Estos son los css y js de bootstrap
app.use("/css",express.static("./node_modules/bootstrap/dist/css"));
app.use("/js",express.static("./node_modules/bootstrap/dist/js"));
