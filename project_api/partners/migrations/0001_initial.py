# Generated by Django 2.2.7 on 2019-11-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'partner',
            },
        ),
    ]
