from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from . import models
from django.contrib.auth.decorators import login_required
from Codm.models import Cart
from django.http import HttpResponse
from django.contrib import messages

group_list = [
    'CP', 'COC', 'CR'
]
def ProductView(request, pname):
    if pname in group_list:
        group = models.Group.objects.get(tag=pname)
        products = group.product_set.all()

        context = {
            'group': group,
            'products': products,
        }
        return render (request, 'Products/index.html', context)

@login_required(login_url='Users:login')
def ProductAddCart(request, pname, pcode):
    if pname in group_list:
        group = models.Group.objects.get(tag=pname)
        product = group.product_set.get(code=pcode)
        if product:
            cart = request.user.cart
            cart.product.add(product)
            cart.final_price += product.price
            cart.save()
            messages.success(request, 'کالا به سبد خرید شما اضافه شد!')
            return redirect('Users:cart')
        else:
            messages.error(request, 'مشکلی پیش آمده! دوباره تلاش کنید')
            return redirect('Products:PV', pname)

@login_required(login_url='Users:login')
def ProductRemoveCart(request, pname, pcode):
    if pname in group_list:
        group = models.Group.objects.get(tag=pname)
        product = group.product_set.get(code=pcode)
        if product:
            cart = request.user.cart
            cart.final_price -= product.price
            cart.product.remove(product)
            cart.save()
            messages.success(request, 'کالا از سبد خرید شما حذف شد!')
            return redirect('Users:cart')
        else:
            messages.error(request, 'مشکلی پیش آمده! دوباره تلاش کنید')
            return redirect('Products:PV', pname)

