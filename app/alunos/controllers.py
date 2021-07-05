from app.alunos.model import Aluno
from flask import request, Blueprint, jsonify
from app.extensions import db

aluno_api = Blueprint('aluno_api',__name__)

@aluno_api.route('/alunos',methods=['POST'])
def criar_aluno():
    if request.method == 'POST':
        dados = request.json
        nome = dados.get('nome')
        if not isinstance(nome,str):
            return {'error':'tipo invalido'}
        dre = dados.get('dre')
        aluno = Aluno(nome=nome,dre=dre)
        db.session.add(aluno)
        db.session.commit()

        return aluno.json(),200
    
    if request.method == 'GET':
        alunos = Aluno.query.all()
        return jsonify([aluno.json() for aluno in alunos]),200

@aluno_api.route('/alunos/<int:id>',methods=['PATCH','GET','PUT','DELETE'])
def pagina_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    if request.method == 'GET':
        return aluno.json(),200
    if request.method == 'PATCH':
        dados = request.json
    nome = dados.get('nome',aluno.nome)
    dre = dados.get('dre',aluno.dre)
    aluno.nome = nome
    aluno.dre = dre
    db.session.commit()
    return aluno.json(),200




