from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    subscribe = models.BooleanField(default=False)
    subscribe_date = models.DateField(null=True, blank=True, default='2001-09-11')
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        default='',
        validators=[RegexValidator('\+[0-9]{1}\([0-9]{3}\)[0-9]{3}\-[0-9]{4}')],
        error_messages='Телефон нөмірі қате енгізілді.',
    )