# programs/migrations/0002_load_intial_data.py
import os
from django.db import migrations
import json

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))


def load_fixture(apps, schema_editor):
    Program = apps.get_model("programs", "Program")
    Partner = apps.get_model("partners", "Partner")
    fixture_file = os.path.join(fixture_dir, "programs.json")
    fixture_data = []
    fixture = open(fixture_file, "rb")
    fixture_entries = json.loads(fixture.read().decode("utf-8"))
    for entry in fixture_entries:
        partner = Partner.objects.filter(
            name=entry["fields"]["partner_name"]
        ).first()
        Program.objects.create(
            program_name=entry["fields"]["program_name"],
            program_code=entry["fields"]["program_code"],
            description=entry["fields"]["description"],
            partner=partner,
        )
    fixture.close()


def unload_fixture(apps, schema_editor):
    Program = apps.get_model("programs", "Program")
    Program.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
