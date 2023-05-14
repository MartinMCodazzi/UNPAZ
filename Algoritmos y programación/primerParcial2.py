# 19/04/2023
# Martín Nahuel Muñoz Codazzi

import random

class tdaProducto():
    def __init__(self, codigo, stock, precio):
        self.codigo = codigo #falta validar entradas vacias
        self.stock = self.validarEntrada(stock,"stock", "int")
        self.precio = self.validarEntrada(precio, "precio", "float")

    def __str__ (self):
        return f'El producto tiene el código {self.codigo} \nHay {self.stock} unidades en existencia.\nTiene un precio de ${self.precio}\n'

    def validarEntrada(self,variable, nombreVariable, tipo):
        while True:
            try:
                match tipo:
                    case "int":
                        variable = int(variable)
                    case "float":
                        variable = float(variable)
                if variable < 0:
                    raise Exception
            except TypeError:
                match tipo:
                    case "int":
                        variable = input(
                            f'ERROR: En {nombreVariable} debe ingresar un entero: ')
                        continue
                    case "float":
                        variable = input(
                            f'ERROR: En {nombreVariable} debe ingresar un entero o un flotante separdo con ".": ')
                        continue            
            except:
                variable = input(f'La variable {nombreVariable} sólo acepta valores positivos: ')
            else:
                return variable
                    
    def getPrecio(self) -> int:
        return self.precio

### FIN DE LA CLASE ###

def cargarProductos (vector):
    for i in range(5):
        codigo = input('Por favor ingrese el código del producto: ')
        stockSinSanitizar = input('Ingrese el stock del producto: ')
        #stockSinSanitizar = random.randrange(1,10)
        precioSinSanitizar = input('Ingrese el precio del producto: $')
        #precioSinSanitizar = random.randrange(1,10)
        vector[i] = tdaProducto(codigo,stockSinSanitizar,precioSinSanitizar)

def calcularPromedio(vector):
    acumulador = 0
    contador = 0
    for producto in vector:
        acumulador += producto.precio
        contador += 1
    return acumulador/contador

def calcularProductosSobrePromedio(vector):
    promedio = calcularPromedio(vector)
    print(f'El promedio de precios de producto es :^{promedio}')
    for producto in vector:
        if producto.precio > promedio:
            print('*' * 25)
            print(producto)

def menuPrincipal():
    while True:
        print('*' * 25)
        print('Bienvendido al sistema de carga y proceso de productos')
        print('*' * 25)
        print('Pulse 1 para cargar productos')
        print('Pulse 2 para informar los productos con precio por encima del promedio')
        print('pulse 3 para salir')
        try:
            seleccion = int(input('Su selección: '))
            if seleccion < 1 or seleccion > 3:
                raise Exception
        except:
            print('Por favor ingrese un número entre 1 y 3')
        else:
            return seleccion

def procesarMenuPrincipal (vector):
    while True:
        seleccion = menuPrincipal()
        match seleccion:
            case 1:
                cargarProductos(vector)
            case 2:
                calcularProductosSobrePromedio(vector)
            case 3:
                print('Gracias por usar el sistema')
                break

### FINAL DE FUNCIONES ###

vectorProductos = [0] * 5
procesarMenuPrincipal(vectorProductos)
exit(0)