from flask import  request, jsonify, render_template
from flask.views import MethodView #Faz com que a classe seja vista como um método para requisição HTTP
from app.alunos.model import Aluno
from app.extensions import db, mail
from flask_mail import Message

#As rotas vão ser acessadas quando o front fizer uma requisição para o backend
#No python é mais interessante trabalhar com classes do que com funções, até por causa do quesito segurança
#e também porque ajudam a simplificar a modelagem dos dados e as ações em programas

class AlunosCreate(MethodView):      #/aluno/create
    def get(self):
        aluno = Aluno.query.all()  #Pegar todos os alunos no db (lista)
        return jsonify([aluno.json() for aluno in aluno]),200 #Os dados são retornados pelo formato de json (dicionário)

#Não podemos deixar os erros chegarem ao banco, isso demonstra uma falha de segurança

    def post(self):
        dados = request.json  #Pegar só o que tá vindo do json      
        nome = dados.get('nome')  #Função do python para ler o json e pegar o comapo nome
        dre = dados.get('dre')
        email= dados.get('email')

        if Aluno.query.filter_by(dre=dre).first():
            return {'error': 'Aluno já cadastrado'}

        if not isinstance(nome, str) or not isinstance (dre, int) or not isinstance(email,str):
            return {"error" : "Algum tipo invalido"}, 400
        
        aluno = Aluno(nome = nome, dre = dre, email=email) #colocar aluno em uma variável e passar os atributos (cria o objeto aluno)

        db.session.add(aluno) #Abrindo uma seção no bd para adicionar um aluno
        db.session.commit()   #Salva no bd

        msg = Message(sender='camilamaia@poli.ufrj.br',
                      recipients= [email.html],
                      subject= 'Bem-vindo!', 
                      html = render_template('email.html', nome=aluno.nome)) #Quem vai receber o email
        mail.send(msg)

        return aluno.json() , 200 #retornando para o front os valores que estão no model
        
 #quem vai enviar o email -> Depois devem ir no Send Atentication para configurar o email que pode aparecer no sender
#SendGrid-> Email Api -> Integration Guide -> SMTP (Protocolo de comunicação por email)

class AlunosDetails(MethodView):      #/aluno/details/<int:id>
    def get(self,id):
        aluno = Aluno.query.get_or_404(id)
        return aluno.json(),200

    def put(self,id):
        aluno = Aluno.query.get_or_404(id)
        dados = request.json             
        nome = dados.get('nome')
        dre = dados.get('dre')
        
        aluno.nome = nome
        aluno.dre = dre
        
        db.session.commit() #Salva no bd
        return aluno.json() , 200

    def patch(self,id):
        aluno = Aluno.query.get_or_404(id)
        dados = request.json        

        nome = dados.get('nome', aluno.nome) #Se ele não encontrar o nome, ele recebe a variável nome do aluno
        dre = dados.get('dre', aluno.dre)

        aluno.nome = nome #Trocando os dados
        aluno.dre = dre

        db.session.commit() #Salva no bd
        return aluno.json() , 200

    def delete(self,id):
        aluno = Aluno.query.get_or_404(id)
        db.session.delete(aluno)
        db.session.commit()
        return aluno.json(), 200




