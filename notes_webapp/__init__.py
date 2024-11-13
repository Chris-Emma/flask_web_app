from flask import Flask

def create_app():
    app = Flask(__name__) #defines name of the application
    app.config['SECRET_KEY'] = 'saint' #encrypts or secures cookies and session data
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app