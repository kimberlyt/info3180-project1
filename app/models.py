from . import db

class Profiles(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(88))
    lastname = db.Column(db.String(88))
    gender = db.Column(db.String(10))
    email= db.Column(db.String(120), unique=True)
    location = db.Column(db.String(40))
    biography = db.Column(db.String(255))
    filename = db.Column(db.String(255))
    time_created = db.Column(db.String(255))


    def __init__(self, firstname, lastname, gender, email, location, biography, filename, time_created):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.filename = filename
        self.time_created = time_created

    def __repr__(self):
        return '<User %r>' %self.firstname