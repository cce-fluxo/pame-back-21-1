from sqlalchemy.orm import backref
from app.extensions import db
#from app.association import association_table

class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20),nullable=False)
    dre = db.Column(db.Integer,nullable=False)
    email = db.Column(db.String(100), unique=True)

    #turma = db.relationship("Turma", secondary=association_table, back_populates="aluno")

    def json(self):
        {'nome':self.nome,
         'dre': self.dre, 
         'email': self.email
        }

