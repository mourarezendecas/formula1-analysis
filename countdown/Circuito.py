from datetime import date, datetime

class Circuito:
    def __init__(self, nome, data, circuito):
        self.nome = nome
        self.data = data
        self.circuito = circuito

    def imprimeCircuito(self):
      print ("Circuito: ", self.nome,  ", Data: ", self.data,  ", Circuito: ", self.circuito)

listaDeCircuitos = []
listaDeCircuitos.append(Circuito("do Barém - 🇧🇭", date(2024,2,29),"Circuito Internacional do Bahrein"))
listaDeCircuitos.append(Circuito("da Arábia Saudita - 🇸🇦", date(2024,3,7),"Circuito Jeddah Corniche"))
listaDeCircuitos.append(Circuito("da Austrália - 🇦🇺", date(2024,3,22),"Circuito de Albert Park"))
listaDeCircuitos.append(Circuito("do Japão - 🇯🇵", date(2024,4,5),"Circuito de Suzuka"))

def retornaGrandPrixMaisProximo():
    hoje = date.today()

    removeCircuitosPassados()

    if((listaDeCircuitos[0].data - hoje).days == 1):
        return(f"Falta {(listaDeCircuitos[0].data - hoje).days} dia para o Grande prêmio {listaDeCircuitos[0].nome}")
    elif((listaDeCircuitos[0].data - hoje).days == 0):
        return(f"Começa hoje o Grande prêmio {listaDeCircuitos[0].nome} ! \n No {listaDeCircuitos[0].circuito}")
    else:
        return(f"Faltam {(listaDeCircuitos[0].data - hoje).days} dias para o Grande prêmio {listaDeCircuitos[0].nome}")

def removeCircuitosPassados():
    hoje = date.today()
    global listaDeCircuitos
    listaDeCircuitos = [circuito for circuito in listaDeCircuitos if (circuito.data - hoje).days >= 0]