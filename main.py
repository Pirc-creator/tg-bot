from flask import Flask, request
from flask_cors import CORS
import telebot
import os

# Загружаем данные из переменных окружения Render
TOKEN = os.getenv("TOKEN", "")
CHAT_IDS = os.getenv("CHAT_IDS", "")  # строка вида "123,456,789"
CHAT_IDS = [chat_id.strip() for chat_id in CHAT_IDS.split(",") if chat_id.strip()]

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)
CORS(app)

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

    success = 0
    for chat_id in CHAT_IDS:
        try:
            bot.send_message(chat_id, text, parse_mode='HTML')
            success += 1
        except Exception as e:
            print(f"❌ Не вдалося надіслати повідомлення {chat_id}: {e}")

    if success:
        return "OK", 200
    else:
        return "Failed to send to all recipients", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
