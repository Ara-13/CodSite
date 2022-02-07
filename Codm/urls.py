from django.urls import re_path
from . import views

app_name = 'Codm'

urlpatterns = [
    re_path(r'^$', views.home, name="home"),
    re_path(r'^Codm/codaccounts/$', views.codm, name="codm"),
    re_path(r'^Codm/codaccounts/detail/(?P<co>[0-9]{1,3})/$', views.account, name="account"),
    re_path(r'^Codm/codaccounts/publish-account/$', views.publish_account, name="publish-account"),
]
