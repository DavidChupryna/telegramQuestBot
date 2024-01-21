import json


def load_user_data(data_path):
    try:
        with open(data_path, "r") as file:
            return json.load(file)
    except:
        return {}


def save_user_data(user_data, data_path):
    with open(data_path, "w", encoding='utf8') as file:
        json.dump(user_data, file, ensure_ascii=False)