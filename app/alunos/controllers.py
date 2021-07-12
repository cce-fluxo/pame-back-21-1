from app.alunos.model import Aluno
from flask import request, jsonify, render_template
from flask.views import MethodView
from app.extensions import db, mail
from flask_mail import Message

class AlunosCreate(MethodView): #/aluno/create
    def get(self):
        aluno = Aluno.query.all()
        return jsonify([aluno.json() for aluno in aluno]), 200

    def post(self):
        dados = request.json 

        nome = dados.get('nome')
        dre = dados.get('dre')
        email = dados.get('email')

        if not isinstance(nome,str) or not isinstance (dre, int):
            return {'error':'tipo invalido'}
        
        aluno = Aluno(nome=nome, dre=dre, email = email)

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
    def get(self, id):
        aluno = Aluno.query.get_or_404(id)
        return aluno.json(), 200

    def put(self, id):
        aluno = Aluno.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome') 
        dre = dados.get('dre')

        aluno.nome = nome 
        aluno.dre = dre

        db.session.commit()

        return aluno.json(), 200

    def patch(self, id): 
        aluno = Aluno.query.get_or_404(id)
        dados = request.json

        nome = dados.get('nome', aluno.nome) 
        dre = dados.get('dre', aluno.dre)

        aluno.nome = nome
        aluno.dre = dre

        db.session.commit()

        return aluno.json(), 200


    def delete(self, id):
        aluno = Aluno.query.get_or_404(id)
        db.session.delete(aluno)
        db.session.commit()
        return aluno.json(), 200





    

    

    









