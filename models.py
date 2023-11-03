from peewee import CharField
from playhouse.flask_utils import FlaskDB

flask_db = FlaskDB()

class Person(flask_db.Model):
    name = CharField()
