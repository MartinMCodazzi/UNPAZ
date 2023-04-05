# 04/04/2023
# Martín Nahuel Muñoz Codazzi

"""
Efectuar la carga de una matriz de 3x2 desde teclado. Obtener como resultado la
matriz transpuesta. Mostrarla por pantalla.
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

def UDFTransponerMatriz(matrizOriginal,matrizTranspuesta):
    for fila in range(len(matrizOriginal)):
        for columna in range(len(matrizOriginal[0])):
            matrizTranspuesta[columna][fila] = matrizOriginal[fila][columna]

def UDFMuestraMatriz(matriz):
    for fila in range(len(matriz)):        
        for columna in range(len(matriz[0])):        
            print(matriz[fila][columna],end="|")      
        print("\n")

#Programa principal

miMatriz = np.zeros(shape=(3,2),dtype=int)
miMatrizTranspuesta = np.zeros(shape=(2,3),dtype=int)

UDFCargaMatriz(miMatriz,True)
UDFTransponerMatriz(miMatriz,miMatrizTranspuesta)
print("Matriz Original:")
UDFMuestraMatriz(miMatriz)
print("Matriz transpuesta:")
UDFMuestraMatriz(miMatrizTranspuesta)