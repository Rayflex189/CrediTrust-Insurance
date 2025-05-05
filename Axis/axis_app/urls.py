from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.LogOut, name='logout'),
    path('activate_card/', views.activate_card, name='activate_card'),
    path('account_frozen_page/', views.account_frozen_page, name='account_frozen_page'),
    path('pendingProMax/', views.pendingProMax, name='pendingProMax'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('loginview/', views.loginview, name='loginview'),
    path('register/', views.register, name='register'),
    path('reset_profile/', views.reset_profile, name='reset_profile'),
    path('linking_page/', views.linking_view, name='linking_view'),
    path('imf/', views.imf, name='imf'),
    path('tac/', views.tac, name='tac'),
    path('vat/', views.vat, name='vat'),
    path('pendingPro/', views.pendingPro, name='pendingPro'),
    path('pending/', views.pending, name='pending'),
    path('profile/', views.profile, name='profile'),
    path('loans/', views.loans, name='loans'),
    path('analytics/', views.analytics, name='analytics'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('kyc/', views.kyc, name='kyc'),
    path('bank_transfer/', views.bank_transfer, name='bank_transfer'),
    path('skrill/', views.skrill, name='skrill'),
    path('Upgrade_Account/', views.Upgrade_Account, name='Upgrade_Account'),
]
