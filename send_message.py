import os
from os import listdir
from dotenv import load_dotenv
import telegram
import time


def send_message():
    chat_id = '@SpacePhotosBaby'
    while True:
        try:
            for images in listdir(direc):
                bot.send_document(chat_id=chat_id, document=open(f"{direc}{'/'}{images}",'rb'))
                time.sleep(86400)
        except:
            print('Папки с таким названием не сущесвует')
            break


if __name__ == '__main__':
    direc = input('Введите название папки, из которой будут отпраляться фото ')
    load_dotenv()
    tgbot_api_key = os.getenv('TGBOT_API_KEY')
    bot = telegram.Bot(token=tgbot_api_key)
    send_message()