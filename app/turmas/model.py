from app.extensions import db
from app.association import association_table


class Turma(db.Model):
    __tablename__ = 'turma'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20),nullable=False)
    turno = db.Column(db.String(20),nullable=False)

    #materia_id = db.Column(db.Integer,db.ForeignKey('materia.id'))

    #aluno = db.relationship("Aluno", secondary=association_table, back_populates="turma")

