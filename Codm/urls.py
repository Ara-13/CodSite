from django.urls import re_path
from . import views
from uuid import uuid1
app_name = 'Codm'

id_list = str(uuid1()).split('-')
id1, *_, id2= id_list

urlpatterns = [
    re_path(r'^$', views.home, name="home"),
    re_path(r'^Codm/codaccounts/$', views.codm, name="codm"),
    re_path(r'^Codm/codaccounts/detail/(?P<co>[0-9]{1,3})/$', views.account, name="account"),
    re_path(r'^Codm/codaccounts/publish-account/$', views.publish, name="publish-account"),

    re_path(r'^user/cart/details/$', views.user_cart, name="cart"),
    re_path(r'^user/cart/all/cartend/success/{}/{}/$'.format(id1, id2), views.cart_finished, name="cart-success"),
    re_path(r'^user/cart/details/shopping/render/ok$', views.shopping, name="shopping"),
    re_path(r'^user/addtocart/account/(?P<co>[0-9]{1,3})/$', views.addtocart, name="addtocart"),
]
