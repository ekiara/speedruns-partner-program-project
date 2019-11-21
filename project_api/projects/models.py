# projects/models.py
from django.db import models


class Project(models.Model):

    class Meta:
        db_table = 'project'

    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=1024, null=False)
    program = models.ForeignKey('programs.Program', related_name='projects', on_delete=models.CASCADE)
