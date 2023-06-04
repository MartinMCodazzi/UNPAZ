# Martín Nahuel Muñoz Codazzi
# Segundo Parcial
# 03/06/2023

"""
Antes de entregar:
    - Modificar ruta de archivo en main()
    - BONUS: Posibilidad de cargar nuevos exámenes, y que las materias estén limitadas. Validador de componentes
    - BONUS: Modificar búsqueda binaria para contemplar que haya más de un resultado
"""


"""Desarrollar un algoritmo en python que mediante un menú de opciones permita

 1) Leer un archivo de texto de Notas de Estudiantes alojado en la carpeta cd su ordenador “c:\pyfiles\examenes.txt”. Examenes.txt estará delimitados por ; (punto y coma) y proveer de su contenido al TDA la siguiente estructura: 

    idExamen 
    Apellido y Nombre Estudiante
    Nota Estudiante
    Materia

Validación 1) En la lectura deberá validarse mediante el uso de excepciones que la ruta existe y el archivo existe.
Validación 2) En la lectura deberá validarse que si el archivo está vacío se informa por pantalla “Archivo vacio” y finaliza el algoritmo.

2) Dado el IdExamen permitir modificar datos del Exámen(no debe modificar el idExamen). Finalmente grabar el txt nuevamente.
3) Dado el IdExamen permitir eliminar un examen (finalmente grabar el txt nuevamente)
4) Informar los exámenes Ordenado por Nota (Método de burbuja)
5) Buscar una nota mediante búsqueda binaria
6) Ingresando el nombre de una materia traer todos los alumnos que rindieron y la nota.

"""

class TDAExamen:    
    def __init__(self, idExamen, nombreEstudiante, notaEstudiante, materia):
        self.idExamen = idExamen
        self.nombreEstudiante = nombreEstudiante
        self.notaEstudiante = notaEstudiante
        self.materia = materia

    def __str__(self):
        """Básicamente, lo muestro así, para respetar la forma como se lee el archivo,
        para mostrarlo de otra manera, puedo usar los get"""
        return f"{self.idExamen};{self.nombreEstudiante};{self.notaEstudiante};{self.materia}"
    
    def getIdExamen(self):
        return int(self.idExamen)
    
    def getNombreEstudiante(self):
        return self.nombreEstudiante
    
    def getNota(self):
        return float(self.notaEstudiante)
    
    def getMateria(self):
        return self.materia

def validadorFormatoExamen(linea):
    """
        Creé esta función para validar cada elemento que va a entrar al array de exámenes
        Si todo sale bien, los valores convertidos a los formatos que corresponden
    """
    
    try:
        #idExamen = int(linea[0])
        idExamen = linea[0]  # No sé si hacerlo con integers o strings, por si hay que llenar los 0s a la izq
        nombreEstudiante = linea[1]
        notaEstudiante = float(linea[2])
        materia = linea[3]

        if int(idExamen) < 0:
            raise Exception("Id del examen incorrecto")        
        if len(nombreEstudiante) < 3:
            raise Exception("Nombre de estudiante incorrecto, es muy corto")
        if notaEstudiante < 0 or notaEstudiante > 10:
            raise Exception("Formato de nota incorrecto")
        if not materia.isalpha():
            raise Exception("Formato de materia incorrecto")
    except Exception as e:
        print(f"Ocurrió un error al querer cargar el examen: {e}")
        exit() #Directamente salgo del programa, quizá es mucho...

    return idExamen, nombreEstudiante, notaEstudiante, materia

