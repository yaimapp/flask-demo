
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.models import User
from flaskr.auth import login_required
from flaskr.database import db

bp = Blueprint('users', __name__)

@bp.route('/users')
@login_required
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)