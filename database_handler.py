import sqlite3

class DatabaseHandler:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

    def fetch_column_names(self):
        try:
            return [description[0] for description in self.cursor.description]
        except Exception as e:
            print(f"Error fetching column names: {e}")
            raise

    def close_connection(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
            raise
