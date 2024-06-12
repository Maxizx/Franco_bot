import random
import datetime

class operador:
    def __init__(self, login:int,nombre:str, franco_ofrecido:datetime, franco_pedido:datetime) -> None:
        self.__id_operador = login
        self.__nombre_opedador =  nombre
        self.__franco_ofrecido1 = franco_ofrecido
        self.__franco_ofrecido2 = None
        self.__franco_pedido1 = franco_pedido

    def get_datos(self):
        return f"{self.get_id()} {self.get_nombre()} {self.get_francos_ofrecidos()} {self.get_francos_pedidos()}"

    def get_id(self):
        return self.__id_operador

    def get_nombre(self):
        return self.__nombre_opedador
    
    def get_francos_ofrecidos(self):
        # return [self.__franco_ofrecido1,self.__franco_ofrecido2]
        return self.__franco_ofrecido1
    
    def get_francos_pedidos(self):
        return self.__franco_pedido1