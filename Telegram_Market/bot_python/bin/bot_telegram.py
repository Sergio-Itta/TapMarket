import telepot
from pprint import pprint
import socket
import json

TOKEN = '1814493027:AAFfdTSi9hCi-eQgZhsG4w-siX2FqEldNMc'

def send_to_logstash(host, port, data):
    error = True
    while(error):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created. sock: " + str(sock))
        
            sock.connect((host, port))
            print("Socket connected to HOST: " + host + " PORT: " + str(port))
            print("Socket connected. Sock: " + str(sock))

            print("Sending message: " + str(data))
            
            sock.sendall(json.dumps(data).encode())
            print("End connection")
            sock.close()
            error = False
        except:
            print("Connection error. There will be a new attempt in 10 seconds")
            time.sleep(10)


def on_chat_message(msg): 
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    response=bot.getUpdates()#crea un json
    tmp = True
    
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        pprint(msg)
        
        if txt.startswith('/tap'):
            bot.sendMessage(chat_id, 'ciao {}, tap è una materia bellissima e piena di meme!'.format(name))
            tmp = False
        elif txt.startswith('/help'):
            bot.sendMessage(chat_id, 'Ecco i comandi che capisco:\n - /tap\n - /help\n - /tapmarket\n - /finaleeuropeo')
            tmp = False
        elif txt.startswith('/finaleeuropeo'):
            bot.sendMessage(chat_id, 'It s coming to Rome')
            bot.sendPhoto(chat_id, photo=open('Rome.jpg', 'rb'))
            tmp = False
        elif txt.startswith('/tapmarket'):
            bot.sendMessage(chat_id, 'Tap market è un progetto nato dalla voglia di monitorare le offerte di mercato attraverso lo strumento di telegram ormai molto utilizzato per pubblicizzare offerte e sconti sui vari siti di e-commerce. Idea attuata da Sergio Itta e Daniele Coniglione al fine di conservare le offerte.')
            tmp = False
    if (tmp == True):
        pprint(msg)
        response.append(msg)#aggiunge il messaggio al json
        send_to_logstash('10.0.100.8', 5000, response)  
        

if __name__ == '__main__':
    bot = telepot.Bot(TOKEN)
    response=bot.getUpdates()
    bot.sendMessage(-1001564970014, 'Ciao, sei pronto ad esaurire lo stipendio?')
    bot.sendPhoto(-1001564970014, photo=open('lettino.jpg', 'rb'))
    pprint(response)
    bot.message_loop(on_chat_message)

    print('Listening ...')

import time
while 1:
    time.sleep(10)