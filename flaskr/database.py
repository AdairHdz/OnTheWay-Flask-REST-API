from flask_sqlalchemy import SQLAlchemy
from app import app
from decouple import config

database_username = config("DB_USER")
database_password = config("DB_PASSWORD")
database_host = config("DB_HOST")
database_port = config("DB_PORT")
database_name = config("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}:{}/{}".format(database_username, database_password, database_host, database_port, database_name)

database = SQLAlchemy(app)

class User(database.Model):    
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)        

    def __repr__(self):
        return '<User %r>' % self.username

