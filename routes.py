from flask import jsonify,request,Blueprint
from games import games

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
    user_platform = user_preferences.get("platform")

    for game in games:
        game_score = 0

        for genre in user_genres:
            if genre in game["genres"]:
                game_score +=2
            

        if user_platform == game["platform"]:
            game_score += 1

        if game_score > 0:
            results.append({
              "game":game,
              "score":game_score
         })

    results.sort(key=lambda x: x["score"], reverse=True)

    return jsonify(results)
            
            
            
            


    

    
