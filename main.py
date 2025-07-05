from flask import Flask, request
from flask_cors import CORS
import telebot
import os

# Отримуємо токен і chat_id з середовища
TOKEN = os.getenv("TOKEN", "")
CHAT_ID = os.getenv("CHAT_ID", "")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
CORS(app)  # Дозволяє CORS-запити з інших доменів

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
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
