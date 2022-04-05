from flask_app.models.model_user import User
from flask_app.models.model_show import Show
from flask_app import app, bcrypt
from flask_app.models import model_user
from flask_app.models import model_show
from flask import render_template,redirect,request,session,flash


@app.route('/')
def index():
    # all_users=User.get_all()
    return render_template('index.html')

@app.route('/user/login', methods=['post'])
def login():
    is_valid= User.validator_login(request.form)

    if not is_valid:
        return redirect('/')
    
    if 'user_id' in session:
        return redirect('/loggedin')

    return redirect('/')

@app.route('/loggedin')
def loggedin():
    if 'user_id' not in session:
        return redirect('/')
    
    # if 'user_id' in session:
    all_shows=model_show.Show.get_all_shows()
    all_users=model_user.User.get_all()
    return render_template('logged_in.html', all_shows=all_shows, all_users=all_users)

@app.route('/logout')
def logout():
    del session['user_id']
    return redirect('/')

@app.route('/user/new')
def new():
    pass

@app.route('/user/create',methods=['post'])
def create():
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
    return redirect('/')


@app.route('/user/edit/<int:id>')
def edit(id):
    user= User.get_one({'id': id})
    return render_template("user_edit.html", user=user)

@app.route('/user/show/<int:id>')
def display(id):
    pass


@app.route('/user/update/<int:id>', methods=['post'])
def update(id):
    # User.update(request.form)
    # return redirect('/')
    pass

@app.route('/user/delete/<int:id>')
def delete(id):
    # User.delete({'id':id})
    # return redirect('/')
    pass