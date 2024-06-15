import sqlite3
from clases.class_operador import operador

class manageDB:
    def __init__(self) -> None:
        self.nombre_del_archivo = "bd_solicitudes.db"


    def crear_tabla(self):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
                conexion.execute("create table if not exists solicitudes (nombre TEXT,franco_ofrecido DATE,franco_pedido DATE);")

    def agregar_datos(self,nombre,franco_ofrecido,franco_pedido):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
            conexion.execute("insert into solicitudes(nombre,franco_ofrecido,franco_pedido) values (?,?,?)", (str(nombre),franco_ofrecido,franco_pedido))
            conexion.commit()#


    def recibir_datos(self):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
            cursor = conexion.execute("SELECT * FROM solicitudes;")
            lista = []
            for fila in cursor:
                op = operador(fila[0],fila[1],fila[2])
                lista.append(op)
            return lista


