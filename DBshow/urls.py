from django.urls import path
from DBshow import views
from django.contrib import admin

app_name='DBshow'

urlpatterns = [
    path('', views.index),
    path('db/', views.index),
    path('basket/', views.basket),
    path('check/', views.check),
    path('testing/', views.testing),
    path('parameter/', views.changeDBandRefreshPage, name='parameter'),

    path('product_database/modify/<int:rent_id>/',views.change_rentable_num,
         name="change_rentable_num"),
]