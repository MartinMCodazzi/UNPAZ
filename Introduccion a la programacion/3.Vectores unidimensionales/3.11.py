# 5/11/2022
# Martín Nahuel Muñoz Codazzi

"""Escribir un programa que lea tres números y los guarde en un vector. A
continuación, los ordenará y guardará los valores ordenados en otro vector.
Finalmente sacará ambos vectores por la pantalla"""

import array, random
#Inicializo variables
vectorOrigen = array.array("i",range(3))

#Carga del vector
for i in range(len(vectorOrigen)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    vectorOrigen[i] = int(random.random() * 10)