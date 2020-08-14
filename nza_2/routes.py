from nza_2 import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from nza_2.forms import UserInfoForm, NoteForm, LoginForm
from nza_2.models import User, Note, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user


#Note Display route
@app.route('/note')
@login_required
def note_display():
    notes = Note.query.all()
    return render_template("notes.html", notes=notes)

# Cindy Work here (Retrieve route)
@app.route('/notes/<int:note_id>')
@login_required
def note_detail(note_id):
    note = Note.query.get_or_404(note_id)  # get_or404 throws and exception if your post_id does not exist, 404 is a clinet error
    return render_template('note_detail.html',note=note)














# Nate work here (Register route)





















#  Asia work here (Login + Logout routes)













# Nibras Work below (Update + Delete)