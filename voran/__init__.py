from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "vorantest"}
app.config["SECRET_KEY"] = "test123whoaderp"
app.secret_key = 'development key'

db = MongoEngine(app)

import voran.routes