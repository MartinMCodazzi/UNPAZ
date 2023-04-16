# 16/04/2023
# Martín Nahuel Muñoz Codazzi

"""
Desarrollar un TDA Alumno mediante código de programación la carga de datos de 5
alumnos y que posea la siguiente estructura:
    Codigo_Alumno INT
    Apellido y Nombre CHAR(50)
    Telefono Char(12)
    Edad INT
Finalmente escribir la rutina que lista los datos cargados.
"""


class TDAAlumno():
    def __init__(self, Codigo, Apellido, Nombre, Telefono, Edad):
        self.codigo = self.checkParam("código",Codigo, "int")
        self.apellido = self.checkParam("apellido",Apellido, "str", 25)
        self.nombre = self.checkParam("nombre",Nombre, "str", 25)
        self.telefono = self.checkParam("telefono",Telefono, "str", 12)
        self.edad = self.checkParam("edad", Edad, "int")        

    def checkParam(self, nombreParam, param, tipo, largo=0):
        while True:
            try:
                match tipo:
                    case "int":
                        int(param)
                    case "str":
                        str(param)
                # Esto sirve para chequear el largo de los nombres como el de los teléfonos
                if largo != 0 and len(param) > largo:
                    raise Exception
            except TypeError:
                match tipo:
                    case "int":
                        param = input(
                            f'ERROR: En {nombreParam} debe ingresar un entero: ')
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

    def __str__(self) -> str:
        codigo = f'El código del estudiante es {self.codigo} \n'        
        nombre = f'El nombre completo del estudiante es {self.apellido}, {self.nombre} \n'
        telefono = f'El teléfono del estudiante es {self.telefono} \n'
        edad = f'La edad del estudiante es {self.edad} \n'
        return '\n' + codigo + nombre + telefono + edad


### PROGRAMA PRINCIPAL ###
estudiantes = [0]*5 # Para emular un array 

for i in range(5):        
    codigoSinChequear = input('Ingrese el código del estudiante: ')
    apellidoSinChequear = input('Ingrese el apellido del estudiante: ')
    nombreSinChequear = input('Ingrese el nombre del estudiante: ')
    teléfonoSinChequear = input('Ingrese el teléfono del estudiante: ')
    edadSinChequear = input('Ingrese la edad del estudiante: ')
    estudiantes[i] = TDAAlumno(codigoSinChequear,apellidoSinChequear,nombreSinChequear,teléfonoSinChequear,edadSinChequear)
    #Debería limpiar la pantalla después de cada carga

for estudiante in estudiantes: 
    print(estudiante) 



