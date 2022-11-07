# 06/11/2022
# Martín Nahuel Muñoz Codazzi

"""Realizar un programa principal que mediante el llamado de una función calcula el
factorial de un número entero n.
A. Mediante una estructura repetitiva
B. Mediante la siguiente fórmula recursiva: n! = n * (n-1)! Teniendo en cuenta
que: 1! = 1.
Por medio de un menú se podrá elegir si el resultado se calcula por la opción A o
por la opción B."""

# Defino funciones

def separador(lineas=1, sep="*",veces=25 ):
    def escribir():
        print(f"{sep}" * veces)
    if lineas > 1:
        for i in range(lineas):
            escribir()
    else:
        escribir()

def factorialRepetitiva(numero):
    acumulador = 1
    if numero > 1:
        for i in range(numero, 0, -1):
            acumulador *= i
        return acumulador
    else:
        return False

def factorialRecursiva(numero):
    if numero == 1:
        return 1
    else:
        # Se llamará a si misma hasta que número valga 1
        return numero * factorialRecursiva(numero -1)

def menuPrincipal():
    print("Calcular factorial usando estructura repetitiva o recursividad?")
    print("1 -> Estructura repetitiva")
    print("2 -> Estructura recursiva")
    print("0 -> Salir del programa")
    separador()
    seleccion = int(input("Uso repeticiones, o recursividad? 0 para salir: "))
    return seleccion

def leeNumero():
    while True:
        numero = int(input("Ingrese el nùmero natural a factorizar: "))
        if numero >= 0:
            break
        else:
            print("ERROR!, por favor ingrese un nùmero mayor a 0")
            separador()
    return numero

# Programa principal

print("Bienvenido al programa para calcular factoriales")
separador(2)
while True:
    seleccion = menuPrincipal()
    if seleccion == 0:
        break
    # Preguntará por el número sólo si sigue
    numero = leeNumero()
    if seleccion == 1:
        print(f"El factorial de {numero} usando el método de repetición es {factorialRepetitiva(numero)}")
    elif seleccion == 2:
        print(f"El factorial de {numero} usando el método de repetición es {factorialRecursiva(numero)}")

    separador(2)

exit(0)