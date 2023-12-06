from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def user_register():
    return render_template("register.html")

@app.route('/login')
def user_login():
    return render_template("login.html")

@app.route('/register/user', methods=["POST"])
def create_user():
    # if there are errors:
    if not User.validate_user(request.form):
        return redirect('/')
    flash(" Account was created!! ",'acc_created')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "phone_number": request.form["phone_number"],
        "password": pw_hash
    }
    session['int_registered_user'] = User.save(data)
    return redirect('/login')

@app.route('/login/user', methods=['POST'])
def login():
    data = {'email': request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password",'login')
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password",'login')
        return redirect('/login')
    session['int_registered_user'] = user_in_db.id
    return redirect('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')