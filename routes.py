from flask import jsonify,request
from app import app,games


@app.route("/games", methods = ["GET"])
def listar_games():
    return jsonify(games)

@app.route("/recommend")
def recomentar_app():
    user_preferences = request.get_json()

    if not user_preferences:
        return jsonify({"Erro":"Dados não enviados"})
    
    results = []

    user_genres = user_preferences.get("genres",[])
    user_plataform = user_preferences.get("plataform",[])
    

    
