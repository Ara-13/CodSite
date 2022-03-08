from django.forms import ModelForm
from jdatetime import date
from Codm import models
#User
from django.conf import settings
User = settings.AUTH_USER_MODEL

class CodAccountForm(ModelForm):
    class Meta:
        model = models.CodAccount
        fields = ['level', 'image', 'region', 'c', 'cp', 
        'multi_ranked', 'battle_ranked', 'battle_pass',
        'description', 'price']

'''class CodAccountVideoForm(ModelForm):
    class Meta:
        model = models.Video
        fields = [
            'account',
        ]'''

class CodAccountLinkForm(ModelForm):
    class Meta:
        model = models.Link
        fields = [
            'Type',
        ]

'''class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'name', 'username', 'phone', 'email', 'password'
        ]'''