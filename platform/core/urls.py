# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path('admin' , admin.site.urls),          # Django admin route 
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             
]
