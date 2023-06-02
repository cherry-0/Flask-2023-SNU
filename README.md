# 웹 어플리케이션 동작 원리 특강

본 저장소는 웹 어플리케이션 동작 원리를 전달하고자 간단한 할 일 관리 어플리케이션을 두 가지 방법으로 구현해놓은 코드를 포함하고 있습니다.

작은 기능을 추가해보는 활동을 통해, 많은 코드 중 각 부분들의 역할 및 실행 위치, 실행 시점등을 이해하는 것을 목표로 합니다.

# 파일 및 폴더 설명

- `todos_app/__init__.py`
    - Flask app 정의
- `todos_app/database.py`
    - 데이터베이스 연결 및 초기화
- `todos_app/todo_repository.py`
    - 데이터베이스의 todos 테이블에 접근
- `todos_app/todo.py`
    - 할 일 항목을 나타내는 클래스
- `todos_app/todos_html/blueprint.py`
    - HTML 내장 기능만 활용해서 할 일 관리 어플리케이션을 구현
    - 템플릿 위치: `todos_app/templates/todos_html/`
- `todos_app/todos_js/blueprint.py`
    - JavaScript, DOM API를 활용해서 할 일 관리 어플리케이션을 구현
    - 템플릿 위치: `todos_app/templates/todos_js/`


# 실행 방법

GitHub Codespaces 실행 시 자동으로 서버가 실행되고 브라우저 창이 뜨면서 웹사이트에 접속됩니다.

직접 서버를 실행시키고 싶으시면, 아래 명령을 GitHub Codespaces 터미널에서 실행해주세요.

```
flask --debug run
```

- 터미널에 308 상태코드가 출력되며 페이지에 접속되지 않는 경우, 주소 끝에 슬래시(/)를 붙여주세요. [관련 StackOverflow 글](https://stackoverflow.com/questions/61954538/308-redirect-when-using-post-to-upload-a-file-to-flask-application)

# 참고 자료

- [GitHub Codespaces Flask template](https://github.com/github/codespaces-flask)
- [Flask 공식 문서](https://flask.palletsprojects.com/en/2.3.x/patterns/javascript/)
