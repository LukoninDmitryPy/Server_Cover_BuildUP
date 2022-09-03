from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Unit(models.Model):
    unit = models.IntegerField('Рейтинг')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='files')
    reach = models.ManyToOneRel(
        to = unit,
        on_delete=models.CASCADE,
        field_name='unit',
        field=float)

    def __str__(self):
        return self.unit


class Reach(models.Model):
    unit = models.ManyToOneRel(
        to = Unit,
        on_delete=models.CASCADE,
        field_name='unit',
        field='unit')
    reach = models.FloatField('охват', unique=True)

    def __str__(self):
        return self.reach
