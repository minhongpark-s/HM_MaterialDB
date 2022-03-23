from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    studentNumber = forms.IntegerField(label='학번')
    real_name = forms.CharField(label='진짜이름')
    user_phone = forms.IntegerField(label='전화번호')
    user_major = forms.CharField(label='전공')

    class Meta:
        model = Profile
        fields = ("username", "password1", "password2", "email", "studentNumber", "real_name", "user_phone", "user_major", )