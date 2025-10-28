from Domain.Cliente import Cliente
from Domain.Producto import Producto
from Domain.Pedido import Pedido
from Services.PedidoService import PedidoService

class TestPedidoService:
    def test_procesar_pedido(self):
        cliente = Cliente("Juan Perez", "juan.perez@example.com", 25)
        producto1 = Producto("Laptop", 1500, 1)
        producto2 = Producto("Mouse", 50, 2)
        pedido = Pedido([producto1, producto2])
        servicio = PedidoService(cliente, pedido)
        assert servicio.procesar_pedido() == 1600
        servicio.agregar_descuento("PROMO10")        
        assert servicio.procesar_pedido() == 1440