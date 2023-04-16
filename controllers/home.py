from flask import Blueprint, render_template

from database import db
from models import Alumno, Profesor


home = Blueprint('home', __name__)

@home.route('/')
def index():
    alumnos = db.session.execute(db.select(Alumno)).scalars()

    return render_template('index.html', alumnos=alumnos)

@home.route('/color')
def color():
    return render_template('color.html')
