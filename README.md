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

# 두 가지 제작 방식의 특성 비교

## 서버 측 템플릿 언어와 HTML을 사용해서 문서를 만드는 방식

- 템플릿: HTML 중간중간에 Python 값을 넣어서 HTML 문서를 완성키기는 기능
- 템플릿으로 문서를 생성하는 Python 코드는 Python 서버에서 실행된다.
- 매 요청마다 웹 서버가 문서를 새로 생성해서 보여준다.
- 매 요청마다 문서를 새로 생성하기 때문에, 구현이 단순하다.
- 상호작용을 할 때마다 웹 브라우저 상에서 페이지 새로고침을 필요로 하기 때문에, 응답성이 나쁘다.


## JavaScript 를 활용해서 문서를 조작하는 방식

- 웹 브라우저에서 실행되는 JavaScript 를 통해 문서를 생성 및 조작하는 방식
- JavaScript 측에서 서버에 요청을 보내, 필요한 데이터를 받는다.
- 이후 DOM API를 통해 해당 데이터로부터 문서를 생성하거나 조작해서 내용을 표시한다.
- 상호작용을 할 때마다 페이지 새로고침을 할 필요가 없어서, 응답성이 좋다.
- 필요한 데이터를 받아와서, 필요한 부분만 DOM API를 통해서 조작해야 하기 때문에, 구현이 복잡하다.
