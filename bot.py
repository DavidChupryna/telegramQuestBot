import random

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from info import bot_responses, locations
from data import load_user_data, save_user_data


token = '6490053327:AAEMjdralHZNF63fwQV5UK7VPeyNcIFxfus'
bot = telebot.TeleBot(token=token)

data_path = 'users.json'
user_data = load_user_data(data_path)


def create_two_button(btn1, btn2):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(telebot.types.KeyboardButton(btn1))
    keyboard.add(telebot.types.KeyboardButton(btn2))
    return keyboard


def create_three_button(btn1, btn2, btn3):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(telebot.types.KeyboardButton(btn1))
    keyboard.add(telebot.types.KeyboardButton(btn2))
    keyboard.add(telebot.types.KeyboardButton(btn3))
    return keyboard


def create_four_button(btn1, btn2, btn3, btn4):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(telebot.types.KeyboardButton(btn1))
    keyboard.add(telebot.types.KeyboardButton(btn2))
    keyboard.add(telebot.types.KeyboardButton(btn3))
    keyboard.add(telebot.types.KeyboardButton(btn4))
    return keyboard



def create_character(user_id):
    user_data[user_id]['money'] = 0
    user_data[user_id]['weapon'] = ""
    user_data[user_id]['magic'] = ""
    save_user_data(user_data, data_path)

@bot.message_handler(commands=['start'])
def say_start(message):
    bot.send_message(message.chat.id, f"{random.choice(bot_responses['hello'])}.\n"
                                      f"Ты попал на тест по базовому Python. \n"
                                      f"Для полного ознакомления с ботом напишите команду: /help\n"
                                      f"Для начала теста введите команду /quest")


@bot.message_handler(commands=['quest'])
def create_user(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data:
        user_data[user_id] = {}
        user_data[user_id]['username'] = message.from_user.first_name

        create_character(user_id)
        print(user_id)
        print(user_data)
    elif user_id in user_data:
        create_character(user_id)
        bot.send_message(message.chat.id, f"{message.from_user.first_name} рад вас снова видеть,"
                                          f"Money: {user_data[user_id]['money']} Weapon: {user_data[user_id]['weapon']}")

    location_one(message.chat.id)


def location_one(chat_id):
    keyboard = create_three_button(locations["kingdom_light"]["name"],
                                   locations["kingdom_dark"]["name"],
                                   locations["kingdom_magic"]["name"])
    bot.send_message(chat_id, f"{locations["road"]["name"]}: \n"
                                      f"{locations["road"]["descriptions"]}.\n"
                              f"Выбери свой путь!", reply_markup=keyboard)
    bot.send_photo(chat_id, locations["road"]["image"])


@bot.message_handler(func=lambda message: message.text in [locations["kingdom_light"]["name"],
                                                           locations["kingdom_dark"]["name"],
                                                           locations["kingdom_magic"]["name"]])
def location_two(message):
    if message.text == locations["kingdom_light"]["name"]:
        keyboard = create_two_button(locations['light_city']['name'], locations['garden']['name'])
        bot.send_message(message.chat.id, f"Добро пожаловать в {locations['kingdom_light']['name']}\n"
                                          f"{locations['kingdom_light']['descriptions']}")
        bot.send_photo(message.chat.id, locations["kingdom_light"]["image"])
        bot.send_message(message.chat.id, f"Выбери куда пойти дальше? \n"
                                          f"{locations['light_city']['name']}\n"
                                          f"{locations['garden']['name']}", reply_markup=keyboard)
    elif message.text == locations["kingdom_dark"]["name"]:
        bot.send_message(message.chat.id, f"Ты попал в {locations['kingdom_dark']['name']}\n"
                                          f"{locations['kingdom_dark']['descriptions']}")
        bot.send_photo(message.chat.id, locations["kingdom_dark"]["image"])
    elif message.text == locations["kingdom_magic"]["name"]:
        bot.send_message(message.chat.id, f"Вас приветствует {locations['kingdom_magic']['name']}\n"
                                          f"{locations['kingdom_magic']['descriptions']}")
        bot.send_photo(message.chat.id, locations["kingdom_magic"]["image"])


@bot.message_handler(func=lambda message: message.text in [locations['light_city']['name'], locations['garden']['name']])
def location_three(message):
    if message.text == locations['light_city']['name']:
        keyboard = create_four_button(locations['light_city']['jobs'][0]['name'],
                                      locations['light_city']['jobs'][1]['name'],
                                      locations['light_city']['jobs'][2]['name'],
                                    locations["road"]["name"])

        bot.send_message(message.chat.id, f"Ты пришел в {locations['light_city']['name']}!\n"
                                          f"{locations['light_city']['descriptions']}", reply_markup=keyboard)
        bot.send_photo(message.chat.id, locations["light_city"]["image"])

    elif message.text == 'Desert':
        bot.send_message(message.chat.id, "Desert Hello")
        # bot.send_photo(message.chat.id, open(locations["desert"]["image"], "rb"))


@bot.message_handler(func=lambda message: message.text in [locations['light_city']['jobs'][0]['name'],
                                      locations['light_city']['jobs'][1]['name'],
                                      locations['light_city']['jobs'][2]['name'],
                                      locations["road"]["name"]])
def job_or_back(message):
    user_id = str(message.from_user.id)
    if message.text == locations['light_city']['jobs'][0]['name']:
        bot.send_message(message.chat.id, "Ты благополучно защитил караван от бандитов и заработал 200 монет!")

        user_data[user_id]['money'] += 200
    elif message.text == locations['light_city']['jobs'][1]['name']:
        bot.send_message(message.chat.id, "Ты хорошо выполнил работу ремесленика, держи 50 монет!")

        user_data[user_id]['money'] += 50
    elif message.text == locations['light_city']['jobs'][2]['name']:
        bot.send_message(message.chat.id, "Ты молодец! Праздник был замечателен, местные жителе в восторге! "
                                          "Держи твои 100 монет!")

        user_data[user_id]['money'] += 100
    elif message.text == locations["road"]["name"]:
        location_one(message.chat.id)
    if user_data[user_id]['money'] > 500:
        bot.send_message(message.chat.id, f"Ты заработал достаточно монет чтобы прикупить себе что-нибудь. "
                                          f"Отправляйся в {locations["kingdom_magic"]["name"]} и посети местного торговца.")
    save_user_data(user_data, data_path)

@bot.message_handler(func=lambda message: message.text in ["sword", "spear", 'axe'])
def take_weapon(message):
    user_id = str(message.from_user.id)

    if message.text == 'sword':
        bot.send_message(message.chat.id, "You take sword")
        user_data[user_id]['weapon'] = 'sword'
    elif message.text == 'spear':
        bot.send_message(message.chat.id, "You take spear")
        user_data[user_id]['weapon'] = 'spear'
    elif message.text == 'axe':
        bot.send_message(message.chat.id, "You take axe")
        user_data[user_id]['weapon'] = 'axe'

    save_user_data(user_data, data_path)
    print(user_data)
    keyboard = create_two_button("Finish", "Kingdom Dark")
    if user_data[user_id]['magic']:
        bot.send_message(message.chat.id, "Battle with spider, You Win")
    else:
        bot.send_message(message.chat.id, f"Battle with spider, for battle you need magic, if   ...... you must buy in Kingdom Dark", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Finish')
def say_finish(message):
    bot.send_message(message.chat.id, "finish game")

bot.polling()