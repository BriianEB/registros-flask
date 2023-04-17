import utils.validations as validation
from database import db


class Alumno(db.Model):
    __tablename__ = 'alumnos'

    id = db.mapped_column(db.Integer, primary_key=True)
    matricula = db.mapped_column(db.String(7), unique=True, index=True)
    nombre = db.mapped_column(db.String(64))
    carrera = db.mapped_column(db.String(64))
    email = db.mapped_column(db.String(64), unique=True, index=True)
    telefono = db.mapped_column(db.String(64), unique=True)

    validations = {
        'matricula': [validation.required],
        'nombre': [validation.required],
        'carrera': [validation.required],
        'email': [validation.required, validation.email],
        'telefono': [validation.required, validation.phone]
    }
