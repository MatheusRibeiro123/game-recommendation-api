from flask import Flask ,jsonify
from routes import rec_bp

app = Flask(__name__)
app.register_blueprint(rec_bp)

games = [
    {"name": "The Witcher 3", "genres": ["RPG", "Aventura"], "platform": "PC"},
    {"name": "FIFA 24", "genres": ["Esporte"], "platform": "PS5"} ,
    ]


if __name__ == "__main__":
    app.run(debug=True)
