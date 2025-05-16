from database.db_manager import get_connection

class DiscountCategory:
    def __init__(self, id=None, name=None, discount_percent=0.0):
        self.id = id
        self.name = name
        self.discount_percent = discount_percent

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""
                INSERT INTO discount_categories (name, discount_percent)
                VALUES (?, ?)
            """, (self.name, self.discount_percent))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE discount_categories SET name = ?, discount_percent = ?
                WHERE id = ?
            """, (self.name, self.discount_percent, self.id))
        conn.commit()
        conn.close()

def get_all_discount_categories():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, discount_percent FROM discount_categories
    """)
    rows = cursor.fetchall()
    conn.close()
    return [DiscountCategory(id=row[0], name=row[1], discount_percent=row[2]) for row in rows]

def get_discount_category_by_id(category_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, discount_percent FROM discount_categories WHERE id = ?
    """, (category_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return DiscountCategory(id=row[0], name=row[1], discount_percent=row[2])
    return None

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
