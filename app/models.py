from . import db

class Images:
    def __init__(self,id,userImageURL,webformatURL):
        self.id= id
        self.userImageURL=userImageURL
        self.webformatURL=webformatURL
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key =True)
    username =db.Column(db.String(255))
    def __repr__(self):
        return f'User {self.username}'
