import utils.validations as validation
from database import db


class Profesor(db.Model):
    __tablename__ = 'profesores'

    id = db.mapped_column(db.Integer, primary_key=True)
    no_empleado = db.mapped_column(db.String(6), unique=True, index=True)
    nombre = db.mapped_column(db.String(64))
    carrera = db.mapped_column(db.String(64))
    telefono = db.mapped_column(db.String(64), unique=True)

    validations = {
        'no_empleado': [validation.required()],
        'nombre': [validation.required()],
        'carrera': [validation.required()],
        'telefono': [validation.required(), validation.phone()]
    }
