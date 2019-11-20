# partners/migrations/0002_load_intial_data.py
import os
from django.db import migrations
import json

fixture_dir = \
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))


def load_fixture(apps, schema_editor):
    Partner = apps.get_model("partners", "Partner")
    fixture_file = os.path.join(fixture_dir, "partners.json")
    fixture_data = []
    fixture = open(fixture_file, "rb")
    fixture_entries = json.loads(fixture.read().decode("utf-8"))
    for entry in fixture_entries:
        partner = Partner(
            name=entry["fields"]["name"],
        )
        fixture_data.append(partner)
    fixture.close()
    Partner.objects.bulk_create(fixture_data)


def unload_fixture(apps, schema_editor):
    Partner = apps.get_model("partners", "Partner")
    Partner.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
