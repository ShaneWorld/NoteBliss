from app.edit import bp3
from app.extensions import login_required, db
from app.edit.forms import WriteForm
from flask import render_template, request, session, redirect, url_for
from app.models.notes import Notes
import markdown

@bp3.route("/write/", methods = ["GET", "POST"])
@login_required
def write():
    
    # Create form
    form = WriteForm()

    if request.method == "POST":
        
        # Get markdown text and title
        markdown_text = form.edit.data
        title = form.title.data
        
        # Convert markdown text to html
        html_text = markdown.markdown(markdown_text)
        
        # Add to database
        note = Notes(session["user_id"], markdown_text, title, html_text)
        db.session.add(note)
        db.session.commit()
        
        return redirect(url_for('main.index'))


    else:
        return render_template('write.html', form = form)
