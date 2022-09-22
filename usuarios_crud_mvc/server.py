from flask_crud_mvc import app
from flask_crud_mvc.controllers import users
from flask import render_template

if __name__ == "__main__":
    app.run(debug=True)