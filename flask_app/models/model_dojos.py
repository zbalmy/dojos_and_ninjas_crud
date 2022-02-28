from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninjas

DATABASE = 'dojos_and_ninja_schema_db'

class Dojo:  
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

# Now we use class methods to query our database

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojos_id = connectToMySQL(DATABASE).query_db(query,data)

# returns the id number of the new room created

        return dojos_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)

        if results :
            dojos = []
            for user in results:
                dojos.append(cls(user))
            return dojos
        return []

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = "SELECT * FROM dojos WHERE id = %(id)s;" # -> () || False
        result = connectToMySQL(DATABASE).query_db(query,data) # returns us a list of dictionary
        if result:
            return cls(result[0])
        return False

    # @classmethod
    # def get_one_with_ninjas(cls, data:dict) -> object:
    #     query = "SELECT * FROM ninjas RIGHT JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;" # -> () || False
    #     results = connectToMySQL(DATABASE).query_db(query,data) # returns us a list of dictionary
    #     dojo= cls(results[0])
    #     print(results)
    #     if results[0]['id'] != None:
    #         for ninja in results:
    #             ninja_data = {'id': ninja['id'],
    #                         'first_name': ninja['first_name'],
    #                         'last_name': ninja['last_name'],
    #                         'age': ninja['age'],
    #                         'created_at': ninja['created_at'],
    #                         'updated_at': ninja['updated_at'],
    #                         'dojo_id': ninja['dojo_id']}
    #             dojo.ninjas.append(model_ninjas.Ninja(ninja_data))
    #     return dojo

    @classmethod
    def get_one_with_ninjas(cls, data:dict) -> object:
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;" # -> () || False
        results = connectToMySQL(DATABASE).query_db(query,data) # returns us a list of dictionary
        dojo= cls(results[0])
        print(results)
        dojo.ninjas = []
        if results:
            for row_from_db in results:
                ninja_data = {
                    **row_from_db,
                    'id':row_from_db['ninjas.id'],
                    'created_at':row_from_db['ninjas.created_at'],
                    'updated_at':row_from_db['ninjas.updated_at']
                }
                dojo.ninjas.append(model_ninjas.Ninja(ninja_data))
        return dojo


    @classmethod
    def update_one(cls, data):
        pass
    # don't forget to pass data into the query.db(query,data)

    @classmethod
    def delete_one(cls, data):
        pass
        # don't forget to pass data into the query.db(query,data)