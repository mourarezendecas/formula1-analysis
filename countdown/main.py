import time
import tweepy
import datetime
import os
from dotenv import load_dotenv
import Circuito

print('EXECUTANDO')

load_dotenv()

api = tweepy.Client(
    consumer_key= os.environ.get('API_KEY'),
    consumer_secret= os.environ.get('API_SECRET_KEY'),
    access_token= os.environ.get('ACCESS_TOKEN'),
    access_token_secret= os.environ.get('ACCESS_TOKEN_SECRET')
)

hora_execucao = "02:36"

while True:
    hora_atual = datetime.datetime.now().strftime("%H:%M")
    if hora_atual == hora_execucao:
        print("Hora de executar o comando!")
        try: 
            tweet = api.create_tweet(text=Circuito.retornaGrandPrixMaisProximo())
            print(tweet)
            print('Executado às: ',hora_atual)
        except Exception as e:
            print('Erro: ',e)
    time.sleep(60)