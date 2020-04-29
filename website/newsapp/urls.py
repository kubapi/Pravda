from django.urls import path

from . import views


app_name = 'newsapp'
urlpatterns = [
    # Landing page
    path('', views.index, name = 'index'),
    path('faq/', views.FAQListView.as_view(), name='faq'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    path('archiwum/', views.archive, name='archive'),
    
    # URLs to Plain Views
    path('o-nas/', views.about, name='about'),
    path('wtyczka/', views.extension, name='extension'),
    path('finansowanie/', views.finances, name='finances'),
    path('wsparcie/', views.support, name='support'),
    path('wolontariat/', views.voluntary_service, name='voluntary_service'),
]
