# Martín Nahuel Muñoz Codazzi
# 15/05/2023

"""
Realizar un programa principal que mediante el llamado de funciones y archivos  permita en un archivo BINARIO: 
∙ Agregar un contacto 
∙ Mostrar todos los contactos 
∙ Eliminar un contacto 
∙ Consultar un contacto por DNI 
∙ Modificar un contacto 
La estructura de registros a agendar es la siguiente :  
DNI INT , 
Apellido CHAR(50),  
Nombre Char(50) 
Telefono Char(20) 
El archivo sobre el que se guardará la información se llamará contacto.dat 
"""

class TDAcontacto:
    def __init__(self, dni, apellido, nombre, telefono):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self) -> str:
        return f"DNI:\t{self.dni}\nNombre completo:\t{self.nombre} {self.apellido}\nTeléfono:\t{self.telefono}"

def agregar_contacto():
    pass
def mostrar_contactos():
    pass
def eliminar_contacto():
    pass
def consultar_contacto_por_dni():
    pass
def modificar_contacto():
    pass

def cargar_contactos_a_memoria():
    with open("contacto.dat", "rb") as archivo:
        pass

def guardar_contactos_en_archivo(lista_contactos):
    with open("contacto.dat", "wb") as archivo:
        archivo.write(lista_contactos)
    return True

