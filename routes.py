from flask import jsonify,request,Blueprint
from app import games

rec_bp = Blueprint("recommendations",__name__)

@rec_bp.route("/games", methods = ["GET"])
def listar_games():
    return jsonify(games)

@rec_bp.route("/recommend", methods=["POST"])
def recomentar_game():
    user_preferences = request.get_json()

    if not user_preferences:
        return jsonify({"Erro":"Dados não enviados"})
    
    results = []

    user_genres = user_preferences.get("genres",[])

    for game in games:
        for genre in user_genres:
            if genre in game["genres"]:
                results.append(game)

    return jsonify(results)


    

    
