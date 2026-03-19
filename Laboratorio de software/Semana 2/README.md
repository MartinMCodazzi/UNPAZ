## Laboratorio de software - Semana 2

ENUNCIADO
=========
Se desea desarrollar una aplicación en Java que modele un sistema simple
de alquiler de vehículos.
La empresa trabaja con vehículos de distintos tipos. Todos los vehículos
comparten los siguientes atributos:
- marca
- modelo
- precio por día de alquiler
Además, existen dos tipos particulares de vehículos:
- Auto: debe incluir la cantidad de puertas.
- Moto: debe incluir la cilindrada.
Todo vehículo que pueda ser alquilado debe ofrecer una operación que
permita calcular el precio total del alquiler según la cantidad de días.
El sistema también debe contemplar clientes. De cada cliente se necesita
almacenar:
- nombre
- dni
Asimismo, se deben registrar reservas. Cada reserva debe relacionar:
- un cliente !
- un vehículo !
- una cantidad de días de alquiler
La reserva debe permitir mostrar la información vinculada al cliente,
al vehículo y el total a pagar.
Por último, se solicita implementar una clase genérica que permita
almacenar objetos en memoria, de manera reutilizable para distintos
tipos de elementos del sistema.
Se espera que en la solución se apliquen correctamente los conceptos de:
interfaz, clase abstracta, herencia, asociación y genéricos.


NOTA:
====
Para agregar la clase generica, debemos luego modificar las clases
App.java
Reserva.java
y crear una nueva clase Repositorio.java