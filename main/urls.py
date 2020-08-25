from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, about_view, all_artPieces, art_detail, all_exibited, artExibition_detail

app_name = 'main'

urlpatterns = [    
   path('', home_view, name='main'),
   path('about', about_view, name='about'),
   path('allartpieces', all_artPieces, name='allartpieces'),
   path('allexibitedpieces', all_exibited, name='allexibitedpieces'),
   path('<slug:artpiece>/', art_detail, name='artDetail'),
   path('<slug:artpiece>/', artExibition_detail, name='artExibitedDetail'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)