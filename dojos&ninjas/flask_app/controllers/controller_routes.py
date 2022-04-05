from flask_app.models.model_person import Person
from flask_app import app
from flask import render_template,redirect,request,session,flash
@app.route('/')
def index():
    return render_template('index.html')

