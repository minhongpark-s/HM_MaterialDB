from django.urls import path
from DBshow import views
from django.contrib import admin

app_name='DBshow'

urlpatterns = [
    path('', views.main),
    path('Database/', views.Database, name="Database"),
    path('product_database/modify/<int:rent_id>/', views.change_rentable_num,
         name="change_rentable_num"),

    path('product_database/modify_again/<int:rent_id>/', views.change_rent_num,
         name="change_rent_num"),

    path('my_page/', views.my_page, name="my_page"),

    path('main/', views.main, name="main")
]