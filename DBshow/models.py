from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.

class DB(models.Model):
    product_name = models.CharField(max_length=30)
    rentable_num = models.IntegerField()
    total_num = models.IntegerField()

    registeredTime = models.DateTimeField(auto_now_add=True)
    modifiedTime = models.DateTimeField(auto_now=True)

    image=models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    tag = models.CharField(max_length=128)

    def __str__(self):
        return f'[{self.pk}]{self.product_name}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

class Rent(models.Model):
    rent_code = models.IntegerField(blank=True, null=True)
    #대여번호
    name = models.CharField(max_length=40, null=True, blank=True)
    #회원
    product_name = models.CharField(max_length=30, null=True, blank=True)
    #물품명
    rent_num = models.IntegerField(null=True, blank=True)
    #대여수량
    rent_date = models.DateTimeField(null=True, blank=True)
    #대여일자
    return_date = models.DateTimeField(null=True, blank=True)
    #반납일
    note = models.CharField(max_length=30, blank=True, null=True)
    #비고
    image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'[{self.pk}]{self.rent_code}번 대여입니다.'


