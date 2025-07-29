# main.py

import telebot
from config import TOKEN, ADMIN_USERNAME

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, f"Welcome to PesaDEX, {message.from_user.first_name}! 💰\n\nBuy & Sell USDT P2P.\nUse /buy or /sell to start.")

bot.polling()
