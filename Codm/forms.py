from django.forms import ModelForm
from pyrsistent import field
from jdatetime import date
from . import models
from Codm.models import CodAccount

class CodAccountForm(ModelForm):
    class Meta:
        model = models.CodAccount
        fields = ['level', 'image', 'region', 'c', 'cp', 
        'multi_ranked', 'battle_ranked', 'battle_pass',
        'description', 'price']
