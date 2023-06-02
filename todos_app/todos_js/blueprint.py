"""
JavaScript + DOM API로 구현된 todo app을 위한 요청 처리 함수 모음
"""

from flask import Blueprint, render_template, request, abort

from ..database import get_db
from ..todo_repository import TodoRepository


blueprint = Blueprint('todos_js', __name__, template_folder='templates', url_prefix='/todos_js')


@blueprint.get('/')
def index():
    return render_template('todos_js/index.html')


@blueprint.get('/api/todos')
def list_todos():
    repo = TodoRepository(get_db())
    todos = [todo.as_dict() for todo in repo.get_todos()]
    return todos


@blueprint.post('/api/todos')
def create_todo():
    repo = TodoRepository(get_db())
    title = request.json['title'] or 'No title'
    todo = repo.create_todo(title)
    return todo.as_dict()


@blueprint.get('/api/todos/<pk>')
def get_todo(pk):
    repo = TodoRepository(get_db())
    todo = repo.get_todo(pk)
    if todo:
        return todo.as_dict()
    else:
        return abort(404)


@blueprint.delete('/api/todos/<pk>')
def delete_todo(pk):
    repo = TodoRepository(get_db())
    repo.delete_todo(pk)
    return {'ok': True}


@blueprint.post('/api/todos/<pk>/toggle')
def toggle_todo(pk):
    repo = TodoRepository(get_db())
    repo.toggle_todo(pk)
    return {'ok': True}
