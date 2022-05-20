from app import app
import views
from posts.posts import posts

app.register_blueprint(posts, url_prefix='/blog')

if __name__=='__main__':
    app.run()