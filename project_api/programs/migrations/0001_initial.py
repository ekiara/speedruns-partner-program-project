# Generated by Django 2.2.7 on 2019-11-21 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0002_load_intial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('program_name', models.CharField(max_length=1024)),
                ('program_code', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=4096)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='partners.Partner')),
            ],
            options={
                'db_table': 'program',
            },
        ),
    ]
