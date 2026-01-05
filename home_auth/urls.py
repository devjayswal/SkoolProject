
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('signup/',views.signup_view, name='signup'),
    path('login/',views.login_view, name='login'),
    path('forgot-password/',views.forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>/',views.reset_password_view, name='reset-password'),
    path('logout/',views.logout_view, name='logout'),
    
]
