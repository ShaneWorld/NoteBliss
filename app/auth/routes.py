from flask import render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from app.auth import bp2
from app.extensions import db, login_required
from app.models.auth import Users
from app.auth.forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash 


@bp2.route('/login/', methods = ["GET", "POST"])
def login():

    # Forget any user id
    session.clear()

    # link form
    form = LoginForm()

    if request.method == "POST" and form.validate():

        # Get the user input
        username = form.username.data
        password = form.password.data

        # retrieve username
        user = Users.query.filter(Users.username == username).first()

        # Condition1: Username does not exist
        if not user:
            flash('Username does not exist!', 'error')
            return render_template('login.html', form = form)
        
        # Condition2: Password is incorrect
        if check_password_hash(user.hash, password):
            session["user_id"] = user.id
            return redirect(url_for('main.index'))
        else:
            flash('Password is incorrect. Please try again.', 'error')
            return render_template('login.html', form = form)
        
    else:
        return render_template('login.html', form = form)


@bp2.route('/register/', methods = ["GET", "POST"])
def register():
    
    # Link form
    form = RegisterForm()

    if request.method == "POST" and form.validate():

        # Get user info
        username = form.username.data
        password = form.password.data

        # Hash the password
        hash = generate_password_hash(password)
        user = Users(username, hash)

        # Add info to database
        db.session.add(user)
        db.session.commit()
        
        return redirect('/login')

    else:
        return render_template('register.html', form = form)


@bp2.route('/logout/')
@login_required
def logout():
    
    # Forget any user id
    session.clear()
    
    return redirect('/')


@bp2.route('/delete/')
@login_required
def delete():

    # Delete the user form database
    Users.query.filter(Users.id == session["user_id"]).delete()
    db.session.commit()

    # Forget any user id
    session.clear()

    return redirect('/login')

    
@bp2.route('/account/')
@login_required
def account():
    user = Users.query.filter(Users.id == session["user_id"]).first()
    return render_template('account.html', user = user)
