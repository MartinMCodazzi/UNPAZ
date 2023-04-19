# 17/4/2023
# Martín Nahuel Muñoz Codazzi

"""
Diseñar un algoritmo que permita la carga de una matriz de 3x3 desde teclado. A
esta matriz la llamaremos MatOrigen.
Una vez cargada la matriz efectuar el análisis de los valores cargados y obtener
como resultado otra matriz la cual llamaremos MatDestino en donde como resultado
deberá alojar en la misma fila columna el valor 1 (uno) en caso de que el valor
origen sea par y un 0 (cero) en caso de que el valor sea impar.
Mostrar el resultado de la matriz destino por pantalla.
"""

import numpy as np
import random

matOrigen = np.array([[0,0,0],[0,0,0],[0,0,0]],dtype=int) # 3x3 original
matDestino = np.array([[0,0,0],[0,0,0],[0,0,0]],dtype=int) # 3x3 destino,

def cargaMatrizOrigen(matriz):
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[0])): 
            matriz[filas][columnas] = int(random.random()*10)

def cargaMatrizDestino(matrizOrigen, matrizDestino):
    for filas in range(len(matrizOrigen)):
        for columnas in range(len(matrizOrigen[0])):
            if matrizOrigen[filas][columnas] % 2 == 0: 	# si es par
                matrizDestino[filas][columnas] = 1
            else:
                matrizDestino[filas][columnas] = 0 # si es impar


cargaMatrizOrigen(matOrigen)
cargaMatrizDestino(matOrigen,matDestino)
print(matOrigen)
print(matDestino)