def leerArchivo(lista, ruta):  # Devuelve booleano, lo que significaría que se cargó el arreglo
    """Esta función lee el archivo que se le pasa por parámetro y carga la lista que también se le pasa por parámetro
        En el proceso, chequea lo que se va a cargar al array usando la función validadorFormatoExamen
        Devuelve True si pudo cargar correctamente el archivo, False si no"""
    
    #lista = [] #Chequear si esto está bien, para cuando quiera leer el archivo de nuevo
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            pruebaVacío = archivo.read(1)
            archivo.seek(0)
            if not pruebaVacío:
                raise Exception("El archivo está vacío")
            for linea in archivo:
                linea = linea.strip().split(";")                
                if len(linea) != 4:
                    raise Exception(f"el formato del archivo en la línea {linea} está mal")

                idExamen, nombreEstudiante, notaEstudiante, materia = validadorFormatoExamen(linea)                
                examen = TDAExamen(idExamen, nombreEstudiante, notaEstudiante, materia)                
                lista.append(examen)
                
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Ocurrión un error: {e}")
        
    if len(lista) != 0:
        setSetting('archivo cargado',True)
        setSetting('cantidad de examenes',len(lista))
        setSetting('ordenado',False)
    # me gustan los operadores ternarios :)
    return True if len(lista) != 0 else False

def separador(sep="*",veces=25):
    print(sep*veces)

def imprimirSettings():
    """Como getSettings devuelve el diccionario completo, 
    quizás imprima los settings de a uno, 
    sólo los que me importa mostrar"""
    for setting in getSettings().items():        
        print(setting)

def getSettings():
    """Lo hago así para acceder a la variable global y poder editarla """
    return globals()['settings']

def getSetting(key):
    try:
        return getSettings()[key]
    except KeyError:
        print(f"La key ingresada \"{key}\" no existe".upper())
    return False

def setSetting(key, valor):
    try:
        getSettings()[key]
        getSettings()[key] = valor
        return True
    except KeyError:
        print(f"La key ingresada \"{key}\" no existe".upper())
    return False

def bubbleSort(lista, parametro, modificaSetting = True):
    """Recibo una lista de TDAExamen y un parámetro, 
    para ordenar la lista según ese parámetro. No devuelvo nada    
    """    
    n = len(lista)
    # Recorrer todos los elementos del arreglo o lista
    match parametro:
        case "idExamen":
            for i in range(n - 1):        
                hayCambios = False
                for j in range(0, n - i - 1):
                    if lista[j].getIdExamen() > lista[j + 1].getIdExamen():
                        hayCambios = True                    
                        aux = lista[j]
                        lista[j] = lista[j + 1]
                        lista[j + 1] = aux
                if not hayCambios:
                    break
        case "notaEstudiante":
            for i in range(n - 1):        
                hayCambios = False
                for j in range(0, n - i - 1):
                    if lista[j].getNota() > lista[j + 1].getNota():
                            hayCambios = True
                            aux = lista[j]
                            lista[j] = lista[j + 1]
                            lista[j + 1] = aux
                if not hayCambios:
                    break
        case "materia":
             for i in range(n - 1):        
                hayCambios = False
                for j in range(0, n - i - 1):
                    if lista[j].getMateria() > lista[j + 1].getMateria():
                            hayCambios = True
                            aux = lista[j]
                            lista[j] = lista[j + 1]
                            lista[j + 1] = aux
                    if not hayCambios:
                        break

    #Esto lo hago por si quiero ordenar un subset que, no sea la lista principal
    if modificaSetting:
        setSetting('ordenado',parametro)
    return
    

