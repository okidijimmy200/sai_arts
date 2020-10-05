from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, about_view, all_artPieces, art_detail, all_exibited, artExibition_detail, sai_view, emma_view, aramu_view

app_name = 'main'

urlpatterns = [    
   path('', home_view, name='main'),
   path('about', about_view, name='about'),
   path('artist/sai', sai_view, name='sai'),
   path('artist/emma', emma_view, name='emma'),
   path('artist/aramu', aramu_view, name='aramu'),
   path('allartpieces', all_artPieces, name='allartpieces'),
   path('allexibitedpieces', all_exibited, name='allexibitedpieces'),
   path('<slug:artpiece>/', art_detail, name='artDetail'),
   path('<slug:artpiece>/', artExibition_detail, name='artExibitedDetail'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)