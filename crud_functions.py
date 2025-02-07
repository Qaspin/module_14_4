import sqlite3

def db():
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        ) 
    """)
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * From Products WHERE id > ?', (0,))
    return cursor.fetchall()
    connection.commit()
    connection.close()