import tweepy
import openpyxl
from datetime import datetime
import os 

# Inserta tus credenciales de Twitter aquí
consumer_key = os.environ['consumer_key_h']
consumer_secret = os.environ[ 'consumer_secret_h']
access_token = os.environ[ 'access_key_h']
access_token_secret = os.environ['access_secret_h']

# Autenticación con la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Búsqueda de tweets
search_words = 'bolsa de valores' # Inserta la palabra clave para la búsqueda aquí
tweets = tweepy.Cursor(api.search_tweets, q=search_words, lang='es', tweet_mode='extended').items(1000)

# Creación de un libro de Excel y una hoja de trabajo
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Escritura de los encabezados en la primera fila
headers = ['ID', 'Fecha', 'Detalle', 'Usuario']
worksheet.append(headers)

# Iteración sobre los tweets y escritura de la información en el archivo Excel
for tweet in tweets:
    # Convertir la fecha y hora a la zona horaria local
    local_datetime = tweet.created_at.replace(tzinfo=None)
    
    row = [tweet.id_str, local_datetime, tweet.full_text, tweet.author.screen_name]
    worksheet.append(row)

# Guardado del archivo Excel
workbook.save('tweetsPrograma13.xlsx')
