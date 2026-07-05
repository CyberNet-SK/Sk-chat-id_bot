import telebot

# তোমার Telegram Bot Token
TOKEN = "8237707641:AAFLUIzx7zQN4gUE3V5HWsVoEx0oGb4Ecgg"

bot = telebot.TeleBot(TOKEN)

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
    bot.reply_to(message, "শুধু /start কমান্ড ব্যবহার করো Chat ID দেখার জন্য।")

print("🤖 Bot চালু হয়েছে... Ctrl+C চাপো বন্ধ করতে।")
bot.polling(none_stop=True)
