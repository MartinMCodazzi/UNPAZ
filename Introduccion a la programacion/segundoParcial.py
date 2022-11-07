# 12/11/2022
# Martín Nahuel Muñoz Codazzi

""""""
# Defino importaciones

import array, random

# Defino variables globales

vectorOrigen = array.array("i",range(10))
vectorDestino = array.array("i",range(10))

# Defino funciones

def separador(lineas=1, sep="*",veces=25 ):
    def escribir():
        print(f"{sep}" * veces)
    if lineas > 1:
        for i in range(lineas):
            escribir()
    else:
        escribir()

def cargaVector(vector):
    for i in range(len(vector)):
        # Control de lo que se ingresa? con un while numero > 0, por ejemplo
        #vector[i] = int(input(f"Ingrese el valor número {i + 1} :"))
        vector[i] = int(random.random() * 100)
    return vector


# Programa principal
print("Bienvenido a mi programa!")
separador()





exit(0)