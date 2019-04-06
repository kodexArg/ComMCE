from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Ddbb25(models.Model):
    id = models.SmallIntegerField(db_column='Número', primary_key=True)  # Field name made lowercase.
    posición_anterior = models.CharField(db_column='Posición anterior', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    posición_nueva = models.CharField(db_column='Posición Nueva', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isla = models.CharField(db_column='ISLA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devol = models.FloatField(db_column='DEVOL', blank=True, null=True)  # Field name made lowercase.
    hold = models.FloatField(db_column='HOLD', blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='ACCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sala_anterior = models.CharField(db_column='Sala anterior', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sala_nueva = models.CharField(db_column='Sala Nueva', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fabricante = models.CharField(db_column='Fabricante', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    año_fab = models.FloatField(db_column='Año Fab', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    juego = models.CharField(db_column='Juego', max_length=255, blank=True, null=True)  # Field name made lowercase.
    denom_anterior = models.CharField(db_column='Denom Anterior', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    denom_nueva = models.CharField(db_column='Denom Nueva', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    progresivo = models.CharField(db_column='Progresivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    participacion = models.CharField(db_column='Participacion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DDBB25'

    objects = models.Manager()

class Tdatos(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    field_date = models.DateTimeField(db_column='_DATE', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_slot = models.IntegerField(db_column='_SLOT', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_model = models.CharField(db_column='_MODEL', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_denom = models.FloatField(db_column='_DENOM', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_devol = models.FloatField(db_column='_DEVOL', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_in = models.FloatField(db_column='_IN', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_out = models.FloatField(db_column='_OUT', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_hp = models.FloatField(db_column='_HP', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_drop = models.FloatField(db_column='_DROP', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_games = models.FloatField(db_column='_GAMES', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_bill = models.FloatField(db_column='_BILL', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_jp = models.FloatField(db_column='_JP', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_win = models.FloatField(db_column='_WIN', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_sala = models.CharField(db_column='_SALA', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'TDATOS'

    objects = models.Manager()

