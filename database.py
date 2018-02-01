import sqlite3
import hashlib

class Database:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def open(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def create_db(filename):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        sql = """
            CREATE TABLE users(
                id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT,
                password_hash TEXT,
                first_name TEXT,
                last_name TEXT);
            """
        print(sql)
        try:
            cur.executescript(sql)
        except sqlite3.DatabaseError as err:
            print("Ошибка: ", err)
        else:
            print("Запрос успешно выполнен")
        cur.close()
        con.close()

    def password_hash(self, password):
        hash = hashlib.sha256(bytearray(password, 'utf-8'))
        return hash.hexdigest()

    def add_user(self, login, password, first_name, last_name):
        password = self.password_hash(password)
        sql = """
        INSERT INTO users (login, password_hash, first_name, last_name)
        VALUES (?, ?, ?, ?);
        """
        param = (login, password, first_name, last_name)
        try:
            self.cursor.execute(sql, param)
        except sqlite3.DatabaseError as err:
            print("Ошибка: ", err)
        else:
            print("Запрос выполнен успешно")
            self.connection.commit()

    def get_users_data(self):
        sql = "SELECT * FROM users;"
        self.cursor.execute(sql)
        for user_data in self.cursor:
            print(user_data)

