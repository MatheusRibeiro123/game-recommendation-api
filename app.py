from flask import Flask 
from routes import rec_bp
from models.games import Game
from database import db


app = Flask(__name__)
app.register_blueprint(rec_bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run(debug=True)
