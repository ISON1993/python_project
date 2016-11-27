from flask import Flask
import sqlite3
import form
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from form import LoginForm

# 配置文件
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app=Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",name='tuzhenyu')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9999, use_reloader=True)
