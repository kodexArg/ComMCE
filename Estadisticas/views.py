from django.shortcuts import render
# from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime, timedelta, date
from Estadisticas.models import Ddbb25, Tdatos
from Estadisticas.tables import DdbbTable
from django_tables2 import RequestConfig
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.base import TemplateResponse
from django.core import serializers
import json

# Create your views here.
def pki(request):
     return render(request, "Estadisticas/base.html")

def ddbb(request):
     table = DdbbTable(Ddbb25.objects.all().order_by('id'))
     RequestConfig(request, paginate={"per_page": 12}).configure(table)
     return render(request, 'Estadisticas/Hojas/hoja1.html', {'table': table})

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))



def beneficios(request):
     d1, d2 = [datetime.today() - timedelta(days=40), datetime.today()] #fechas inicial y final
     data = Tdatos.objects.filter(field_date__range=[d1, d2]).values_list('field_sala').annotate(total=Sum('field_win'))
     jsdata = json.dumps(list(data), default=json_serial)
     args = {'datos': jsdata}
     return render(request, "Estadisticas/Hojas/hoja2.html", args)

