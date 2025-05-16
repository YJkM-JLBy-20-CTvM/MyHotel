from database.db_manager import get_connection

class Checkin:
    def __init__(self, id=None, client_id=None, room_id=None, place_id=None, checkin_date=None, checkout_date=None):
        self.id = id
        self.client_id = client_id
        self.room_id = room_id
        self.place_id = place_id
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""
                INSERT INTO checkins (client_id, room_id, place_id, checkin_date, checkout_date)
                VALUES (?, ?, ?, ?, ?)
            """, (self.client_id, self.room_id, self.place_id, self.checkin_date, self.checkout_date))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE checkins SET client_id = ?, room_id = ?, place_id = ?, checkin_date = ?, checkout_date = ?
                WHERE id = ?
            """, (self.client_id, self.room_id, self.place_id, self.checkin_date, self.checkout_date, self.id))
        conn.commit()
        conn.close()

def get_all_checkins():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, client_id, room_id, place_id, checkin_date, checkout_date FROM checkins
    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        Checkin(
            id=row[0],
            client_id=row[1],
            room_id=row[2],
            place_id=row[3],
            checkin_date=row[4],
            checkout_date=row[5]
        )
        for row in rows
    ]

def get_checkin_by_id(checkin_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, client_id, room_id, place_id, checkin_date, checkout_date FROM checkins WHERE id = ?
    """, (checkin_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Checkin(
            id=row[0],
            client_id=row[1],
            room_id=row[2],
            place_id=row[3],
            checkin_date=row[4],
            checkout_date=row[5]
        )
    return None