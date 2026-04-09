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

@rec_bp.route("/recommend/v2", methods= ["POST"])
def recomendar_game_2():
    data = request.get_json()

    user_preferences = data.get("genres",[])
    user_platform = data.get("platform")

    recomendations = []

    for game in games:
        game_score= 0

        for genre in user_preferences:
            if genre in game["genres"]:
                game_score += 2

        if user_platform == game["platform"]:
            game_score += 1

        if game_score>0:
            recomendations.append({"name":game["name"],
                                  "score":game_score})

    recomendations.sort(key=lambda x:x["score"], reverse=True)

    return jsonify(recomendations)



            

            
            
            
            


    

    
