import time
import tweepy
from keys import consumer_key, consumer_secret, access_token, access_token_secret
import datetime

api = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

hora_execucao = "03:00"

while True:
    hora_atual = datetime.datetime.now().strftime("%H:%M")
    if hora_atual == hora_execucao:
        print("Hora de executar o comando!")
        try: 
            tweet = api.create_tweet(text="Hello world!!!.py")
            print(tweet)
            print('Executado às: ',hora_atual)
        except Exception as e:
            print('Erro: ',e)
    time.sleep(60)