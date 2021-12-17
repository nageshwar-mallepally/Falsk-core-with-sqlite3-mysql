from flask import Flask, render_template, redirect, url_for, Blueprint, request
import mysql.connector
from mysql.connector import Error

mysql_app = Blueprint('mysql_app', __name__, template_folder='templates')

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'practice',
    'raise_on_warnings': True
}
connection = mysql.connector.connect(**config)

@mysql_app.route('/mysql/conn')
def get_mysql_conn():
    output = ""
    try:
        if connection.is_connected():
            db_Info = connection.get_server_info()
            output = output +"Connected to MySQL Server version "
            print(db_Info)
            cursor = connection.cursor()
            record = cursor.fetchone()
    except Error as e:
        output = output+"Error while connecting to MySQL", (e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return output

@mysql_app.route('/create/laptop')
def create_table():
    mySql_Create_Table_Query = """CREATE TABLE Laptop6 ( 
                                 Id int(11) NOT NULL,
                                 Name varchar(250) NOT NULL,
                                 Price varchar(250) NOT NULL,
                                 Purchase_date varchar(250) NOT NULL,
                                 PRIMARY KEY (Id)) """
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    return  "Laptop Table created successfully "


@mysql_app.route('/mysql/enternew')
def new_laptop():
    return render_template('laptop_input.html')

@mysql_app.route('/mysql/addrec',methods = ['POST', 'GET'])
def addrec1():
    msg = ""
    if request.method == 'POST':
        try:
            id = request.form['id']
            name = request.form['name']
            price = request.form['price']
            purchase_date = request.form['purchase_date']
            print(name, price, purchase_date)

            cur = connection.cursor()
            query2 = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s) """
            record = (id, name, price, purchase_date)
            cur.execute(query2, record)
            connection.commit()

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("laptop_result.html")
            con.close()


@mysql_app.route('/mysql/list')
def laps_list():
    sql_select_Query = "select * from Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()

    print(records)
    return render_template("laptop_list.html", records = records)