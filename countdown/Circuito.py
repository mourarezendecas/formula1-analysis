from datetime import date, datetime

class Circuito:
    def __init__(self, nome, data):
        self.nome = nome 
        self.data = data
    
    def imprimeCircuito(self):
      print ("Circuito: ", self.nome,  ", Data: ", self.data)

list = []

list.append(Circuito("do Barém - 🇧🇭", date(2023,3,3)))
list.append(Circuito("da Arábia Saudita - 🇸🇦", date(2023,3,17)))
list.append(Circuito("da Austrália - 🇦🇺", date(2023,3,31)))
list.append(Circuito("do Azeibarjão - 🇦🇿", date(2023,4,28)))
list.append(Circuito("dos Estados Unidos - 🇺🇸", date(2023,5,5)))
list.append(Circuito("da Itália - 🇮🇹", date(2023,5,19)))
list.append(Circuito("de Mônaco - 🇲🇨", date(2023,5,26)))
list.append(Circuito("da Espanha - 🇪🇸", date(2023,6,2)))
list.append(Circuito("do Canadá - 🇨🇦", date(2023,6,16)))
list.append(Circuito("da Austria - 🇦🇹", date(2023,6,30)))
list.append(Circuito("do Reino Unido - 🇬🇧", date(2023,7,7)))
list.append(Circuito("da Hungria - 🇭🇺", date(2023,7,21)))
list.append(Circuito("da Bélgica - 🇧🇪", date(2023,7,28)))
list.append(Circuito("da Holanda - 🇳🇱", date(2023,8,25)))
list.append(Circuito("da Itália - 🇮🇹", date(2023,9,1)))
list.append(Circuito("de Singapura - 🇸🇬", date(2023,9,15)))
list.append(Circuito("do Japão - 🇯🇵", date(2023,9,22)))
list.append(Circuito("do Qatar - 🇶🇦", date(2023,10,6)))
list.append(Circuito("dos Estados Unidos - 🇺🇸", date(2023,10,20)))
list.append(Circuito("do México - 🇲🇽", date(2023,10,27)))
list.append(Circuito("do Brasil - 🇧🇷", date(2023,11,3)))
list.append(Circuito("dos Estados Unidos - 🇺🇸", date(2023,11,16)))
list.append(Circuito("de Abu Dhabi - 🇺🇸", date(2023,11,24)))

def retornaGrandPrixMaisProximo():
    hoje = date.today()

    for circuito in list:
            if((circuito.data-hoje).days<0):
                list.remove(circuito)    

    if((list[0].data - hoje).days == 1):
        return(f"Falta {(list[0].data - hoje).days} dia para o Grande prêmio {list[0].nome}")    
    else:    
        return(f"Faltam {(list[0].data - hoje).days} dias para o Grande prêmio {list[0].nome}")