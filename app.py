import requests
import os
from flask import Flask, render_template, request
from models import Person, flask_db

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


@app.route("/external-api")
def external_api():
    r = requests.get("http://worldtimeapi.org/api/timezone/Europe/London")
    return r.json()


@app.route("/say-hi/<name>")
def say_hi(name):
    return 'Hi {}'.format(name)


@app.route("/say-hi-again")
def say_hi_again():
    name = request.args.get('name', '')
    return 'Hi again {}'.format(name)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        return 'Hi {} {}'.format(request.form["fname"], request.form["lname"])

    return render_template('form.html')


@app.route("/form-with-db", methods=["GET", "POST"])
def form_with_db():
    if request.method == "POST":
        Person.create(name="{} {}".format(request.form["fname"], request.form["lname"]))
        return 'Hi {} {}'.format(request.form["fname"], request.form["lname"])

    return render_template('form.html')


@app.route("/list-people")
def list_people():
    people = Person.select()

    names = []
    for person in people:
        names.append(person.name)

    return names


if __name__ == '__main__':
    app.config['DATABASE'] = os.environ.get('DATBASE_URL', 'sqlite:///my_app.db')
    flask_db.init_app(app)

    flask_db.database.create_tables([Person], safe=True)
    app.run(debug=True, port=os.environ.get('PORT', 5000), host='0.0.0.0')

