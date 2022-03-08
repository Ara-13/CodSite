from django.urls import re_path
from . import views

app_name = 'Users'

urlpatterns = [
    re_path(r'^login/$', views.LoginFunc, name="login"),
    re_path(r'^logout/$', views.LogoutFunc, name="logout"),
    re_path(r'^registration/$', views.RegisterFunc, name="signup"),
]