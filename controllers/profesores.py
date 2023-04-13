from flask import Blueprint, render_template

from database import db
from models import Alumno, Profesor


profesores = Blueprint('profesores', __name__)

@profesores.route('/profesores/crear')
def create():
    return render_template('profesores/create.html')
