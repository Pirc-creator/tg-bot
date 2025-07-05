from flask import Flask, request
import telebot
import os

# Загружаем токен и chat_id из переменных среды или хардкодом (на первое время)
TOKEN = os.getenv("TOKEN", "7508154894:AAHTjKUGpnaZTj_vu7fANNNL2MdCOyfE87Y")
CHAT_ID = os.getenv("CHAT_ID", "761743415")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is running!'

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    if not data:
        return "No data", 400

    name = data.get('name')
    phone = data.get('phone')
    message = data.get('message')

    if not all([name, phone, message]):
        return "Missing fields", 400

    text = f"<b>Нове повідомлення з сайту</b>\nІм’я: {name}\nТелефон: {phone}\nЗапитання: {message}"
    try:
        bot.send_message(CHAT_ID, text, parse_mode='HTML')
        return "OK", 200
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
