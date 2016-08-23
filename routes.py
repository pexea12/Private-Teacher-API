from api import app
from flask import render_template

@app.route('/')
def log():
    return render_template('login.html')


@app.route('/add')
def add():
    return render_template('add_teacher.html')

@app.route('/list_own')
def list_own():
    return render_template('list_own.html')
