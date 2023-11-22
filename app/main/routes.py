from flask import render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy
from app.main import bp1
from app.extensions import login_required, db
from app.models.notes import Notes

@bp1.route("/")
@login_required
def index():
    notes = Notes.query.filter(Notes.user_id == session["user_id"]).all()
    return render_template('index.html', notes = notes)
    
@bp1.route('/preview/<int:id>')
@login_required
def preview(id):
    note = Notes.query.filter(Notes.id == id).first()
    return render_template('preview.html', note = note)

@bp1.route('/delnotes/<int:id>')
@login_required
def delnotes(id):
    Notes.query.filter(Notes.id == id).delete()
    db.session.commit()
    return redirect('/')
