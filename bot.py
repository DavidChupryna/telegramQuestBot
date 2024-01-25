import random

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from info import bot_responses, locations, back_on_road, went_to_cat, ready_to_fight, image_error
from data import load_user_data, save_user_data


token = '6490053327:AAEMjdralHZNF63fwQV5UK7VPeyNcIFxfus'
bot = telebot.TeleBot(token=token)

data_path = 'users.json'
user_data = load_user_data(data_path)


def create_buttons(list_buttons: list):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    for button in list_buttons:
        keyboard.add(KeyboardButton(button))

    return keyboard


def create_character(user_id):
    user_data[user_id]['money'] = 0
    user_data[user_id]['weapon'] = ""
    user_data[user_id]['magic'] = False
    save_user_data(user_data, data_path)


@bot.message_handler(commands=['start'])
def say_start(message):
    bot.send_message(message.chat.id, f"{random.choice(bot_responses['hello'])}.\n"
                                      f"В застывшем во времени мире, поделенном на три великих королевства — "
                                      f"Королевство Магии, Королевство Света и Королевство Тьмы. Ты рыцырь, "
                                      f"должен встать на защиту баланса и спасти мир от вековой тьмы.\n"
                                      f"Для детального ознакомления с ботом, воспользуйтесь командой /help")


@bot.message_handler(commands=['help'])
def say_help(message):
    bot.send_message(message.chat.id, "Игрок воплотится в роль рыцаря, отправляющегося в эпическое приключение "
                                      "через таинственные и опасные земли трех королевств. Поднявшись против сил зла, "
                                      "рыцарь обнаружит, что в каждом королевстве скрыты уникальные тайны и вызовы.\n"
                                      "Для начала квеста воспользуйтесь командой /quest")


@bot.message_handler(commands=['quest'])
def create_user(message):
    user_id = str(message.from_user.id)
    if user_id not in user_data:
        user_data[user_id] = {}
        user_data[user_id]['username'] = message.from_user.first_name
        create_character(user_id)

    elif user_id in user_data:
        create_character(user_id)
        bot.send_message(message.chat.id, f"{message.from_user.first_name} рад вас снова видеть,"
                                          f"Монеты: {user_data[user_id]['money']} Оружие: {user_data[user_id]['weapon']}")

    location_one(message.chat.id)


def location_one(chat_id):
    keyboard = create_buttons([locations['kingdom_light']['name'],
                               locations['kingdom_dark']['name'],
                               locations['kingdom_magic']['name']])
    try:
        bot.send_photo(chat_id, locations['road']['image'])
    except:
        bot.send_message(chat_id, image_error)

    bot.send_message(chat_id, f"{locations['road']['name']}: \n"
                              f"Выбери свой путь!", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in [locations['kingdom_light']['name'],
                                                           locations['kingdom_dark']['name'],
                                                           locations['kingdom_magic']['name']])
def three_kingdom(message):
    if message.text == locations['kingdom_light']['name']:
        keyboard = create_buttons([locations['light_city']['name'], locations['fruit_gardens']['name']])
        try:
            bot.send_photo(message.chat.id, locations['kingdom_light']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Добро пожаловать в {locations['kingdom_light']['name']}\n"
                                          f"{locations['kingdom_light']['descriptions']}")
        bot.send_message(message.chat.id, f"Выбери куда пойти дальше? \n"
                                          f"{locations['light_city']['name']}\n"
                                          f"{locations['fruit_gardens']['name']}", reply_markup=keyboard)

    elif message.text == locations['kingdom_dark']['name']:
        keyboard = create_buttons([locations['dark_tunnel']['name'], back_on_road])
        try:
            bot.send_photo(message.chat.id, locations['kingdom_dark']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты попал в {locations['kingdom_dark']['name']}\n"
                                          f"{locations['kingdom_dark']['descriptions']}")
        bot.send_message(message.chat.id, "Впереди тебя ждут темные тунелли. Ты готов?", reply_markup=keyboard)

    elif message.text == locations['kingdom_magic']['name']:
        keyboard = create_buttons([locations['witch_city']['name'], locations['illusion_forest']['name']])
        try:
            bot.send_photo(message.chat.id, locations['kingdom_magic']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Вас приветствует {locations['kingdom_magic']['name']}\n"
                                          f"{locations['kingdom_magic']['descriptions']}")
        bot.send_message(message.chat.id, f"Выбери куда пойти дальше? \n"
                                          f"{locations['witch_city']['name']}\n"
                                          f"{locations['illusion_forest']['name']}", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in [locations['light_city']['name'],
                                                           locations['fruit_gardens']['name']])
