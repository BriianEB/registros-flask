from flask import Blueprint, render_template

from database import db
from models import Alumno, Profesor


alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/alumnos/crear')
def create():
    return render_template('alumnos/create.html')
