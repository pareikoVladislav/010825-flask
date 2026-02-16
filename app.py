from flask import Flask

from core.app_runner import create_app


app = Flask(__name__)

create_app(app)

@app.route("/")
def index():
    return "Welcome to Community Pulse"


@app.route("/questions")
def get_all_questions():
    return "List of all questions"


if __name__ == '__main__':
    app.run()















#
# app = Flask(__name__)  # __main__ | app.py
#
# # 1. host == localhost:5000
# # localhost == 127.0.0.1
# # 2. /
# @app.route("/")
# def index():
#     return "<h1>Hello from our first application!</h1>"
#
#
# @app.route("/username/<username>")
# def greetings(username):
#     return f"Greetings, {username}"
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
