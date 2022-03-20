from django.urls import path
from DBshow import views
from django.contrib import admin


app_name='DBshow'

urlpatterns = [
    path('', views.main),
    path('Database/', views.Database, name="Database"),
    path('xlsxAdd/', views.xlsxAdd, name="xlsxAdd"),
    path('DeleteDB/', views.DeleteDB, name="DeleteDB"),

    #대여/반납 로직 url
    path('product_database/modify/<int:rent_id>/', views.change_rentable_num,
         name="change_rentable_num"),
    path('product_database/modify_again/<int:rent_id>/', views.change_rent_num,
         name="change_rent_num"),

    path('my_page/', views.my_page, name="my_page"),

    #메인 페이지 url
    path('main/', views.main, name="main"),


    #레이저 커팅 url
    path('LaserCuttingForm/', views.LC, name="LC"),
    path('LC_reserve/', views.LC_reserve, name="LC_reserve"),
]