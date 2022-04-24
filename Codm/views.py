from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from django.contrib import messages
from Codm.models import Order, Cart, Video
from django.db.models import Q
from Codm.forms import AccountForm, AccountLinkForm, CodAccountForm, AccountImageForm, AccountVideoForm
from django.http import Http404
#User Login
from django.contrib.auth.decorators import login_required
from django.conf import settings
User1 = settings.AUTH_USER_MODEL
from Users.models import User
#random
from random import randint

def home(request):
    sliders = models.Slider.objects.filter(show__exact=True)
    sliders_count = sliders.count()

    responsivesliders = models.ResponsiveSlider.objects.filter(show__exact=True)
    responsivesliders_count = responsivesliders.count()

    banners = models.Banner.objects.filter(show__exact=True).order_by('-code')
    banners_count = banners.count()

    middle_banner= banners.filter(Type__exact='middlebanner')[:2]
    small_banner = banners.filter(Type__exact='smallbanner')[:4]

    accounts = models.Account.objects.filter(status__exact='available').order_by('-code')[:10]
    if request.user.is_authenticated:
        cart = request.user.cart
        if cart.account.exists() or cart.product.exists():
            cart_account = request.user.cart.account.all()
            cart_product = request.user.cart.product.all()
            cart_n = cart_account.count() + cart_product.count()
            cart.save()
    context = {
        'HomePage' : True,
        'sliders' : sliders[1:sliders_count+1],
        'responsivesliders' : responsivesliders[1:responsivesliders_count+1],
        'banners' : banners,
        'banners_count' : banners_count,
        's_range' : range(sliders_count-1),
        'rs_range' : range(responsivesliders_count-1),
        'b_range' : range(banners_count),
        'first_slider' : sliders[0] if sliders else None,
        'first_rs' : responsivesliders[0] if responsivesliders else None,
        'sug_accounts' : accounts,
        'middle_banners' : middle_banner,
        'small_banners' : small_banner,
    }
    return render(request, 'Codm/index.html', context)

def codm(request):
    q = request.GET.get('q')
    if q == None:
        accounts = models.Account.objects.filter(status__exact='available')
        q = 'available'
    else:
        accounts = models.Account.objects.filter(
            Q(status__exact=q) |
            Q(code__icontains=q) |
            Q(price__icontains=q)
        )
    if q == 'available' or q == 'sold' or q == 'w4p': 
        page = q
    else: 
        page = 'No-filter'
    context = {
        'accounts' : accounts,
        'main_filter' : page,
    }
    return render(request, 'Codm/products.html', context)
def account(request, co):
    account = models.Account.objects.get(pk=co)
    if account.group == 'codm':
        codaccount = models.CodAccount.objects.get(account=account)
    links = account.link_set.all()
    images = account.image_set.all()

    context = {
        'account' : account,
        'codaccount' : codaccount,
        'links' : links,
        'l_count': links.count(),
        'images' : images,
    }
    return render(request, 'Codm/single-product.html', context)

def ListView(request, gr, page):
    group = models.Account.objects.filter(group__exact=gr, status__exact='available')
    page = int(page)
    n = group.count()
    mini = 1
    if n >= 3:
        maxi = (n // 3) +2
        if page <= maxi:
            page_n = (page-1) * 3
            page_m = page_n + 3
            accounts = group[page_n:page_m]
        else: 
            raise Http404
    else:
        maxi = 1
        page = 1
        accounts = group
    context = {
        'accounts': accounts,
        'max_page' : maxi,
        'max_range' : range(page, maxi),
        'min_range' : range(1, page),
        'page' : page,
    }
    return render(request, 'Codm/products.html', context)

@login_required(login_url='Users:login')
def publish(request, co):
    availables = request.user.account_set.filter(status__exact='available').count()
    w4ps = request.user.account_set.filter(status__exact='w4p').count()
    if availables + w4ps >= 3:
        messages.error(request, 'شما نمی توانید بیش از 3 اکانت همزمان آگهی کنید. میتوانید آگهی های فعلی را پاک کنید تا بتوانید اکانت جدید آگهی کنید.')
        return redirect('Users:UserAccounts')
    account_number = models.Account.objects.all().count()+1001
    form = AccountForm()
    if co == 'Codm':
        form2 = CodAccountForm()
    videoform = AccountVideoForm()
    imageform1 = AccountImageForm()
    imageform2 = AccountImageForm()
    imageform3 = AccountImageForm()
    linkform = AccountLinkForm()
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES)
        if co == 'Codm':
            form2 = CodAccountForm(request.POST)
        videoform = AccountVideoForm(request.POST, request.FILES)
        imageform1 = AccountImageForm(request.POST, request.FILES)
        imageform2 = AccountImageForm(request.POST, request.FILES)
        imageform3 = AccountImageForm(request.POST, request.FILES)
        linkform = AccountLinkForm(request.POST)
        if form.is_valid():
            main_account = form.save(commit=False)
            main_account.seller = request.user
            main_account.code = account_number
            main_account.price += 50000
            main_account.save()
        if form2.is_valid():
            account = form2.save(commit=False)
            account.account = main_account
            account.save()
        if videoform.is_valid():
            videoaccount = videoform.save(commit=False)
            videoaccount.account = main_account
            videoaccount.save()
        if imageform1.is_valid():
            imageaccount1 = imageform1.save(commit=False)
            imageaccount2 = imageform2.save(commit=False)
            imageaccount3 = imageform3.save(commit=False)
            imageaccount1.account = main_account
            imageaccount2.account = main_account
            imageaccount3.account = main_account
            imageaccount1.save()
            imageaccount2.save()
            imageaccount3.save()
        if linkform.is_valid():
            link = linkform.save(commit=False)
            link.account = main_account
            link.save()
            return redirect('Codm:home')

    context = {
        'form' : form,
        'form2': form2,
        'videoform' : videoform,
        'imageform1' : imageform1,
        'imageform2' : imageform2,
        'imageform3' : imageform3,
        'linkform' : linkform,
        'code' : account_number,
    }

    return render(request, 'Codm/publish.html', context)

'''def publish_account(request):
    account_number = models.Account.objects.all().count()+1

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

        Account = models.Account(seller=request.user,
        level=level, 
        code=account_number, pub_date=Date, image=image,
        region=region, multi_ranked=multi_ranked,
        battle_ranked=battle_ranked,
        battle_pass=battle_pass,
        description=description,
        price=final_price)
        Account.save()
        return redirect('/Codm/Accounts/')
    return render(request, 'Codm/publishaccount.html', context)'''
