# Generated by Django 2.2 on 2020-10-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientMonitor', '0019_delete_patient_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='temperature_sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.FloatField(blank=True)),
                ('Patient', models.ManyToManyField(to='patientMonitor.patient_registration')),
            ],
        ),
    ]
