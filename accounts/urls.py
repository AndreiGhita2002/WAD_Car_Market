from django.urls import path
from accounts import views

app_name = 'cars'

urlpatterns = [

    path('register/', views.register, name='register'),
]