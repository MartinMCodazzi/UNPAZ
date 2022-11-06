# 5/11/2022
# Martín Nahuel Muñoz Codazzi

"""Realiza un programa que permita el ingreso de dos cadenas de caracteres llame a
unas funciones programadas por ti que realicen las mismas tareas que la función
len( ) y strcmp( ) (Existentes en lenguaje C.)"""

# Drfino funciones

def myUDFcuentaCaracteres(cadena):
    contador = 0
    for x in cadena:
        contador += 1
    return contador

def myUDFcomparaCadenas(cadena1,cadena2):
    if cadena1 == cadena2:
        return True
    else: return False

def separador(sep="*",veces=25):
    print(f"{sep}" * veces)

# Programa principal

cadena1 = input("Ingrese una cadena de texto: ")
cadena2 = input("Ingrese una cadena de texto: ")

# Imprimo resultados
separador()
print(f"la cantidad de caracteres de {cadena1} es {myUDFcuentaCaracteres(cadena1)} , y el de {cadena2} es {myUDFcuentaCaracteres(cadena2)}")
if (myUDFcomparaCadenas(cadena1,cadena2)):
    print("Las cadenas son iguales")
else:
    print("Las cadenas son diferentes")

exit(0)