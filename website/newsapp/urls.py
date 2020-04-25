from django.urls import path

from . import views

urlpatterns = [
    path('faq/', views.FAQListView.as_view(),name = 'faq'),

     # Landing page
    path('', views.index, name = 'index'),

     # URLs to Plain Views
    path('o-nas/', views.about, name='about'),
    path('kontakt/', views.contact, name='contact'),
    path('wtyczka/', views.extension, name='extension'),
    path('finansowanie/', views.finances, name='finances'),
    path('wesprzyj/', views.support, name='support'),
    path('wolontariat/', views.voluntary_service, name='voluntary_service'),
]
