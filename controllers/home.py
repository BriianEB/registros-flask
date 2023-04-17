from flask import Blueprint, render_template

from database import db
from models import Alumno, Profesor


home = Blueprint('home', __name__)

@home.route('/')
def index():
    alumnos = db.session.execute(db.select(Alumno)).scalars()
    alumnos_count = db.session.execute(db.select(db.func.count(Alumno.id))).scalar_one()
    profesores = db.session.execute(db.select(Profesor)).scalars()
    profesores_count = db.session.execute(db.select(db.func.count(Profesor.id))).scalar_one()

    return render_template('index.html',
        alumnos=alumnos,
        alumnos_count=alumnos_count,
        profesores=profesores,
        profesores_count=profesores_count
    )

@home.route('/color')
def color():
    return render_template('color.html')
