# blog.py - controller

#imports
from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3
from functools import wraps

#Configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = ';\xf2\xed\x81\xd9\xe0\xe8\xf2<L-\xc5\xb7\xd10\x98\x85v\x93/V\x10\\\xec'

app = Flask(__name__)

#Uses uppercase to look for app configuration
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connection(app.config['DATABASE_PATH'])

@app.route('/', methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error)

@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash('You were logged out')
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)