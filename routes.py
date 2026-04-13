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
        plataformas_game = [p.strip() for p in game.plataforma.split(",")]
        generos_game = [g.strip() for g in game.genero.split(",")]
        
        
        if any(p.strip() in plataformas_game for p in user_platform):
            game_score += 1

        for genre in user_preferences:
            if genre.strip() in generos_game:
                game_score += 2

        if game_score > 0 :
            recomendations.append({
                "name":game.nome,
                "score":game_score
            })

    recomendations.sort(key=lambda x : x["score"],reverse=True)

    return jsonify(recomendations[:5])

        



            

            
            
            
            


    

    
