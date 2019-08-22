from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # 'Post' can be provided as a string with the class name if the model is defined later in the module.
    # The backref argument defines the name of a field that will be added to the objects of the "many" class that points back at the "one" object.
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # note that I did not include the () after utcnow, so I'm passing the function itself, and not the result of calling it
    # In general, you will want to work with UTC dates and times in a server application.
    # This ensures that you are using uniform timestamps regardless of where the users are located.
    # These timestamps will be converted to the user's local time when they are displayed.
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # It is an unfortunate inconsistency that in some instances such as in a db.relationship() call, the model is referenced by the model class, which typically starts with an uppercase character, while in other cases such as this db.ForeignKey() declaration, a model is given by its database table name, for which SQLAlchemy automatically uses lowercase characters and, for multi-word model names, snake case.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.body}>'