from datetime import date, datetime

class Circuito:
    def __init__(self, nome, data):
        self.nome = nome 
        self.data = data
    
    def imprimeCircuito(self):
      print ("Circuito: ", self.nome,  ", Data: ", self.data)

listaDeCircuitos = []

listaDeCircuitos.append(Circuito("do Barém - 🇧🇭", date(2024,2,29)))

def retornaGrandPrixMaisProximo():
    hoje = date.today()

    removeCircuitosPassados()

    if((listaDeCircuitos[0].data - hoje).days == 1):
        return(f"Falta {(listaDeCircuitos[0].data - hoje).days} dia para o Grande prêmio {listaDeCircuitos[0].nome}")    
    elif((listaDeCircuitos[0].data - hoje).days == 0):
        return(f"Começa hoje o Grande prêmio {listaDeCircuitos[0].nome} !!!")
    else:    
        return(f"Faltam {(listaDeCircuitos[0].data - hoje).days} dias para o Grande prêmio {listaDeCircuitos[0].nome}")

def removeCircuitosPassados():
    hoje = date.today()
    global listaDeCircuitos
    listaDeCircuitos = [circuito for circuito in listaDeCircuitos if (circuito.data - hoje).days >= 0]