def busquedaBinariaModificada(lista, parametro, valor):
    """Recibo una lista de TDAExamen y un valor, 
    para buscar ese valor en la lista y devolver otra lista con el o los objetos que cumplan
    Lo único a tener en cuenta es que la lista debe estar ordenada según el parámetro que estemos buscando, ya sea por id ,por nota
    o por materia
    """
    resultado = []     
    izq = 0
    der = len(lista) - 1
    
    match parametro:
        case "idExamen":
            while izq <= der:
                mid = (izq + der) // 2
                if lista[mid].getIdExamen() == valor:
                    resultado.append(lista[mid])
                    # Escaneo hacia la izquierda
                    i = mid - 1
                    while i >= izq and lista[i] == valor:
                        resultado.append(lista[i])
                        i -= 1
                    # Escaneo hacia la derecha
                    i = mid + 1
                    while i <= der and lista[i] == valor:
                        resultado.append(lista[i])
                        i += 1
                    return resultado
                elif lista[mid].getIdExamen() < valor:
                    izq = mid + 1
                else:
                    der = mid - 1
            return resultado
        
        case "notaEstudiante":
            while izq <= der:
                mid = (izq + der) // 2               
                if lista[mid].getNota() == valor:                    
                    resultado.append(lista[mid])
                    # Escaneo hacia la izquierda
                    i = mid - 1
                    while i >= izq and lista[i].getNota() == valor:
                        resultado.append(lista[i])
                        i -= 1
                    # Escaneo hacia la derecha
                    i = mid + 1
                    while i <= der and lista[i].getNota() == valor:
                        resultado.append(lista[i])
                        i += 1
                    return resultado
                elif lista[mid].getNota() < valor:
                    izq = mid + 1
                else:
                    der = mid - 1            
            return resultado





    """ while izq <= der:
        mid = (izq + der) // 2
        if lista[mid] == valor:
            resultado.append(mid)
            # Escaneo hacia la izquierda
            i = mid - 1
            while i >= izq and lista[i] == valor:
                resultado.append(i)
                i -= 1
            # Escaneo hacia la derecha
            i = mid + 1
            while i <= der and lista[i] == valor:
                resultado.append(i)
                i += 1
            return resultado
        elif lista[mid] < valor:
            izq = mid + 1
        else:
            der = mid - 1
    return resultado """

def escribirArchivo(lista, ruta):
    """Recibo una lista de TDAExamen, y la ruta para escribir a archivo
    """
    pass

def modificarExamen(examen):
    """Recibo TDAExamen, debería validar los datos antes de asignarlos
    Debo volcar a archivo una vez que termine"""
    pass

