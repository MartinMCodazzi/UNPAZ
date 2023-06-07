# Martín Nahuel Muñoz Codazzi
# Segundo Parcial
# 03/06/2023

"""
Antes de entregar:
    - Modificar ruta de archivo en el root

    TODO:
        - Modificar las funciones para llamar a las variables globales lo menos posible
        - Modificar cómo se lee el archivo
        - Revisar todos los inputs, englobarlos en try
        - Seguir revisando la búsqueda binaria de notas
        - Si voy a lo específico de lo que se pide con respecto al punto 6, estoy trayendo más de lo que se pide
        - Revisar los comentarios
        - x BONUS: Posibilidad de cargar nuevos exámenes, y que las materias estén limitadas.
        - ✓ BONUS: Modificar búsqueda binaria para contemplar que haya más de un resultado
"""


"""Desarrollar un algoritmo en python que mediante un menú de opciones permita

 ✓1) Leer un archivo de texto de Notas de Estudiantes alojado en la carpeta cd su ordenador “c:\pyfiles\examenes.txt”. Examenes.txt estará delimitados por ; (punto y coma) y proveer de su contenido al TDA la siguiente estructura: 

    idExamen 
    Apellido y Nombre Estudiante
    Nota Estudiante
    Materia

✓ Validación 1) En la lectura deberá validarse mediante el uso de excepciones que la ruta existe y el archivo existe.
✓ Validación 2) En la lectura deberá validarse que si el archivo está vacío se informa por pantalla “Archivo vacio” y finaliza el algoritmo.
✓ 2) Dado el IdExamen permitir modificar datos del Exámen(no debe modificar el idExamen). Finalmente grabar el txt nuevamente.
✓ 3) Dado el IdExamen permitir eliminar un examen (finalmente grabar el txt nuevamente)
✓ 4) Informar los exámenes Ordenado por Nota (Método de burbuja)
✓ 5) Buscar una nota mediante búsqueda binaria
✓ 6) Ingresando el nombre de una materia traer todos los alumnos que rindieron y la nota.

"""

class TDAExamen:    
    def __init__(self, idExamen, nombreEstudiante, notaEstudiante, materia):
        self.idExamen = idExamen
        self.nombreEstudiante = nombreEstudiante
        self.notaEstudiante = notaEstudiante
        self.materia = materia

    def __str__(self):
        """ No pude hacer andar el grabar archivo sin llamar a __str__() ya fué, creo otra función"""
        return f"{self.getIdExamen()};{self.getNombreEstudiante()};{self.getNota()};{self.getMateria()}"
    
    def getIdExamen(self):
        return int(self.idExamen)
    
    def getNombreEstudiante(self):
        return self.nombreEstudiante
    
    def getNota(self):
        return float(self.notaEstudiante)
    
    def getMateria(self):
        return self.materia

    def setNombreEstudiante(self, nombreEstudiante):
        self.nombreEstudiante = nombreEstudiante 

    def setNota(self, notaEstudiante):
        self.notaEstudiante = notaEstudiante

    def setMateria(self, materia):
        self.materia = materia

    def showOne(self):  # formateado "bonito", para mostrar de a uno
        return f"- ID Examen: {self.idExamen}\n- Nombre de estudiante: {self.nombreEstudiante}\n- Nota obtenida: {self.notaEstudiante}\n- Materia: {self.materia}"
    
    def showInFileFormat(self): #Formateo para escribir a archivo, me falló el __str__ y tengo mucho sueño como para ver por qué
        """lo muestro así, para respetar la forma como se lee el archivo"""
        return f"{self.idExamen};{self.getNombreEstudiante()};{self.getNota()};{self.getMateria()}"
        #Devuelvo idExamen así, para no modificar la estructura del archivo
    
    def showInTableFormat(self): #Formateo para imprimirlo en tabla
        resultado = ""
        resultado += f"| {self.getIdExamen()}\t\t"
        resultado += f"{self.getNombreEstudiante()}"
        resultado += "\t"*2
        resultado += "\t" if len(self.getNombreEstudiante()) <= 15 else ""
        resultado += "\t" if len(self.getNombreEstudiante()) <= 8 else ""
        resultado += f"{self.getNota()}\t\t"
        resultado += f"{self.getMateria()}"
        resultado += "\t" if len(self.getMateria()) <= 7 else ""
        resultado += "\t" if len(self.getMateria()) <= 11 else ""
        resultado += "|"        
        # Qué ganas de jodeeer!!! XD
        return resultado

