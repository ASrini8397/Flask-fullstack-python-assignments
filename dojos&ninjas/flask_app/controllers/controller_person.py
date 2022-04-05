from flask_app.models.model_person import Person
from flask_app import app
from flask import render_template,redirect,request,session,flash

@app.route('/person/new')
def new():
    return render_template("person_new.html")

@app.route('/person/create',methods=['POST'])
def create():
    pass


@app.route('/person/edit/<int:id>')
def edit(id):
    pass

@app.route('/person/show/<int:id>')
def show(id):
    pass


@app.route('/person/update/<int:id>')
def update():
    pass

@app.route('/person/destroy/<int:id>')
def destroy(id):
    pass