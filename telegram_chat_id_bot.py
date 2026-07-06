import os
import threading
from flask import Flask
import telebot

# === Environment Variable থেকে Token নেওয়া হবে ===
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable সেট করা হয়নি!")

bot = telebot.TeleBot(TOKEN)

# === Flask Server (Render এর জন্য) ===
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Telegram Bot is running on Render!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Background এ Flask চালাও
threading.Thread(target=run_flask, daemon=True).start()

# === Bot Commands ===
@bot.message_handler(commands=['start'])
def send_chat_id(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    bot.reply_to(
        message,
        f"👋 হ্যালো {first_name}!\n\n"
        f"✅ তোমার Chat ID হলো:\n"
        f"📌 {chat_id}\n\n"
        f"এই Chat ID টি কপি করে রাখো।"
    )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "শুধু /start কমান্ড ব্যবহার করো।")

print("🤖 Bot চালু হয়েছে...")
bot.polling(none_stop=True)
