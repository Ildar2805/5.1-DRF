# Generated by Django 4.1 on 2022-08-29 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0008_remove_measurement_sensor_measurement_sensor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
