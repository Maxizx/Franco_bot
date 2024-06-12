import re
import datetime


class aux():

    def filtro_numero(string:str):
        patron = "[0-9]"
        x = re.findall(patron,string)
        numeros = ""
        for i in x:
            numeros += i
        return numeros

    def format_date(string:str):
        
        separado = re.split("/",string)
        fecha = datetime.date(int(separado[2]),int(separado[1]),int(separado[0]))
        return fecha





