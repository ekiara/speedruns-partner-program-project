# partners/models.py
from django.db import models


class Partner(models.Model):

    class Meta:
        db_table = 'partner'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
