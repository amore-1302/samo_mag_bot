#Т.е по галерее.
# Входные параметры функции
# параметр1 'rest'  или 'dish'
# параметр 2  id
# параметр 3 id_chat
#
# Необходимо по параметру 1 и два найти подпапку
# просмотреть там файлы от 1 до 10 и если фвйл существует то вывести его в телеграмм


import os
from telegram import Bot

def send_images(param1, param2, param3):
    # init Токен нужно будет вставить
    bot = Bot("your_telegram_token")

    # Путь к папке с изображениями
    folder_path = f'static/{param1}/{param2}/'

    # Проверка существования папки
    if os.path.exists(folder_path):
        # Просмотр файлов с 1 по 10 и отправка их в Telegram, *если они существуют*
        for i in range(1, 11):
            image_path = os.path.join(folder_path, f"{i}.jpg")
            if os.path.exists(image_path):
                with open(image_path, 'rb') as photo:
                    bot.send_photo(chat_id=param3, photo=photo)
    else:
        print(f"Папка для параметра {param1} и id {param2} не найдена.")

#example
send_images('rest', 123, 'your_chat_id')
