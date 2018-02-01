import database
import sqlite3

if __name__ == "__main__":
    db = database.Database()
    db.open("database.db")
    db.add_user("ichega", "qwerty", "Pavel", "Katskov")
    db.get_users_data()
    db.close()
