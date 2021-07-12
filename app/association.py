'''from extensions import db

association_table = db.Table('association',db.Model.metadata,
                             db.Column('turmas', db.Integer, db.ForeignKey('turma.id')),
                             db.Column('alunos', db.Integer, db.ForeignKey('aluno.id')))
'''