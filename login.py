from flask import Flask, render_template, redirect, url_for, Blueprint, request

login_page = Blueprint('login_page', __name__, template_folder='templates')

@login_page.route('/login/view')
def login_view():
    return render_template('login.html')

@login_page.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@login_page.route('/get/success/<name>')
def success_get(name):
   return 'welcome %s' % name


# for get request send <url?nm='Admin'>
@login_page.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('login_page.success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('login_page.success_get',name = user))
