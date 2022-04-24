from django.urls import URLPattern, path, include, re_path
from . import views

app_name = 'Products'

urlpatterns = [
    path('view/Our-Products/<str:pname>/', views.ProductView, name="PV"),
    path('view/Our-Products/addtocart/<str:pname>/<int:pcode>/', views.ProductAddCart, name="PAC"),
    path('view/Our-Products/removefromcart/<str:pname>/<int:pcode>/', views.ProductRemoveCart, name="PRC"),
]