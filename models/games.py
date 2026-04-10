from database import db

class Game(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(100),nullable = False)
    genero = db.Column(db.String(100),nullable = False)
    plataforma = db.Column(db.String(50),nullable = False)

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "genero":self.genero,
            "plaforma":self.plataforma
        }