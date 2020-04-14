from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = './app/static/uploads'

app = Flask(__name__)

app.config['SECRET_KEY'] = "h24rfchHUW9iHBu00ih8HHJ9gfes8rd6RYFKDODRTC76R"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jcvnexqcvcycqr:482a675fec7f179a5c41d7107046f1cb55efbd91a10e5799d5aac19673f47341@ec2-54-210-128-153.compute-1.amazonaws.com:5432/detrhaqimcsahi"

# postgresql://project1:project1@localhost/project1"
#postgresql://rhpdiandwrgjnj:aae5cd2e861ef24cac08418b6d756f6da365684aeaa62ac3c09b03c9f1ed92e8@ec2-3-223-21-106.compute-1.amazonaws.com:5432/d5ilnvsieien5g"
 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # added just to suppress a warning

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views, models
