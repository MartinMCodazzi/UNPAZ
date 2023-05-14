# Martín Nahuel Muñoz Codazzi
# 13/05/2023

"""
Realizar un programa en código C que ejecute una rutina para que lea y examine  el contenido de un archivo de texto ya existente. El archivo de texto esta en la unidad c:  y su nombre es archivo.txt, el contenido del archivo es una cadena que dice: 
Remp1azar e1 numero 1 por 1a 1etra L  
El resultado de la rutina deberá crear otro archivo en la unidad C: llamado resultado.txt y  deberá contener la siguiente cadena: RempLazar eL numero L por La Letra L 

"""
cadena = "Remp1azar e1 numero 1 por 1a 1etra L"
print(f"la cadena original es: {cadena}")
with open("archivo.txt","w+") as archivo:
    archivo.write(cadena)
    archivo.seek(0)
    cadena = archivo.read()
archivo.close()
cadena = cadena.replace("1","L")
with open("resultado.txt","w") as archivo:
    archivo.write(cadena)
archivo.close()
print(f"la cadena modificada es: {cadena}")
