from flask import Flask ,jsonify

app = Flask(__name__)

games = [
    {"name": "The Witcher 3", "genres": ["RPG", "Aventura"], "platform": "PC"},
    {"name": "FIFA 24", "genres": ["Esporte"], "platform": "PS5"} ,
    ]


if __name__ == "__main__":
    app.run(debug=True)
