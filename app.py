from flask import Flask,request, jsonify, json
from models import db, User, Character, Location, Favorito

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

@app.route("/")
def home():
    return "Hello SQLAlchemy y Flask"

@app.route("/users", methods=["POST"])
def create_user():
    user = User()
    user.username = request.json.get("username")
    user.password = request.json.get("password")
    user.age = request.json.get("age")

    db.session.add(user)
    db.session.commit()

    return "Usuario guardado"


    
    
@app.route("/users/list", methods=["GET"])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)


@app.route("/users/favorito/<int:id>", methods=[ "GET"])
def get_oneuser(id):
    user = User.query.get(id)
    if user is not None:
       return jsonify(user.serialize())

    else:
        return jsonify("No encontrado"), 418 
    

#@app.route("/favorito/planet/<int:id>", methods=["POST"])
#def add_oneplanet(id):
    user = User.query.get(id)
    favorito = Favorito.query.filter_by(user=user.username).first()
    location = Location.query.filter_by(favorito=favorito.location).first()
    print(location)
    if user is not None:
       location.name = request.json.get("name")
       db.session.add(location)
       db.session.commit()

       return jsonify("Modificado")

    else:
        return jsonify("No encontrado"), 418     
   




@app.route("/users/<int:id>", methods=["PUT", "DELETE"])
def update_user(id):
    user = User.query.get(id)
    if user is not None:
        if request.method == "DELETE":
            db.session.delete(user)
            db.session.commit()

            return jsonify("Eliminado"), 204
        else:
            user.age = request.json.get("age")
            user.name =request.json.get("name")
            user.password = request.json.get("password")
            db.session.commit()
            
            return jsonify("Usuario actualizado"), 200
    
    return jsonify("Usuario no encontrado"), 418


## personajes

@app.route("/add/character", methods=["POST"])
def add_people():
    character = Character()
    character.name = request.json.get("name")
    character.status = request.json.get("status")
    character.species = request.json.get("species")
    character.gender = request.json.get("gender")
   
   
    db.session.add(character)
    db.session.commit()

    return "Personaje guardado"



@app.route("/character/list", methods=["GET"])  
def get_characters():
    characters = Character.query.all()
    result = []
    for character in characters:
        result.append(character.serialize())
    return jsonify(result)

@app.route("/character/<int:id>", methods=["GET"])
def get_onecharacter(id):
    character = Character.query.get(id)
    if character is not None:
       return jsonify(character.serialize())

    else:
        return jsonify("No encontrado"), 418   



@app.route("/character/<int:id>", methods=["PUT", "DELETE"])
def update_character(id):
    character = Character.query.get(id)
    if character is not None:
        if request.method == "DELETE":
            db.session.delete(character)
            db.session.commit()

            return jsonify("Eliminado"), 204
        else:
            character.name = request.json.get("name")
            character.status = request.json.get("status")
            character.species = request.json.get("species")
            character.gender = request.json.get("gender")
            
            db.session.commit()
            
            return jsonify("Personaje actualizado"), 200
    
    return jsonify("Personaje no encontrado"), 418




 ## Location



@app.route("/add/location", methods=["POST"])
def add_location():
    location = Location()
    location.name = request.json.get("name")
    location.dimension = request.json.get("dimension")
    location.residents = request.json.get("residents")
  
   
    db.session.add(location)
    db.session.commit()

    return "Locacion guardado"


@app.route("/location/<int:id>", methods=["GET"])
def get_onelocation(id):
    location = Location.query.get(id)
    if location is not None:
       return jsonify(location.serialize())

    else:
        return jsonify("No encontrado"), 418  
    

@app.route("/location/list", methods=["GET"])  
def get_locations():
    locations = Location.query.all()
    result = []
    for location in locations:
        result.append(location.serialize())
    return jsonify(result)



@app.route("/location/<int:id>", methods=["PUT", "DELETE"])
def update_location(id):
    location = Location.query.get(id)
    if location is not None:
        if request.method == "DELETE":
            db.session.delete(location)
            db.session.commit()

            return jsonify("Eliminado"), 204
        else:
            location.name = request.json.get("name"),
            location.dimension = request.json.get("dimension"),
            location.residents = request.json.get("residents")
            
            db.session.commit()
            
            return jsonify("locacion actualizado"), 200
    
    return jsonify("Locacion no encontrado"), 418   

##  Favoritos


@app.route("/add/favorite", methods=["POST"])
def add_favorite():
    favorito = Favorito()
    favorito.user = request.json.get("user")
    favorito.character = request.json.get("character")
    favorito.location = request.json.get("location")
  
   
    db.session.add(favorito)
    db.session.commit()

    return "Favorito guardado"


@app.route("/favorito/<int:id>", methods=["GET"])
def get_onefavorito(id):
    favorito = Favorito.query.get(id)
    if favorito is not None:
       return jsonify(favorito.serialize())

    else:
        return jsonify("No encontrado"), 418  
    

@app.route("/favorito/list", methods=["GET"])  
def get_favoritos():
    favoritos = favorito.query.all()
    result = []
    for favorito in favoritos:
        result.append(favorito.serialize())
    return jsonify(result)



@app.route("/favorito/<int:id>", methods=["PUT", "DELETE"])
def update_favorito(id):
    favorito = Favorito.query.get(id)
    if favorito is not None:
        if request.method == "DELETE":
            db.session.delete(favorito)
            db.session.commit()

            return jsonify("Eliminado"), 204
        else:
            
            favorito.user = request.json.get("user"),
            favorito.character = request.json.get("character"),
            favorito.location = request.json.get("location")
  
            
            db.session.commit()
            
            return jsonify("Favorito actualizado"), 200
    
    return jsonify("Favorito no encontrado"), 418

with app.app_context():
    db.create_all()


app.run(host="localhost", port="5050")