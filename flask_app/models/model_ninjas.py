from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = DATABASE = 'dojos_and_ninja_schema_db'

class Ninja:  
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# Now we use class methods to query our database

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        ninjas_id = connectToMySQL(DATABASE).query_db(query,data)

# returns the id number of the new room created

        return ninjas_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)

        if results :
            ninjas = []
            for user in results:
                ninjas.append(cls(user))
            return ninjas
        return []

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = "SELECT * FROM ninjas WHERE id = %(id)s;" # -> () || False
        result = connectToMySQL(DATABASE).query_db(query,data) # returns us a list of dictionary
        if result:
            return cls(result[0])
        return False

    @classmethod
    def update_one(cls, data):
        pass
    # don't forget to pass data into the query.db(query,data)

    @classmethod
    def delete_one(cls, data):
        pass
        # don't forget to pass data into the query.db(query,data)