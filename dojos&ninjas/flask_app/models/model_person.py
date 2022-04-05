from flask_app.config.mysqlconnection import connectToMySQL
DATABASE='dojos_ninjas'

class Person:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            users = []
            for u in results:
                users.append( cls(u) )
            return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name,age) VALUES (%(first_name)s,%(last_name)s,%(age)s);"

        # comes back as the new row id
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)