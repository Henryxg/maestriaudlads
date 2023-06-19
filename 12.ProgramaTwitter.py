import tweepy #https://github.com/tweepy/tweepy
import csv
import os 
import json

#Credenciales del Twitter API


consumer_key = "DhsrhpsjPxSks5YR6BwohUeV0"
consumer_secret = "FvMyQTgP8izDaasHiuWF6r1APyIu5HvlaAHSkUhQwd7ydlziCf"
access_key = "857624694-ajLMNBMZzQzYn9i0wCfJU01HuhBWilzGb2p2IBUw"
access_secret = "HX6cc9F6uA27y8rOc2E1TGR3xIAulrB2vicLTld6Qx1wt"



#Remover los caracteres no imprimibles y los saltos de línea del texto del tweet
def strip_undesired_chars(tweet):
    stripped_tweet = tweet.replace('\n', ' ').replace('\r', '')
    char_list = [stripped_tweet[j] for j in range(len(stripped_tweet)) if ord(stripped_tweet[j]) in range(65536)]
    stripped_tweet=''
    for j in char_list:
        stripped_tweet=stripped_tweet+j
    return stripped_tweet

def get_all_tweets(screen_name):
    #Este método solo tiene permitido descargar máximo los ultimos 3240 tweets del usuario
    #Especificar aquí durante las pruebas un número entre 200 y 3240
    limit_number = 3240
    
    #autorizar twitter, inicializar tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #inicializar una list to para almacenar los Tweets descargados por tweepy
    alltweets = []    
    
    #Hacer una petición inicial por los 200 tweets más recientes (200 es el número máximo permitido)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)


    
    #guardar los tweets más recientes
    alltweets.extend(new_tweets)
    
    #guardar el ID del tweet más antiguo menos 1
    oldest = alltweets[-1].id - 1
    
    #recorrer todos los tweets en la cola hasta que no queden más
    while len(new_tweets) > 0 and len(alltweets) <= limit_number:
        print ("getting tweets before" + str(oldest))
	

        #en todas las peticiones siguientes usar el parámetro max_id para evitar duplicados
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
	
	

        #guardar los tweets descargados
        alltweets.extend(new_tweets)
        
        #actualizar el ID del tweet más antiguo menos 1
        oldest = alltweets[-1].id - 1
        
        #informar en la consola como vamos
        print (str(len(alltweets)) + " tweets descargados hasta el momento")
    
    #transformar los tweets descargados con tweepy en un arreglo 2D array que llenará el csv
    outtweets = [(tweet.id_str, tweet.created_at, strip_undesired_chars(tweet.text),tweet.retweet_count,str(tweet.favorite_count)+'') for tweet in alltweets]
        


    #escribir el csv    
    with open('%s_tweets.csv' % screen_name, "w", encoding="utf-8", newline='') as f:  
     


        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['id','created_at','text','retweet_count','favorite_count'''])
        writer.writerows(outtweets)    


    pass

if __name__ == '__main__':
    #especificar el nombre de usuario de la cuenta a la cual se descargarán los tweets
    get_all_tweets("Agregar TwitterUser")