# 5/11/2022
# Martín Nahuel Muñoz Codazzi

"""Dado un vector de 6 posiciones se debe
a. Sumar los valores pares
b. Multiplicar los valores impares
Mostrar el resultado por pantalla."""

import array, random
#Inicializo variables
vectorOrigen = array.array("i",range(6))
suma = 0
mult = 1

#Carga del vector
for i in range(len(vectorOrigen)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    vectorOrigen[i] = int(random.random() * 10)

# Proceso el vector
for i in vectorOrigen:
    if (i % 2 == 0):
        suma += i
    else:
        mult *= i

#Musetro los resultados
print(vectorOrigen)
if suma != 0:
    print(f"La suma de los números pares cargados en el array fué {suma}")
else:
    print("No se cargaron números pares")
if mult != 1:
    print(f"La multiplicacion de los números impares cargados en el array fue {mult}")
else:
    print("no se cargaron números impares")