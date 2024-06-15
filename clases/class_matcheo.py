from clases.class_operador import operador

class match:

    def __init__(self) -> None:
        self.lista_ops = list()

    def add_lists(self,op:operador):
        self.lista_ops.append(op)

    def get_list(self):
        return self.lista_ops
    
    def cargar_db(self,lista:list[operador]):
        for op in lista:
            self.add_lists(op)
        print("Se cargó lista con exito")

    def buscar_V3(self):
        msj = ""
        lista_encontrados = list()
        copia_lista = self.lista_ops.copy()
        for op_necesita in self.lista_ops:
            for op_ofrece in copia_lista:
                if op_necesita.get_id() != op_ofrece.get_id():
                     francos_ofrecidos_op = op_ofrece.get_francos_ofrecidos()
                     franco_necesitado = op_necesita.get_francos_pedidos()
                    #  for franco in francos_ofrecidos_op:
                     if francos_ofrecidos_op == franco_necesitado:
                        op_nombre_donante = op_ofrece.get_nombre()
                        op_nombre_aceptante = op_necesita.get_nombre()
                        msj =f"el operador: **{op_nombre_donante}** ofrece el franco: **{francos_ofrecidos_op}** que: **{op_nombre_aceptante}** necesita "
                        lista_encontrados.append(msj)
        
        return lista_encontrados
                        

    def buscar_V4(self, op_necesita:operador):
        msj = ""
        lista_resultados = list()
        for op_ofrece in self.lista_ops:
            if op_necesita.get_nombre() != op_ofrece.get_nombre():
                francos_ofrecidos_op = op_ofrece.get_francos_ofrecidos()
                franco_necesitado = op_necesita.get_francos_pedidos()
                # for franco in francos_ofrecidos_op:
                if francos_ofrecidos_op == franco_necesitado:
                    op_nombre_donante = op_ofrece.get_nombre()
                    op_nombre_aceptante = op_necesita.get_nombre()
                    msj =f"el operador: **{op_nombre_donante}** ofrece el franco: **{francos_ofrecidos_op}** que: **{op_nombre_aceptante}** necesita"
                    lista_resultados.append([op_nombre_donante,francos_ofrecidos_op,op_nombre_aceptante]) 

        return lista_resultados
