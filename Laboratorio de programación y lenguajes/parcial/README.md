# Practica Parcial I - Laboratorio de Programación

Comenzaste a trabajar en un empresa de seguridad informática y a los pocos día te encomiendan una tarea de determinar que usuarios no cumplirán con la nueva política de contraseñas que actualmente se está elaborando.

Tu misión es desarrollar un servicio web con un endpoint de consulta que lea el archivo de usuarios y determine cuales tienen un password asociado que no cumple con las reglas de la nueva política de seguridad para poder notificarles por correo que deberán ajustar sus contraseña.

## Política de seguridad

La política de seguridad todavía no está totalmente terminada, pueden agregarse y/o quitarse nuevas reglas en las próximas semanas. Nuestro desarrollo debe estar preparado para leer las reglas de seguridad desde un archivo independiente y seguir funcionando si se agregan o quitan reglas.

Hasta el momento hay definidas estas 6 reglas

1. Dado el password alfanumérico, la longitud mínima de dicho password debe ser de **8** caracteres.
2. Dado el password alfanumérico, la longitud máxima de dicho password debe ser de **12** caracteres.
3. Dado el password alfanumérico, no puede contener espacios en blanco.
4. Dado el password alfanumérico, debe contener al menos uno de los siguiente caracteres **!#$%&=**
5. Dado el password alfanumérico, debe contener al menos un dígito número.
6. Dado el password alfanumérico, el último caracter **no** puede ser ninguno de los definidos en la regla 4

## Archivo de Usuarios

Desde el sector de base de datos nos van a pasar un archivo json con la lista de todos los usuarios del sistema. Nos adelantaron el que formato de archivo va a ser el siguiente

```
[
    {
        userName: 'gonzager',
        email: 'gerardo.gonzalez@gmail.com",
        password: "1qaz!QAZ"
    },
    {
        userName: 'florcita1975',
        email: 'florcita1975@gmail.com",
        password: "flor1975"
    },
    ......
]
```

## Endpoint y Respuesta

El endpoint de consulta debe llamarse **/validador** y la respuesta deberá ser la lista de usuarios que no cumpla con al menos 1 regla de la política. La respuesta del endpoint sería el usuario que no cumple con su correspondiente email (pero no incluir el atributo password). Por ejemplo

```
[
    {
        userName: 'florcita1975',
        email: 'florcita1975@gmail.com",
    },
    ......
]
```

## Puerto de la aplicación

Debe poder configurar a través de variables de entorno en que puerto va a estar escuchando la aplicación.

## Estructura de directorios de la aplicación

La aplicación debe respetar la siguiente estructura de directorios

```
└── src
    ├── data
        ├── usuarios.json    # archivo json de usuarios con los password
    └── politica
        ├── reglas.js     # reglas que se pueden ir agregando y quitando
    └─index.js   # donde esta el endpoint /validator y listen por entorno
    └─package.json     # descripción y
```

## Ejemplo para hacer pruebas

```
[
  {
    "userName": "juanperez",
    "email": "juan.perez@hotmail.com",
    "password": "abc123!"
  },
  {
    "userName": "carloslopez",
    "email": "carlos.lopez@yahoo.com",
    "password": "clopez#2023"
  },
  {
    "userName": "anafernandez",
    "email": "ana.fernandez@outlook.com",
    "password": "aa f=23"
  },
  {
    "userName": "pedrorodriguez",
    "email": "pedro.rodriguez@gmail.com",
    "password": "rodr1Pedro="
  },

  {
    "userName": "jorgediaz",
    "email": "jorge.diaz@yahoo.com",
    "password": "jdiaz#1234567890"
  },

  {
    "userName": "elenasanchez",
    "email": "elena.sanchez@hotmail.com",
    "password": "elenita=1234"
  }
]
```

Los usuarios que no cumplen las reglas son:

1.  **juanperez**: reglas incumplidas: [ Longitud mínima de 8 carateres y termina en especial].

2.  **anafernandez**: reglas incumplidas: [ Longitud mínima de 8 carateres, No puede contener espacios en blanco].

3.  **pedrorodriguez**: reglas incumplidas: [El último caracter no puede ser caractere especial].

4.  **jorgediaz**: regals inclumplidas: [Longitud máxima de 12 caracteres].

Los usuarios que sí cumplen todas las reglas son:

1. carloslopez
2. elenasanchez

## Puntos extras para el 10 de nota

1. Generar un nuevo endpoind llamado **/validador/con-reglas** que reutilice el máximo posible del codigo realizado en el endpoint anterior **/validador** para que en la salida de este nuevo endpoint se incluya ls reglas que no cuemple cada usuario.

Ejemplo:

```
[
    {
        "userName": "juanperez",
        "email": "juan.perez@hotmail.com",
        "reglasInclumplidas": [
            "Reglas longitud < 8",
            "El último caracter no puede ser uno de los definidos en la regla 4"
        ]
    }
    .....
]
```

2. Utilizando parte del código que hay implementado crear un nuevo endpoint que retorne los ususarios que si cumple con las reglas. Al idea es reutilziar codigo que hayan realizado. El endpoint será llamado **/usuarios-correctos**

Siguiente con el ejemplo. El resultado debería ser:

```
[
    {
        "userName": "carloslopez",
        "email": "carlos.lopez@yahoo.com"
    },
    {
        "userName": "elenasanchez",
        "email": "elena.sanchez@hotmail.com"
    }
]
```
