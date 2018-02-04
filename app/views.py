from flask import render_template # импорт шаблонов
from flask import request #импорт flask.request, иначе получим ошибку nameerror name 'request' is not defined flask
from app.forms import SignInForm, SignUpForm
from app import app
import database

@app.route('/')
@app.route('/index')
def base():
    return render_template('index.html')

@app.route('/users')
def show_users():
    db = database.Database()
    db.open("dormitory.db")
    users_data = db.get_users_data()
    names = ['id', 'login', 'password_hash', 'first_name', 'last_name']
    users = list()
    for item in users_data:
        user = dict(zip(names, item))
        users.append(user)
    print(users)
    db.close()
    return render_template('users.html', users=users)
    
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    error = None
    if request.method == 'POST':
        form = request.form
        print(request.form)


    return render_template('sign_in.html', error=error, form=SignInForm())

@app.route('/registry', methods=['GET', 'POST'])
def registry():
    error = None
    if request.method == 'POST':
        form = request.form
        print(form)
        login = form['login']
        password = form['password']
        db = database.Database()
        db.open("dormitory.db")
        user = db.get_user_data_login(login)
        if user == None:
            print('Пользователь добавлен')
            db.add_user(login, password, "Pavel", 'Katskov')
        else:
            print('Логин уже занят')
        print(user)
        db.close()
    return  render_template('registry.html', error=error, form=SignUpForm())