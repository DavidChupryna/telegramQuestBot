bot_responses = {
    "hello": ["Привет, путник!", "Здравствуйте!", "Приветствую!", "Добрый день!", "Здорова!", "Хай",
              "Хеллоу(да-да я из Англии)", "Привет, шеф!"]}

locations = {
    "road": {
        "name": "Дорога трех королевств",
        "descriptions": "Путь к трём удивительным королевствам начинается с извилистой дороги, утопающей в пышной зелени"
                        " лесов. Этот путь, известен как Дорога Трех Королевств",
        "image": "https://disk.yandex.ru/i/p1yFa6W2vl_ClA"
    },
    "kingdom_light": {
        "name": "Королевство Света ☀️",
        "descriptions": "Под светлым небесным сводом, Королевство Света воссияло золотыми полями и лучистыми городами."
                        " Мириады цветов и кристаллов сверкали, отражая благосклонный свет, "
                        "наполняя все вокруг теплом и радостью.",
        "image": "https://disk.yandex.ru/i/C5sW8HmxlNMjdQ"
    },
    "kingdom_dark": {
        "name": "Королевство Тьмы 🌙",
        "descriptions": "В недрах тайного Королевства Тьмы простирался мистический мрак. "
                        "Силы тьмы, непостижимые и неуловимые, "
                        "владеют этим таинственным уголком мира.",
        "image": "https://disk.yandex.ru/i/V9ITCUqUorwxnQ"
    },
    "kingdom_magic": {
        "name": "Королевство Магии 🔮",
        "descriptions": "Волшебство воплощалось в каждом камне и лепестке в этом удивительном Королевстве Магии. "
                        "Здесь заклинания и чары были частью повседневной жизни, "
                        "а воздух наполнялся тонкой аурой волшебства.",
        "image": "https://disk.yandex.ru/i/G9cq8TaVWpGzmQ"
    },
    "light_city": {
        "name": "Лучистый город",
        "descriptions": "Лучистый город - это символ мира, надежды и красоты. "
                        "Он привлекает путешественников со всего мира, желающих увидеть его чудеса.",
        "image": "https://disk.yandex.ru/i/CAB9I8_uTBCJfA",
        "elder_image": "https://disk.yandex.ru/i/Zk0O804_aUa9Lg",
        "city_jobs": [{
            "name": "Защита каравана",
            "image": "https://disk.yandex.ru/i/K_1mua1e-wjjig"},
            {
            "name": "Помощь ремесленику",
            "image": "https://disk.yandex.ru/i/-5T-eDmoMzCLpA"},
            {
            "name": "Организация городского праздника",
            "image": "https://disk.yandex.ru/i/iOoectdUVwLJ9A"
            }]
    },
    "fruit_gardens": {
        "name": "Фруктовые сады",
        "descriptions": "Фруктовые сады – место вдохновения, где каждый цветок – часть живого полотна, "
                        "приглашающего вас отдохнуть и насладиться красотой природы.",
        "image": "https://disk.yandex.ru/i/e6w3QzpAOFfh_Q",
        "garden_jobs": [{
            "name": "Сбор трав",
            "image": "https://disk.yandex.ru/i/mrShsDT1d_xf1w"},
            {
            "name": "Устранение сорняков",
            "image": "https://disk.yandex.ru/i/X_GMcT6c7VmpMQ"},
            {
            "name": "Посадка деревьев",
            "image": "https://disk.yandex.ru/i/epQF0KDqFzeV1w"}]
    },
    "dark_tunnel": {
        "name": "Темные тунели",
        "descriptions": "В паутинных просторах этих туннелей обитает страж — Гигантский Паук🕸. "
                        "Его окаменелые глаза сверкают во мраке, а паутина, словно нить между мирами, "
                        "покрывает каждый уголок.",
        "image": "https://disk.yandex.ru/i/FdVmo70r863jiw",
        "spider": {
            "name": "Страж тунелей",
            "image": "https://disk.yandex.ru/i/8NWyvmnizf9YJg"
        }
    },
    "forgotten_fortress": {
        "name": "Забытая крепость",
        "descriptions": "Это место наполнено зловещей аурой и мистической энергией, словно само восстание из прошлого. "
                        "В самом сердце крепости раскинул своё гнездо Тёмный Рыцарь, хранитель древнего артефакта. "
                        "Тёмная броня, покрытая рунами, излучает тьму, а его глаза сверкают мраком в ответ на ваши шаги.",
        "image": "https://disk.yandex.ru/i/Oq5oMo5R_Xxgeg",
        "final_fight_img": ["https://disk.yandex.ru/i/dcjUG5TltJ_eLw", "https://disk.yandex.ru/i/9iyMiA9UFR_4eA",
                            "https://disk.yandex.ru/i/6Tfi9g0kal3pEg", "https://disk.yandex.ru/i/PeroRlOc5YGTxQ"]
    },
    "witch_city": {
        "name": "Колдовской город",
        "descriptions": "Колдовской Город — таинственное место, где запреты сливаются с возможностями. "
                        "В его торговых улочках торгуют всем, от волшебных зелий и артефактов до экзотических ингредиентов.",
        "image": "https://disk.yandex.ru/i/P2xe_Zc3FolsZQ",

    },
    "weapon_shop": {
        "name": "Оружейная лавка",
        "descriptions": "Магазин предлагает широкий ассортимент: от внушительных двуручных мечей до изысканных кинжалов "
                        "с инкрустацией драгоценными камнями",
        "image": "https://disk.yandex.ru/i/6UwYLAu804AhdQ",
        "weapons": [{
            "name": "Меч затмения",
            "descriptions": "",
            "image": "https://disk.yandex.ru/i/jF7LlsoxbfqwSQ"
        },
        {
            "name": "Левиафан",
            "descriptions": "",
            "image": "https://disk.yandex.ru/i/QOAQHQR7fss6Bg"
            },
        {
            "name": "Копьё ужаса",
            "descriptions": "",
            "image": "https://disk.yandex.ru/i/jnN8ImkaTpnxDg"
        }]
    },
    "illusion_forest": {
        "name": "Лес иллюзий",
        "descriptions": "Лес Иллюзий — магическое световое полотно, где деревья образуют витражи из света и тени. "
                        "Среди этого волшебства обитает Ученый Кот, исследующий тайны времени и пространства.",
        "image": "https://disk.yandex.ru/i/QaE1XksibeIVwg",
        "cat": {
            "image": "https://disk.yandex.ru/i/HqQRX72jsm0U8g",
            "riddle": "Ветры шепчут тайны, листья шорохом говорят, \n"
                      "В лесу волшебном скрыто, то что глазом не видать.",
            "wrong_answers": ["Время", "Эхо"],
            "true_answer": "Тайна",
            "swamp_image": "https://disk.yandex.ru/i/gAy4mNxR5xZt9g"
        }
    }
}

back_on_road = "Вернуться на дорогу трех королевств"
went_to_cat = "Подойти к коту"
ready_to_fight = "Готов!"
image_error = "Что-то пошло не так с загрузкой изображения! Но мы над этим работаем!"