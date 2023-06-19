import tweepy
import csv
from unidecode import unidecode

# Agrega tus credenciales de API

consumer_key = "DhsrhpsjPxSks5YR6BwohUeV0"
consumer_secret = "FvMyQTgP8izDaasHiuWF6r1APyIu5HvlaAHSkUhQwd7ydlziCf"
access_token = "857624694-ajLMNBMZzQzYn9i0wCfJU01HuhBWilzGb2p2IBUw"
access_token_secret = "HX6cc9F6uA27y8rOc2E1TGR3xIAulrB2vicLTld6Qx1wt"


# Autenticación con las credenciales de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crear la API de Tweepy
api = tweepy.API(auth)

# Buscar tweets con la palabra clave especificada
tweets = tweepy.Cursor(api.search_tweets, q='covid', lang='es').items(100)

# Abrir el archivo CSV y escribir la cabecera
with open('tweetsPrograma14.csv', 'w', encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Usuario", "Fecha", "Texto"])

    # Escribir cada tweet en el archivo CSV
    for tweet in tweets:
        text_without_accents = unidecode(tweet.text)
        writer.writerow([tweet.user.screen_name, tweet.created_at, text_without_accents])
