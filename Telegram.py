from multiprocessing.connection import answer_challenge
import requests
import time
import telebot
import json
import urllib3
urllib3.disable_warnings()

''' 
    videos usados = ["https://www.youtube.com/watch?v=NZlITndRKLI",
    "https://www.youtube.com/watch?v=ps1yeWwd6iA",
    "https://www.youtube.com/watch?v=UEvzqZu7Qfc&list=PLVCgi5HZ0-Yt534vFsbzdw36yfC3OtiuY&index=2",
    "https://core.telegram.org/bots/api"]
    token = "5352030026:AAFIvUiXxEJPO2h00ABGxKtS_tHM4Mjl504"
    url_base = "https://api.telegram.org/bot"
    chat_id = "-679872173"
'''


'''TESTES:
import requests
def send_msg(text):
   token = "your_token"
   chat_id = "your_chatId"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())

send_msg("Hello there!")
'''

class Telegram:
    def __init__(self):
        self.__token = "5352030026:AAFIvUiXxEJPO2h00ABGxKtS_tHM4Mjl504"
        self.__url_base = "https://api.telegram.org/bot"
        self.chat_id = "-1001565886573" #"-679872173"

    def start(self):
        update_id = None
        while True:
            time.sleep(1)
            update = self.get_message(update_id)
            #Imprime o dicionario completo
            print(update)
            
            #Pega a chave result
            full_dict = update['result']
            if full_dict:
                for single_dict in full_dict:
                    try:
                        update_id = single_dict['update_id']
                        chat_id =  single_dict['message']['from']['id']
                        user = single_dict['message']['from']['first_name']
                        user_text = single_dict['message']['text']
                        date = single_dict['message']['date']
                        answer_bot = self.answer(user, date, user_text)
                        self.send_answer(answer_bot)
                    except:
                        pass

    def get_message(self, update_id):
        end_point = f"/getUpdates?timeout=1000"
        link_request = self.__url_base + self.__token + end_point #+ "?chat_id=" + self.chat_id
        if update_id:
            link_request = self.__url_base + self.__token + "/getUpdates?timeout=1000" + f"&offset={update_id + 1}"  
        result = requests.get(link_request, verify=False)
        return json.loads(result.content)
    
    def answer(self, user, date, user_text):
        return f"Mensagem enviada por: '{user}' - no dia {date}. Texto: '{user_text}' "
    
    def send_answer(self, text):
        url_req = "https://api.telegram.org/bot" + self.__token + "/sendMessage" + "?chat_id=" + self.chat_id + "&text=" + text
        results = requests.get(url_req, verify=False)
        print(results.json())


bot = Telegram()
bot.start()
