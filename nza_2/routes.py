from nza_2 import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from nza_2.forms import UserInfoForm, NoteForm, LoginForm
from nza_2.models import User, Note, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user


#Note Display route
@app.route('/note')
def note_display():
    notes = Note.query.all()
    return render_template("notes.html", notes=notes)

# Cindy Work here (Retrieve route)















# Nate work here (Register route)





















#  Asia work here (Login + Logout routes)













# Nibras Work below (Update + Delete)