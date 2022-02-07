from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from matplotlib.style import available
from sympy import solve_undetermined_coeffs
from . import models
from django.db.models import Q
from jdatetime import date
from .forms import CodAccountForm

def home(request):
    return render(request, 'Codm/home.html')

def codm(request):
    q = request.GET.get('q')
    if q == None:
        accounts = models.CodAccount.objects.filter(status__exact='available')
        q = 'available'
    else:
        accounts = models.CodAccount.objects.filter(
            Q(status__exact=q) |
            Q(code__icontains=q) |
            Q(price__icontains=q) |
            Q(region__icontains=q)
        )
    if q == 'available' or q == 'sold' or q == 'w4p': 
        page = q
    else: 
        page = 'No-filter'
    context = {
        'accounts' : accounts,
        'main_filter' : page,
    }
    return render(request, 'Codm/codpage.html', context)
def account(request, co):
    account = models.CodAccount.objects.get(pk=co)
    links = account.link_set.all()
    context = {
        'account' : account,
        'links' : links,
    }
    return render(request, 'Codm/accountview.html', context)

def publish_account(request):
    account_number = models.CodAccount.objects.all().count()+1

    context = {
        'code' : account_number,
    }
    if request.method == "POST":
        Date = date.today()
        level = request.POST.get('level')
        image = request.POST.get('image')
        video = request.POST.get('video') if request.POST.get('video') != None else None
        activision = request.POST.get('activision')
        facebook = request.POST.get('facebook')
        gmail = request.POST.get('gmail')
        apple_id = request.POST.get('apple_id')
        line = request.POST.get('line')
        region = request.POST.get('region')
        multi_ranked = request.POST.get('multi_ranked')
        battle_ranked = request.POST.get('battle_ranked')
        battle_pass = request.POST.get('battle_pass')
        description = request.POST.get('description')
        price = int(request.POST.get('price'))
        final_price = price + 50000

        Account = models.CodAccount(seller=request.user,
        level=level, 
        code=account_number, pub_date=Date, image=image,
        region=region, multi_ranked=multi_ranked,
        battle_ranked=battle_ranked,
        battle_pass=battle_pass,
        description=description,
        price=final_price)
        Account.save()
        return redirect('/Codm/codaccounts/')
    return render(request, 'Codm/publishaccount.html', context)

def publish(request):
    form = CodAccountForm()
    if request.method == "POST":
        form = CodAccountForm(request.POST)
        if form.is_valid:
            account = form.save(commit=False)

    return render(request, 'Codm/publish.html', {'form' : form,})

def login_page(request):
    pass
def user_profile(request):
    pass
def user_cart(request):
    pass