import database
import sqlite3

def cmdline():
    cmd = ""
    while (cmd != "exit"):
        cmd = input()
        if cmd == "add":
            print("Введите login, password, first_name, last_name:")
            login = input()
            password = input()
            f_name = input()
            l_name = input()
            db.add_user(login, password, f_name, l_name)
        elif cmd == "delete":
            pass
        elif cmd == "show":
            users = db.get_users_data()
            for user in users:
                print(user)
        else:
            print("Ошибка: Incorrect command")


if __name__ == "__main__":
    global db
    db = database.Database()
    db.open("dormitory.db")
    cmdline()
    db.close()


