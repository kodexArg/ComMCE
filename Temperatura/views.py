from django.shortcuts import render
from .models import TbTemperatura
from django.db.models import Count, Min, Avg, Sum, Max
from datetime import datetime, timedelta, date, timezone
from django_pandas.io import read_frame
# from django.utils.timezone import localtime
from django.db.models.functions import Extract

dnow = datetime.now()
d0 = dnow - timedelta(days = 1)
d1 = d0 - timedelta(days = 1)
d2 = d0 - timedelta(days = 1)

def _Qry24hs():
    temperatura = TbTemperatura \
    .objects \
    .filter(fecha__range=[d1, d0]) \
    .annotate(
        avg_temp=Avg('temperatura'),
        hora=Extract('fecha', 'hour'),
        dia=Extract('fecha', 'day'),
        ) \
    .order_by()
    return temperatura

def Qry24hs():
    temperatura = TbTemperatura \
    .objects \
    .filter(fecha__range=[d1, d0]) \
    .extra(select={'hora': 'hour(fecha)', 'dia': 'date(fecha)'}) \
    .values('rpi', 'hora', 'dia') \
    .annotate(avg_temp=Avg('temperatura')) \
    .order_by()
    return temperatura

def QrySemana():
    temperatura = TbTemperatura \
    .objects \
    .filter(fecha__range=[d2, d0]) \
    .values('rpi', 'temperatura', 'fecha') \
    .order_by()
    return temperatura

# Create your views here.
def _24hs(request):
    df = read_frame(Qry24hs())
    print(df)
    df['avg_temp'] = df['avg_temp'].apply(str)

    rpi_lista = df['rpi'].drop_duplicates().tolist()
    hor_lista = df['hora'].drop_duplicates().tolist()

    ultimo = list(TbTemperatura.objects.aggregate(Max('fecha')).values())[0]
    
    args = {
        'rpi_lista': rpi_lista,
        'hor_lista': hor_lista,
        'dataframe': df,
        'ultimo': ultimo,
        }
    return render(request, "Temperatura/24hs.html", args)


def semana(request):
    df = read_frame(QrySemana())

    rpi_lista = df['rpi'].drop_duplicates().tolist()

    ultimo = list(TbTemperatura.objects.aggregate(Max('fecha')).values())[0]

    args = {
        'dataframe': df,    
        'rpi_lista': rpi_lista,
        'ultimo': ultimo,
        }
    return render(request, 'Temperatura/semana.html', args)
