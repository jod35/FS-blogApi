from . import db,login_manager





class User(db.Model):
    __tablename__='blog_user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text)
    posts=db.relationship('Post',backref='author',lazy=True)


    def __repr__(self):
        return self.username

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class Post(db.Model):
    __tablename__='blog_posts'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(25),nullable=False)
    body=db.Column(db.Text,nullable=False)
    author_id=db.Column(db.Integer(),db.ForeignKey('blog_user.id'))


