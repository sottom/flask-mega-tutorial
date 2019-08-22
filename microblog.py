# you need to have a Python script at the top-level that defines the Flask application instance.
from app import app, db
from app.models import User, Post

# The app.shell_context_processor decorator registers the function as a shell context function. When the flask shell command runs, it will invoke this function and register the items returned by it in the shell session.
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }