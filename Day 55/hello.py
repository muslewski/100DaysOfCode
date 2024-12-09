from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>  "


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye, World!"


@app.route("/user/<path:name>")
def greet(name):
    return 'Hello, ' + name + '!'


if __name__ == "__main__":
    app.run(debug=True)
