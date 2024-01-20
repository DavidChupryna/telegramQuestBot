import telebot

token = '6490053327:AAEMjdralHZNF63fwQV5UK7VPeyNcIFxfus'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def say_start(message):
    bot.send_message(message.chat.id, '')

bot.polling()