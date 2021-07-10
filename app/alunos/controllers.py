from flask import  request, jsonify
from flask.views import MethodView #Faz com que a classe seja vista como um método para requisição HTTP
from app.alunos.model import Aluno
from app.extensions import db
from flask_jwt_extended import create_access_token

#As rotas vão ser acessadas quando o front fizer uma requisição para o backend
#No python é mais interessante trabalhar com classes do que com funções, até por causa do quesito segurança
#e também porque ajudam a simplificar a modelagem dos dados e as ações em programas

class AlunosCreate(MethodView):      #/aluno/create
    def get(self):
        aluno = Aluno.query.all()
        return jsonify([aluno.json() for aluno in aluno]),200

    def post(self):
        dados = request.json        
        nome = dados.get('nome')
        dre = dados.get('dre')
        senha = str(dados.get('senha'))

        if Aluno.query.filter_by(dre = dre).first():
            return{"error":"CPF já cadastrado"}
        
        aluno = Aluno(nome = nome, dre = dre, senha = senha)

        db.session.add(aluno)
        db.session.commit()

        return aluno.json() , 200

class AlunosDetails(MethodView):      #/aluno/details/<int:id>
    def get(self,id):
        aluno = Aluno.query.get_or_404(id)
        return aluno.json(),200

    def put(self,id):
        aluno = Aluno.query.get_or_404(id)
        dados = request.json             
        nome = dados.get('nome')
        dre = dados.get('dre')
        senha = str(dados.get('senha'))
        
        aluno.nome = nome
        aluno.dre = dre
        aluno.senha = senha
        
        db.session.commit()
        return aluno.json() , 200

    def patch(self,id):
        aluno = Aluno.query.get_or_404(id)
        dados = request.json        

        nome = dados.get('nome', aluno.nome)
        dre = dados.get('dre', aluno.dre)
        senha = dados.get('senha', aluno.senha)

        aluno.nome = nome
        aluno.dre = dre
        aluno.senha = senha

        db.session.commit()
        return aluno.json() , 200

    def delete(self,id):
        aluno = Aluno.query.get_or_404(id)
        db.session.delete(aluno)
        db.session.commit()
        return aluno.json(), 200

class AlunoLogin(MethodView):   #/aluno/login
    def post(self):
        dados = request.json
        email = dados.get('email')
        senha = str(dados.get('senha'))
        
        aluno = Aluno.query.filter_by(email=email).first()

        if not aluno :
            return {"error":"E-mail não cadastrado"}, 400

        token = create_access_token(identity = aluno.id)

        return {"token":token}, 200




