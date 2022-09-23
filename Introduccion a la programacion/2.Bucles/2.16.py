# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
Hacer un algoritmo donde se Ingresan los siguientes datos de 5 alumnos:
● nota (float),
● Edad = (entero)
Mostrar por pantalla la mejor nota y qué edad tenía.
"""
notaMayor = float(input("ingrese la nota (float) :"))
edadMayor = int(input("ingrese la edad (entero) :"))
print("*"*25) # Separador de bajo presupuesto :p

for i in range(4): 
    nota = float(input("ingrese la nota (float) :"))
    edad = int(input("ingrese la edad (entero) :"))
    print("*"*25) # Separador de bajo presupuesto :p
    if (nota > notaMayor):
        notaMayor = nota
        edadMayor = edad

print("la mayor nota ingresada fue",notaMayor,"y su edad es",edadMayor)

exit(0)