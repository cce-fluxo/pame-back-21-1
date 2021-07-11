'''
from app.extensions import db

association_table = db.Table('association',db.Model.metadata,
                             db.Column('turma', db.Integer, db.ForeignKey('turma.id')),
                             db.Column('aluno', db.Integer, db.ForeignKey('aluno.id')))
'''