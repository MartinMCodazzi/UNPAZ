import myOrdenamientoyBusquedaLibrary

numeros = [51, 21, 39, 80, 36]
print("Arreglo de numeros orinales:")
print(numeros)

viOpcion=-1 #Global
vlListaOrdenada = False
while viOpcion!=6:
    print('\n')
    print('1-Ordenamiento por Seleccion')
    print('2-Ordenamiento por Burbujeo')
    print('3-Ordenamiento por Insercion')
    print('4-Busqueda Secuencial')
    print('5-Busqueda Binaria')
    print('6-Salir')
    viOpcion=int(input("Seleccione:"))

    if viOpcion==1:
        print("Arreglo de numeros ordenado x Seleccion: ")
        myOrdenamientoyBusquedaLibrary.udfSeleccion(numeros)
        vlListaOrdenada = True
        print(numeros)
    elif viOpcion == 2:
        print("Arreglo de numeros ordenado x Burbuja: ")
        myOrdenamientoyBusquedaLibrary.udfBubbleSort(numeros)
        vlListaOrdenada = True
        print(numeros)
    elif viOpcion == 3:
        print("Arreglo de numeros ordenado x Insercion: ")
        myOrdenamientoyBusquedaLibrary.udfInsertionSort(numeros)
        vlListaOrdenada = True
        print(numeros)
    elif viOpcion == 4:
        print("Busqueda Secuencial: ")
        miNro = int(input("Ingrese Nro a Buscar en la Lista o arreglo:"))
        posEncontro=myOrdenamientoyBusquedaLibrary.udfBusquedaSecuencial(numeros, miNro)
        if posEncontro == -1:
            print("El elemento no fue encontrado")
        else:
            print(f"El Elemento {numeros[posEncontro]}, en la posicion {posEncontro}")
    elif viOpcion == 5:
        if vlListaOrdenada:
            print("Busqueda Binaria: ")
            miNro=int(input("Ingrese Nro a Buscar en la Lista o arreglo:"))
            posEncontro=myOrdenamientoyBusquedaLibrary.udfBusquedaBinaria(numeros, miNro)
            if posEncontro == -1:
                print("El elemento no fue encontrado")
            else:
                print(f"El Elemento {numeros[posEncontro]}, en la posicion {posEncontro}")
        else:
            print("Debe ordenar primero la lista")

    elif viOpcion == 6:
        print('Salir')
    else:
        print('Incorrecto')