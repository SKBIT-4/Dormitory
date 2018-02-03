from flask import render_template # импорт шаблонов
from flask import request #импорт flask.request, иначе получим ошибку nameerror name 'request' is not defined flask
from app import app

@app.route('/')
@app.route('/base')
def base():
    return render_template('base.html')
    
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries')) #Перенаправление на страницу при удачном входе пользователя
    return render_template('sign_in.html', error=error)
