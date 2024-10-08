# Generated by Django 2.2 on 2020-10-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientMonitor', '0009_auto_20201015_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_registration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patient_registration',
            name='user',
        ),
        migrations.AddField(
            model_name='doctor_registration',
            name='Doctor_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='doctor',
            field=models.ManyToManyField(to='patientMonitor.doctor_registration'),
        ),
    ]
