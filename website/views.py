from flask import Blueprint,render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/')
def welcome():
    return render_template("welcome.html", user=current_user)

@login_required
@views.route('/home')
def home():
    return render_template("home.html", user=current_user)

@views.route('/review')
def review():
    if request.method == 'POST': 
        note = request.form.get('note')
    
        if len(note) < 1:
                flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note) 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("review.html", user=current_user)

@views.route('/about')
def about():
    return render_template('about.html', user=current_user)

@views.route('/contact')
def contact():
    return render_template('contact.html', user=current_user)

@views.route('/bread')
def bread():
    return render_template('bread.html', user=current_user)

@views.route('/cookies')
def cookies():
    return render_template('cookies.html', user=current_user)

@views.route('/cake')
def cake():
    return render_template('cake.html', user=current_user)

@views.route('/bread/cornbread')
def cornbread():
    return render_template('cornbread.html', user=current_user)

@views.route('/bread/basicbread')
def basicbread():
    return render_template('basicbread.html', user=current_user)

@views.route('/bread/cranberrybread')
def cranberrybread():
    return render_template('cranberrybread.html', user=current_user)

@views.route('/cookies/chocolatechipcookies')
def chocolatechipcookies():
    return render_template('chocolatechipcookies.html', user=current_user)

@views.route('/cookies/buttercookies')
def buttercookies():
    return render_template('buttercookies.html', user=current_user)

@views.route('/cookies/redvelvetcookies')
def redvelvetcookies():
    return render_template('redvelvetcookies.html', user=current_user)

@views.route('/cake/brownie')
def brownie():
    return render_template('brownie.html',user = current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

