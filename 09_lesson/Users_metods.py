from sqlalchemy import create_engine, text


class Users():

    scripts = {
        "insert": text(
            "INSERT INTO users(\"user_email\") VALUES (:new_email)"),
        "select": text(
            "SELECT * FROM users WHERE(\"user_email\") = :new_email"),
        "delete": text(
            "DELETE FROM users WHERE(\"user_email\") = :new_email"),
        "updated": text(
            'UPDATE users '
            'SET "user_email" = :put_mail '
            'WHERE "user_email" = :new_email'
            ),

    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def insert_users(self, email_insert):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["insert"], {"new_email": email_insert})
        transaction.commit()
        conn.close()

    def get_users(self, email_insert_get):
        conn = self.db.connect()
        result = conn.execute(self.scripts["select"], {
            "new_email": email_insert_get})
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete_users(self, email_insert_delete):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["delete"], {
            "new_email": email_insert_delete})
        transaction.commit()
        conn.close()

    def updated_users(self, put_mail, email_insert_updated):
        conn = self.db.connect()
        transaction = conn.begin()
        conn.execute(self.scripts["updated"], {
            "put_mail": put_mail, "new_email": email_insert_updated})
        transaction.commit()
        conn.close()
