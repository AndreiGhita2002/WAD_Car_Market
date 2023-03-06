from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about, name='about_us'),
    path('contact_us/', views.about, name='contact_us'),
]