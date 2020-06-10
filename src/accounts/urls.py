from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('signup/',views.Register.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(),name='login') ,
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    ]