from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views
from accounts.views import PasswordChangeViews
from accounts.forms import UserLoginForm

app_name = 'cars'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=UserLoginForm), name='login'),
    path('profile/', views.profile, name='profile'),
    path('settings/', PasswordChangeViews.as_view(template_name='accounts/settings.html'), name='settings'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]