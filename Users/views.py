from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Users.models import User
from Products.models import EP, Product
from Codm.models import Cart, Order, Account, Banner
from .forms import UserCreationForm, UserEditionForm
from random import randint
from datetime import date
from django.contrib import messages
from time import sleep

def LoginFunc(request):
    Page = 'login'
    message = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try: 
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'ایمیل و رمز وارد شده اشتباه است.')
        else:
            USER = authenticate(request, email=email, password=password)

            if USER:
                login(request, USER)
                messages.success(request, '.شما وارد شدید')
                return redirect('Users:UserPanel')
            else:
                messages.error(request, 'ایمیل و رمز وارد شده اشتباه است.')
    final_message = message if message != None else ''
    context = {
        'message' : final_message,
        'Page' : Page,
    }
    return render(request, 'login.html', context)

@login_required(login_url='Users:login')
def LogoutFunc(request):
    logout(request)
    messages.success(request, 'شما از حساب کاربری خود خارج شده اید.')
    return redirect('Codm:home')

def RegisterFunc(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            cart = Cart(user=user, status='fn')
            cart.save()
            login(request, user)
            message = "You Successfully logged in!"
            return redirect('Users:welcome')
    return render(request, 'signup.html', {'form' : user_form})

def WelcomeFunc(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html', {'user': request.user})
    else:
        return redirect('Users:login')

@login_required(login_url='Users:login')
def user_cart(request):
    cart = request.user.cart
    cart.save()

    cart_account = request.user.cart.account.all()
    cart_product = request.user.cart.product.all()

    for naccount in cart_account:
        if naccount.status != 'available':
            cart.final_price -= naccount.price
            cart.account.remove(naccount)
            cart.save()
            messages.error(request, 'اکانت به شماره آگهی {} قبل از نهایی شدن خرید شما فروخته یا پاک شد و بنابراین از سبد خرید شماحذف شد'.format(naccount.code))
    for nproduct in cart_product:
        if nproduct.status != 'AV':
            cart.final_price -= nproduct.price
            cart.product.remove(nproduct)
            cart.save()
            messages.error(request, 'محصول {} .دیگر موجود نیست و از سبد خرید شما حذف شد'.format(nproduct.name))      
    if cart.account.exists() or cart.product.exists():
        cart_account = request.user.cart.account.all()
        cart_product = request.user.cart.product.all()
        cart_n = cart_account.count() + cart_product.count()
        cart.save()
        context = {
            'cart' : cart,
            'cart_account' : cart_account,
            'cart_product' : cart_product,
            'n' : cart_n,
            'page' : 'cart'
        }
        return render(request, 'cart.html', context)
    else:
        return render(request, 'cart-empty.html')

@login_required(login_url='Users:login')
def cart_continue(request):
    cart = request.user.cart
    cart_account = request.user.cart.account.all()
    cart_product = request.user.cart.product.all()
    eps = request.user.ep_set.all()

    for naccount in cart_account:
        if naccount.status != 'available':
            cart.final_price -= naccount.price
            cart.account.remove(naccount)
            cart.save()
            messages.error(request, 'اکانت به شماره آگهی {} قبل از نهایی شدن خرید شما فروخته یا پاک شد و بنابراین از سبد خرید شما حذف شد'.format(naccount.code))
            return redirect('Users:cart')
    for nproduct in cart_product:
        if nproduct.status != 'AV':
            cart.final_price -= nproduct.price
            cart.product.remove(nproduct)
            cart.save()
            messages.error(request, 'محصول {} .دیگر موجود نیست و از سبد خرید حذف شد'.format(nproduct.name))
            return redirect('Users:cart')
    if cart.account.exists() or cart.product.exists():
        if request.method == 'POST':
            Type = request.POST.get('type')
            email = request.POST.get('email')
            password = request.POST.get('password')
            ep = EP(user=request.user, Type=Type, email=email, password=password)
            ep.save()
            return redirect('Users:cart_continue')


        context = {
            'cart' : cart,
            'cart_accounts' : cart_account,
            'cart_products' : cart_product,
            'EPs' : eps,
        }
        return render(request, 'shopping.html', context)
    else:
        return redirect('Users:cart')

@login_required(login_url='Users:login')
def add_account_product(request, pk, pr):
    ep = EP.objects.get(pk=pk)
    product = Product.objects.get(pk=pr)
    product.ep.add(ep)
    product.save()
    return redirect('Users:cart_continue')

@login_required(login_url='Users:login')
def cart_success(request):
    cart = request.user.cart
    if cart.status != 'f':
        return redirect('Users:cart')
    else:
        order = Order(user=request.user, order_number=randint(10000, 20000),
        factor_number=randint(20000, 30000), date=date.today())
        order1 = Order(user=request.user, order_number=randint(10000, 20000),
        factor_number=randint(20000, 30000), date=date.today())
        order.save()
        cart_account = request.user.cart.account.all()
        cart_product = request.user.cart.product.all()

        for account in cart_account:
            account.status = 'sold'
            account.order = order1
            seller = User.objects.get(email=account.seller.email)
            seller.sells += 1
            seller.save()
            account.save()
            request.user.buys += 1
            request.user.save()
        order1.save()
        #code ersal payam inja
        for product in cart_product:
            order.product.add(product)
            order.save()
            request.user.buys += 1
            request.user.save()
        #code ersal payam inja

        order1.save()
        order.save()

        cart.delete()
        new_cart = Cart(user=request.user, status='fn')
        new_cart.save()
        return redirect('Users:cart-finished', order.order_number)

@login_required(login_url='Users:login')
def cart_finished(request, order):
    user_order = Order.objects.get(order_number=order)
    if user_order.status == 'w4c':
        if user_order.product.exists():
            product = True
        else:
            product = False
        context = {
            'order' : user_order,
            'product' : product,
        }
        return render(request, 'shopping-complete.html', context)
@login_required(login_url='Users:login')
def addtocart(request, co):
    account = Account.objects.get(pk=co)
    account.save()
    cart = request.user.cart
    cart.save()
    cart.account.add(account)
    cart.final_price += account.price
    cart.save()
    messages.success(request, 'اکانت به سبد خرید شما اضافه شد!')
    return redirect('Users:cart')
@login_required(login_url='Users:login')
def removefromcart(request, co):
    account = Account.objects.get(pk=co)
    account.save()
    cart = request.user.cart
    cart.save()
    cart.final_price -= account.price
    cart.account.remove(account)
    cart.save()
    messages.success(request, 'اکانت از سبد خرید شما حذف شد!')
    return redirect('Users:cart')

@login_required(login_url='Users:login')
def shopping(request):
    cart = request.user.cart
    if cart.account != None:
        cart.status = 'f'
        cart.save()
        return redirect('Users:cart-success')
    elif cart.product != None:
        cart.status = 'f'
        cart.save()
        return redirect('Users:cart-success')
    else:
        return redirect('Users:cart')

@login_required(login_url='Users:login')
def user_panel(request):
    user = User.objects.get(username=request.user.username)
    user_phone = list(str(user.phone))[3::]
    user_phone = ''.join(user_phone)
    orders = Order.objects.filter(user__exact=user)[0:3]
    context = {
        'user' : user,
        'user_phone': user_phone,
        'orders' : orders,
        'page' : 'base',
    }
    context['suggestion'] = Account.objects.filter(status__exact='available').order_by('?')[:3]

    return render(request, 'Panel/myinfo.html', context)

@login_required(login_url='Users:login')
def user_edit(request):
    user = User.objects.get(username=request.user.username)
    form = UserEditionForm(instance=user)

    user_phone = list(str(user.phone))[3::]
    user_phone = ''.join(user_phone)
    if request.method == 'POST':
        user_form = UserEditionForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            messages.success(request, 'اطلاعات شما با موفقیت ثبت شد')
            return redirect('Users:UserPanel')
        else:
            messages.error(request, 'اشکالی در فرم شما وجود دارد!')
    context = {
        'user_phone' : user_phone,
        'user' : user,
        'form' : form,
        'page' : 'editinfo',
    }
    context['suggestion'] = Account.objects.filter(status__exact='available').order_by('?')[:3]

    return render(request, 'Panel/editinfo.html', context)

@login_required(login_url='Users:login')
def user_accounts(request):
    user = User.objects.get(username=request.user)
    user_accounts = Account.objects.filter(seller__exact=user)
    banners = Banner.objects.filter(show__exact=True)

    user_phone = list(str(user.phone))[3::]
    user_phone = ''.join(user_phone)

    context = {
        'user_phone' : user_phone,
        'user_accounts' : user_accounts,
        'page' : 'accounts',
        'n' : user_accounts.count(),
    }
    context['suggestion'] = Account.objects.filter(status__exact='available').order_by('?')[:3]

    return render(request, 'Panel/myaccounts.html', context)

@login_required(login_url='Users:login')
def user_orders(request):
    user = User.objects.get(username=request.user)
    user_orders = Order.objects.filter(user__exact=user)

    user_phone = list(str(user.phone))[3::]
    user_phone = ''.join(user_phone)

    context = {
        'user_phone' : user_phone,
        'user_orders' : user_orders,
        'page' : 'orders',
        #'sujestion' : accounts,
    }
    context['suggestion'] = Account.objects.filter(status__exact='available').order_by('?')[:3]

    return render(request, 'Panel/myorders.html', context)

@login_required(login_url='Users:login')
def UserOrderDetail(request, co):
    try:
        order = Order.objects.get(order_number=co)
    except:
        raise Http404
    else:
        products = order.product.all()
        accounts = order.account_set.all()
        
        context = {
            'order': order,
            'products' : products,
            'accounts' : accounts,
            'page': 'orders',
        }
        context['suggestion'] = Account.objects.filter(status__exact='available').order_by('?')[:3]
        
        return render(request, 'Panel/myorder_detail.html', context)


@login_required(login_url='Users:login')
def user_delete_account(request, co):
    account = Account.objects.get(code=co)
    if account.status != 'sold':
        account.status = 'canceled'
        account.save()
        return redirect('Users:UserAccounts')
    else:
        raise Http404