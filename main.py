import sqlite3
import telebot

def  sql_list_command(message):
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM restaurants"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    curent_pos = 0
    res_str = 'Список ресторанов :\n'
    for row in rows:
        curent_pos = curent_pos + 1
        res_str = res_str + f'{curent_pos} {row[1]}\n'
    if curent_pos <= 0:
        res_str = 'Список ресторанов пустой !!!'

    #print(res_str)
    bot.reply_to(message, res_str)



def  sel_sql000():
    conn = sqlite3.connect('samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM restaurants"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)

def sql_rest123():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM restaurants"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    for row in rows:
        print(row)
    conn.close()

#sql_rest123()
#a = 10 / 0

TOKEN = '7093861093:AAH5k8q2J-fITlb7lfSOv3hlYFtwLCG1CsM'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Подключение к базе данных SQLite
    conn = sqlite3.connect('./samo_mag_bot.db', check_same_thread=False)
    cursor = conn.cursor()

    user_first_name = message.from_user.first_name  # Имя пользователя
    user_username = '@'+message.from_user.username  # Ник пользователя в Telegram (может быть None)
    user_id = message.from_user.id

    cursor.execute('SELECT * FROM users WHERE telega_id=?', (user_id,))
    user = cursor.fetchone()

    if user:
        bot.send_message(message.chat.id, f"Добро пожаловать, {user_first_name}! Я чат-бот Доставка еды!")
    else:
        cursor.execute('INSERT INTO users (telega_id, telega_url, name) VALUES (?, ?, ?)',
                       (user_id, user_username, user_first_name))
        conn.commit()

        cursor.execute('SELECT * FROM users WHERE telega_id=?', (user_id,))
        user = cursor.fetchone()

    conn.close()

    return user[0]
# @bot.message_handler(commands=["start"])
# def start_message(message):
#     bot.reply_to(message, 'Привет! Я чат бот Доставка еды !')

@bot.message_handler(commands=["list"])
def list_message(message):
    sql_list_command(message)


bot.polling(none_stop=True)
