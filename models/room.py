from database.db_manager import get_connection

class Room:
    def __init__(self, id=None, type=None, capacity=None, price=None, place=None):
        self.id = id
        self.type = type
        self.capacity = capacity
        self.price = price
        self.place = place

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute('''
                INSERT INTO rooms (place, type, capacity, price)
                VALUES (?, ?, ?, ?)
            ''', (self.place, self.type, self.capacity, self.price))
            self.id = cur.lastrowid
        else:
            cur.execute('''
                UPDATE rooms SET type = ?, capacity = ?, price = ?, place = ?
                WHERE id = ?
            ''', (self.place, self.type, self.capacity, self.price, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('DELETE FROM rooms WHERE id = ?', (self.id,))
            conn.commit()
            conn.close()

def get_all_rooms():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, type, capacity, price, place FROM rooms')
        rows = cur.fetchall()
        conn.close()
        return [Room(*row) for row in rows]

def get_room_by_id(room_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, type, capacity, price, place FROM rooms WHERE id = ?', (room_id,))
        row = cur.fetchone()
        conn.close()
        return Room(*row) if row else None
