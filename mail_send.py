from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_mail import Mail, Message

mail_app = Blueprint('mail_app', __name__, template_folder='templates')

mail_app.config['MAIL_SERVER']='smtp.gmail.com'
mail_app.config['MAIL_PORT'] = 465
mail_app.config['MAIL_USERNAME'] = 'nagehshreddy2471@gmail.com'
mail_app.config['MAIL_PASSWORD'] = '123456778'
mail_app.config['MAIL_USE_TLS'] = False
mail_app.config['MAIL_USE_SSL'] = True

mail = Mail(mail_app)

@app.route("/send/mail")
def index():
   msg = Message('Hello', sender = 'nageshreddy2471@gmail.com', recipients = ['phani.raghava@cassinisys.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"
