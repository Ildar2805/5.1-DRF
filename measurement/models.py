from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['pk']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='ID датчика')
    temperature = models.FloatField(verbose_name='Температура при измерении')
    created_at = models.DateField(auto_now=True,  verbose_name='Дата измерения')


    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
