import re
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not re.fullmatch(r'\d+', value):
        raise ValidationError('Phone number must contain only digits.')

def validate_name(value):
    if not re.fullmatch(r'[A-Za-z\s]+', value):
        raise ValidationError('Name must contain only letters and spaces.')