def validadorFormatoExamen(linea):
    """ Creé esta función para validar cada elemento que va a entrar al array de exámenes
        Si todo sale bien, los valores convertidos a los formatos que corresponden.
        Creo que se puede mejorar para abarcar más casos, como el de modificar"""
    
    try:        
        idExamen = linea[0]  # No sé si hacerlo con integers o strings, por si hay que llenar los 0s a la izq
        nombreEstudiante = linea[1]
        notaEstudiante = float(linea[2])
        materia = linea[3]

        if int(idExamen) < 0: # Puede traer problemas, si por ejemplo, cambia el formato de idExamen
            raise Exception("Id del examen incorrecto")        
        if len(nombreEstudiante) < 3:
            raise Exception("Nombre de estudiante incorrecto, es muy corto")
        if notaEstudiante < 0 or notaEstudiante > 10:
            raise Exception("Formato de nota incorrecto")
        if not materia.isalpha():
            raise Exception("Formato de materia incorrecto")
    except Exception as e:
        print(f"Ocurrió un error al querer cargar el examen: {e}")
        exit() #Directamente salgo del programa, quizá sea mucho...

    return idExamen, nombreEstudiante, notaEstudiante, materia

def leerArchivo(lista, ruta):
    """ Esta función lee el archivo que se le pasa por parámetro y carga la lista que también se le pasa por parámetro
        En el proceso, chequea lo que se va a cargar al array usando la función validadorFormatoExamen
        Devuelve True si pudo cargar correctamente el archivo, False si no"""
    
    if len(lista) != 0:        
        lista.clear() #Por si cargo el archivo más de una vez
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            pruebaVacío = archivo.read(1)
            archivo.seek(0)
            if not pruebaVacío:
                raise Exception("El archivo está vacío")
            for linea in archivo:
                #Creo que de esta forma, hago uso ineficiente de la lectura de disco...
                #Creo que primero debería leer el archivo, y procesarlo una vez que está en memoria
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
        cargarMaterias(lista,globals()['materias'])
        setSetting('archivo cargado',True)
        setSetting('cantidad de examenes',len(lista))
        setSetting('ordenado',False)
    # me gustan los operadores ternarios :)
    return True if len(lista) != 0 else False

def separador(sep="*",veces=50):
    print(sep*veces)

