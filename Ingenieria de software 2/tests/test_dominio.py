from Domain.CuponDescuento import CuponDescuento
from Domain.Cliente import Cliente
from Domain.Producto import Producto
from Domain.Pedido import Pedido

class TestCliente:
    def test_edad_valida(self):
        cliente = Cliente("Juan Perez","juan.perez@example.com", 25)
        assert cliente.edad_valida() == True

        cliente_menor = Cliente("Ana Gomez","ana.gomez@example.com", 17)
        assert cliente_menor.edad_valida() == False

        cliente_mayor = Cliente("Carlos Ruiz","carlos.ruiz@example.com", 121)
        assert cliente_mayor.edad_valida() == False
    
class TestCuponDescuento:
    def test_obtener_descuento(self):
        cupon = CuponDescuento("PROMO10", 10)
        cupon2 = CuponDescuento("DESCUENTO20", 20)
        assert cupon.obtener_nominal_descuento() == 10
        assert cupon2.obtener_nominal_descuento() == 20
        assert CuponDescuento.obtener_nominal("INVALIDO") == 0
        assert CuponDescuento.obtener_nominal("PROMO10") == 10
        assert CuponDescuento.obtener_nominal("DESCUENTO20") == 20

    def test_es_codigo_valido(self):
        cupon = CuponDescuento("PROMO10", 10)
        cupon2 = CuponDescuento("DESCUENTO20", 20)
        assert CuponDescuento.es_codigo_valido("PROMO10") == True
        assert CuponDescuento.es_codigo_valido("DESCUENTO20") == True
        assert CuponDescuento.es_codigo_valido("INVALIDO") == False

class TestProducto:
    def test_crear_producto(self):
        producto = Producto("Laptop", 1500, 1)
        assert producto.nombre == "Laptop"
        assert producto.precio == 1500
        assert producto.cantidad == 1

class TestPedido:
    def test_crear_pedido(self):                
        producto1 = Producto("Laptop", 1500, 1)
        producto2 = Producto("Mouse", 50, 2)
        pedido = Pedido([producto1, producto2])        
        assert len(pedido.productos) == 2
        assert pedido.subtotal() == 1600

    def test_agregar_producto(self):
        producto = Producto("Teclado", 100, 1)
        pedido = Pedido([producto])
        assert len(pedido.productos) == 1
        assert pedido.subtotal() == 100
        nuevo_producto = Producto("Monitor", 300, 1)
        pedido.agregar_producto(nuevo_producto, 2)
        assert len(pedido.productos) == 2
        assert pedido.subtotal() == 700
        
