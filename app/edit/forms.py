from wtforms import TextAreaField, StringField
from flask_wtf import FlaskForm

class WriteForm(FlaskForm):
    edit = TextAreaField(label="edit")
    title = StringField(label="title", render_kw={'placeholder': 'Title'}) 