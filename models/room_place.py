from database.db_manager import get_connection

class RoomPlace:
    def __init__(self, id=None, room_id=None, place_number=None):
        self.id = id
        self.room_id = room_id
        self.place_number = place_number

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""
                INSERT INTO room_places (room_id, place_number)
                VALUES (?, ?)
            """, (self.room_id, self.place_number))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE room_places SET room_id = ?, place_number = ?
                WHERE id = ?
            """, (self.room_id, self.place_number, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM room_places WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()
