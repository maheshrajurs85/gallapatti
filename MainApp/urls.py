"""
URL configuration for gallapatti project.

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
from MainApp.models import Suppliers
from . import views
from .views import get_supplier_suggestions

urlpatterns = [
    path('goods/', views.GoodsView, name='GoodsView'),
    path('goods_add_row/', views.goods_add_row, name='goods_add_row'),
    
    path('suppliers/', views.SuppliersView, name='SuppliersView'),
    path('suppliers_add_row/', views.Suppliers_add_row, name='suppliers_add_row'),
    
    path('buyers/', views.BuyersView, name='BuyersView'),
    path('buyers_add_row/', views.Buyers_add_row, name='Buyers_add_row'),
    
    path('mandiExpenses/', views.MandiExpensesView, name='MandiExpenses'),
    path('expenses_add_row/', views.MandiExpenses_add_row, name='MandiExpenses_add_row'),
    
    path('update_cell/', views.update_cell, name='goods_update_cell'),
    
    path('importgoods/', views.importgoods, name='importgoods'),  # formset test 
    path('get_supplier_suggestions/', views.get_supplier_suggestions, name='get_supplier_suggestions'),
    path('get_goods_suggesions/', views.get_goods_suggesions, name='get_goods_suggesions'),
    

    path('mandi-bill-list/', views.mandi_bill_list, name='mandi_bill_list'),
    path('imported-goods-list/<str:bill_number>/', views.imported_goods_list, name='imported_goods_list'),

    path('importedgoods/', views.ImportedGoodsView, name='ImportedGoodsView'),
    path('importedgoods_add_row/', views.ImportedGoods_add_row, name='ImportedGoods_add_row'),
  
]
