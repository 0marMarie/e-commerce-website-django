from django.contrib import admin
from . import views

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'
urlpatterns = [


    path('',views.index,name='index'),
    path('cart/',views.cart,name='cart'),
    path('<slug:slug>/', views.categories, name='category'),
    path('<slug:slug>/<int:id>/', views.product_detail, name='product_detail'),
    path('search/results/', views.search , name='search')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


