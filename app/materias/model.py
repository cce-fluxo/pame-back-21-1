from app.extensions import db

class Materia(db.Model):
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20),nullable=False)
    
    #turmas = db.relationship('Turma',backref='materia')

    