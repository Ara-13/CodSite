from django.forms import ModelForm
from jdatetime import date
from Codm import models
#User
from django.conf import settings
User = settings.AUTH_USER_MODEL

class AccountForm(ModelForm):
    class Meta:
        model = models.Account
        fields = ['price', 'picture']

        labels = {
            'picture' : 'تصویر نمایش اکانت',
            'price' : 'قیمت'
        }

class CodAccountForm(ModelForm):
    class Meta:
        model = models.CodAccount
        fields = ['level', 'region', 'c', 'cp', 
        'multi_ranked', 'battle_ranked', 'battle_pass',
        'description']

        labels = {
            'level' : 'لول',
            'region' : 'ریجن اکانت',
            'c' : 'تعداد c اکانت',
            'cp' : 'تعداد cp اکانت',
            'multi_ranked' : 'رنک مولتی اکانت',
            'battle_ranked' : 'رنک بتل اکانت',
            'battle_pass' : 'بتل پس های اکانت',
            'description' : 'سایر توضیحات شما',
        }

class AccountVideoForm(ModelForm):
    class Meta:
        model = models.Video
        fields = [
            'video',
        ]
        labels = {
            'video' : 'ویدیو اکانت'
        }

class AccountLinkForm(ModelForm):
    class Meta:
        model = models.Link
        fields = [
            'Type',
        ]
        labels = {
            'Type' : 'سیو اکانت'
        }

class AccountImageForm(ModelForm):
    class Meta:
        model = models.Image
        fields = [
            'image',
        ]
        labels = {
            'image' : 'سایر تصاویر اکانت'
        }


'''class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'name', 'username', 'phone', 'email', 'password'
        ]'''