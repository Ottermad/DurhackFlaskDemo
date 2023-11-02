from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/another")
def another_route():
    return "Another Route 2"


@app.route("/template-example")
def template_example():
    return render_template('hello.html')


@app.route("/json-example")
def json_example():
    return {
        "hello": "world"
    }
