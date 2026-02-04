import telebot
import yt_dlp

BOT_TOKEN = "8248428620:AAFm8_fwmd-h4nu5MB-HZdvmpprIOSxltwE"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Отправь ссылку с YouTube или Instagram, и я скачаю видео!")

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text
    bot.send_message(message.chat.id, "Скачиваю...")

    try:
        ydl_opts = {
            "format": "best",
            "outtmpl": "video.mp4"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open("video.mp4", "rb") as video:
            bot.send_video(message.chat.id, video)

    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка! Проверь ссылку.")

bot.infinity_polling()
