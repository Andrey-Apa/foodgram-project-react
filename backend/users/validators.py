import re

from django.core.exceptions import ValidationError


def validate_username(value):
    """Проверка поля username модели user на допустимые символы."""

    if re.findall(r'[^\w.@+-]+', value):
        raise ValidationError(
            'Используйте буквы, цифры и символы @/./+/-/ при создании имени.'
        )


def email_normalization(email):
    """ Приводит домен к одному регистру."""
    email = email or ''
    try:
        email_name, domain = email.strip().rsplit('@', 1)
    except ValueError:
        pass
    else:
        email = email_name.lower() + '@' + domain.lower()
    return email
