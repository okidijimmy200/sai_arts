from django.urls import path
from django.contrib import admin
from .views import home_view, about_view

app_name = 'main'

urlpatterns = [    
   path('', home_view, name='main'),
   path('about', about_view, name='about')
   
]