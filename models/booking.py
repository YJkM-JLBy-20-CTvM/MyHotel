from database.db_manager import get_connection

class Booking:
    def __init__(self, id=None, client_id=None, room_id=None, start_date=None, end_date=None, is_confirmed=False):
        self.id = id
        self.client_id = client_id
        self.room_id = room_id
        self.start_date = start_date
        self.end_date = end_date
        self.is_confirmed = is_confirmed

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute('''
                INSERT INTO booking (client_id, room_id, start_date, end_date, is_confirmed)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.client_id, self.room_id, self.start_date, self.end_date, self.is_confirmed))
            self.id = cur.lastrowid
        else:
            cur.execute('''
                UPDATE booking SET client_id = ?, room_id = ?, start_date = ?, end_date = ?, is_confirmed = ?
                WHERE id = ?
            ''', (self.client_id, self.room_id, self.start_date, self.end_date, self.is_confirmed, self.id))
        conn.commit()
        conn.close()
def get_all_bookings():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT id, client_id, room_id, start_date, end_date, is_confirmed FROM booking
    ''')
    rows = cur.fetchall()
    conn.close()
    return [
        Booking(
            id=row[0],
            client_id=row[1],
            room_id=row[2],
            start_date=row[3],
            end_date=row[4],
            is_confirmed=bool(row[5])
        )
        for row in rows
    ]

def get_booking_by_id(booking_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT id, client_id, room_id, start_date, end_date, is_confirmed FROM booking WHERE id = ?
    ''', (booking_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return Booking(
            id=row[0],
            client_id=row[1],
            room_id=row[2],
            start_date=row[3],
            end_date=row[4],
            is_confirmed=bool(row[5])
        )
    return None