# 06/11/2022
# Martín Nahuel Muñoz Codazzi

"""Realiza un programa principal que lea una palabra desde el teclado e identifica si la
misma es palindroma (capicua)."""

# Defino variables globales

palabra = ""

# Defino funciones

def separador(sep="*",veces=25):
    print(f"{sep}" * veces)

def leePalabra():
    lectura = input("Ingrese una palabra para saber si es palíndromo: ")
    return lectura

def esPalindromo(palabra):
    medio = int(len(palabra) / 2)
    if medio > 1:
        for i in range(1,medio):
            if not (palabra[i-1] == palabra[-i]):
                return False
    else:
        if (palabra[0] != palabra[1]):
                return False    
    return True

# Programa principal

print("Bienvenido a sistema de detección de palíndromos")
separador()
while (len(palabra) < 2): 
    palabra = leePalabra()
if esPalindromo(palabra):
    print(f"{palabra} es palíndromo")
else:
    print(f"{palabra} no es palíndromo")





exit(0)