import os
from flask import Flask
from flask_migrate import Migrate

from config import config
from database import db

from controllers import home
from models import Alumno, Profesor


basedir = os.path.abspath(os.path.dirname(__file__))

migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__, template_folder=os.path.join(basedir, 'views'))
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join(basedir, 'database/migrations'))

    app.register_blueprint(home)

    return app

app = create_app(os.environ.get('APP_ENV'))

# shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Alumno=Alumno, Profesor=Profesor)
