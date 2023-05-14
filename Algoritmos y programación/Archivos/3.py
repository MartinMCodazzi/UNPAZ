# Martín Nahuel Muñoz Codazzi
# 13/05/2023

"""
Efectuar un programa el cual ejecute una rutina que lea y depure un  archivo de texto ya existente.  
El archivo de texto se aloja en el la unidad C: y su nombre es Parcial.txt. 
El contenido del archivo es una cadena de este tipo 
“de*bo dep*urar la cadena eliminando el cará*cter asterisco” 

El resultado de la rutina deberá crear otro archivo en la unidad C: y su nombre será 
Parcialdepurado.txt. Este deberá tener la cadena depurada. 
Resultado esperado: “debo depurar la cadena eliminando el carácter asterisco” 
"""

string = "de*bo dep*urar la cadena eliminando el carácter asterisco"
with open("Parcial.txt", "w") as file:
    file.write(string)
   
with open("Parcial.txt", "r") as file:
    string = file.read()
    print(f"El archivo contiene esta cadena previa manipulación: {string}")
    
with open("ParcialDepurado.txt", "w") as file:    
    string = string.replace("*", "")
    file.write(string)
    
    print(f"El archivo contiene esta cadena después de manipulación: {string}")
