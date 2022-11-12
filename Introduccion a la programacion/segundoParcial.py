# 12/11/2022
# Martín Nahuel Muñoz Codazzi

"""
Desarrollar un algoritmo que permita mediante un menú de opciones :

1- Realizar la carga de un vector de 5 posiciones con valores enteros positivos.
 En caso que ingrese un valor menor a cero debera completar todo lo que resta del vector con cero.

2- Valores del vector superiores a X .

3- Mostrar el vector cargado

4- Salir

Ejemplo

Opcion 1 

Si se ingresan 12,3,5,-1 el arreglo que queda cargado deberia ser este
12	3	5	0	0

Opcion 2
Si elige la opcion 2  el algoritmo deberá pedir el valor de X. Si en este ejemplo X fuera 4 solo mostraría el valor 12 y 5.

FUNCIONES: IMPLEMENTAR AL MENOS 2 FUNCIONES"""
import array
#Inicializo variables
vectorOrigen = array.array("i",[0,0,0,0,0])
seleccionMenuPrincipal = 0
vectorCargado = False

# Defino funciones

def separador(sep="*",veces=25):
    print(f"{sep}" * veces)

def menuPrincipal():
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
    for numero in vector:
        print(numero)
    leerIngreso()

# Programa principal
print("Bienvenido a mi programa!")
separador()
while (seleccionMenuPrincipal != 4):
   seleccionMenuPrincipal = menuPrincipal()
   if (seleccionMenuPrincipal == 1):
      cargaVector(vectorOrigen)
      vectorCargado = True
   elif (seleccionMenuPrincipal == 2):
        if (vectorCargado == True):
            #pondría un try
            numero = int(leerIngreso("Ingrese un número con el que comparar :"))
            mayoresANumero(numero,vectorOrigen)
        else:
            leerIngreso("El vector aún no ha sido cargado, pulse Enter para continuar")
   elif (seleccionMenuPrincipal == 3):
        if (vectorCargado == True):
            mostrarVector(vectorOrigen)
        else:
            print("El vector aún no ha sido cargado, pulse Enter para continuar")
   elif(seleccionMenuPrincipal == 4):
        print("Gracias por usar mi programa")
   else:
        print("Selección incorrecta, por favor intente nuevamente")
  



exit(0)