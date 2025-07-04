import os
from flask import Flask, request
import telebot

TOKEN = os.getenv("TOKEN", "7508154894:AAHTjKUGpnaZTj_vu7fANNNL2MdCOyfE87Y")
CHAT_ID = os.getenv("CHAT_ID", "761743415")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Бот запущено!'

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    if not data:
        return "No data received", 400

    name = data.get('name')
    phone = data.get('phone')
    message = data.get('message')

    if not all([name, phone, message]):
        return "Missing fields", 400

    text = f"<b>Нове повідомлення з сайту</b>\nІм’я: {name}\nТелефон: {phone}\nЗапитання: {message}"

    try:
        bot.send_message(CHAT_ID, text, parse_mode='HTML')
        return "Message sent", 200
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
