from rest_framework.validators import ValidationError


def validate_phone_number(instance, value):
    user = instance.objects.filter(phone_number=value)
    if not user.exists():
        raise ValidationError({"phone_number": "Пользователь с таким номером телефона не найден"})
    return value


def validate_email(instance, value):
    user = instance.objects.filter(email=value)
    if not user.exists():
        raise ValidationError({"email": "Пользователь с таким email не найден"})
    return value
