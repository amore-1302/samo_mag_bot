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
        curent_pos = curent_pos + 1;
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


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот Доставка еды !')

@bot.message_handler(commands=["list"])
def list_message(message):
    sql_list_command(message)


bot.polling(none_stop=True)
