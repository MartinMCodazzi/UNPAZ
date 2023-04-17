# 16/04/2023
# Martín Nahuel Muñoz Codazzi

"""
Diseñar un TDA “Empleado” el cual respete la siguiente estructura y validaciones
sobre los atributos
    ID-> Autoincremental
    Apellido
    Nombre
    Sueldo > 0 
    Categoria -> (T) Temporal o (P) Planta 
    Edad > 18

La cantidad de empleados a cargar tiene una limitación de hasta 5 empleados, con
lo cual deberá controlar no exceder esa cantidad.
Se requiere desarrollar un algoritmo el cual mediante un menú de opciones
permite.
1) Cargar los empleados. Deberá considerar si carga los 5 juntos o si permite
preguntar si continúa cargando o no.
2) Mostrar todos los empleados con su sueldo bruto (Ordenado x importe)
3) Informar el empleado que más gana
4) Informat el empleado que menos gana
5) Informar la cantidad de empleados Temporales y el promedio de sueldo y la
cantidad de Planta y su promedio de sueldo.
6) Permitir la Búsqueda de un empleado determinado por ID. En caso que no
exista deberá informar “El empleado x no existe en nuestro registros”

"""

class TDAEmpleado:
    def __init__(self, id, nombre, apellido, sueldo, edad, categoria):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = self.checkMayorQue('Sueldo', sueldo, 0)
        self.edad = self.checkMayorQue('Edad', edad, 18)
        self.categoria = self.checkCategoria(categoria)

    def __str__(self):
        pass
    
    def checkCategoria(self,categoria):
        while True:
            if categoria.upper() == 'T' or categoria.upper() == 'P':
                return categoria.upper()
            else:
                categoria = input(
                    'ERROR: La categoria debe ser "T" o "P": ')
                continue
       
    def getCategoria(self):
        return self.categoria

    def checkMayorQue(self,nombreParam, param, comparar ):
        while True:
            try:
                if float(param) < comparar:
                    raise Exception
            except:
                param = input(
                    f'ERROR: en {nombreParam} debe ser mayor que {comparar}: ')
                continue # No sé si está de más, creo que sí...

            else:
                return float(param)

    def checkParam(self, nombreParam, param, tipo, largo=0):
        while True:
            try:
                match tipo:
                    case "int":
                        int(param)
                    case "str":
                        str(param)
                    case "float":
                        float(param)
                # Esto sirve para chequear el largo de los nombres como el de los teléfonos
                if largo != 0 and len(param) > largo:
                    raise Exception
            except TypeError:
                match tipo:
                    case "int":
                        param = input(
                            f'ERROR: En {nombreParam} debe ingresar un entero: ')
                    case "float":
                        param = input(
                            f'ERROR: En {nombreParam} debe ingresar un entero o un flotante separdo con ".": ')
                continue # No sé si está de más, creo que sí...

            except:
                param = input(
                    f'ERROR: en {nombreParam} se deben ingresar, como mucho {largo} caracteres: ')
                continue # No sé si está de más, creo que sí...

            else:
                match tipo:
                    case "int":
                        return int(param)
                    case "str":
                        return str(param)
                    case "float":
                        return float(param)

    def getNombreCompleto(self):
        return f'{self.apellido}, {self.nombre}'

### FIN DE LA CLASE ###

def empleadoMasGanador(empleados) -> str:
    ganador = empleados[0]
    for empleado in empleados:
        if empleado.sueldo > ganador.sueldo:
            ganador = empleado
    return f'El empleado que más gana es: {ganador.getNombreCompleto()}'

def empleadoMenosGanador(empleados) -> str:
    ganador = empleados[0]
    for empleado in empleados:
        if empleado.sueldo < ganador.sueldo:
            ganador = empleado
    return f'El empleado que menos gana es: {ganador.getNombreCompleto()}'
    
