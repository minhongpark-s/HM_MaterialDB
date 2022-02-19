from django.urls import path
from DBshow import views
from django.contrib import admin

app_name='DBshow'

urlpatterns = [
    path('', views.index),
    path('db/', views.index),
    path('testing/', views.testing, name="testing"),

    path('product_database/modify/<int:rent_id>/', views.change_rentable_num,
         name="change_rentable_num"),
    path('mypage/', views.mypage),
<<<<<<< HEAD
    #path('product_database/modify_again/<char:product_name>/', views.change_rent_num,
         #name="change_rent_num"),
=======
    path('newpagetesting/', views.newpagetesting, name="newpagetesting")
>>>>>>> 2_19_first
]