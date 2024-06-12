from clases.class_operador import operador
from clases.class_matcheo import match
import random
import datetime
from clases.class_sqlite import manageDB

lista_dias = ["Lunes", "Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
lista_ops = list()

lista_abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

db= manageDB()
db.crear_tabla()
m = match()

for i in range(4):
    fecha_random = datetime.date(year=2024, month=6,day=random.randint(1,30))
    fecha_random2 = datetime.date(year=2024, month=6,day=random.randint(1,30))
    db.agregar_datos(login=random.randint(1000,9999),nombre=random.choice(lista_abc),franco_ofrecido=fecha_random,franco_pedido=fecha_random2)
    # op = operador(login=random.randint(1000,9999),nombre=random.choice(lista_abc),franco_ofrecido=fecha_random,franco_pedido=fecha_random2)
    # m.add_lists(op)
    # print(op.get_datos())

lista_op = db.recibir_datos()
for op in lista_op:
    print(op.get_datos())

# encuentra = match()
# encuentra.buscar_V3(lista_ops) 

# op = operador(login=random.randint(1000,9999),nombre="patooo",franco_ofrecido=fecha_random,franco_pedido=fecha_random2)
# print("---------------------------------")
# print(op.get_datos())
# print(m.buscar_V3())
# print(m.buscar_V4(op))
# # encuentra = match(lista_ops)
# # encuentra.volver_a_buscar()



# operador1 = operador("juan",franco_ofrecido= random.choice(lista_dias), franco_ofrecido2=random.choice(lista_dias),franco_pedido=random.choice(lista_dias),franco_pedido2=random.choice(lista_dias))
# operador2 = operador("manuel",franco_ofrecido= random.choice(lista_dias), franco_ofrecido2=random.choice(lista_dias),franco_pedido=random.choice(lista_dias),franco_pedido2=random.choice(lista_dias))



# macheo_de_op = match(operador1,operador2)
# print(f"{operador1.nombre_opedador} ofrecidos {operador1.franco_ofrecido1}  {operador1.franco_ofrecido2}")
# print(f"{operador2.nombre_opedador} pedidos {operador2.franco_pedido1}  {operador2.franco_pedido2}")

# print(f"{operador2.nombre_opedador} ofrecidos {operador2.franco_ofrecido1}  {operador2.franco_ofrecido2}")
# print(f"{operador1.nombre_opedador} pedidos {operador1.franco_pedido1}  {operador1.franco_pedido2}")

# macheo_de_op.buscar_coincidencias()



