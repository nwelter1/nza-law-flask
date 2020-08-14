from nza_2 import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from nza_2.forms import UserInfoForm, NoteForm, LoginForm
from nza_2.models import User, Note, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user


#Note Display route
@app.route('/notes')
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
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserInfoForm()
    if request.method =='POST' and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username, password, email)
        user = User(username, email, password)
        #Adding into database
        db.session.add(user)
        db.session.commit()
        #forming and sending welcome email via sendgrid
        msg = Message(f"Thanks for signing up, {username}!", recipients=[email])
        msg.body = ('Thanks for registering!')
        msg.html = ('<h1>Welcome to the NZA LAw site!</h1>' '<p>You can now leave case notes after logging in.</p>')


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

#  Asia work here (Login + Logout routes)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('notes'))

