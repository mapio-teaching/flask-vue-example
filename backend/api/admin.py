import click

from flask.cli import with_appcontext
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

from api.model import db, User, Post

def init_admin(app):
    db.init_app(app)
    admin = Admin(app, name = 'flaskr-revisited', template_mode = 'bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Post, db.session))
    app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    db.create_all()
    with open('data.sql') as inf:
      for statement in inf:
        db.engine.execute(statement)
    click.echo('Initialized the database.')
