from flask import Flask
from app.db import Base, engine
from app.api import rule, event, user


app = Flask(__name__)

# @app.route("/")
#def hello_world():
#    return "Hello, World!"

# Create Blueprints
app.register_blueprint(rule)
app.register_blueprint(event)
app.register_blueprint(user)

# Create tables
Base.metadata.create_all(engine)
