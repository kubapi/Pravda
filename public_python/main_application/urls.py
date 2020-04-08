from django.contrib import admin
from django.urls import path, include

# Linking applications views
from main_application import views

#Used for template tagging
app_name = 'main_application'

urlpatterns = [
    path('wtyczka/', views.extension, name='extension'),
    path('kontakt/', views.contact, name='contact'),
    path('o-nas/', views.about, name='about')
]
