import discord
from clases.class_operador import operador
from discord.ext import commands
from clases.class_aux import aux
from clases.class_matcheo import match
from clases.class_sqlite import manageDB

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)
matcheo = match()
db = manageDB()

db.crear_tabla()
matcheo.cargar_db(db.recibir_datos())

def check_channel(ctx):
      return ctx.channel.id == 1250230495128850494

@commands.command()
@commands.check(check_channel)
async def test(ctx,ingresado_franco_ofrecido=None , ingresado_franco_pedido=None):

        if not(ingresado_franco_ofrecido == None or ingresado_franco_pedido == None):
            ingresado_franco_ofrecido = aux.format_date(ingresado_franco_ofrecido)
            ingresado_franco_pedido = aux.format_date(ingresado_franco_pedido)
            nombre = ctx.author
            db.agregar_datos(nombre,ingresado_franco_ofrecido,ingresado_franco_pedido)
            op_ingresado = operador(nombre=nombre,franco_ofrecido=ingresado_franco_ofrecido,franco_pedido=ingresado_franco_pedido)

            matcheo.add_lists(op_ingresado)
            lista_resultados = matcheo.buscar_V4(op_ingresado)
            for resultado in lista_resultados:
                 await ctx.send(f"{resultado[0].mention} tiene el franco ({resultado[1]}), que {resultado[2].mention}")
                 op_necesita = resultado[0]
                 op_ofrece = resultado[2]
                 await op_necesita.send(f"{resultado[2]} Tiene el franco q necesitás: {resultado[1]} y pide el q ofreces")
                 await op_ofrece.send(f"{resultado[0]} pide el franco q ofreces: {resultado[1]} y tiene el q necesitas.")
                 print(f"log: Se mandó priv a {op_necesita} y {op_ofrece}")
            await ctx.send(f"Agregado con exito.")
        else:
            await ctx.send(f"**Error de capa 8**. francos faltantes o mal escrito")
            await ctx.send(f"Soporte: Tener dos fechas ingresadas con el formato de fecha **dd/mm/aaaa**")
             
@commands.command()
async def list(ctx):
    lista = matcheo.get_list()
    for op in lista:
        await ctx.send(op.get_datos())

@commands.command()
async def tinder(ctx):
        lista = matcheo.buscar_V3()
        await ctx.send(f"Los matchs hasta el momento:")
        for msj in lista:
             await ctx.send(f"{msj}\n")

@commands.command()
async def msj(ctx):
     autor = ctx.author
     await autor.send(autor)

bot.add_command(test)
bot.add_command(list)
bot.add_command(tinder)
bot.add_command(msj)


bot.run(TOKEN_DS)




