# 12/11/2022
# Martín Nahuel Muñoz Codazzi

import array
#Inicializo variables
vectorOrigen = array.array("i",[0,0,0,0,0])

# Defino funciones

def separador(sep="*",veces=25):
    print(f"{sep}" * veces)

def imprimirMenuPrincipal():
    separador("-")
    print("Menú Principal")
    separador("-")
    print("Ingrese lo que desea hacer")
    print("Opción 1: Cargar vector")
    print("Opción 2: Mostrar valores superiores a X")
    print("Opción 3: Mostrat el vector cargado")
    print("Opción 4: Salir del programa")
    separador()
    # Acá pondría un try
    ingreso = int(leerIngreso("Elija la opción que desee : "))
    return ingreso

def leerIngreso(texto = "Pulse Enter para continuar :"):
    datoIngresado = input(f"{texto}")
    return datoIngresado

def cargaVector(vector):
    separador()
    for numeroPosicion in range(len(vector)):
        # pondría un try
        numeroIngresado = int(leerIngreso(f"Ingrese un número para cargar en la posicion {numeroPosicion} :"))
        if (numeroIngresado > 0) :
            vector[numeroPosicion] = numeroIngresado
        else:
            break

def mayoresANumero(numeroAComparar,vector):
    huboMayores = False
    for numeroEnVector in vector:
        if (numeroEnVector > numeroAComparar):
            print(f"{numeroEnVector} es mayor a {numeroAComparar}")
            huboMayores = True
        if not huboMayores:
            print(f"En el vector cargado, no extisten números mayores a {numeroAComparar}")
            leerIngreso()

def mostrarVector(vector):
    separador()
    print("Se ha cargado el siguiente vector:")
    for numero in vector:
        print(numero)
    leerIngreso()

def logicaMenuPrincipal():
    seleccionMenuPrincipal = 0
    vectorCargado = False
    while (seleccionMenuPrincipal != 4):
        seleccionMenuPrincipal = imprimirMenuPrincipal()
        separador("-")
        if (seleccionMenuPrincipal == 1):
           cargaVector(vectorOrigen)
           vectorCargado = True
        elif (seleccionMenuPrincipal == 2):
            if (vectorCargado == True):
                #pondría un try
                numero = int(leerIngreso("Ingrese un número con el que comparar : "))
                mayoresANumero(numero,vectorOrigen)
            else:
                leerIngreso("El vector aún no ha sido cargado, pulse Enter para continuar ")
        elif (seleccionMenuPrincipal == 3):
            if (vectorCargado == True):
                mostrarVector(vectorOrigen)
            else:
                leerIngreso("El vector aún no ha sido cargado, pulse Enter para continuar ")
        elif(seleccionMenuPrincipal == 4):
            print("Gracias por usar mi programa")
        else:
            leerIngreso("Selección incorrecta, por favor intente nuevamente")


# Programa principal
print("Bienvenido a mi programa!")
separador()
logicaMenuPrincipal()

exit(0)