"""
URL configuration for FraudDetection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from FraudDetection import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="homepage"),
    path('process/', views.processClaim, name='process'),
    path('customer-login/', views.customerLogin, name='custoLogin'),
    path('garage-login/', views.garageLogin, name='garageLogin'),
    path('login-submit/', views.customerLoginSubmit, name='loginSubmit'),
    path('customer-options', views.custAfterLogin, name='custOptions'),
    path('claim-request', views.requestClaim, name='claimRequest'),
    path('customer-register', views.customerRegister, name='customerRegister'),
    path('garage-options', views.garagePage, name='garageAfterLogin'),
    path('garage-options-after-input', views.garagePageAfterInput, name='garageAfterInput'),
    path('customer-opt-validation', views.afterOPTSubmit, name='afterOTP'),
    path('about-us/',views.aboutUs, name='aboutUs'),
    path('faq-s/',views.faqs, name='faqs'),
]

