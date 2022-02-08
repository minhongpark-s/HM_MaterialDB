from django.db import models
import os

# Create your models here.

class DB(models.Model):
    물품명 = models.CharField(max_length=30)
    남은_개수 = models.IntegerField()
    총_개수 = models.IntegerField()

    물품등록시점 = models.DateTimeField(auto_now_add=True)
    최종수정시점 = models.DateTimeField(auto_now=True)

    image=models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.물품명}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

class Rent(models.Model):
    대여번호 = models.IntegerField()
    회원이름 = models.CharField(max_length=10)
    물품명 = models.CharField(max_length=30)
    대여수량 = models.IntegerField()
    대여일자 = models.DateTimeField()
    반납일자 = models.DateTimeField(null=True, blank=True)
    비고 = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.대여번호}번 대여입니다.'