def imprimirSettings():
    """Como getSettings devuelve el diccionario completo, 
    quizás imprima los settings de a uno, sólo los que me importa mostrar"""
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
    para ordenar la lista según ese parámetro. No devuelvo nada"""

    n = len(lista)    
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
        case _:
            raise Exception(f"Parametrización de bubbleSort(lista,{parametro}) es inválido")
        
    #Esto lo hago por si quiero ordenar un subset que, no sea la lista principal
    if modificaSetting:
        setSetting('ordenado',parametro)
    return    

def busquedaBinariaModificada(lista, parametro, valor):
    """Recibo una lista de TDAExamen, parametro (que sería la columna) y un valor, Devuelvo UN TDAExamen en el caso de buscar por IDexamen, y una lista en el caso de buscar por nota  
    Lo único a tener en cuenta es que la lista debe estar ordenada según el parámetro que esté buscando, ya sea por id o por nota
    """
    resultado = []     
    izq = 0
    der = len(lista) - 1
    
    match parametro:
        case "idExamen":                        
            while izq <= der :            
                med = (izq + der) // 2                
                if lista[med].getIdExamen() < valor:
                    izq = med + 1                
                elif lista[med].getIdExamen() > valor:
                    der = med - 1                
                else:
                    return lista[med]           
            return False

        case "notaEstudiante":
            while izq <= der:
                med = (izq + der) // 2               
                if lista[med].getNota() == valor:                    
                    resultado.append(lista[med])
                    # Escaneo hacia la izquierda
                    i = med - 1
                    while i >= izq and lista[i].getNota() == valor:
                        resultado.append(lista[i])
                        i -= 1
                    # Escaneo hacia la derecha
                    i = med + 1
                    while i <= der and lista[i].getNota() == valor:
                        resultado.append(lista[i])
                        i += 1
                    return resultado
                elif lista[med].getNota() < valor:
                    izq = med + 1
                else:
                    der = med - 1            
            return resultado
        case _:
            raise Exception(f"Parametrización de búsquedaBinariaModificada(lista,{parametro},{valor}) inválida")

def escribirArchivo(lista, ruta):
    """Recibo una lista de TDAExamen, y la ruta para escribir a archivo"""
    try:
        with open(ruta, 'w',encoding='utf-8') as archivo:
            for examen in lista:
                archivo.write(examen.showInFileFormat() + "\n")
    except:
        raise Exception("Error al escribir en archivo, ¿quizás falta de permisos de escritura?")
    else:
        return True

def cargarMaterias(lista, materias):
    for examen in lista:
        if examen.getMateria() not in materias:
            materias.append(examen.getMateria())

def getMateria():
    for i in range(len(globals()['materias'])):
        print(f"{i+1}) {globals()['materias'][i]}")
    separador("-")
    while True: #Puede ser así, o retornando False
        try:
            seleccion = int(input(f"Seleccione una materia (1/{len(globals()['materias'])}): "))
            if seleccion < 1 or seleccion > len(globals()['materias']):
                raise Exception()
        except:
            print("Opción inválida")            
        else:
            return globals()['materias'][seleccion - 1]

def getExamenPorMateria(lista, materia):
    """Recibo una lista de TDAExamen y una materia, y devuelvo una lista de TDAExamen"""

    resultado = []
    for examen in lista:
        if examen.getMateria() == materia:
            resultado.append(examen)    
    bubbleSort(resultado, "notaEstudiante", False)    
    return resultado

def modificarExamen(examen):
    """Recibo TDAExamen, debería validar los datos antes de asignarlos    
    devuelvo el objeto modificado o False si se decide no modificarlo
    Quizás debería comparar si se modificó alguna característica antes de volver"""
    
    examenModificado = examen
    while True:
        separador("-")
        print("MODIFICAR EXAMEN")
        separador("_")
        print(examenModificado.showOne())
        separador("-")
        print("1) Modificar nombre del estudiante")
        print("2) Modificar nota del estudiante")
        print("3) Modificar materia")
        print("9) Guardar cambios y volver al menú principal")
        print("0) Cancelar sin hacer cambios")
        separador("-")
        try:
            opcion = int(input("Ingrese una opción: "))
        except KeyboardInterrupt:
            return False
        except:
            print("Opción inválida")
        else:
            match opcion:
                case 1: # Modificar nombre
                    nuevoNombre = input("Ingrese el nuevo nombre del estudiante: ")
                    if len(nuevoNombre) > 30 or len(nuevoNombre) < 3:
                        print("Nombre inválido")
                    else:
                        examen.setNombreEstudiante(nuevoNombre)
                case 2: # Modificar nota
                    try:
                        nuevaNota = float(input("Ingrese la nueva nota del estudiante: "))
                        if nuevaNota < 0 or nuevaNota > 10:
                            raise Exception()
                    except:
                        print("Nota inválida")
                    else:
                        examenModificado.setNota(nuevaNota)
                case 3: # Modificar materia
                    materiaNueva = getMateria()
                    if materiaNueva:
                        examenModificado.setMateria(materiaNueva)
                    else:
                        print("No se modificó la materia")
                case 9: # Guardar cambios y volver al mená principal
                    return examenModificado
                case 0: # Cancelar
                    return False
                case _:
                    print("Opción inválida")

def printTable(lista):
    """Recibo una lista de TDAExamen, y la imprimo como una tabla, ponele"""
    limiteVertical = 20
    limiteHorizontal = 81
    def cabecera():
        separador("_",limiteHorizontal)
        print(f"|ID Examen\tNombre del estudiante\tNota del estudiante\tMateria\t\t|")
        separador("_",limiteHorizontal)

    veces = 0    
    cabecera()    
    for i in range(len(lista)):        
        print(lista[i].showInTableFormat())
        if (i + 1) % (limiteVertical) == 0 and i != 0:
            veces += 1                    
            print(f"Mostrando resultados {limiteVertical*(veces -1) + 1} a {limiteVertical*veces} de {len(lista)}")
            input("Pulse Enter para continuar...")
            cabecera()
    separador("_",limiteHorizontal)

def menuPrincipal():
    #Quizá cambie los elif por match-case...
    while True:        
        opcion = ""
        separador("_")
        print("MENU PRINCIPAL")
        imprimirSettings()
        separador("-")
        print("1) Leer exámenes desde archivo")
        print("2) Modificar examen")
        print("3) Eliminar examen")
        print("4) Ordenar examenes")
        print("5) Buscar examen/es")
        print("6) Imprimir exámenes como están en memoria")
        print("7) Imprimir exámenes según materia")
        print("0) Salir")
        separador()
        try:
            opcion = int(input("Ingrese una opción: "))
        except KeyboardInterrupt:
            opcion = 0
        except:
            pass
        #Cargar archivo       
        if opcion == 1:
            if leerArchivo(globals()['listaTDA'], globals()['ruta']) :
                print("Archivo cargado correctamente")
                input("pulse Enter para continuar...")

        #Modificar examen
        elif opcion == 2:
            if getSetting('archivo cargado'):
                if getSetting('ordenado') != "idExamen":
                    bubbleSort(globals()['listaTDA'], "idExamen")
                try:
                    examenAModificar = int(input("Ingrese el ID del examen a modificar: "))
                except:
                    examenAModificar = False # si falla el input, ni se molesta en buscar
                else:
                    examenAModificar = busquedaBinariaModificada(globals()['listaTDA'],"idExamen", examenAModificar)
                if examenAModificar: 
                    examenModificado = modificarExamen(examenAModificar)
                    if examenModificado:
                        globals()['listaTDA'].remove(examenAModificar)
                        # Puedo insertarlo así, porque en la función modificarExamen, copié el objeto
                        globals()['listaTDA'].append(examenModificado)
                        setSetting('ordenado', False)
                        escribirArchivo(globals()['listaTDA'], globals()['ruta'])
                        print("Examen modificado con éxito")
                        input("pulse Enter para continuar...")
                    else:
                        print("Examen no modificado")
                        input("pulse Enter para continuar...")
                else: 
                    print("ERROR: examen no encontrado")
                    input("pulse Enter para continuar...")                                     
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
                    decision = input("Está seguro que desea eliminar el examen? Esta acción no se puede deshacer S/N :")
                    if decision.upper() == "S":
                        globals()['listaTDA'].remove(examenAEliminar)
                        setSetting('cantidad de examenes',len(globals()['listaTDA']))
                        print("Examen eliminado con éxito")
                        escribirArchivo(globals()['listaTDA'], globals()['ruta'])
                        input("pulse Enter para continuar...")
                    else:
                        print("Examen no eliminado")
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
                    print("2) Por nota del examen (Ordena y muestra)")                    
                    print("0) Volver atrás")
                    try:
                        seleccion = int(input("Ingrese una opción: "))
                    except KeyboardInterrupt:
                        exit(0)
                    except:
                        pass
                    else:
                        match seleccion:
                            case 1:
                                if getSetting('ordenado') != "idExamen":
                                    bubbleSort(globals()['listaTDA'], "idExamen")
                                break
                            case 2:
                                if getSetting('ordenado') != "notaEstudiante":                                
                                    bubbleSort(globals()['listaTDA'], "notaEstudiante")
                                printTable(globals()['listaTDA'])                                
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
                                    separador()
                                    print(examenABuscar.showOne())
                                    input("pulse Enter para continuar...")
                                else:
                                    print("ERROR: examen no encontrado")
                                    input("pulse Enter para continuar...")

                        # Buscar por nota
                        case 2:
                            if getSetting('ordenado') != "notaEstudiante":
                                bubbleSort(globals()['listaTDA'], "notaEstudiante")
                            try:
                                examenABuscar = float(input("Ingrese la nota a buscar: "))
                            except:
                                print("ERROR: Ningún examen encontrado, escribió bien la nota?")
                            else:
                                examenes = busquedaBinariaModificada(globals()['listaTDA'],"notaEstudiante", examenABuscar)
                                if examenes:                                    
                                    printTable(examenes)
                                    input("pulse Enter para continuar...")
                                else:
                                    print("ERROR: Ningún examen encontrado, escribió bien la nota?")
                        # Volver al menù principal
                        case 0:
                            break
                        case _:
                            print("Opción incorrecta")
                    separador()
                    seleccion = input("Desea buscar otro examen? (S)/N :")
                    if seleccion.upper() == "N":
                        break                    
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        #Imprimir exámenes como están en memoria
        elif opcion == 6:
            if getSetting('archivo cargado'):
                printTable(globals()['listaTDA'])                              
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        #Imprimir exámenes según materia
        elif opcion == 7:            
            if getSetting('archivo cargado'):
                separador("_")
                print("Seleccione una materia para ver los exámenes cargados")
                separador("-")
                materiaSeleccionada = getMateria()
                examenesPorMateria = getExamenPorMateria(globals()['listaTDA'], materiaSeleccionada)
                printTable(examenesPorMateria)
                input("pulse Enter para continuar...")                
            else: 
                print("ERROR: exámenes no cargados")
                input("pulse Enter para continuar...")

        # Salir
        elif opcion == 0:
            break 
        # Opcion incorrecta
        else:
            print("Opción incorrecta")
    
#ruta = r"c:\pyfiles\examenes.txt"
ruta = "examenes.txt"
materias = []
listaTDA = []    
settings = {'ordenado': False, 'archivo cargado': False, 'cantidad de examenes' : 0} #Lo creo acá, porque tiene que ser global
menuPrincipal()

#leerArchivo(listaTDA, ruta)
#cargarMaterias(listaTDA, materias)
#print(materias) 
#print(getMateria())