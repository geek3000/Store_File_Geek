from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from views import app
import os

db = SQLAlchemy(app)
class Save_files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(20), nullable=False)
    id1 = db.Column(db.String(20), nullable=False)
    pubdate = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __init__(self, file_name, id1):
        self.file_name = file_name
        self.id1=id1

db.create_all()
