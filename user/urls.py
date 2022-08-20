import logging
from django.urls import path
from . import views as ezekiel_views
from django.contrib.auth import views as lemmy_views



urlpatterns = [
    path('', ezekiel_views.register, name='register'),
    path('login/', lemmy_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', lemmy_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', ezekiel_views.profile, name='profile'),
]
