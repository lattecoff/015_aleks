"""
В вашей базе данных есть таблица "Books" со следующими столбцами: "id" (целое число, первичный ключ), "title" (текстовый тип), "author" (текстовый тип), "year" (целое число) и "price" (вещественный тип). Вам необходимо выполнить следующие действия:

- вставьте несколько записей в таблицу "Books" с информацией о различных книгах, включая название, автора, год издания и цену.

- выберите все записи из таблицы "Books", отсортированные по году издания в порядке возрастания.

- выберите книги, у которых цена выше определенного значения.

- обновите цену книги с определенным ID.

- удалите книги, у которых год издания меньше определенного значения.
"""
import sqlite3

conn = sqlite3.connect('Books.db')
cursor = conn.cursor()

# Создаем таблицу.
cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title VARCHAR(100), author VARCHAR(100), year INTEGER, price DEC)''')
conn.commit()

# Добавляем записи в таблицу.
cursor.execute('''INSERT INTO books (title, author, year, price)
VALUES ('Изучаем Python', 'Эрик Мэтьюз', '2022', '1825.00'),
       ('Программирование на Python', 'Васильев А.Н.', '2022', '1306.00'),
       ('Простой Python', 'Любанович Б.', '2021', '2016.00');''')

# Сортируем книги по годам.
cursor.execute('''SELECT * FROM books ORDER BY year''')
table_sort = cursor.fetchall()
print(table_sort)

# Выбираем кнги чья цена выше 2000р.
cursor.execute('''SELECT * FROM books WHERE price > 2000''')
# Обновлем цену на книгу с id = 1.
cursor.execute('''UPDATE books SET price = ? WHERE id = ?''', (1000, 1))
# Выбираем книги изданные раньше 2022г.
cursor.execute('''SELECT * FROM books WHERE year < 2022''')
# Удалаем книги изданные раеньше 2022г.
cursor.execute('''DELETE FROM books WHERE year < 2022''')

conn.commit()

cursor.close()
conn.close()