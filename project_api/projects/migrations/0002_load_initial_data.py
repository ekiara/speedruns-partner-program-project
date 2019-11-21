# projects/migrations/0002_load_intial_data.py
import os
from django.db import migrations
import json

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))


def load_fixture(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Program = apps.get_model("programs", "Program")

    fixture_file = os.path.join(fixture_dir, "projects.json")
    fixture = open(fixture_file, "rb")
    fixture_entries = json.loads(fixture.read().decode("utf-8"))
    for entry in fixture_entries:
        program = Program.objects.filter(
            program_code=entry["fields"]["program_code"]
        ).first()
        Project.objects.create(
            project_name=entry["fields"]["project_name"],
            program=program,
        )
    fixture.close()


def unload_fixture(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Project.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
