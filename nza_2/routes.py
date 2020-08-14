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
@app.route('/notes/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def note_update(note_id):
    note = Note.query.get_or_404(note_id)
    update_form = NoteForm()

    if request.method == 'NOTE' and update_form.validate():
        case = update_form.case.data
        case_notes = update_form.content.data
        user_id = current_user.id
        # Update case with case notes info
        note.case = case
        note.case_notes = case_notes
        note.user_id = user_id

        # Commit change to db
        db.session.commit()
        return redirect(url_for('note_update', note_id=note.id))

    return render_template('note_update.html', update_form=update_form)


@app.route('/posts/delete/<int:note_id>', methods=['POST'])
@login_required
def note_delete(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('home'))