import requests
import json
from datetime import datetime
from googletrans import Translator

today = datetime.today()


class GrandPrix:
    def __init__(self, name, circuit, country, day):
        self.name = name
        self.circuit = circuit
        self.country = country
        self.day = day
        self.daysLeft = self.day - today

    def printGrandPrix(self):
        print("Circuito: ", self.name, ", Data: ", self.day, ", Dias faltando: ", self.daysLeft)


url = "https://ergast.com/api/f1/2023.json"
response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
else:
    print("Erro na solicitação da API")

grandPrixList = []

for race in data['MRData']['RaceTable']['Races']:
    # setting it up
    dateInputFormat = "%Y-%m-%d"
    translator = Translator(service_urls=['translate.googleapis.com'])

    # collecting
    name = translator.translate(race['raceName'],dest='pt')
    circuit = race['Circuit']['circuitName']
    country = race['Circuit']['Location']['country']
    day = race['date']
    time = race['time']

    # attributing
    grandPrix = GrandPrix(name, circuit, country, datetime.strptime(day, dateInputFormat))
    grandPrixList.append(grandPrix)

for GrandPrix in grandPrixList:
    if GrandPrix.daysLeft.days >= 0:
        GrandPrix.printGrandPrix()
