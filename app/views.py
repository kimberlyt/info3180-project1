"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
import datetime, os, time
from werkzeug.utils import secure_filename
from .models import Profiles
from .forms import ProfileForm, PhotoForm
###
# Routing for your application.
###
def format_date_joined():
    now = datetime.datetime.now() # today's date
    date_joined = datetime.date(now.year, now.month, now.day) # a specific date
    ## Format the date to return only month and year date
    return  "Joined on " + date_joined.strftime("%B %d, %Y") 

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Kimberly Taylor")

@app.route('/profiles')
def profiles():
    list=[]
    profile = Profiles.query.all()
    filenames = get_uploaded_images()

    return render_template('profiles.html', profile=profile, filenames=filenames)

def get_uploaded_images():
    list = []
    rootdir = os.getcwd()
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            list.append(os.path.join( file))

        return list[1:]

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_profile = ProfileForm()
    photoform = PhotoForm()

    if request.method == 'POST'and user_profile.validate_on_submit():
        if request.method == 'POST' and photoform.validate_on_submit():
            

            photo = request.files['photo']
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], filename
            ))

            time_created = format_date_joined()
            firstname = user_profile.firstname.data
            lastname = user_profile.lastname.data
            gender = user_profile.gender.data
            email = user_profile.email.data
            location = user_profile.location.data
            biography = user_profile.biography.data
            picname = photo.filename

            p = Profiles(firstname = firstname, lastname = lastname, gender = gender, email = email, location = location, biography = biography, filename = picname, time_created = time_created )
            db.session.add(p)
            db.session.commit()

            flash('You have successfully filled out the form', 'success')

            return redirect(url_for('profiles'))
        

    return render_template('profile.html', form=user_profile, upload=photoform)


@app.route('/profile/<userid>', methods=['GET','POST'])
def userprofile(userid):
    user = Profiles.query.filter_by(id=userid).first()
    if request.method == 'POST':
        return render_template('individual.html', profile=user)

    elif request.method == 'GET' and user:
        return render_template('individual.html', profile=user)

    #return render_template('individual.html')

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
