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
            print('Введите логин:')
            login = str(input())
            db.delete_user(login)
        elif cmd == "show":
            users = db.get_users_data()
            for user in users:
                print(user)
        elif cmd == "newcolumn":
            print('Введите название таблицы и информацию о колонке:')
            table = input()
            column_info = input()
            db.add_column(table, column_info)
        else:
            print("Ошибка: Incorrect command")


if __name__ == "__main__":
    global db
    db = database.Database()
    db.open("dormitory.db")
    cmdline()
    db.close()


