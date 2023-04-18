from flaskr.database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100), nullable=False)
    profile = db.Column(db.String(500), nullable=True)

    def __init__(self, email=None, password=None, profile=None):
        self.email = email
        self.password = password
        self.profile = profile
    
    def __repr__(self):
        return f'<User {self.email!r}>'