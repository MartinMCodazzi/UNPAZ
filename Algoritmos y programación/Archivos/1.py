# Martín Nahuel Muñoz Codazzi
# 13/05/2023

"""
Dado un archivo de texto existente examinar el mismo e informar la cantidad de vocales que contiene.
"""

try:   
    #Usando "with", no hace falta cerrar el archivo 
    fpArchivo = open("archivo.txt", "r")
    contenido = fpArchivo.read()
    contador = 0
    for letras in contenido:
        if letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u":
            contador += 1
    print("La cantidad de vocales es: ", contador)
except FileNotFoundError:
    print("El archivo no existe")
    
fpArchivo.close()
