class CuponDescuento:    
    cupones = []

    def __init__(self, codigo, porcentaje):
        self.codigo = codigo
        self.porcentaje = porcentaje        
        self.registrar_cupon(self)  

    def obtener_nominal_descuento(self):
        return self.porcentaje  

    @classmethod
    def es_codigo_valido(cls, codigo):        
        return any(codigo == cupon.codigo for cupon in cls.cupones)
    
    @classmethod
    def obtener_nominal(cls, codigo):        
        for cupon in cls.cupones:
            if cupon.codigo == codigo:
                return cupon.obtener_nominal_descuento()
        return 0

    @classmethod
    def registrar_cupon(cls, cupon):
        cls.cupones.append(cupon)

    @classmethod
    def obtener_cupones(cls):
        return cls.cupones
    
    