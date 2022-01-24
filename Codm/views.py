from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    return render(request, 'Codm/home.html')

def codm(request):
    accounts = models.CodAccount.objects.all()
    context = {
        'accounts' : account
    }
    return render(request, 'Codm/codpage.html')

def account(request, co):
    return HttpResponse('Account: {}'.format(co))