def menuPrincipal():
    opcion = ""
    while opcion != 9:
        separador("-")
        print("MENU PRINCIPAL")
        imprimirSettings()
        separador("-")
        print("1) Cargar exámenes")
        print("2) Modificar examen")
        print("3) Eliminar examen")
        print("4) Ordenar examenes")
        print("5) Buscar examen/es")
        print("6) Imprimir exámenes como están en memoria")
        print("7) Imprimir exámenes según materia")
        print("9) Salir")
        separador()
        opcion = int(input("Ingrese una opción: "))
        
        #Cargar archivo       
        if opcion == 1:
            leerArchivo(globals()['listaTDA'], globals()['ruta'])

        #Modificar examen
        elif opcion == 2:
            if getSetting('archivo cargado'):
                pass
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        #Eliminar examen
        elif opcion == 3:
            if getSetting('archivo cargado') == True:                          
                if getSetting('ordenado') != "idExamen":
                    bubbleSort(globals()['listaTDA'], "idExamen")
                try:
                    examenAEliminar = int(input("Ingrese el ID del examen a eliminar: "))
                except:
                    examenAEliminar = False # si falla el input, ni se molesta en buscar
                else:
                    examenAEliminar = busquedaBinariaModificada(globals()['listaTDA'],"idExamen", examenAEliminar)
                if examenAEliminar:
                    # Estaría bueno usar un método que no sea permanente                    
                    decision = input("Está seguro que desea eliminar el examen? Esta acción no se puede deshacer S/N")
                    if decision.upper() == "S":
                        globals()['listaTDA'].pop(examenAEliminar[0])
                        setSetting('cantidad de examenes',len(globals()['listaTDA']))
                        print("Examen eliminado con éxito")
                        escribirArchivo(globals()['listaTDA'], globals()['ruta'])
                        input("pulse Enter para continuar...")
                else:
                    print("ERROR: examen no encontrado")
                    input("pulse Enter para continuar...")
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        #Ordenar examenes
        elif opcion == 4:
            """parto de la base de que cuando leo el archivo, los examenes no están ordenados"""
            if getSetting('archivo cargado'):                                            
                while True:
                    print("4) Ordenar examenes")
                    separador()
                    print("Los ordena por ID del examen, o por nota del examen?")
                    print("1) Por ID del examen")
                    print("2) Por nota del examen")
                    print("3) Por materia")
                    print("0) Volver atrás")
                    seleccion = int(input("Ingrese una opción: "))
                    match seleccion:
                        case 1:
                            if getSetting('ordenado') != "idExamen":
                                bubbleSort(globals()['listaTDA'], "idExamen")
                            break
                        case 2:
                            if getSetting('ordenado') != "notaEstudiante":                                
                                bubbleSort(globals()['listaTDA'], "notaEstudiante")                                
                            break
                        case 3:
                            if getSetting('ordenado') != "materia":                                
                                bubbleSort(globals()['listaTDA'], "materia")                                
                            break
                        case 0:
                            break                            
                        case _:
                            print("Opción incorrecta")
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        #Buscar examen
        elif opcion == 5:
            """Buscar examen por id o por nota, imprimir resultados, preguntar si buscar otra vez"""           
            if getSetting('archivo cargado'):
                while True:
                    separador()
                    print("5) Buscar examen/es")
                    separador()
                    print("1) Buscar por ID")
                    print("2) Buscar por nota")
                    print("0) Volver atrás")
                    seleccion = int(input("Ingrese una opción: "))
                    match seleccion:
                        case 1:
                            if getSetting('ordenado') != "idExamen":
                                bubbleSort(globals()['listaTDA'], "idExamen")
                            try:
                                examenABuscar = int(input("Ingrese el ID del examen a buscar: "))
                            except:
                                print("ERROR: examen no encontrado, escribió bien el Id?")
                            else:                                
                                examenABuscar = busquedaBinariaModificada(globals()['listaTDA'],"idExamen", examenABuscar)
                                if examenABuscar:
                                    separador("-*")
                                    print(examenABuscar[0])

                        case 2:
                            if getSetting('ordenado') != "notaEstudiante":
                                bubbleSort(globals()['listaTDA'], "notaEstudiante")
                            try:
                                examenABuscar = float(input("Ingrese la nota de los examenes a buscar: "))
                            except:
                                print("ERROR: Ningún examen encontrado, escribió bien la nota?")
                            else:
                                examenes = busquedaBinariaModificada(globals()['listaTDA'],"notaEstudiante", examenABuscar)
                                if examenes:
                                    separador("-*")
                                    for examen in examenes:
                                        print(examen)
                                else:
                                    print("ERROR: Ningún examen encontrado, escribió bien la nota?")
                        case 0:
                            break
                        case _:
                            print("Opción incorrecta")
                    separador()
                    ("Desea buscar otro examen? S/N")
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        #Imprimir exámenes como están en memoria
        elif opcion == 6:
            if getSetting('archivo cargado'):
                for examen in globals()['listaTDA']:
                    print(examen)                
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        #Imprimir exámenes según materia
        elif opcion == 7:
            """Quiero tener una variable donde estén las materias, y ciclarlas en un menú
              para poder elegir qué materia buscar. Luego, ordenarlos por nota"""
            if getSetting('archivo cargado'):
                if getSetting('ordenado') != "materia":                                
                    bubbleSort(globals()['listaTDA'], "materia")               
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")
        else:
            print("Opción incorrecta")
    else: 
        print("Muchas gracias, hasta luego")

# ruta = r"c:\pyfiles\examenes.txt"
ruta = "examenes.txt"
listaTDA = []    
settings = {'ordenado': False, 'archivo cargado': False, 'cantidad de examenes' : 0} #Lo creo acá, porque tiene que ser global
menuPrincipal()
