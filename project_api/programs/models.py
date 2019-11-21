# programs/models.py
from django.db import models


class Program(models.Model):

    class Meta:
        db_table = 'program'

    id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=1024, null=False)
    program_code = models.CharField(max_length=128)
    description = models.CharField(max_length=4096, null=False)
    partner = models.ForeignKey(
        'partners.Partner',
        related_name='programs',
        on_delete=models.CASCADE,
    )
