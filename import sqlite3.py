##16.8

import sqlite3
import sqlalchemy  

conn = sqlalchemy.create_engine('sqlite://')
conn = sqlite3.connect('book.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books
            (title VARCHAR (20) PRIMARY KEY,
            author VARCHAR(20),
            year INT)''')

curs.execute('SELECT title from books ORDER BY NAME') 
