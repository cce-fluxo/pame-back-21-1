from flask import Flask
from app.extensions import db, mail
from app.extensions import migrate
from app.config import Config
from app.alunos.routes import aluno_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)

    app.register_blueprint(aluno_api)

    return app