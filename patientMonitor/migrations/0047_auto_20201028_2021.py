# Generated by Django 2.2 on 2020-10-28 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientMonitor', '0046_auto_20201028_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prescription',
            options={'ordering': ['-prescription_date']},
        ),
    ]
