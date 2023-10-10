import telebot
from gtts import gTTS 
import os
audio = False
image = False
token = "6623055526:AAH4IfM8CFxminCTR8MtGWKC8odpFS_hvp8"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("audio")
    btn2 = telebot.types.KeyboardButton("image")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Это тестовый бот для сдачи преподавателю\nЧтобы получить исходный код пропишите /Git", reply_markup=markup)
@bot.message_handler(commands=['Git'])
def git(message):
    bot.send_message(message.chat.id, "git url")
@bot.message_handler(func=lambda message: True, content_types=['text'])
def answer(message):
    global audio
    if message.text == "audio":
        audio = True
        bot.send_message(message.chat.id ,"Введите любой текст для создания аудио файла")
    elif message.text == "image":
        bot.send_video(message.chat.id, "https://i.imgur.com/6z0PLq5.gif")
    else:
        if audio:
            audio_for_write = gTTS(text = message.text, lang = 'ru', slow = False)
            audio_for_write.save("audio.mp3")
            with open("audio.mp3",'rb') as audio_ready:
                bot.send_audio(message.chat.id, audio_ready)
            os.remove("audio.mp3")
            audio = False
if __name__ == '__main__':
    bot.infinity_polling()