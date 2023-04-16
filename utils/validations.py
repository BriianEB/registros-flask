import re


def required(value):
    return 'Debes llenar este campo' if value == '' else False

def email(value):
    return 'Ingresa un email válido' if re.search('[\w-]+@[\w]+\.[\w]+', value) == None else False

def phone(value):
    return 'Ingresa un número de teléfono válido' if re.search('^[\d-]+$', value) == None else False

def validate(validations, data):
    errors = {}

    for field, field_validations in validations.items():
        for validation in field_validations:
            error = validation(data[field])

            if error:
                errors.update({field: error})
                break

    return errors
