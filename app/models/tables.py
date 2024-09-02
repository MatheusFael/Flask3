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
    user_id = db.Collum(db.Integer, Foreign_Key = )
