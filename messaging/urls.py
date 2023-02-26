from django.urls import path
from .views import message_seller

urlpatterns = [
    path('', message_seller, name='message_seller'),
]
