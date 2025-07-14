from django.core.exceptions import ValidationError


def esMayorACero(value):
    if value < 0:
        raise ValidationError(
            '%(value)s debe ser número positivo',
            params={"value": value}
            )
    
def esMenorACien(value):
    if value > 100:
        raise ValidationError(
            '%(value)s debe ser mayor a cien',
            params={"value": value}
            )
