from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from matplotlib.style import available, context
from sympy import solve_undetermined_coeffs
from . import models
from Codm.models import Order, Cart
from django.db.models import Q
from jdatetime import date
from Codm.forms import CodAccountForm, CodAccountLinkForm
#User Login
from django.contrib.auth.decorators import login_required
from django.conf import settings
User1 = settings.AUTH_USER_MODEL
from Users.models import User
#random
from random import randint

def home(request):
    context = {
        'HomePage' : True,
    }
    return render(request, 'Codm/old-home.html', context)

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


'''def publish_account(request):
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
    return render(request, 'Codm/publishaccount.html', context)'''

@login_required(login_url='Users:login')
def publish(request):
    account_number = models.CodAccount.objects.all().count()+1
    form = CodAccountForm()
    linkform = CodAccountLinkForm()
    if request.method == "POST":
        form = CodAccountForm(request.POST)
        linkform = CodAccountLinkForm(request.POST)
        if form.is_valid:
            account = form.save(commit=False)
            account.seller = request.user
            account.code = account_number
            account.save()
            link = linkform.save(commit=False)
            link.account = account
            link.save()
            return redirect('Codm:home')

    context = {
        'form' : form,
        'linkform' : linkform,
        'code' : account_number,
    }

    return render(request, 'Codm/publish.html', context)

@login_required(login_url='Users:login')
def user_cart(request):
    cart = request.user.cart
    cart.save()
    cart_account = request.user.cart.account.all()
    for account in cart_account:
        if account.status != 'available':
            cart.account.remove(account)
            cart.save()
    cart_account = request.user.cart.account.all()
    context = {
        'cart' : cart,
        'cart_account' : cart_account,
    }
    return render(request, 'Codm/cart.html', context)

@login_required(login_url='Users:login')
def cart_finished(request):
    cart = request.user.cart
    if cart.status != 'f':
        return redirect('Codm:cart')
    else:
        order = Order(user=request.user, order_number=randint(10000, 20000),
        factor_number=randint(20000, 30000), date=date.today())
        order.save()
        cart_account = request.user.cart.account.all()
        for account in cart_account:
            account.status = 'sold'
            account.final_status = 'sold'
            account.order = order
            account.save()

        order_accounts = order.codaccount_set.all()
        context = {
            'order' : order,
            'order_accounts' : order_accounts,
        }
        cart.delete()
        new_cart = Cart(user=request.user, status='fn')
        new_cart.save()
        return render(request, 'Codm/cart-success.html', context)

def addtocart(request, co):
    account = models.CodAccount.objects.get(pk=co)
    account.save()
    cart = request.user.cart
    cart.save()
    cart.account.add(account)
    cart.save()
    return redirect('Codm:cart')
    
def shopping(request):
    cart = request.user.cart
    cart.status = 'f'
    cart.save()
    return redirect('Codm:cart-success')