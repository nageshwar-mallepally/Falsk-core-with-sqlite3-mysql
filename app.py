from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message

from login import login_page
from student import student_app
from db_connet import db_app
from mysql_conn import mysql_app

app = Flask(__name__)

app.register_blueprint(login_page)
app.register_blueprint(student_app)
app.register_blueprint(db_app)
app.register_blueprint(mysql_app)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/base")
def base():
	return render_template('base.html')

@app.route("/title")
def title():
	return "This is the new flask application"

@app.route("/details")
def details():
	return render_template('details.html')

@app.route('/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/<int:val>')
def hello_int1(val):
    return 'Integer value %d' %val

@app.route('/<float:val1>')
def hello_float1(val1):
    return 'Float value %f' %val1

@app.route('/flask')
def flask_display():
    return '/flask'

@app.route('/flask/')
def flask_display1():
    return '/flask/'

@app.route('/user1/<name>')
def hello_user(name):
    if name =='admin':
       return redirect(url_for('hello_admin'))
    else:
       return redirect(url_for('hello_guest',guest = name))

@app.route('/admin11')
def hello_admin():
   return 'This is Admin user'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 534
app.config['MAIL_USERNAME'] = 'nageshreddy2471@gmail.com'
app.config['MAIL_PASSWORD'] = '123456778'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/send/mail")
def send_mail():
   msg = Message('Hello', sender = 'nageshreddy2471@gmail.com', recipients = ['phani.raghava@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"


