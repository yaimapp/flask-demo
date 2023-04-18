from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.models import User
from flaskr.auth import login_required
from flaskr.database import db

bp = Blueprint('profile', __name__)

@bp.route('/profile')
@login_required
def index():
    user_id = g.user.id
    user = get_user(user_id)
    return render_template('profile/index.html', user=user)

@bp.route('/profile/update', methods=('GET', 'POST'))
@login_required
def update():
    user_id = g.user.id
    user = get_user(user_id)

    if request.method == 'POST':
        profile = request.form['profile']
        error = None

        if not profile:
            error = 'プロフィールを入力してください'

        if error is not None:
            flash(error)
        else:
            user.profile = profile
            db.session.commit()
            return redirect(url_for('profile.index'))

    return render_template('profile/update.html', user=user)

def get_user(id):
    user = User.query.filter(User.id == id).first()

    if user is None:
        abort(404, f"ユーザーが見つかりませんでした")

    return user