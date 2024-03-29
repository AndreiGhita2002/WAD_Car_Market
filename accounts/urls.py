from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views
from accounts.forms import UserLoginForm
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=UserLoginForm),
         name='login'),

    path('profile/', views.profile, name='profile'),

    path('settings/', auth_views.PasswordChangeView.as_view(template_name='accounts/settings.html',
         success_url=reverse_lazy('accounts:profile')),
         name='settings'),

    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('mycars', views.mycars, name='mycars'),
    path('add-wishlist/<int:car_id>', views.add_wishlist, name='add_wishlist'),
    path('My-wishlist', views.wishlist, name='wishlist'),
]

#Some urls are using django built in views, those views are diffrentiated by having auth_views infront of them