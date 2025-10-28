class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def nombre(self):
        return self.__nombre.title()

    @property
    def precio(self):
        return self.__precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.__cantidad = cantidad

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @precio.setter
    def precio(self, precio):
        self.__precio = precio
