def udfSeleccion(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        min_idx = i
        for j in range(i+1, longitud):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j

        # Intercambiar
        if i != min_idx:
            aux = arreglo[i]
            arreglo[i] = arreglo[min_idx]
            arreglo[min_idx] = aux


def udfBubbleSort(arr):
    n = len(arr)
    # optimizar el código, por lo que si la matriz ya está ordenada, no es necesario
    # para pasar por todo el proceso
    #hayCambios = False #Interruptor

    # Recorrer todos los elementos del arreglo o lista
    for i in range(n - 1):
        # range(n) también funciona, pero el bucle externo lo hará
        # repetir una vez más de lo necesario.
        # Los últimos elementos i ya están en su lugar
        hayCambios = False
        for j in range(0, n - i - 1):
            # recorrer el arreglo de 0 a n-i-1
            # Cambiar si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j + 1]:
                hayCambios = True
                #arr[j], arr[j + 1] = arr[j + 1], arr[j]
                aux = arr[j]
                arr[j] = arr[j + 1];
                arr[j + 1] = aux;
        if not hayCambios:
            # si no hemos necesitado hacer un solo intercambio,
            # puede simplemente salir del bucle principal.
            return


def udfInsertionSort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        # Mueve elementos de arr[0..i-1], que son
        # mayor que key, a una posicion por delante
        # de su posición actual
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key



def udfBusquedaSecuencial(unaLista, item):
    pos = 0
    encontrado = False
    while pos < len(unaLista):
        if unaLista[pos] == item:
            return pos
        else:
            pos = pos+1
    return -1



def udfBusquedaBinaria(lista, x):
    '''Busqueda binaria
    Precondicion: lista esta ordenada
    Devuelve -1 si x no esta en lista
    Devuelve p tal que lista[p] == x, si x esta en lista'''
    # Busca en toda la lista dividiéndola en segmentos y considerando
    # a la lista completa como el segmento que empieza en 0 y termina
    # en len(lista) - 1.
    izq = 0 # izq guarda el índice inicio del segmento
    der = len(lista) -1 # der guarda el índice fin del segmento
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio =int((izq+der)/2)
        print ("DEBUG:", "izq:", izq, "der:", der, "medio:", medio)
        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio] == x:
            return medio
        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > x:
            der = medio-1
        # sino, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio+1
        # si no salió del ciclo, vuelve a iterar con el nuevo segmento

    # salió del ciclo de manera no exitosa: el valor no fue encontrado
    return -1