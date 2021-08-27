import os
from os import listdir
from dotenv import load_dotenv
import telegram
import time


def photo_publication(bot,directory):
    while True:
        for images in listdir(directory):   
             with open (f"{direc}/{images}","rb") as file:
                 bot.send_document(chat_id, document=file)
                 time.slepp(86400)

if __name__ == "__main__":
    directory = input("Введите название папки, из которой будут отпраляться фото ")
    load_dotenv()
    chat_id = os.getenv("CHAT_ID")
    tgbot_api_key = os.getenv("TGBOT_API_KEY")
    bot = telegram.Bot(token=tgbot_api_key)
    photo_publication(bot,directory)