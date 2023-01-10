from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ =  'users' 
