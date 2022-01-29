from unicodedata import name
from django.urls import URLPattern, path
from rango import views

app_name = 'rango'

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about')
    
]