from django.urls import path

from . import views

app_name = 'pravda_brain'
urlpatterns = [
    path('', views.index, name='index'),

]