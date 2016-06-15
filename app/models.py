from app import db

class Markov(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Unicode(32), index=True, unique=False)
    chain = db.Column(db.Unicode(64), index=True, unique=False)
    nextWord = db.Column(db.Unicode(32), index=False, unique=False)
    
