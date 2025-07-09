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

    path('visitedacompletare/', visite_non_completate, name='visite_non_completate'),
    path( 'login_auth', login_auth, name='login_auth'),
    path( 'logout', logout, name='logout'),
    path( 'login_auth_raw_unsafe', login_auth_raw_unsafe, name='login_auth_raw_unsafe'),
    path('aggiungiprenotazione', aggiungi_prenotazione, name='aggiungi_prenotazione'),
    path('referti', visualizza_referti, name='visualizza_referti'),
    path('fatture', visualizza_fatture, name='visualizza_fatture'),

    path('downloadfatturapdf/<int:numero_fattura>/', download_fattura_pdf, name='download_fattura_pdf'),

    path('dashboard_paziente', dashboard_paziente, name='dashboard_paziente'),

    path('dashboard_personale', dashboard_personale, name='dashboard_personale'),

    path('registrazione', registrazione,  name='registrazione'),

    path('visualizzaprenotazione', visualizza_prenotazione, name='visualizza_prenotazione'),

    path('gestioneprestazioni', gestione_prestazioni, name='gestione_prestazioni')




]
