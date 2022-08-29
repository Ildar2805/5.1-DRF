# Generated by Django 4.1 on 2022-08-28 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_id_measurement_sensor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата измерения'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Measurement', to='measurement.sensor', verbose_name='ID датчика'),
        ),
    ]
