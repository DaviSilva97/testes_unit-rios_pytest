from distutils.log import error
import sqlite3

connection = sqlite3.connect("C:\\Users\\davis\\Documents\\SGA Sistemas\\Repositórios\\testes unitários\\src\\dados\\books.db")
cur = connection.cursor()


def add_in_database(title, price):
    try:
        cur.execute("INSERT INTO books (title, price) VALUES(?, ?)", (title, price))
        connection.commit()
        return True
    except error: 
        print(error)
        return False

def get_all_books():
    cur.execute("SELECT * FROM BOOKS")
    return cur.fetchall()
    
               