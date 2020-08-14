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
    return redirect(url_for('index'))
# Nibras Work below (Update + Delete)