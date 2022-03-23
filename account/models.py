from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    real_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='real_name')
    studentNumber = models.IntegerField(blank=True, null=True, verbose_name='studentNumber')
    user_major = models.CharField(max_length=100, blank=True, null=True, verbose_name='user_major')
    user_phone = models.IntegerField(blank=True, null=True, verbose_name='user_phone')


