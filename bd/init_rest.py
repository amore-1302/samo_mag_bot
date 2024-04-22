
import sqlite3
def add_sql():
    rest = []
    rest.append( ("Вкусно и Точка", "Москва ул Лесная д 5", ) )
    rest.append( ("БургергКинг", "Москва ул Металлургов д 10", ) )
    rest.append( ("ДодоПица", "Москва Волгоградский проспект д 110", ) )
    rest.append( ("Пипони", "Москва ул Вавилова д 37", ) )

    for el in rest:
        print(el)
        print("")
        conn = sqlite3.connect('../samo_mag_bot.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO restaurants (name, address) VALUES (?, ?)', el)
        conn.commit()
        conn.close()

def  sel_sql():
    conn = sqlite3.connect('../mydatabase.db')
    cursor = conn.cursor()
    query = "SELECT * FROM restaurants"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    for row in rows:
        print(row)
    conn.close()

# для заполнения таблицы
#add_sql()

# для просмотра таблицы
sel_sql()