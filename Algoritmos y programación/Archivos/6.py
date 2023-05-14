# Martín Nahuel Muñoz Codazzi
# 13/05/2023

"""
Se desea obtener una estadística de un archivo de caracteres ya existente. El  mismo se llama carta.txt. Escribir un programa para contar e informe el número de  palabras de que consta un archivo, así como la longitud promedio en caracteres. 
Ejemplo carta.txt 
“Esta es una carta de ejemplo 
y vamos a contar las palabras” 
Resultado deberá analizar el texto y mostrara por pantalla: 
“Esta(4) es(2) una(3) carta(5) de(2) ejemplo(7) 
y(1) vamos(5) a(1) contar(5) las(3) palabras(8)” 
“Se han contabilizado 12 palabras el archivo. La longitud promedio es de 3.83 caracteres”
"""

with open("carta.txt", "w") as archivo:
    archivo.write("Esta es una carta de ejemplo \ny vamos a contar las palabras")

resultado = ""
acumulador_longitud_palabras = 0
with open("carta.txt", "r") as archivo:
    contenido = archivo.read()

palabras = contenido.split()
for palabra in palabras:
    acumulador_longitud_palabras += len(palabra)
    resultado += f"{palabra}({len(palabra)}) "

print(resultado)
print(f"Se han contabilizado {len(palabras)} palabras en el archivo. La longitud promedio es de {round(acumulador_longitud_palabras/len(palabras),2)}") #Round(numero, cantidad de decimales) es una alternativa a usar .2f en el resultado de una divisiión
# No estoy contando los espacios que hay entre palabras como caracteres.
