# Martín Nahuel Muñoz Codazzi
# 13/05/2023

"""
Efectuar un programa el cual ejecute una rutina que lea y examine el contenido de un archivo de texto ya existente. Al examinar el contenido deberá contabilizar la cantidad de asteriscos que hay en el mismo. El archivo de texto se aloja  en el la unidad C: y su nombre es Parcial.txt. El contenido del archivo es una cadena de  este tipo 
“de*bo conta*bilizar el cará*cter asterisco” 
El resultado de la rutina deberá crear otro archivo en la unidad C: y su nombre será  Parcialcontabilizado.txt. Este deberá tener la cadena con el resultado de la cantidad de  asteriscos. Resultado esperado: “Se han encontrado 3 asteriscos” 
"""

try:
    contador = 0
    with open("Parcial.txt", "r") as archivo:
        contenido = archivo.read()
        for letra in contenido:            
            if letra == "*":
                contador += 1
    
    with open("ParcialContabilizado.txt","w") as archivo:
        archivo.write(f"Se han encontrado {contador} asteriscos")
    
except FileNotFoundError:
    print("No se encontró el archivo")

finally:
    print(f"Se han encontrado {contador} asteriscos")