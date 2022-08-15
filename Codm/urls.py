from django.urls import re_path, path
from . import views
from uuid import uuid1
app_name = 'Codm'

id_list = str(uuid1()).split('-')
id1, *_, id2= id_list

urlpatterns = [
    re_path(r'^$', views.home, name="home"),
    re_path(r'^(?P<gr>[a-z]{1,10})/Accounts/(?P<page>[0-9]{1,5})$', views.ListView, name="Game"),
    #path('<str:gr>/Accounts/Page<int:page>/', views.ListView, name="codm"),
    re_path(r'^(?P<gr>[a-z]{1,10})/Accounts/detail/(?P<co>[0-9]{1,5})/$', views.account, name="account"),
    path('<str:co>/Accounts/publish-account/', views.publish, name="publish-account"),
]
