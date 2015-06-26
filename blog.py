# blog.py - controller

#imports
from flask import Flask, render_template, request, session, \
	flash, redirect, url_for, g
import sqlite3

#Configuration
DATABASE = 'blog.db'

app = Flask(__name__)

#Uses uppercase to look for app configuration
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connection(app.config['DATABASE_PATH'])

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/main')
def main():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=True)