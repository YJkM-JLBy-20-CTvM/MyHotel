import sqlite3

from .. import config

def get_connection():
    return sqlite3.connect(config.DB_NAME)

def initialize_db():
    conn = get_connection
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS clients(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   surname TEXT NOT NULL,
                   name TEXT NOT NULL,
                   patronymic TEXT,
                   passport_details TEXT NOT NULL UNIQUE,
                   address TEXT,
                   comment TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXIST discount_categories(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   discount_percent REAL NOT NULL CHECK(discount_percent >= 0))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS client_discounts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   client_id INTEGER NOT NULL,
                   discount_category_id INTEGER NOT NULL,
                   FOREIGN KEY (client_id) REFERENCES client(id),
                   FOREIGN KEY (discount_category_id) REFERENCES discount_categories(id))''')
    
    cursor.execute('''CREATE TABLE rooms(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   type TEXT NOT NULL CHECK(type IN ("люкс", "полулюкс", "обычный")),
                   capacity INTEGER NOT NULL CHECK(capacity > 0),
                   price REAL NOT NULL CHECK(price >= 0),)''')
    
    cursor.execute('''CREATE TABLE room_places(
                   id INTEGER PRIMARY KEY AUTOINCRECEMENT,
                   room_id INTEGER NOT NULL,
                   place_number INTEGER NOT NULL CHECK(place_number > 0),
                   FOREIGN KEY (room_id) REFERENCES rooms(id))''')
    
    cursor.execute('''CREATE TABLE checkins(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   client_id INTEGER NOT NULL,
                   room_id INTEGER NOT NULL,
                   place_id INTEGER,
                   checkin_date DATE NOT NULL,
                   checkout_date DATE,
                   FOREIGN KEY (client_id) REFERENCES clients(id),
                   FOREIGN KEY (room_id) REFERENCES rooms(id)
                   FOREIGN KEY (place_id) REFERENCES room_places(id)''')
    
    cursor.execute('''CREATE TABLE booking(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   client_id INTEGER NOT NULL,
                   room_id INTEGER NOT NULL,
                   start_date DATE NOT NULL,
                   end_date DATE NOT NULL,
                   is_confirmed BOOLEAN NOT NULL DEFAULT 0,
                   FOREIGN KEY (client_id) REFERENCES clients(id),
                   FOREIGN KEY (room_id) REFERENCES rooms(id))''')
    conn.commit()
    conn.close()