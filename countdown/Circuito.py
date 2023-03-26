from datetime import date, datetime

class Circuito:
    def __init__(self, nome, data):
        self.nome = nome 
        self.data = data
    
    def imprimeCircuito(self):
      print ("Circuito: ", self.nome,  ", Data: ", self.data)

listaDeCircuitos = []

listaDeCircuitos.append(Circuito("do Barém - 🇧🇭", date(2023,3,3)))
listaDeCircuitos.append(Circuito("da Arábia Saudita - 🇸🇦", date(2023,3,17)))
listaDeCircuitos.append(Circuito("da Austrália - 🇦🇺", date(2023,3,31)))
listaDeCircuitos.append(Circuito("do Azeibarjão - 🇦🇿", date(2023,4,28)))
listaDeCircuitos.append(Circuito("dos Estados Unidos - 🇺🇸", date(2023,5,5)))
listaDeCircuitos.append(Circuito("da Itália - 🇮🇹", date(2023,5,19)))
listaDeCircuitos.append(Circuito("de Mônaco - 🇲🇨", date(2023,5,26)))
listaDeCircuitos.append(Circuito("da Espanha - 🇪🇸", date(2023,6,2)))
listaDeCircuitos.append(Circuito("do Canadá - 🇨🇦", date(2023,6,16)))
listaDeCircuitos.append(Circuito("da Austria - 🇦🇹", date(2023,6,30)))
listaDeCircuitos.append(Circuito("do Reino Unido - 🇬🇧", date(2023,7,7)))
listaDeCircuitos.append(Circuito("da Hungria - 🇭🇺", date(2023,7,21)))
listaDeCircuitos.append(Circuito("da Bélgica - 🇧🇪", date(2023,7,28)))
listaDeCircuitos.append(Circuito("da Holanda - 🇳🇱", date(2023,8,25)))
listaDeCircuitos.append(Circuito("da Itália - 🇮🇹", date(2023,9,1)))
listaDeCircuitos.append(Circuito("de Singapura - 🇸🇬", date(2023,9,15)))
listaDeCircuitos.append(Circuito("do Japão - 🇯🇵", date(2023,9,22)))
listaDeCircuitos.append(Circuito("do Qatar - 🇶🇦", date(2023,10,6)))
listaDeCircuitos.append(Circuito("dos Estados Unidos - 🇺🇸", date(2023,10,20)))
listaDeCircuitos.append(Circuito("do México - 🇲🇽", date(2023,10,27)))
listaDeCircuitos.append(Circuito("do Brasil - 🇧🇷", date(2023,11,3)))
listaDeCircuitos.append(Circuito("dos Estados Unidos - 🇺🇸", date(2023,11,16)))
listaDeCircuitos.append(Circuito("de Abu Dhabi - 🇺🇸", date(2023,11,24)))


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