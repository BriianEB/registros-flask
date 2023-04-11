from flask import Blueprint, render_template

from database import db
from models import Alumno, Profesor


home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('index.html')
