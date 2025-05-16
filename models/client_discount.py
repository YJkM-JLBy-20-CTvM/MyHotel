from database.db_manager import get_connection

class ClientDiscount:
    def __init__(self, id=None, client_id=None, discount_category_id=None):
        self.id = id
        self.client_id = client_id
        self.discount_category_id = discount_category_id

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""
                INSERT INTO client_discounts (client_id, discount_category_id)
                VALUES (?, ?)
            """, (self.client_id, self.discount_category_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE client_discounts SET client_id = ?, discount_category_id = ?
                WHERE id = ?
            """, (self.client_id, self.discount_category_id, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM client_discounts WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_discounts_by_client_id(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, client_id, discount_category_id FROM client_discounts
        WHERE client_id = ?
    """, (client_id,))
    rows = cursor.fetchall()
    conn.close()
    return [ClientDiscount(id=row[0], client_id=row[1], discount_category_id=row[2]) for row in rows]
