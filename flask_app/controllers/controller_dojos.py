from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_dojos import Dojo


@app.route('/dojos')
def index():
  all_dojos = Dojo.get_all()
  return render_template('index.html', all_dojos=all_dojos)

# @app.route('/dojos/new')
# def new_dojos():
#   pass

@app.route('/dojos/create', methods=['POST'])
def create_dojos():
  print(request.form)
  id = Dojo.create(request.form)
  print(id)
  return redirect('/dojos')
# this is the route to create new dojo goes in the form

@app.route('/dojos/<int:id>')
def show_dojos(id):
  dojo = Dojo.get_one_with_ninjas({'id':id})
  return render_template('dojos_show.html', dojo= dojo)
 

@app.route('/dojos/<int:id>/edit')
def edit_dojos(id):
  pass

@app.route('/dojos/<int:id>/update', methods=['POST'])
def update_dojos(id):
  pass

@app.route('/dojos/<int:id>/delete')
def delete_dojos(id):
  pass