from flask import Flask
from app.extensions import db
from app.extensions import migrate
from app.config import Config
from app.alunos.routes import aluno_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(aluno_api)
    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(aluno_api)
    
    return app