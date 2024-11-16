#21/09/2023
"""
1.4 Generar un algoritmo que permita el ingreso de palabras desde la consola. El algoritmo
deberá examinar cada palabra e identificar la cantidad de letras que tiene. El algoritmo finaliza
con la palabra “FIN” (no debe ser considerada. Una vez que esto ocurre deberá indicar cuál fue
la palabra más grande y cuál fue la palabra más pequeña.
El tamaño de la palabra lo obtenemos con la siguiente función len(palabra)
En este ejemplo, el usuario ingresó varias palabras, incluyendo "Manzana", "Plátano", "Perro", y
"Gato". El programa determinó que la palabra más larga fue "Manzana" con 7 letras, y la palabra
más corta fue "Gato" con 4 letras. La palabra "FIN" no se consideró al calcular estas longitudes.
"""

def LeerPalabra():
    while True: #Este while lo uso para que itere si no se ingresa un valor válido
        palabra = input("Ingrese una palabra: ").strip() #<- Con strip la "sanitizás", 
        #sacándole espacios adelante y atrás de la palabra

        #Con esto solucioné el bug de los ingresos vacíos
        if CalcularLongitud(palabra.strip()) == 0:
            print("ERROR: No se permiten palabras vacías")
            continue #Este continue hace que se pida de nuevo la palabra

        if palabra.upper() != "FIN": #Upper lo uso para que termine si se ingresa "FIN", "fin" o "FiN"
            return palabra
        else:
            return False #Este false va a servir para cortar el while del programa ppal

def CalcularLongitud(palabra):
    return len(palabra)

maximo = 0
minimo = 0
PalabraLarga = ""
PalabraCorta = ""

while True:
    palabra = LeerPalabra()
    if palabra == False: #Podría ser if != palabra:
        break
    if maximo == 0: #Condición de primera ejecución
        maximo = CalcularLongitud(palabra)
        PalabraLarga = palabra
    else: # Después de la primer ejecución, va a comparar con lo que tiene 
        if CalcularLongitud(palabra) > maximo:
            maximo = CalcularLongitud(palabra)
            PalabraLarga = palabra
    
    if minimo == 0: #Lo mismo hago con el mínimo
        #Minimo tiene el bug de que si no ponés nada, te lo toma como una palabra válida
        minimo = CalcularLongitud(palabra)
        PalabraCorta = palabra
    else:
        if CalcularLongitud(palabra) < minimo:
            minimo = CalcularLongitud(palabra)
            PalabraCorta = palabra

print(f"La palabra más larga es {PalabraLarga} con {maximo} letras")
print(f"La palabra más corta es {PalabraCorta} con {minimo} letras")

exit(0)



