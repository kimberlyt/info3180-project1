from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class ProfileForm(FlaskForm):
 firstname = StringField('First Name', validators=[DataRequired()])
 lastname = StringField('Last Name', validators=[DataRequired()])
 gender = SelectField('Gender', validators=[DataRequired()], choices=[('NAN','Select a gender'), ('Female','Female'), ('Male', 'Male')])
 email = StringField('Email', validators=[DataRequired(), Email()])
 location = StringField('Location', validators=[DataRequired()])
 biography = TextAreaField('Biography') 
 
class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[ FileRequired(), 
        FileAllowed(['jpg', 'png','Images Only!'])
    ])

