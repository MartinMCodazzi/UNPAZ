# Martín Nanhuel Muñoz Codazzi
# 15/10/2022

mesMenor = 0
cantidadMenor = 0
contadorMes = 0
cantidadPasajeros = 1
promPrimerSemestre = 0 
promSegundoSemestre = 0

print("Bienvenido al sistema de la empresa de turismo")
print("*" * 30)

while (contadorMes < 12)  :
    cantidadPasajeros = int(input("Ingrese la cantidad de pasajeros para el mes : "))
    # Compruebo si el dato ingresado es menor a 0, corto el ciclo anticipadamente, es muy práctico el break...
    if cantidadPasajeros < 0 :
        break
    else:
        contadorMes += 1
        
    #Check si se ingresó una cantidad menor a la menor, la primera vez se asigna lo primero
    if (contadorMes == 1):
        cantidadMenor = cantidadPasajeros
        mesMenor = contadorMes
    elif (cantidadPasajeros < cantidadMenor) :
        cantidadMenor = cantidadPasajeros
        mesMenor = contadorMes
    
    #Si es del primer o del segundo cuatrimestre
    if (contadorMes <= 6):
        promPrimerSemestre += cantidadPasajeros
    else:
        promSegundoSemestre += cantidadPasajeros

print("*" * 30)
if (contadorMes != 0 and cantidadMenor >= 0 ): #Evalúo si al menos se ingresó un dato válido
    print("El mes que menos pasajeros viajó es el mes", mesMenor,", la cantidad fue", cantidadMenor)

    if ( contadorMes <= 6 ): #Evalúo si se ingresaron uno o dos semestres
        print("El promedio de viajes del primer semestre fue :",promPrimerSemestre / (contadorMes ) )
        
    else: 
        print("El promedio de viajes del primer semestre fue :",promPrimerSemestre / 6  )
        print("El promedio de viajes del segundo semestre fue :",promSegundoSemestre / ( contadorMes - 6 ) )
                 
else: 
    print("No se ingresó ningún pasajero")