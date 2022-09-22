#se importa el app
from flask_crud_mvc import app
#se importa el modelo que contiene la clase
from flask_crud_mvc.models.user import User
#se importa las funciones de flask
from flask import  render_template, redirect, request, session, flash
#se importan el modulo de fechas
from datetime import datetime


@app.route("/limpiar")
def limpiar():
    session.clear()
    flash("se limpio la session","info")
    return redirect("/")

#Funcion para obtener los registros de todos los usuarios
# obtiene todos los usuarios y las devuelve en una lista de objetos de usuarios
@app.route('/')
def usuarios():
  return render_template('index.html',usuarios=User.get_all())

#Funcion para insertar un nuevo usuario
# se llama al formulario para insertar
@app.route('/insertar')
def usuarios_insertar():
   return render_template("form_insertar.html")

#Funcion para obtener el registro de un usuario segun id
# Devuelve los datos para el menu mostrar
@app.route('/mostrar/<int:id>')
def usuarios_mostrar(id):
   return render_template("form_mostrar.html", usuario=User.get_by_id(id))

#Funcion para obtener el registro de un usuario segun id
# Devuelve los datos para el menu editar
@app.route('/editar/<int:id>')
def usuarios_editar(id):
   return render_template("form_editar.html", usuario=User.get_by_id(id))


#Funcion para crear un usario en la db con los datos que vienen de un formulario
@app.route('/crear',methods=['POST'])
def usuarios_crear():
	data = {
        	"first_name" : request.form['nombre_usuario'],
        	"last_name" : request.form['apellido_usuario'],
        	"email" : request.form['email_usuario'],
	}
	User.save(data)
	flash(f"Exito al crear el usuario {data['first_name']}","success")
	return redirect('/limpiar')


#Funcion para editar un usario en la db con los datos que vienen de un formulario
@app.route("/actualizar/<id>", methods=["POST"])
def usuarios_actualizar(id):
  data = {
        	"first_name" : request.form['nombre_usuario'],
        	"last_name" : request.form['apellido_usuario'],
         	"email" : request.form['email_usuario'],
     	    'id' : id
    }

  resultado = User.update(data)

  if resultado == False:
      flash(f"Error al actualizar el usuario {data['first_name']}","error")
  else:
      flash(f"Exito al actualizar el usuario {data['first_name']}","success")

  return redirect("/limpiar")

#Funcion para eliminar un usuario en la base de datos
@app.route('/eliminar/<int:id>')
def usuarios_eliminar(id):

  #se graba en el el objeto de la clase Userscr
  User.delete(id)

  flash(f"Exito al eliminar el usuario","success")

  return redirect('/limpiar')