from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def custom_validation(data):
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()
    
    if not email or User.objects.filter(email=email).exists():
        raise ValidationError('choose another email')
    
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')

    if not username:
        raise ValidationError('choose another username')
    return data


