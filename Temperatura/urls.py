from django.urls import path
from . import views

urlpatterns = [
        path('', views._24hs),
        path('24hs', views._24hs, name='24hs'),
        path('semana', views.semana, name='semana'),
        ]

