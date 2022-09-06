from django.contrib.auth import get_user_model
from django.db import models

from .validators import reach_value_validator, unit_value_validator


User = get_user_model()


class Unit(models.Model):
    unit = models.IntegerField(
        'Рейтинг',
        null=True,
        validators=[unit_value_validator]
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='authors')

    def __str__(self):
        return self.unit


class Reach(models.Model):
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name='reach',)
    reach = models.FloatField('охват', validators=[reach_value_validator])

    def __str__(self):
        return str(self.reach)
