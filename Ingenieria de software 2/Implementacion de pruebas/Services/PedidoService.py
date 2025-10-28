from Domain.CuponDescuento import CuponDescuento
from Domain.Cliente import Cliente
from Domain.Pedido import Pedido

class PedidoService:
    def __init__(self, cliente: Cliente, pedido: Pedido):
        self.pedido = pedido
        self.cliente = cliente
        self.porcentaje_descuento = 0

    def agregar_descuento(self, codigo_descuento):
        if CuponDescuento.es_codigo_valido(codigo_descuento):
            self.porcentaje_descuento = CuponDescuento.obtener_nominal(codigo_descuento)
        else:
            raise ValueError("El código de cupón no es válido.")

    def procesar_pedido(self):
        if not self.cliente.edad_valida():
            raise ValueError("La edad del cliente no es válida para realizar el pedido.")
        subtotal = self.pedido.subtotal()
        descuento = subtotal * self.porcentaje_descuento / 100
        total = subtotal - descuento
        return total