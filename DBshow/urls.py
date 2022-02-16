from django.urls import path
from DBshow import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name = 'db'

urlpatterns = [
    path('', views.index),
    path('db/', views.index),
    path('basket/', views.basket),
    path('check/', views.check, name='check'),
    path('testing/', views.testing),
]