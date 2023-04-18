import functools
from flaskr.database import db

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None

        if not email:
            error = 'メールアドレスが必要です'
        elif not password:
            error = 'パスワードが必要です'
        
        if error is None:
            try:
                user = User(email, generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
            except:
                error = f"メールアドレス {email} は登録できませんでした"
            else:
                return redirect(url_for("auth.login"))
        
        flash(error)
    
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        user = User.query.filter(User.email == email).first()

        if user is None:
            error = 'メールアドレスが違います'
        elif not check_password_hash(user.password, password):
            error = 'パスワードが違います'
        
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('profile.index'))
        
        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter(User.id == user_id).first()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view