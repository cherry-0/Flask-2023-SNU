from flask import Flask, g, render_template

from .todos_html.blueprint import blueprint as todo_html_blueprint
from .todos_js.blueprint import blueprint as todo_js_blueprint
from .database import create_tables


# Flask app (웹 서버를 대표하는 객체) 를 생성합니다.
app = Flask(__name__)

# 작성해놓은 Blueprint 를 등록합니다.
app.register_blueprint(todo_html_blueprint)
app.register_blueprint(todo_js_blueprint)

# 데이터베이스에 테이블을 생성합니다.
with app.app_context():
    create_tables()

# 홈페이지 핸들러
@app.get('/')
def index():
    return render_template('index.html')

# 매 요청이 끝날 때마다 데이터베이스 연결을 종료
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
