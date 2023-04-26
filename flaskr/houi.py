from flask import (
    Blueprint, render_template, request
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required

import subprocess

bp = Blueprint('houi', __name__)

@bp.route('/houi', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
        star = request.form['star']
        ymd = request.form['ymd']
        error = None

        if not star:
            error = '本命星が必要です'
        elif not ymd:
            error = '日付が必要です'

        if error is None:
            result = subprocess.run(['./houi/houi', star, ymd.replace('/', '')], capture_output=True, text=True)
            return render_template('houi/index.html', result=result.stdout, )

    return render_template('houi/index.html')
