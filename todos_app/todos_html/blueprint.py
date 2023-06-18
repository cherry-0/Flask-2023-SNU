"""
HTML 내장 기능만으로 동작하는 todo app을 위한 요청 처리 함수 모음
"""

from flask import Blueprint, render_template, request, redirect, url_for, abort

from ..database import get_db
from ..todo_repository import TodoRepository

blueprint = Blueprint('todos_html', __name__, template_folder='templates', url_prefix='/todos_html')


@blueprint.get('/')
def list_todos():
    repo = TodoRepository(get_db())
    todos = repo.get_todos()
    return render_template('todos_html/index.html', todos=todos)


@blueprint.post('/')
def create_todo():
    repo = TodoRepository(get_db())
    title = request.form['title'] or 'No title'
    todo = repo.create_todo(title)
    return redirect(url_for('todos_html.show_todo', pk=todo.pk))


@blueprint.get('/<pk>')
def show_todo(pk):
    repo = TodoRepository(get_db())
    todo = repo.get_todo(pk)
    if todo:
        return render_template('todos_html/todo.html', todo=todo)
    else:
        return abort(404)


@blueprint.post('/<pk>/delete')
def delete_todo(pk):
    repo = TodoRepository(get_db())
    repo.delete_todo(pk)
    return redirect(url_for('todos_html.list_todos'))


@blueprint.post('/<pk>/toggle')
def toggle_todo(pk):
    repo = TodoRepository(get_db())
    repo.toggle_todo(pk)
    return redirect(url_for('todos_html.show_todo', pk=pk))


@blueprint.post('/<pk>/update_title')
def update_todo_title(pk):
    new_title = request.form['title']

    repo = TodoRepository(get_db())
    repo.update_todo_title(pk, new_title)
    return redirect(url_for('todos_html.show_todo', pk=pk))
