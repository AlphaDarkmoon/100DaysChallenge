from django.contrib import admin
from django.urls import path
from loginSys_app import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.login_user,name='login'),
    path('home',views.home,name='home'),
    path('error',views.error,name='error'),
    path('logout',views.logout_user,name='logout'),

]