from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Твой Telegram ID (получить можно у @userinfobot)
ADMIN_CHAT_ID = 123456789  # <- замени на свой ID

@app.route('/send_question', methods=['POST'])
def send_question():
    data = request.json
    name = data.get('name', 'Н/Д')
    phone = data.get('phone', 'Н/Д')
    question = data.get('question', 'Н/Д')

    msg = f"Нове запитання з сайту:\nІм'я: {name}\nТелефон: {phone}\nПитання: {question}"
    bot.send_message(ADMIN_CHAT_ID, msg)

    return {'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
