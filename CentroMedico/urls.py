"""
URL configuration for CentroMedico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path

from CentroMedico.views import *


urlpatterns = [
    path('', home, name='home'),
    path( 'login', login, name='login'),


    path( 'login_auth', login_auth, name='login_auth'),

    path('aggiungiprenotazione', aggiungi_prenotazione, name='aggiungi_prenotazione'),

    path('dashboard_paziente', dashboard_paziente, name='dashboard_paziente'),

    path('visualizzaprenotazione', visualizza_prenotazione, name='visualizza_prenotazione')




]
