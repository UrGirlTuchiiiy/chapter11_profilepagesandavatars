from app import app, db
from app.models import User, Comment

# This function enables easy access to the database instance (db) and User model in the Flask shell session.
def make_shell_context():
    return dict(db=db, User=User)
