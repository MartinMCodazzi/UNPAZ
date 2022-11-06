# 5/11/2022
# Martín Nahuel Muñoz Codazzi

"""Escribir un programa que lea diez números, los guarde en un vector y a
continuación los muestre por pantalla en orden inverso al de su entrada"""

import array, random
#Inicializo variables
vectorOrigen = array.array("i",range(10))
suma = 0
mult = 1

#Carga del vector
for i in range(len(vectorOrigen)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    vectorOrigen[i] = int(random.random() * 10)

# Muestro el resultado
for i in range(len(vectorOrigen)-1,-1,-1):
    print(vectorOrigen[i])    