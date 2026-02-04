import telebot

bot = telebot.TeleBot("8248428620:AAFm8_fwmd-h4nu5MB-HZdvmpprIOSxltwE")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает 24/7!")

bot.polling(non_stop=True)
