from flask import Flask, render_template, redirect, url_for, Blueprint, request
from collections import OrderedDict

student_app = Blueprint('student_app', __name__, template_folder='templates')

@student_app.route('/student/view')
def student():
   return render_template('student.html')

@student_app.route('/student/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      res = OrderedDict(reversed(list(result.items())))
      return render_template("result.html",result = res)
