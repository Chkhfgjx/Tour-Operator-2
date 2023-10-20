import sqlite3

# Создание и подключение к БД
conn = sqlite3.connect('tour_operator.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS tours
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   destination TEXT,
                   duration INTEGER,
                   price REAL)''')

# Добавление данных в таблицу
def add_tour(destination, duration, price):
    cursor.execute('INSERT INTO tours (destination, duration, price) VALUES (?, ?, ?)', (destination, duration, price))
    conn.commit()

# Получение списка туров
def get_tours():
    cursor.execute('SELECT * FROM tours')
    return cursor.fetchall()

# Удаление тура по id
def delete_tour(id):
    cursor.execute('DELETE FROM tours WHERE id=?', (id,))
    conn.commit()

# Пример использования
add_tour('Париж', 7, 1000.0)
add_tour('Барселона', 5, 800.0)
tours = get_tours()
print(tours)

# Закрытие соединения с БД
conn.close()