def informacionEmpleados(empleados) -> str:
    temporal = 0
    planta = 0
    sueldoTemporal = 0
    sueldoPlanta = 0
    for empleado in empleados:
        if empleado.categoria == 'T':
            temporal += 1
            sueldoTemporal += empleado.sueldo
        elif empleado.categoria == 'P':
            planta += 1
            sueldoPlanta += empleado.sueldo
    return f'La cantidad de empleados Temporales es: {temporal}\nEl promedio de sueldo de los empleados Temporales es: {sueldoTemporal/temporal}\nLa cantidad de empleados Planta es: {planta}\nEl promedio de sueldo de los empleados de Planta es: {sueldoPlanta/planta}'

def buscarEmpleado(empleados) -> str:
    id = input('Ingrese el ID del empleado a buscar: ')
    for empleado in empleados:
        if empleado.id == id:
            return f'El empleado con ID {id} es: {empleado.getNombreCompleto()}'
    return f'El empleado con el id {id} no existe en nuestros registros.'    

def mostrarEmpleados(empleados) -> str:
    pass

def menuPrincipal():
    seleccion = 0
    while seleccion != 7:
        print("\nBienvenido al sistema de gestión de empleados.")
        print("*" * 25)
        print("Seleccione una opción:")
        print("1) Cargar los empleados.")
        print("2) Mostrar todos los empleados con su sueldo bruto (Ordenado x importe).")
        print("3) Informar el empleado que más gana.")
        print("4) Informar el empleado que menos gana.")
        print("5) Informar la cantidad de empleados Temporales y el promedio de sueldo y la cantidad de Planta y su promedio de sueldo.")
        print("6) Permitir la BÚsqueda de un empleado determinado por ID.")
        print("7) Salir")
        try:
            seleccion = int(input("Seleccione una opción: "))            
            if seleccion < 1 or seleccion > 7:
                seleccion = int(input("Por favor, ingrese una opción válida, pulse 7 para salir: "))
                continue
        except ValueError:
            print("Por favor, ingrese un nÚmero.")        
        else:
            return seleccion

def comportamientoMenuPrincipal():
    listaEmpleados = [] 
    while True:
        seleccion = menuPrincipal()
        if seleccion == 1:
            cargarEmpleados(listaEmpleados)
        elif seleccion == 2:
            mostrarEmpleados()
        elif seleccion == 3:
            if len(listaEmpleados) == 0:
                print("No hay empleados cargados.")
                continue
            print(empleadoMasGanador(listaEmpleados))
        elif seleccion == 4:
            if len(listaEmpleados) == 0:
                print("No hay empleados cargados.")
                continue
            empleadoMenosGanador()
        elif seleccion == 5:
            if len(listaEmpleados) == 0:
                print("No hay empleados cargados.")
                continue
            print(informacionEmpleados(listaEmpleados))
        elif seleccion == 6:
            if len(listaEmpleados) == 0:
                print("No hay empleados cargados.")
                continue            
            print(buscarEmpleado())
        else:
            print("Gracias por usar nuestro sistema.")

def cargarEmpleados(arrayEmpleados):
    contador = len(arrayEmpleados)
    while contador < 5:
        id = contador 
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        sueldo = float(input("Ingrese el sueldo del empleado: $"))
        edad = int(input("Ingrese la edad del empleado: "))
        categoria = input("Ingrese la categoría del empleado: ")
        arrayEmpleados.append(TDAEmpleado(id, nombre, apellido, sueldo, edad, categoria))
        # No sé de qué otra forma podría hacer que sólo se ingresen 5 empleados.
        if contador == 5:
            print("Se han cargado los 5 empleados.")
            break
        print(f'Empleado {arrayEmpleados[contador].getNombreCompleto()} ingresado con éxito.')
        print("*" * 25)
        contador += 1
        while True:
            try:
                respuesta = input("¿Desea ingresar otro empleado? (S/N) :")
                if respuesta.upper() == "S":
                    break
                elif respuesta.upper() == "N":
                    contador = 5
                    break
            except:
                print("Por favor, ingrese una respuesta válida.")
                continue
        

### PROGRAMA PRINCIPAL  ###

comportamientoMenuPrincipal()