from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    user_id=db.Column(db.String(100), primary_key=True)
    name=db.Column(db.String(120), unique=False, nullable=False)
    email=db.Column(db.String(120), unique=False, nullable=False)
    followers=db.Column(db.Integer, nullable=True)
    photo = db.Column(db.String(255), nullable=False)
    recentTracks = db.Column(db.PickleType, nullable = False)
    topArtists = db.Column(db.PickleType, nullable = False)
    posts = db.relationship('Post', backref='user')
    chats = db.relationship('Chat', backref='user')
    friends = db.relationship('Friend', cascade="all,delete", backref='user', uselist=False)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "followers": self.followers,
            "photo": self.photo,
            "recentTracks": self.recentTracks,
            "topArtists": self.topArtists
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Chat(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.PickleType)
    user_id = db.Column(db.String(100), db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False) 

    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            "user_id": self.user_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    commentary=db.Column(db.String(120))
    user_id = db.Column(db.String(120), db.ForeignKey('user.user_id', ondelete='CASCADE'), nullable=False) 

    def serialize(self):
        return {
            "id": self.id,
            "commentary": self.commentary,
            "user_id": self.user_id,
            "name": self.user.name,
            "photo": self.user.photo
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Friend(db.Model):
    __tablename__ = 'friends'
    personId = db.Column(db.String(250), primary_key=True)
    friends = db.Column(db.String(250), nullable=False)
    photo = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.String(120), db.ForeignKey('user.user_id', ondelete='CASCADE'), unique=True) 

    def serialize(self):
        return {
            "friends": self.friends,
            "user_id": self.user_id,
            "personId": self.personId,
            "photo": self.photo
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()