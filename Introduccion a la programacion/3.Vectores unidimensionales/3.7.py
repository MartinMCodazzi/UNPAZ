#05/11/2022
#Martin Nahuel Muñoz Codazzi

"""Desarrollar un algoritmo lea desde teclado un vector de 10 posiciones y que detecte
los elementos repetidos de un vector y los reemplace con un 0 y los deposite en
otro vector."""

import array, random
#Inicializo variables
vectorOrigen = array.array("i",range(10))
vectorDestino = array.array("i",range(10))
banderaRepetidos = False

#Carga del vector
for i in range(len(vectorOrigen)):
    #miVector[valor] = int(input(f"Ingrese el valor número {valor + 1} :"))
    vectorOrigen[i] = int(random.random() * 10 +1)

#Proceso los vectores
for i in range(len(vectorOrigen)):
    # quizá no sea eficiente volver a leer el vector completo, 
    # pero de la otra forma, los ultimos se guardaban aunque estuvieran repetidos
    for j in range(len(vectorOrigen)):
        if (i == j):
            continue
        if (vectorOrigen[i] == vectorOrigen[j]):
            vectorDestino[i] = 0
            vectorDestino[j] = 0
            banderaRepetidos = True
    if not banderaRepetidos:
        vectorDestino[i] = vectorOrigen[i]
    else: banderaRepetidos = False        

#imprimo resultados
print(vectorOrigen)
print(vectorDestino)