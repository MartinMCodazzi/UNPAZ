class Cliente:

    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
    
    @property
    def nombre(self):        
        return self.__nombre.title()

    @property
    def email(self):        
        return self.__email.lower()

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.__edad = edad

    @nombre.setter
    def nombre(self, nombre):        
        self.__nombre = nombre

    @email.setter
    def email(self, email):       
        self.__email = email

    def realizar_pedido(self):
        pass

    def edad_valida(self):
        return 18 <= self.edad <= 120


        