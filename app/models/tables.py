from app import db


class User(db.Model):
    _tablename_ = 'users'

    id = db.Collum(db.Integer, primary_key = True)
    username = db.Collum(db.String,unique = True)
    password = db.Collum(db.String, unique = True)
    name = db.Collum(db.String)
    email = db.Collum(db.String, unique = True)

    def __init__ (self, username, passord, name, email):
        self.username = username
        self.email = email
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username
    

class Post(db.Model):
    __tablename__   = "Posts"
    id = db.Collum(db.Integer, primary_key = True )
    content =  db.Collum(db.Text)
    user_id = db.Collum(db.Integer, db.Foreign_Key('users.id'))
    user = db.relationship('User', foreign_keys = user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    def __repr__(self):
        return "<Post %r>" % self.id


class Follow(db.model):
    __tablename__   = "follow"
    id = db.Collum(db.Integer, primary_key = True )
    
    user_id = db.Collum(db.Integer, db.Foreign_Key('users.id'))
    follower_id = db.Collum(db.Integer, db.Foreign_Key('users.id'))

    user = db.relationship("User", foreign_keys = user_id)
    follower = db.relationship("User", foreign_keys = follower_id)

