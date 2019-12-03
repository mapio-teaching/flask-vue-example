from pathlib import Path

from flask import Flask

from api.admin import init_admin

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path(app.instance_path) / 'database.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.update(test_config)

    # ensure the instance folder exists
    Path(app.instance_path).mkdir(exist_ok = True)

    init_admin(app)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
