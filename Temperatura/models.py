# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from time import strftime

class TbTemperatura(models.Model):
    rpi = models.CharField(db_column='RPi', max_length=32)  # Field name made lowercase.
    temperatura = models.IntegerField(db_column='Temperatura', blank=True, null=True)  # Field name made lowercase.
    humedad = models.IntegerField(db_column='Humedad', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_temperatura'
        ordering = ['-fecha']

    objects = models.Manager()
