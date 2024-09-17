import os
from dotenv import load_dotenv
from flask import Flask

from board import pages, posts

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)
    print(f"Current Environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app