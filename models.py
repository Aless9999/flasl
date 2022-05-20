from app import db
from datetime import datetime
import re
import time


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


post_tag = db.Table('post_tag',
                     db.Column('posts_id', db.Integer, db.ForeignKey('posts.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    slug = db.Column(db.String(50), unique=True)  #окончание в адресной строке мы берем из title
    body = db.Column(db.String(500), unique=True)
    time = db.Column(db.DateTime, default=datetime.now())

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()



    tags = db.relationship('Tag',  secondary='post_tag',
                           backref=db.backref('posts', lazy="dynamic"))
                               

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time))

    def __repr__(self):
        return f'<Post id:{self.id}, title:{self.title}>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    slug = db.Column(db.String(50), unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.title)


    def __repr__(self):
        return f'<Post id:{self.id}, name:{self.name}>'