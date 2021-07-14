from app.alunos.model import Aluno
from flask import request, jsonify, render_template
from flask.views import MethodView
from app.extensions import db, mail
from flask_mail import Message
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

import bcrypt

class AlunosCreate(MethodView): #/aluno/create
    def get(self):
        aluno = Aluno.query.all()
        return jsonify([aluno.json() for aluno in aluno]), 200

    def post(self):
        dados = request.json 

        nome = dados.get('nome')
        dre = dados.get('dre')
        email = dados.get('email')
        senha = dados.get('senha')

        aluno = Aluno.query.filter_by(email = email).first()

        if aluno:
            return {'error':'Email ja cadastrado'}, 400

        if not isinstance(nome,str) or not isinstance (dre, int):
            return {'error':'tipo invalido'}, 400
        
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

        aluno = Aluno(nome=nome, dre=dre, email = email, senha_hash=senha_hash)

        db.session.add(aluno)
        db.session.commit()

        msg = Message(
            sender= 'camilamaia@poli.ufrj.br',
            recipients= [email],
            subject = 'Bem-vindo!',
            html = render_template('email.html', nome= nome)
        )

        mail.send(msg)

        return aluno.json(), 200

class AlunosDetails(MethodView): #/aluno/details/<int:id>
    decorators = [jwt_required()]

    def get(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario nao permitido'}, 400

        aluno = Aluno.query.get_or_404(id)
        return aluno.json(), 200

    def put(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario nao permitido'}, 400

        aluno = Aluno.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome') 
        dre = dados.get('dre')

        aluno.nome = nome 
        aluno.dre = dre

        db.session.commit()

        return aluno.json(), 200

    def patch(self, id): 
        if (get_jwt_identity() != id):
            return {'error':'Usuario nao permitido'}, 400

        aluno = Aluno.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome', aluno.nome) 
        dre = dados.get('dre', aluno.dre)

        aluno.nome = nome
        aluno.dre = dre

        db.session.commit()

        return aluno.json(), 200


    def delete(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario nao permitido'}, 400
            
        aluno = Aluno.query.get_or_404(id)
        db.session.delete(aluno)
        db.session.commit()
        return aluno.json(), 200

class AlunoLogin(MethodView):

    def post(self):
        dados = request.json 

        email = dados.get('email')
        senha = dados.get('senha')

        aluno = Aluno.query.filter_by(email = email).first()

        if (not aluno) or (not bcrypt.checkpw(senha.encode(), aluno.senha_hash)) :
            return {'error':'Email ou Senha Invalida'}, 400

        token = create_access_token(identity = aluno.id)

        return {"token" : token } , 200







    

    

    









