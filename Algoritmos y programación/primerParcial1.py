# 19/04/2023
# Martín Nahuel Muñoz Codazzi

import numpy as np

def leerYValidarNumero():
    numero = 1 #Caso para que pase el primer if, igualmente se sobreescribe
    while True:
        try:
            if numero > 9 or numero < 0 :
                raise Exception
            numero = int(input('Por favor ingrese un número del 0 al 9 :'))
        except:
            numero = int(input('ERROR: Por favor ingrese un número entre el 0 y 9 :'))
        else:
            return numero

def cargaMatriz(matriz):
    for fila in (range(len(matriz))):
        for columna in range(len(matriz[0])):
            matriz[fila][columna] = leerYValidarNumero()

def productosEntre6y9(matriz):
    contador = 0
    for fila in (range(len(matriz))):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] >= 6  and matriz[fila][columna] <= 9:
                contador += 1
    return contador

def promedioEntreEmpleados1y2(matriz):
    acumulador = 0
    contador = 0
    for fila in (range(len(matriz))):
        for columna in range(len(matriz[0])):
            if fila <= columna:
                acumulador += matriz[fila][columna]
                contador += 1
                print( matriz[fila][columna]) 
    return acumulador / contador

matriz = np.zeros((3,3))
cargaMatriz(matriz)
print(f'la cantidad de productos vendidos con precio entre $6 y $9 es { productosEntre6y9(matriz) }')
print(f'El promedio de precio de los artículos vendidos entre los empleados 1 y 2 es: { promedioEntreEmpleados1y2(matriz)}')
