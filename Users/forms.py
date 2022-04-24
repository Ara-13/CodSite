from django import forms
from django.forms import ModelForm, widgets
from phonenumber_field.formfields import PhoneNumberField
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
        widgets = {
            'name' : forms.TextInput(attrs={'class':'input-ui pr-2'}),
            'username' : forms.TextInput(attrs={'class' : 'input-ui pr-2'}), 
            'phone' : forms.TextInput(attrs={'class' : 'input-ui pl-2 text-left dir-ltr'}),
            'email' : forms.EmailInput(attrs={'class':'input-ui pl-2 text-left dir-ltr'}),
        }

class UserEditionForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'phone', 'email']
        labels = {
            'name' : 'نام',
            'phone' : 'تلفن همراه',
            'email' : 'ایمیل',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'input-ui pr-2'}),
            'phone' : forms.TextInput(attrs={'class' : 'input-ui pl-2 text-left dir-ltr'}),
            'email' : forms.EmailInput(attrs={'class':'input-ui pl-2 text-left dir-ltr'}),
        }