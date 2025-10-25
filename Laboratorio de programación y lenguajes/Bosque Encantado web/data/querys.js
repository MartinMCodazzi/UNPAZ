// Martin Muñoz Codazzi 4/5/2025

const Database = require("better-sqlite3");
const db = new Database("./data/database.sqlite", /* { verbose: console.log } */);

function get_todas_criaturas() {
    return db.prepare(`
        SELECT 
		    c.criatura_id,
            c.edad, 
            c.poderMagico,
            c.astucia,        
            col.descripcion AS colonia,
            r.descripcion AS rol_descripcion,
            tc.descripcion AS tipoCriatura
        FROM criaturas c
        INNER JOIN colonias col ON c.colonia_id = col.colonia_id
        INNER JOIN roles r ON c.rol_id = r.rol_id
        INNER JOIN tiposCriatura tc ON c.tipoCriatura_id = tc.tipoCriatura_id
        GROUP BY c.rol_id;`).all();
}

function get_todos_roles(){
    return db.prepare(`
        SELECT
            r.rol_id,
            r.descripcion
        FROM roles r`).all();
}

function get_todas_colonias(){
    return db.prepare(`
        SELECT
            c.colonia_id,
            c.descripcion
        FROM colonias c`).all();
}

function get_todos_tiposCriatura(){
    return db.prepare(`
        SELECT
            tc.tipoCriatura_id,
            tc.descripcion
        FROM tiposCriatura tc`).all();
}

module.exports = { 
    get_todas_criaturas,
    get_todos_roles,
    get_todas_colonias,
    get_todos_tiposCriatura

};