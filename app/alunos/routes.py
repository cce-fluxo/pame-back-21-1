from app.alunos.controllers import AlunosCreate
from flask import Blueprint
from app.alunos.controllers import AlunosCreate, AlunosDetails, AlunoLogin

aluno_api = Blueprint('aluno_api',__name__)

aluno_api.add_url_rule(
    '/aluno/create', view_func= AlunosCreate.as_view('aluno_create'), methods=['GET', 'POST']
)

aluno_api.add_url_rule(
    '/aluno/details/<int:id>', view_func= AlunosDetails.as_view('aluno_details'), methods=['GET', 'PUT', 'PATCH', 'DELETE']
)

aluno_api.add_url_rule(
    '/aluno/login', view_func= AlunoLogin.as_view('aluno_login'), methods=['POST']
)