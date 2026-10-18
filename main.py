import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN sozlanmagan!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row("❤️ Layklar", "👥 Obunachilar")
    menu.row("👁️ Ko‘rishlar", "🆓 Bepul xizmatlar")
    menu.row("📞 Yordam")

    bot.send_message(
        message.chat.id,
        "🔥 INSTA FREE UZ BOTIGA XUSH KELIBSIZ!\n\n"
        "Kerakli xizmatni tanlang 👇",
        reply_markup=menu
    )

@bot.message_handler(func=lambda m: m.text in [
    "❤️ Layklar", "👥 Obunachilar",
    "👁️ Ko‘rishlar", "🆓 Bepul xizmatlar"
])
def services(message):
    bot.send_message(
        message.chat.id,
        "🆓 Hozircha xizmatlar ulanmagan.\n"
        "Haqiqiy xizmatlarni keyin API orqali ulaymiz.\n\n"
        "⚠️ Instagram parolingizni yubormang."
    )

@bot.message_handler(func=lambda m: m.text == "📞 Yordam")
def help_user(message):
    bot.send_message(
        message.chat.id,
        "📞 Yordam uchun bot administratoriga murojaat qiling."
    )

print("INSTA FREE UZ ishga tushdi!")
bot.infinity_polling()
