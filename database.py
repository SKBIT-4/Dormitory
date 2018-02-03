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

    def create_db(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        sql = """
            CREATE TABLE users(
                id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT,
                password_hash TEXT,
                first_name TEXT,
                last_name TEXT);
            """
        try:
            self.cursor.executescript(sql)
        except sqlite3.DatabaseError as err:
            print("Ошибка: ", err)
        else:
            print("База данных успешно создана")
        self.cursor.close()
        self.connection.close()

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
            print("Пользователь добавлен")
            self.connection.commit()

    def get_users_data(self):
        sql = "SELECT * FROM users;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_user_data_login(self, login):
        sql = "SELECT * FROM users WHERE login='%s'" % login
        print(sql)
        self.cursor.execute(sql)
        user_data = self.cursor.fetchone()
        return user_data

    def get_user_data_condition(self, condition):
        pass


