from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)

app.config['SECRET_KEY'] = "h24rfchHUW9iHBu00ih8HHJ9gfes8rd6RYFKDODRTC76R"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # added just to suppress a warning

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views, models
