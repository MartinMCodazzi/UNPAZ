from Domain.Producto import Producto

class Pedido:
    def __init__(self, productos: list[Producto]):
        self.productos = productos

    def agregar_producto(self, item: Producto, cantidad: int):
        item.cantidad = cantidad
        self.productos.append(item)

    def subtotal(self) -> float:
        return sum(item.precio * item.cantidad for item in self.productos)