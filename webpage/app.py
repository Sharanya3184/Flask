from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sharanya:sharanya331@cluster0.hhle2tv.mongodb.net/")
db = client["sharanya"]
collection = db["users"]  

app = Flask(__name__)
app.secret_key = 'sdf'

MONGO_URL = "mongodb+srv://sharanya:sharanya331@cluster0.hhle2tv.mongodb.net/"
DB_NAME = "sharanya"
DB_PASSWORD = "sharanya331"

@app.route('/')
def Dashboard():
    return render_template('index.html')



@app.route('/<name>', methods=['GET'])
def render_name(name: str):
    if name:
        return render_template('error.html')
    


@app.route('/form', methods=['GET'])
def get_user_data():
    return render_template('form.html')


@app.route('/form', methods=['POST'])
def post_user_data():
    username = request.form['username']
    password = request.form['password']

    if username and password:
        return redirect(url_for('Dashboard', name=username))

    return redirect(url_for('hello'))



@app.route('/register', methods=['GET'])
def get_register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form.get('confirm_password')  
    gender = request.form.get('gender')  


    if password != confirm_password:
        flash("Password doesn't match", 'error')
        return redirect(url_for('get_register'))

    register_info = {
        "username": username,
        "password": password,
        "gender": gender,
        'created_date': datetime.now()
    }

    print("register_info", register_info)
    if register_info and register_info['username']:
        collection.insert_one(register_info)

    return redirect(url_for('Dashboard'))



@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')



@app.route('/login', methods=['POST'])
def login_post():
    
    username = request.form["username"]
    password = request.form["password"]

    user = collection.find_one({"username": username})
    if user and user.get("password") == password:
        session['username'] = username
        session['login_at'] = datetime.now()
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid username or password", 'error')
        return redirect(url_for('get_login'))


@app.route('/sed')
def session_dict():
    return jsonify(session)

@app.route('/test', methods=['GET'])
def test_api():
    
    username = session.get('username')

    return redirect(url_for(
        'render_name',
        name=username
    ))




if __name__ == '__main__':
    app.run(debug=True)
