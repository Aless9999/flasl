from flask import render_template, request
from models import *
def index():
    q = request.args.get('q', '')
    if q:
        post = Posts.query.filter(Posts.title.contains(q)| Posts.body.contains(q)).all()
    else:
        post= Posts.query.all()
    return render_template('posts.index', post=post)    




def __init__(self, *args, **kwargs):
    super().__init__(self, *args, **kwargs)
    self.slug

    )        