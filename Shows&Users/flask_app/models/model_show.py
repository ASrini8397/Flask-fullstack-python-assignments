from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import bcrypt
from flask_app.models import model_user
import re

DATABASE='tv_shows_db'

class Show:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.description = data['description']
        self.date=data['date']
        self.user_id=data['user_id']

    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            show_list = []
            for b in results:
                show_list.append( cls(b) )
            return show_list

    @classmethod
    def get_my_shows(cls,data):
        query = "SELECT * FROM shows JOIN users on shows.user_id=users.id WHERE shows.id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            my_list=[]
            for shows in results:
                show=cls(shows)
                dict={
                    'id': shows['id'],
                    'title': shows['title'],
                    'network': shows['network'],
                    'description': shows['description'],
                    'date': shows['date'],
                    'user_id': shows['user_id'],
                    'first_name': shows['users.first_name']

                }
                my_list.append(shows)
                print(my_list)
            return my_list
                
        return []
        

    @classmethod
    def createshow(cls, data):
        query = "INSERT INTO shows (title, network, description,date, user_id) VALUES (%(title)s, %(network)s,%(description)s, %(date)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
        

    @classmethod
    def get_one_show(cls,data):
        query  = "SELECT * FROM shows WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            show_details=[]
            for show in result:
                show_details.append(show)
            print(cls(result[0]))
            print(show_details)
            return show_details
        return False

    @classmethod
    def getone(cls,data):
        query  = "SELECT * FROM shows WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def getusername(cls,data):
        query  = "SELECT first_name, last_name FROM users LEFT JOIN shows ON shows.user_id=users.id WHERE shows.id= %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            poster=[]
            for show in result:
                poster.append(show)
            print(poster)
            return poster
        return False

    @classmethod
    def updateshow(cls,data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, description = %(description)s, date= %(date)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def show_validator(form_data):
        show_valid= True

        if len(form_data['title']) <2 :
            show_valid= False
            flash("Show name must be at least 2 characters", "err_title")

        if len(form_data['description']) <2 :
            show_valid= False
            flash("Description Required !", "err_show_description")
            
        
        if len(form_data['network']) <2 :
            show_valid= False
            flash("Network Required", "err_show_network")
    
        return show_valid

