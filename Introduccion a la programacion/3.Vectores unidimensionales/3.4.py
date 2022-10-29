# 28/10/2022
# Martin Nahuel Muñoz Codazzi

"""
Crear un programa que lea e imprima el promedio del total de los elementos pares
de un vector de 10 posiciones
"""

import array, random
#Inicializo variables
miVector = array.array("i",range(10))
cantidadDePares = False
promedio = 0

#Carga del vector
for i in range(len(miVector)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    miVector[i] = int(random.random() * 100)

#Evaluacion
for i in range(len(miVector)):
    if (miVector[i] % 2 == 0 ):
        cantidadDePares += 1
        promedio += miVector[i]

# Informo el resultado
if cantidadDePares:
    print(f"La cantidad de números pares cargados fue de {cantidadDePares} y el promedio fue de {promedio / cantidadDePares}") 
else:
    print("No se cargaron pares")