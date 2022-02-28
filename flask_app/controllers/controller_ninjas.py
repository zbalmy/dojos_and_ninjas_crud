from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model_ninjas import Ninja
from flask_app.models.model_dojos import Dojo

@app.route('/ninjas')
def ninja_index():
  all_dojos = Dojo.get_all()
  return render_template('create.html', all_dojos=all_dojos)

@app.route('/ninjas/new')
def new_ninjas():
  pass

@app.route('/ninjas/create', methods=['POST'])
def create_ninjas():
  print(request.form)
  id = Ninja.create(request.form)
  print(id)
  return redirect('/dojos')

@app.route('/ninjas/<int:id>')
def show_ninjas(id):
  pass

@app.route('/ninjas/<int:id>/edit')
def edit_ninjas(id):
  pass

@app.route('/ninjas/<int:id>/update', methods=['POST'])
def update_ninjas(id):
  pass

@app.route('/ninjas/<int:id>/delete')
def delete_ninjas(id):
  pass