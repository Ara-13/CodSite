from django.urls import re_path
from . import views
from uuid import uuid1
app_name = 'Users'

id_list = str(uuid1()).split('-')
id1, *_, id2= id_list

urlpatterns = [
    re_path(r'^login/$', views.LoginFunc, name="login"),
    re_path(r'^logout/$', views.LogoutFunc, name="logout"),
    re_path(r'^registration/$', views.RegisterFunc, name="signup"),
    re_path(r'^welcome/$', views.WelcomeFunc, name="welcome"),

    re_path(r'^cart/details/$', views.user_cart, name="cart"),
    re_path(r'^cart/continue/UserInfo/$', views.cart_continue, name="cart_continue"),
    re_path(r'^cart/continue/UserInfo/SelectAccount/(?P<pr>[0-9]{1,10})/(?P<pk>[0-9]{1,10})$', views.add_account_product, name="add_account_product"),
    re_path(r'^cart/all/cart-end/success/{}/{}/$'.format(id1, id2), views.cart_success, name="cart-success"),
    re_path(r'^cart/success/finished/order/(?P<order>[0-9]{1,10})/$', views.cart_finished, name="cart-finished"),
    re_path(r'^cart/details/shopping/render/ok$', views.shopping, name="shopping"),
    re_path(r'^addtocart/account/(?P<co>[0-9]{1,5})/$', views.addtocart, name="addtocart"),
    re_path(r'^removefromcart/account/(?P<co>[0-9]{1,5})/$', views.removefromcart, name="removefromcart"),

    re_path(r'^MyAccount/$', views.user_panel, name="UserPanel"),
    re_path(r'^MyAccount/Myinfo/Edit/$', views.user_edit, name="UserEdit"),
    re_path(r'^MyAccount/Orders/$', views.user_orders, name="UserOrders"),
    re_path(r'^MyAccount/Orders/OrderDetail/(?P<co>[0-9]{1,10})/$', views.UserOrderDetail, name="UserOrderDetail"),
    re_path(r'^MyAccount/Accounts/$', views.user_accounts, name="UserAccounts"),
    re_path(r'^MyAccount/Accounts/DeleteAccount/(?P<co>[0-9]{1,5})/$', views.user_delete_account, name="UserAccountDelete"),
]