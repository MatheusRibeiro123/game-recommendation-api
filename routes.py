from flask import jsonify,request,Blueprint
from database import db
from models.games import Game

rec_bp = Blueprint("recommendations",__name__)

@rec_bp.route("/recommend", methods= ["POST"])
def recomendar_game():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    user_preferences = data.get("genres",[])
    user_platform = data.get("platform",[])

    games = Game.query.all()
    recomendations = []

    for game in games:
        game_score = 0
        if game.plataforma in user_platform:
            game_score += 1

        for genre in user_preferences:
            if genre in game.genero:
                game_score += 2

        if game_score > 0 :
            recomendations.append({
                "Game":game.nome,
                "Pontos":game_score
            })

    recomendations.sort(key=lambda x : x["Pontos"],reverse=True)

    return jsonify(recomendations[:5])

        



            

            
            
            
            


    

    
