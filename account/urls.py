"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import * # This will import all the views directly and you just type it in the urls directly
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer-view'),
    path('create_order/<str:pk>/', views.createOrder, name='create-order'),
    path('update_order/<str:pk>/', views.UpdateOrder, name='update-order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete-order'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('not_user/', views.notUserPage, name='not-user'),
    path('account/', views.accountSettings, name='account'),
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', 
    auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset.html_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'), name="password_reset_complete"),
]

