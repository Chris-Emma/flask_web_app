from flask import Flask

def create_app():
    app = Flask(__name__) #defines name of the application
    app.config['SECRET_KEY'] = 'saint' #encrypts or secures cookies and session data
    
    return app