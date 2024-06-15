import datetime

class operador:
    def __init__(self, nombre:str, franco_ofrecido:datetime, franco_pedido:datetime) -> None:

        self.__nombre_opedador =  nombre
        self.__franco_ofrecido1 = franco_ofrecido
        self.__franco_pedido1 = franco_pedido

    def get_datos(self):
        return f"{self.get_nombre()} {self.get_francos_ofrecidos()} {self.get_francos_pedidos()}"

    def get_nombre(self):
        return self.__nombre_opedador
    
    def get_francos_ofrecidos(self):
        return self.__franco_ofrecido1
    
    def get_francos_pedidos(self):
        return self.__franco_pedido1