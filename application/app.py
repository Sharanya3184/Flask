from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from datetime import datetime
from pymongo import MongoClient
from db_config import collection
from auth import login_required 
import os

app = Flask(__name__)


app.secret_key = 'Super secret key'

folder_name ='uploads'


os.makedirs(folder_name, exist_ok=True)



@app.route('/login')

def Hello():
	username         = session.get('username')
	password         = session.get('password')
	confirm_password = session.get('confirm_password')
	
	return render_template('index.html',
						 username = username,
						 password=confirm_password)



@app.route ('/<name>', methods=['GET'])
def render_name(name :str):
	
    if name:
          return render_template('name.html', value=name) 
    else:
        return render_template('error.html', error='Name not provided')
    


@app.route('/form', methods = ['GET'])
@login_required
def get_user_data():
      return render_template('form.html')



@app.route('/form', methods=['POST'])
@login_required
def post_user_data():
    username = request.form.get['username']
    password = request.form.get['password']

    if username and password:
         return redirect(url_for('form'))
    
    else:
        return render_template('error.html', error='Username and password are required')
    


@app.route('/register', methods=['GET'])
def get_register():
     return render_template('register.html')



@app.route('/register', methods=['POST'])

def register_user():
     username           =   request.form["username"]
     password           =   request.form["password"]
     confirm_password   =   request.form["confirm_password"]
     gender             =   request.form['gender']

     user = collection.find_one(
          {"username": username})
     
     if user:
          flash('UserName AlreaDY EX!sit',"ERR0R !!")
          return redirect(url_for('register'))
     
     if password != confirm_password:
          flash('Passwords do not match', "ERR0R !!")
          return redirect(url_for('register'))
     

     dict ={
          'Username'    :    username, 
           'Password'   :    password,
           'gender'     :   gender,
           'Created_at' :   datetime.now(),

     }

     print('dict_data:', dict)

     collection.insert_one(dict)
     flash('User registered successfully', "SUCCESS !!")
     return redirect(url_for('Hello'))



@app.route('/', methods=['GET'])
def login_get():
     return render_template('login.html')




@app.route('/', methods=['POST'])
def login_post():
    username            =   request.form.get('username')
    password            =   request.form.get('password')
    confirm_password    =   request.form.get('confirm_password')
     


    if username and password:
        session['username']             =   username
        session['password']             =   password
        session['confirm_password']     =   confirm_password
        session['login_at']             =   datetime.now()
        session['logged_in']            =   True

        return redirect(url_for('Hello'))
    
    else:
        flash('Username and password are required', "ERR0R !!")
        return redirect(url_for('login_get'))



@app.route('/sed')
def session_dict():
     return jsonify(session)



@app.route('/test', methods=['GET'])
def test_api():
     username = session.get('username')
     return render_template('render_name', name = username)



@app.route('/uploads', methods =['GET'])          
def upload_file_get():
  return render_template('upload.html')



@app.route('/uploads', methods =['POST'])
def upload_file():
  username = session.get("username")
  file = request.files['file']

  if not file:
    return redirect(url_for('upload_file_get'))
  
  if file and file.filename:
    path = f'{folder_name}/{file.filename}'
    data_dict = {
      "username"         : username,
      "filename"         : file.filename,
      "path"             : path,
      "uploadded_at"     : datetime.now()
    }     
    file.save(path)                               
    return redirect(url_for('upload_file_get'))
  
  return redirect(url_for('upload_file_get'))




@app.route('/logout', methods=['GET'])
def logout():
     session.clear()
     return redirect(url_for('login_get'))








if __name__ == '__main__':
    app.run(debug=True)