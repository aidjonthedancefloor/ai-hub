"""Root module for the REST API."""

from flask import Flask
from rest.v1 import v1
from rest.streamed import streamed

app = Flask(__name__)
app.register_blueprint(v1)
app.register_blueprint(streamed)