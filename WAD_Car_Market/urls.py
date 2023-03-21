"""WAD_Car_Market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('message_seller/', include('messaging.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('cars/', include('cars.urls')),
                  path('about-us/', views.about_us, name='about_us'),
                  path('contact-us/', views.contact_us, name='contact_us'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
        path('admin/', admin.site.urls),
        path('', views.home, name='home'),
        path('message_seller/', include('messaging.urls')),
        path('accounts/', include('accounts.urls')),
        path('cars/', include('cars.urls')),
        path('password-reset/',
                auth_views.PasswordResetView.as_view(
                template_name='accounts/forgot_password.html'),name='password_reset'),
        path('password-reset/done/',
                auth_views.PasswordResetDoneView.as_view(
                template_name='accounts/password_email.html'),name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/',
                auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/change_password.html'),name='password_reset_confirm'),
        path('password-reset-complete/',
                auth_views.PasswordResetCompleteView.as_view(
                template_name='accounts/password_changed.html'),name='password_reset_complete'),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 1e1c3409b8e4272a2d0e6c8eee89eae922ca6d1b

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
