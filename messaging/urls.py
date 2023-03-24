from django.urls import path
from .views import message_seller

app_name = 'messaging'

urlpatterns = [
    path('', message_seller, name='message_seller'),
]
