from flask_app import app
from flask_app.controllers import controller_dojos, controller_ninjas

# this needs to be at the bottom of the file 
if __name__=="__main__":
        app.run(debug=True)