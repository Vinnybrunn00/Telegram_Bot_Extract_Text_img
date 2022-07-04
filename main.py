from mytoken import TelegramToken
import pytesseract
import telebot
import time
import cv2
import os

os.system('clear')

token = TelegramToken()
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['photo'])
def Start(message):
    ids = message.photo[-1].file_id
    foto = bot.get_file(ids)
    download = bot.download_file(foto.file_path)

    with open('image.png', 'wb') as file:
        file.write(download)
        file.close()
    time.sleep(0.7)

    try:
        img = cv2.imread('image.png')
        texto = pytesseract.image_to_string(img)
        bot.reply_to(message, texto)
    except:
        bot.send_message(message.chat.id, 'Something went wrong in the image, try again')

bot.infinity_polling()