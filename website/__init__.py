from flask import Flask
from flask_sqlalchemy import SQLAlchemy

Db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']="Hello World"
    app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{DB_NAME}"
    Db.init_app(app)

    return app