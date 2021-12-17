from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_mail import Mail, Message
import sqlite3 as sql

db_app = Blueprint('db_app', __name__, template_folder='templates')

@db_app.route('/create/table')
def create_table():
    conn = sql.connect('flasktest.db')
    print "Opened database successfully"

    conn.execute('CREATE TABLE students12 (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    print "Table created successfully"
    conn.close()


@db_app.route('/enternew')
def new_student():
   return render_template('student_input.html')


@db_app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   msg = ""
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']

         with sql.connect("flasktest.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("student_result.html", msg = msg)
         con.close()

@db_app.route('/list')
def list():
   con = sql.connect("flasktest.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from students")

   rows = cur.fetchall()
   return render_template("student_list.html",rows = rows)