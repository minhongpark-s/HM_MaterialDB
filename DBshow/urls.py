from django.urls import path
from DBshow import views
from django.contrib import admin

urlpatterns = [
    path('', views.index),
    path('db/', views.index),
    path('basket/', views.basket),
    path('check/', views.check),
]