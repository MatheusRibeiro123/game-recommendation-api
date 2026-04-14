from flask import jsonify,request,Blueprint
from database import db
from models.games import Game

rec_bp = Blueprint("recommendations",__name__)

#rota principal, recomendar game
@rec_bp.route("/recommend", methods= ["POST"])
def recomendar_game():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    user_preferences = data.get("genero",[])
    user_platform = data.get("plataforma",[])

    if isinstance(user_preferences, str):
        user_preferences = [user_preferences]

    if isinstance(user_platform, str):
        user_platform = [user_platform]

    games = Game.query.all()
    recommendations = []

    for game in games:
        game_score = 0
        plataformas_game = [p.strip() for p in (game.plataforma or "").split(",")]
        generos_game = [g.strip() for g in (game.genero or "").split(",")]
        
        
        if any(p.strip().lower() in [pg.lower() for pg in plataformas_game] for p in user_platform):
            game_score += 1

        for genre in user_preferences:
            if genre.strip() in generos_game:
                game_score += 2

        if game_score > 0 :
            recommendations.append({
                "name":game.nome,
                "score":game_score
            })

    recommendations.sort(key=lambda x : x["score"],reverse=True)

    return jsonify(recommendations[:5])

#rota criar game
@rec_bp.route("/games",methods = ["POST"])
def criar_game():
    dados = request.get_json()

    if not dados:
        return jsonify({"error":"Dados do game não enviados"}),400
    
    nome = dados.get("nome")
    genero = dados.get("genero")
    plataforma = dados.get("plataforma")

    if not nome or not nome.strip() or not genero or not plataforma:
        return jsonify({"error": "Campos obrigatórios faltando"}), 400    
    
    game = Game(
        nome = nome,
        genero = genero,
        plataforma = plataforma
    )

    db.session.add(game)
    db.session.commit()

    return jsonify(game.to_dict()) , 201



#rota listar games
@rec_bp.route("/games", methods = ["GET"])
def listar_games():
    games = Game.query.all()
    lista_games = [game.to_dict() for game in games]

    return jsonify(lista_games),200

#rota listar game
@rec_bp.route("/games/<int:id>", methods = ["GET"])
def listar_game(id):

    game = Game.query.get_or_404(id)
    
    return jsonify(game.to_dict()),200

#rota editar game

@rec_bp.route("/games/<int:id>", methods = ["PUT"])
def editar_game(id):

    game = Game.query.get_or_404(id)
    
    dados = request.get_json()

    if not dados:
        return jsonify({"error":"Dados do game não enviados!"}),400

    game.nome = dados.get("nome",game.nome)
    game.genero = dados.get("genero",game.genero)
    game.plataforma = dados.get("plataforma",game.plataforma)

    db.session.commit()

    return jsonify(game.to_dict()),200

#rota apagar game
@rec_bp.route("/games/<int:id>", methods = ["DELETE"])
def remover_game(id):

    game = Game.query.get_or_404(id)
    
    db.session.delete(game)
    db.session.commit()

    return jsonify({"mensagem":"Jogo deletado com sucesso"}),200
