# Generated by Django 3.2 on 2022-11-12 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-last_updated']},
        ),
    ]
