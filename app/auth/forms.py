from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[InputRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField(label='Password', validators=[InputRequired()], render_kw={'placeholder': 'Password'})
    login = SubmitField(label='Sign in')
    

class RegisterForm(FlaskForm):
    username = StringField(label='username', validators=[InputRequired(), Length(max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField(label='password', validators=[InputRequired()], render_kw={'placeholder': 'Password'})
    confirm = PasswordField(label='confirm', validators=[InputRequired(), EqualTo('password')], render_kw={'placeholder': 'Confirm password'})
    register = SubmitField(label='register')