def location_light(message):
    if message.text == locations['light_city']['name']:
        keyboard = create_buttons([locations['light_city']['city_jobs'][0]['name'],
                                   locations['light_city']['city_jobs'][1]['name'],
                                   locations['light_city']['city_jobs'][2]['name'],
                                   back_on_road])
        try:
            bot.send_photo(message.chat.id, locations['light_city']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"{locations['light_city']['descriptions']}\n"
                                               f"Ты можешь хорошо заработать и вернуться назад:\n"
                                               f"- {locations['light_city']['city_jobs'][0]['name']}\n"
                                               f"- {locations['light_city']['city_jobs'][1]['name']}\n"
                                               f"- {locations['light_city']['city_jobs'][2]['name']}", reply_markup=keyboard)

    elif message.text == locations['fruit_gardens']['name']:
        keyboard = create_buttons([locations['fruit_gardens']['garden_jobs'][0]['name'],
                                   locations['fruit_gardens']['garden_jobs'][1]['name'],
                                   locations['fruit_gardens']['garden_jobs'][2]['name'],
                                   back_on_road])

        try:
            bot.send_photo(message.chat.id, locations['fruit_gardens']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"{locations['fruit_gardens']['descriptions']}\n"
                                          f"В саду тебя попросили помочь за денежную плату.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in [locations['light_city']['city_jobs'][0]['name'],
                                                           locations['light_city']['city_jobs'][1]['name'],
                                                           locations['light_city']['city_jobs'][2]['name'],
                                                           back_on_road])
