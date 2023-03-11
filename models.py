from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    favorito = db.relationship("Favorito")

    def serialize(self):
        return {
            "username": self.username,
            "id": self.id,
            "age": self.age
        }
    
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    species = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    favorito = db.relationship("Favorito")
    

    def serialize(self):
        return {
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "gender": self.gender,
            
        }


class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    dimension = db.Column(db.String(200), nullable=False)
    favorito = db.relationship("Favorito")
 
    
    def serialize(self):
        return{
            "name": self.name,
            "dimension": self.dimension,
            "residents": self.residents
        }
        


class Favorito(db.Model):
    __tablename__ = 'favorito'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30),db.ForeignKey("user.username"))
    character = db.Column(db.String(30), db.ForeignKey("character.name"))
    location = db.Column(db.String(30), db.ForeignKey("location.name"))
    
    def serialize(self):
        return{
            "user": self.user,
            "character": self.character,
            "location": self.location
        }

