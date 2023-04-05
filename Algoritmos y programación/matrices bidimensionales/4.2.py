# 04/04/2023
# Martín Nahuel Muñoz Codazzi

"""
Efectuar la carga de una matriz de 5x5 desde el teclado. Efectuar la sumatoria de
los valores alojados en la diagonal principal y el promedio de los valores alojados
en la contradiagonal. Mostrar por pantalla los resultados.
"""

import numpy as np
import random

#Defino funciones

def UDFCargaMatriz(matriz, randomizado = False ):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if not randomizado:
                matriz[fila][columna] = int(input("Ingrese un número :"))
            else:
                matriz[fila][columna] = int(random.random() * 100)

def UDFSumatoriaDiagonal(matriz): #Sólo funciona con matrices cuadradas
    sumatoria = 0
    for fila in range(len(matriz)):
        sumatoria += matriz[fila][fila]
    return sumatoria

def UDFPromedioContraDiagonal(matriz): #Sólo funciona con matrices cuadradas
    promedio = 0
    largoTotal = int(len(matriz)) - 1
    columna = largoTotal
    for fila in range(len(matriz)):
        promedio += matriz[fila][columna]
        columna -= 1    
    return promedio / (largoTotal + 1)


def UDFMuestraMatriz(matriz):
    for fila in range(len(matriz)):        
        for columna in range(len(matriz[0])):        
            print(matriz[fila][columna],end=" | ")      
        print("\n")

#Programa principal

miMatriz = np.zeros(shape=(5,5),dtype=int)
UDFCargaMatriz(miMatriz,True)
UDFMuestraMatriz(miMatriz)
print(f'La sumatoria de la diagonal principal es: {UDFSumatoriaDiagonal(miMatriz)}')
print(f'El promedio de la contradiagonal es:{UDFPromedioContraDiagonal(miMatriz)}')
