# Generated by Django 2.2 on 2020-10-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientMonitor', '0030_patient_registration_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_registration',
            name='slug',
            field=models.SlugField(max_length=1264, unique=True),
        ),
    ]
