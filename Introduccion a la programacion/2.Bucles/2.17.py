# Martín Nahuel Muñoz Codazzi
# 23/09/2022

"""
Hacer un algoritmo que registra la temperatura (número decimal), todos los dias a
las 15 hs durante todo una semana cualquiera. Mostrar por pantalla la temperatura
más alta de esa semana y la más baja.
"""

tempMayor = float(input("ingrese la temperatura (float) :"))
tempMenor = tempMayor 
print("*"*25) # Separador de bajo presupuesto :p

for i in range(6): 
    temp = float(input("ingrese la temperatura (float) :"))
    print("*"*25) # Separador de bajo presupuesto :p
    if (temp > tempMayor):
        tempMayor = temp
    if (temp < tempMenor):
       tempMenor = temp

print("La mayor temperatura alcanzada fue",tempMayor,"grados")
print("La menor temperatura alcanzada fue",tempMenor,"grados")    

exit(0)