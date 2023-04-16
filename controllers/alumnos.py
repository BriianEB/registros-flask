from flask import Blueprint, render_template, request, redirect, url_for

import utils.validations as validation
from database import db
from models import Alumno, Profesor


alumnos = Blueprint('alumnos', __name__)

@alumnos.route('/alumnos/crear', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = request.form

        errors = validation.validate(Alumno.validations, data)

        if errors:
            return render_template('alumnos/create.html',
                alumno=data,
                errors=errors
            )

        alumno = Alumno(
            matricula=data['matricula'],
            nombre=data['nombre'],
            carrera=data['carrera'],
            email=data['email'],
            telefono=data['telefono'],
        )

        db.session.add(alumno)
        db.session.commit()

        return redirect(url_for('home.index'))

    return render_template('alumnos/create.html')
