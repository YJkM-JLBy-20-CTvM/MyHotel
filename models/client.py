from database.db_manager import get_connection

class Client:
    def __init__(self, id=None, surname=None, name=None, patronymic=None,
                 passport_details=None, address=None, comment=None):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.passport_details = passport_details
        self.address = address
        self.comment = comment

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""
                INSERT INTO clients (surname, name, patronymic, passport_details, address, comment)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.surname, self.name, self.patronymic, self.passport_details, self.address, self.comment))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""
                UPDATE clients SET surname = ?, name = ?, patronymic = ?, passport_details = ?, address = ?, comment = ?
                WHERE id = ?
            """, (self.surname, self.name, self.patronymic, self.passport_details, self.address, self.comment, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clients WHERE id = ?", (self.id,))
            conn.commit()
            conn.close()

def get_all_clients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, surname, name, patronymic, passport_details, address, comment FROM clients")
    rows = cursor.fetchall()
    conn.close()
    return [Client(*row) for row in rows]

def get_client_by_id(client_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, surname, name, patronymic, passport_details, address, comment FROM clients WHERE id = ?", (client_id,))
    row = cursor.fetchone()
    conn.close()
    return Client(*row) if row else None
