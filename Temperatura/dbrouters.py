from .models import TbTemperatura

class MiRouter(object):

    def db_for_read(self, model, **hints):
        if model == TbTemperatura:
            return 'db_temp'
        return None