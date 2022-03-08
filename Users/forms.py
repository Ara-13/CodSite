from django.forms import ModelForm
from jdatetime import date
from pyrsistent import field
from Codm import models
from . import models

class UserCreationForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'username', 'phone', 'email', 'password']
        labels = {
            'name' : 'نام',
            'username' : 'نام کاربری',
            'phone' : 'تلفن همراه',
            'email' : 'ایمیل',
            'password' : 'رمز',
        }