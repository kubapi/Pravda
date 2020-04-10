from django.contrib import admin
from django.urls import path, include

# Linking applications views
from main_application import views

#Used for template tagging
app_name = 'main_application'

urlpatterns = [
    path('wtyczka/', views.extension, name='extension'),

    # Contact page and subpages
    path('kontakt/', views.contact, name='contact'),
    path('kontakt/wolontariat/'),
    path('kontakt/wspolpraca/'),
    path('kontakt/media/'),

    # About page and subpages
    path('o-nas/', views.about, name='about'),
    # path('o-nas/misja/')
    # path('o-nas/zespol/')
    # path('o-nas/')
]
