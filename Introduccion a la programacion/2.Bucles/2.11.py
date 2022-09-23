# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
2.11.Hacer un algoritmo donde se ingresan 10 números enteros. Mostrar por pantalla el
número más grande ingresado y en qué posición se ingresó.
"""
mayor = False

for i in range(10):
    try:
        numero = int(input("Ingrese un número entero"))
    except:
        print("Debe ingresar un número entero")
    else:
        if (mayor != False):
            if (numero > mayor):
                mayor = numero
                posicion = i
        else:
            mayor = numero
            posicion = i

print("El mayor número fue",mayor,"el cual se ingresó en la posición",posicion)

exit(0)