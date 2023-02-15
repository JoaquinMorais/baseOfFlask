from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes.home import Home

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:c3koV2O5uaUGyYFIskBa@containers-us-west-78.railway.app:6912/railway"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


SQLAlchemy(app)

app.register_blueprint(Home)


