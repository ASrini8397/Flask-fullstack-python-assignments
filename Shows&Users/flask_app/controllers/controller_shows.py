from flask_app.models.model_show import Show
from flask_app.models.model_user import User
from flask_app.models import model_show
from flask_app.models import model_user
from flask_app import app, bcrypt
from flask import render_template,redirect,request,session,flash




@app.route('/show')
def new_show():
    return render_template('showform.html')

@app.route('/show/create', methods=['post'])
def create_show():
    show_valid= model_show.Show.show_validator(request.form)
    if not show_valid: 
        return redirect('/show')
    bid= model_show.Show.createshow(request.form)
    return redirect('/loggedin')


@app.route('/show/edit/<int:id>')
def edit_show(id):
    show= Show.getone({'id': id})
    return render_template("show_edit.html", show=show)

@app.route('/show/myshow/<int:id>')
def show_show(id):
    show= model_show.Show.get_one_show({'id': id})
    poster=model_show.Show.getusername({'id': id})
    print(poster)
    return render_template("myshows.html", show=show, poster=poster )
    


@app.route('/show/update/<int:id>', methods=['post'])
def update_show(id):
    show_valid= model_show.Show.show_validator(request.form)
    Show.updateshow(request.form)
    print(request.form)
    return redirect('/loggedin')
    

@app.route('/show/delete/<int:id>')
def delete_show(id):
    model_show.Show.delete({'id':id})
    return redirect('/loggedin')