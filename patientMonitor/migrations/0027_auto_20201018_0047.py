# Generated by Django 2.2 on 2020-10-17 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientMonitor', '0026_auto_20201018_0017'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='random',
            new_name='randomData',
        ),
        migrations.RenameField(
            model_name='randomdata',
            old_name='random',
            new_name='rand',
        ),
    ]
