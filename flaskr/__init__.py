import os
from flask import Flask, render_template
from flaskr.database import init_db
from dotenv import load_dotenv

def create_app(test_config=None):
    load_dotenv(override=True)
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    init_db(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import profile
    app.register_blueprint(profile.bp)
    
    from . import users
    app.register_blueprint(users.bp)
    app.add_url_rule('/', endpoint='index')

    from . import houi
    app.register_blueprint(houi.bp)

    return app