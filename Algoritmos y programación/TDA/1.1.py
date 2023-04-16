# 16/04/2023
# Martín Nahuel Muñoz Codazzi

"""
Diseñar el TDA OperacionesBasicas el cual tenga dentro de su estructura
información de un NumeroA y de un Numero B. Finalmente el TDA debera expresar
las operaciones de suma, resta, multiplicación y división . Se deberán validar
colocar números mayores a 0.
"""

class OperacionesBasicas:
    def __init__ (self,numeroA,numeroB):
        self.numeroA = self.checkNumeroEntero(numeroA)
        self.numeroB = self.checkNumeroEntero(numeroB)

    def checkNumeroEntero(self,numero):
        while True:
            try:
                int(numero)
                if int(numero) <= 0:
                    raise ValueError
            except ValueError:
                print("ERROR: el número ingresado debe ser mayor a 0, y debe ser entero")
                numero = input("Por favor, ingrese el número nuevamente: ")
            else:
                break
        return int(numero)
    
    def suma(self):
        return self.numeroA + self.numeroB
    
    def resta(self):
        return self.numeroA - self.numeroB
    
    def multiplicacion(self):
        return self.numeroA * self.numeroB
    
    def division(self):
        try:
            resultado = self.numeroA / self.numeroB
        except ZeroDivisionError: # Creo que esta excepción nunca se cumpliría
            return "No se puede dividir por 0"
        else:
            return resultado

    def __str__(self):
        resSuma = f'la suma entre {self.numeroA} y {self.numeroB} es {self.suma()} \n'
        resResta = f'la resta entre {self.numeroA} y {self.numeroB} es {self.resta()} \n'
        resMulti = f'la multiplicación entre {self.numeroA} y {self.numeroB} es {self.multiplicacion()} \n'
        resDivi = f'la división entre {self.numeroA} y {self.numeroB} es {self.division()} \n'
        return "\n" + resSuma + resResta + resMulti + resDivi


### PROGRAMA PRINCIPAL ###
numeroSinChequear1 = input("Ingrese un número entero mayor a 0 :")
numeroSinChequear2 = input("Ingrese otro número entero mayor a 0 :")
conjuntoDeNumeros = OperacionesBasicas(numeroSinChequear1,numeroSinChequear2)

print(conjuntoDeNumeros)

exit(0)