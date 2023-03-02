from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path('used/', views.used_car, name='used'),
    path('new/', views.new_car, name='new'),
    path('car_details/', views.car_details, name='car_details'),
    path('sell_your_car/', views.sell_car, name='sell_your_car'),
    path('sell_your_car/list_car', views.list_car, name='list_car'),
    path('saved/', views.saved, name='saved'),
]