def city_jobs_or_back(message):
    user_id = str(message.from_user.id)
    if message.text == locations['light_city']['city_jobs'][0]['name']:
        user_data[user_id]['money'] += 200
        try:
            bot.send_photo(message.chat.id, locations['light_city']['city_jobs'][0]['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты благополучно защитил караван от бандитов⚔️! Держи 200 монет!\n"
                                          f"У тебя - {user_data[user_id]['money']} монет💰.")

    elif message.text == locations['light_city']['city_jobs'][1]['name']:
        user_data[user_id]['money'] += 50
        try:
            bot.send_photo(message.chat.id, locations['light_city']['city_jobs'][1]['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты хорошо выполнил работу ремесленика, держи 50 монет!\n"
                                          f"У тебя - {user_data[user_id]['money']} монет💰.")

    elif message.text == locations['light_city']['city_jobs'][2]['name']:
        user_data[user_id]['money'] += 100
        try:
            bot.send_photo(message.chat.id, locations['light_city']['city_jobs'][2]['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты молодец! Праздник был замечателен, местные жителе в восторге! "
                                          f"Держи твои 100 монет!\nУ тебя - {user_data[user_id]['money']} монет💰.")

    elif message.text == back_on_road:
        location_one(message.chat.id)

    if user_data[user_id]['money'] > 500:
        bot.send_message(message.chat.id, f"Ты заработал достаточно монет чтобы прикупить себе что-нибудь. "
                                          f"Отправляйся в {locations['kingdom_magic']['name']} и посети местного торговца.")
    save_user_data(user_data, data_path)


@bot.message_handler(func=lambda message: message.text in [locations['fruit_gardens']['garden_jobs'][0]['name'],
                                                           locations['fruit_gardens']['garden_jobs'][1]['name'],
                                                           locations['fruit_gardens']['garden_jobs'][2]['name'],
                                                           back_on_road])
def garden_jobs_or_back(message):
    user_id = str(message.from_user.id)
    if message.text == locations['fruit_gardens']['garden_jobs'][0]['name']:
        user_data[user_id]['money'] += 50
        try:
            bot.send_photo(message.chat.id, locations['fruit_gardens']['garden_jobs'][0]['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты собрал все полезные травы☘️! Держи вознаграждение в виде 50 монет.\n"
                                          f"У тебя - {user_data[user_id]['money']} монет💰.")

    elif message.text == locations['fruit_gardens']['garden_jobs'][1]['name']:
        user_data[user_id]['money'] += 75
        try:
            bot.send_photo(message.chat.id, locations['fruit_gardens']['garden_jobs'][1]['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Надо же! Не единого сорняка! Держи честно заработанные 75 монет.\n"
                                          f"У тебя - {user_data[user_id]['money']} монет💰.")

    elif message.text == locations['fruit_gardens']['garden_jobs'][2]['name']:
        user_data[user_id]['money'] += 100
        try:
            bot.send_photo(message.chat.id, locations['fruit_gardens']['garden_jobs'][2]['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты сделал большое дело🌲, держи свои 100 монет.\n"
                                          f"У тебя - {user_data[user_id]['money']} монет💰.")

    elif message.text == back_on_road:
        location_one(message.chat.id)

    if user_data[user_id]['money'] > 500:
        bot.send_message(message.chat.id, f"Ты заработал достаточно монет чтобы прикупить себе что-нибудь. "
                                          f"Отправляйся в {locations['kingdom_magic']['name']} и посети местного торговца.")
    save_user_data(user_data, data_path)


@bot.message_handler(func=lambda message: message.text in [locations['witch_city']['name'], locations['illusion_forest']['name']])
def location_magic(message):
    if message.text == locations['witch_city']['name']:
        keyboard = create_buttons([locations['weapon_shop']['name'], back_on_road])
        try:
            bot.send_photo(message.chat.id, locations['witch_city']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты попал в {locations['witch_city']['name']}\n"
                                          f"{locations['witch_city']['descriptions']}\n"
                                          f"Посетишь оружейный магазин?", reply_markup=keyboard)

    elif message.text == locations['illusion_forest']['name']:
        keyboard = create_buttons([went_to_cat, back_on_road])
        try:
            bot.send_photo(message.chat.id, locations['illusion_forest']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"Ты попал в {locations['illusion_forest']['name']}\n"
                                          f"{locations['illusion_forest']['descriptions']}", reply_markup=keyboard)
        bot.send_message(message.chat.id, "На дереве ты увидел сидящего кота, подойти к нему?")


@bot.message_handler(func=lambda message: message.text in [locations['weapon_shop']['name'], back_on_road])
def weapon_shop(message):
    user_id = str(message.from_user.id)
    if user_data[user_id]['money'] < 500:
        bot.send_message(message.chat.id, f"У тебя очень мало монет, чтобы что-то купить.\n "
                                          f"Но ты можешь посетить {locations['kingdom_light']['name']} и заработать там.")
    elif user_data[user_id]['money'] > 500:
        if message.text == locations['weapon_shop']['name']:
            keyboard = create_buttons([locations['weapon_shop']['weapons'][0]['name'],
                                       locations['weapon_shop']['weapons'][1]['name'],
                                       locations['weapon_shop']['weapons'][2]['name'],
                                       back_on_road])
            try:
                bot.send_photo(message.chat.id, locations['weapon_shop']['image'])
            except:
                bot.send_message(message.chat.id, image_error)

            bot.send_message(message.chat.id, locations['weapon_shop']['descriptions'], reply_markup=keyboard)

        elif message.text == back_on_road:
            location_one(message.chat.id)


@bot.message_handler(func=lambda message: message.text in [locations['weapon_shop']['weapons'][0]['name'],
                                                           locations['weapon_shop']['weapons'][1]['name'],
                                                           locations['weapon_shop']['weapons'][2]['name'],
                                                           back_on_road])
def buy_weapon(message):
    user_id = str(message.from_user.id)
    if message.text == locations['weapon_shop']['weapons'][0]['name']:
        if user_data[user_id]['money'] < 400:
            bot.send_message(message.chat.id, "У тебя не достаточно монет!")
        else:
            try:
                bot.send_photo(message.chat.id, locations['weapon_shop']['weapons'][0]['image'])
            except:
                bot.send_message(message.chat.id, image_error)

            bot.send_message(message.chat.id, f'Ты купил {locations['weapon_shop']['weapons'][0]['name']}🗡\n')
            user_data[user_id]['weapon'] = 'Sword'
            user_data[user_id]['money'] -= 400

    elif message.text == locations['weapon_shop']['weapons'][1]['name']:
        if user_data[user_id]['money'] < 500:
            bot.send_message(message.chat.id, "У тебя не достаточно монет!")
        else:
            try:
                bot.send_photo(message.chat.id, locations['weapon_shop']['weapons'][1]['image'])
            except:
                bot.send_message(message.chat.id, image_error)

            bot.send_message(message.chat.id, f'Ты купил {locations['weapon_shop']['weapons'][1]['name']}🪓\n')
            user_data[user_id]['weapon'] = 'Axe'
            user_data[user_id]['money'] -= 500

    elif message.text == locations['weapon_shop']['weapons'][2]['name']:
        if user_data[user_id]['money'] < 300:
            bot.send_message(message.chat.id, "У тебя не достаточно монет!")
        else:
            try:
                bot.send_photo(message.chat.id, locations['weapon_shop']['weapons'][2]['image'])
            except:
                bot.send_message(message.chat.id, image_error)

            bot.send_message(message.chat.id, f'Ты купил {locations['weapon_shop']['weapons'][2]['name']}\n')
            user_data[user_id]['weapon'] = 'Spear'
            user_data[user_id]['money'] -= 300

    if message.text == back_on_road:
        location_one(message.chat.id)

    save_user_data(user_data, data_path)


@bot.message_handler(func=lambda message: message.text in [went_to_cat, back_on_road])
def magic_cat(message):

    if message.text == went_to_cat:
        keyboard = create_buttons([locations['illusion_forest']['cat']['wrong_answers'][0],
                                   locations['illusion_forest']['cat']['wrong_answers'][1],
                                   locations['illusion_forest']['cat']['true_answer'],
                                   back_on_road])
        try:
            bot.send_photo(message.chat.id, locations['illusion_forest']['cat']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, "Кот загадывает тебе задку, за которую предлогает ценный для тебя приз."
                                          "Приз - заклинание, которое поможет тебе усмирить паука в Темных тунелях!")
        bot.send_message(message.chat.id, locations['illusion_forest']['cat']['riddle'], reply_markup=keyboard)

    elif message.text == back_on_road:
        location_one(message.chat.id)


@bot.message_handler(func=lambda message: message.text in [locations['illusion_forest']['cat']['wrong_answers'][0],
                                                           locations['illusion_forest']['cat']['wrong_answers'][1],
                                                           locations['illusion_forest']['cat']['true_answer']])
def solve_riddle(message):
    user_id = str(message.from_user.id)
    if message.text in locations['illusion_forest']['cat']['wrong_answers']:
        try:
            bot.send_photo(message.chat.id, locations['illusion_forest']['cat']['swamp_image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, "Ты не угадал. Кот завел тебя в болота и оставил на верную гибель☠️!")
        bot.send_message(message.chat.id, "Чтобы начать заново, нажмите /quest", reply_markup=ReplyKeyboardRemove())

    elif message.text == locations['illusion_forest']['cat']['true_answer']:
        bot.send_message(message.chat.id, "Поздравляю, ты одгадал загадку и кот нашептал тебе на ухо то самое - "
                                          "очень важное заклинание🪄.\n И отправил тебя обратно.")
        user_data[user_id]['magic'] = True
        save_user_data(user_data, data_path)
        location_one(message.chat.id)


@bot.message_handler(func=lambda message: message.text in [locations['dark_tunnel']['name'], back_on_road])
def enter_to_tunnel(message):
    user_id = str(message.from_user.id)
    if message.text == locations['dark_tunnel']['name']:
        try:
            bot.send_photo(message.chat.id, locations['dark_tunnel']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, locations['dark_tunnel']['descriptions'])
        if not user_data[user_id]['magic']:
            keyboard = create_buttons([back_on_road])
            bot.send_message(message.chat.id, "Впереди тебя ждет Страж паук, который неуязвим к силовым ударам. "
                                              "Чтобы его усмирить тебе нужно разыскать кота в магическом королевстве!",
                                              reply_markup=keyboard)

        elif user_data[user_id]['magic']:
            keyboard = create_buttons([locations['forgotten_fortress']['name'], back_on_road])
            try:
                bot.send_photo(message.chat.id, locations['dark_tunnel']['spider']['image'])
            except:
                bot.send_message(message.chat.id, image_error)

            bot.send_message(message.chat.id, "Заклинание, которое тебе дал кот и в правду усмирило паука! "
                                              "Дальше тебя ждет забытая крепость! Ещё есть возможность вернуться назад.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in [locations['forgotten_fortress']['name'], back_on_road])
def fortress(message):
    if message.text == locations['forgotten_fortress']['name']:
        keyboard = create_buttons([ready_to_fight, back_on_road])
        try:
            bot.send_photo(message.chat.id, locations['forgotten_fortress']['image'])
        except:
            bot.send_message(message.chat.id, image_error)

        bot.send_message(message.chat.id, f"{locations['forgotten_fortress']['name']}\n"
                                          f"{locations['forgotten_fortress']['descriptions']}", reply_markup=keyboard)
        bot.send_message(message.chat.id, "Сейчас тебе предстоит сразится с Темным рыцарем, готов?")
    elif message.text == back_on_road:
        location_one(message.chat.id)


@bot.message_handler(func=lambda message: message.text in [ready_to_fight, back_on_road])
def finish_fight(message):
    user_id = str(message.from_user.id)
    if message.text == ready_to_fight:
        if user_data[user_id]['weapon'] == 'Sword':
            chance = random.choice(['Win', 'Lose'])
            if chance == "Win":
                try:
                    bot.send_photo(message.chat.id, locations['forgotten_fortress']['final_fight_img'][1])
                except:
                    bot.send_message(message.chat.id, image_error)

                bot.send_message(message.chat.id, "🥇Темный рыцарь🦂 был не в форме и ты смог его одалеть с помощью меча.🥇 "
                                                   "Но помни, это всего-лишь везение")
                bot.send_message(message.chat.id, "Квест окончен! Чтобы начать заново, воспользуйся командой - /quest", reply_markup=ReplyKeyboardRemove())

            elif chance == 'Lose':
                try:
                    bot.send_photo(message.chat.id, locations['forgotten_fortress']['final_fight_img'][0])
                except:
                    bot.send_message(message.chat.id, image_error)

                bot.send_message(message.chat.id, "Шансы были равны, но Темный рыцарь🦂 смог тебя одалеть. Ты проиграл☠️")
                bot.send_message(message.chat.id, "Квест окончен! Чтобы начать заново, воспользуйся командой - /quest", reply_markup=ReplyKeyboardRemove())

        elif user_data[user_id]['weapon'] == 'Axe':
            try:
                bot.send_photo(message.chat.id, locations['forgotten_fortress']['final_fight_img'][2])
            except:
                bot.send_message(message.chat.id, image_error)

            bot.send_message(message.chat.id, "🥇Темный рыцарь🦂 повержен, победа за тобой!🥇")
            bot.send_message(message.chat.id, "Квест окончен! Чтобы начать заново, воспользуйся командой - /quest", reply_markup=ReplyKeyboardRemove())

        elif user_data[user_id]['weapon'] == 'Spear':
            try:
                bot.send_photo(message.chat.id, locations['forgotten_fortress']['final_fight_img'][3])
            except:
                bot.send_message(message.chat.id, image_error)

            bot.send_message(message.chat.id, "С таким оружием - ты не ровня Темному рыцарю🦂! Ты проиграл☠️!\n"
                                                "Для тебе пригодится оружие Кратоса!")
            bot.send_message(message.chat.id, "Квест окончен! Чтобы начать заново, воспользуйся командой - /quest", reply_markup=ReplyKeyboardRemove())

        elif not user_data[user_id]['weapon']:
            bot.send_message(message.chat.id, "Ты пришел сражаться с Темным рыцарем без оружия?🤬 Темный рыцарь назвал "
                                              "тебя жалким и прогнал прочь!")
            location_one(message.chat.id)


bot.polling()