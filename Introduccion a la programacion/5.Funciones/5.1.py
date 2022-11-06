# 5/11/2022
# Martín Nahuel Muñoz Codazzi

"""Realiza un programa principal que lea tres números enteros por teclado, los
almacene en tres variables (x, y, z) y llame a una función llamada máximo(), con
tres argumentos, que devuelva el máximo de estos tres valores."""

import random
# Definir las funciones

def maximo(var1,var2,var3):
    if (var1 > var2) and (var1 > var3):
        return var1
    elif (var2 > var1) and (var2 > var3):
        return var2
    elif (var3 > var1) and (var3 > var2):
        return var3
    elif (var2 == var1) and (var2 == var3):
        return var1
    
# Programa principal

#x = int(input("Ingrese un número para la variable x"))
#y = int(input("Ingrese un número para la variable y"))
#z = int(input("Ingrese un número para la variable z"))
x = int(random.random() * 100)
y = int(random.random() * 100)
z = int(random.random() * 100)

print(f"El máximo entre {x}, {y} y {z} es {maximo(x,y,z)}")

exit(0)
