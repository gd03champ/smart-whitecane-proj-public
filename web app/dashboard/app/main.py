import mysql.connector
import flask
from flask import Flask, redirect, render_template
from flask_simplelogin import SimpleLogin, is_logged_in

con = mysql.connector.connect(
  host="host",
  port="3306",
  user="user",
  password="",
  database = ""    #optional
)

cur = con.cursor()

app = Flask(__name__)

app.config['SECRET_KEY'] = ''
app.config['SIMPLELOGIN_HOME_URL'] = '/dashboard'
SimpleLogin(app)
#render_template('template.html', data=data)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/dashboard')
def dashboard_route():
  if is_logged_in('admin'):
    cur.execute("SELECT * FROM data")
    data = cur.fetchall()
    return render_template('dashboard.html', data=data)
  else:
    return redirect("/login")

