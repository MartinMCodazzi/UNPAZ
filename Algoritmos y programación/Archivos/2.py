# Martin Nahuel Muñoz Codazzi
# 13/05/2023

"""
Dado un fichero de texto, copiar el contenido del mismo en otro archivo con  diferente nombre.
El nombre del fichero origen y destino debe ingresarse desde teclado y se deberá validar que el 
existan (ambos, origen y destino). Luego procederá a efectuar la copia del contenido de un archivo en el otro.  
"""
nombre_original = input("Introduce el nombre del fichero original: ")
nombre_nuevo = input("Introduce el nombre del fichero nuevo: ")

try:
    open(nombre_nuevo+".txt", "r") #Para que tire error si no existe el fichero. Para mí es medio al cuete...

    with open(nombre_original+".txt", "r") as original:
        with open(nombre_nuevo+".txt", "w") as copia:
            copia.write(original.read())
except FileNotFoundError as e:
    print(f"Error al abrir el fichero {e.filename}") # Esto es interesante :) 
