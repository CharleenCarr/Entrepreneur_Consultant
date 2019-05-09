# import necessary libraries
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#################################################
# Flask Setup
app = Flask(__name__)

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///static/dataset/consultant.sqlite"
db = SQLAlchemy(app)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = db.session
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()