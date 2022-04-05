from flask import render_template, session,redirect, request,flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_message import Message



bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():
    is_valid= User.validator(request.form)
    if not is_valid: 
        return redirect('/')
    
    hash_pw= bcrypt.generate_password_hash(request.form['pw'])
    print(len(hash_pw))

    data={
        **request.form,
        'pw': hash_pw
    }
    
    id= User.create(data)
    session['user_id']=id
    return redirect('/dashboard')
    
@app.route("/login",methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_one_by_email(data)
    print("**********************************")
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    
    if not bcrypt.check_password_hash(user.pw,request.form['pw']):
        flash("Invalid Email/Password","login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect('/dashboard')


# @app.route('/user/create',methods=['post'])
# def create():
#     is_valid= User.validator(request.form)
#     if not is_valid: 
#         return redirect('/')
    
#     hash_pw= bcrypt.generate_password_hash(request.form['pw'])
#     print(len(hash_pw))

#     data={
#         **request.form,
#         'pw': hash_pw
#     }
    
#     id= User.create(data)
#     session['user_id']=id
#     return redirect('/')
    
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    messages = Message.get_user_messages(data)
    users = User.get_all()
    return render_template("dashboard.html",user=user,users=users,messages=messages)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')