from flask.helpers import url_for
from werkzeug.utils import redirect
from app.auth import login
from app.models import User
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name.split()[0])  #split para buscar somente o primeiro nome do nome completo


@main.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    
    if request.method == 'POST':

        user = User.query.filter_by(id=current_user.id).first()
        user.email = request.form['email']
        db.session.commit()
        
        return redirect(url_for('main.profile'))
    
    else:
        return render_template('edit_profile.html')


@main.route('/profile/delete', methods=['GET', 'POST'])
@login_required
def delete_profile():
    
    if request.method == 'GET':
        return render_template('delete_profile.html')
    
    else:
        user = User.query.filter_by(id=current_user.id).first()
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('auth.signup'))
    