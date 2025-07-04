import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Получаем токен из переменных окружения
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привіт! Я бот. Очікую на запитання зі сайту.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Ви написали: " + message.text)

bot.infinity_polling()
