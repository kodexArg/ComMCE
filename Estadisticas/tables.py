import django_tables2 as tables
from Estadisticas.models import Ddbb25

class NumCol(tables.Column):
    def render(self, value):
        return '{0:.0f}'.format(value)

class PerCol(tables.Column):
    def render(self, value):
        return '{0:.2%}'.format(value)


class DdbbTable(tables.Table):
    id = NumCol()
    devol = PerCol()
    hold = PerCol()
    # año_fab = NumCol()

    class Meta:
        template_name = 'django_tables2/semantic.html'
        model = Ddbb25
        fields = (
            'id', 
            'posición_nueva', 
            # 'isla', 
            'sala_nueva',  
            'juego', 
            'fabricante',
            'modelo',
            'denom_nueva',
            'hold',
            'devol',
            'tipo',
            )
        sequence = (
            'id', 
            'posición_nueva', 
            # 'isla', 
            'sala_nueva',  
            'juego', 
            'fabricante',
            'modelo',
            'denom_nueva',
            'hold',
            'devol',
            'tipo',
            )
        orderable = False
