import http
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from MainApp.models import Buyers, MandiExpenses, Suppliers, goods

# Create your views here.
def GoodsView(request):
    goodslist = goods.objects.all()
    return render(request,'goods.html',{'goodslist': goodslist} )

# Goods - Adding new row to the database 
def goods_add_row(request):
    if request.method == 'POST':
        row_id = request.POST.get('row_id')
        GoodsName = request.POST.get('GoodsName')
        FirstQualityPrice = request.POST.get('FirstQualityPrice')
        SecondQualityPrice = request.POST.get('SecondQualityPrice')
        RippedQualityPrice = request.POST.get('RippedQualityPrice')
        
        # Save the data to the database using your Django model
        new_row = goods(
            #row_id=row_id,
            GoodsName=GoodsName,
            FirstQualityPrice=FirstQualityPrice,
            SecondQualityPrice=SecondQualityPrice,
            RippedQualityPrice=RippedQualityPrice,
        )
        new_row.save()

        # Redirect back to the table view
        return redirect(GoodsView)
    else:
        # Handle other HTTP methods as needed
        return redirect(GoodsView)
    

# Goods - Editing and saving existing table data

@csrf_exempt  # Use this decorator for simplicity; consider using csrf tokens in production
def update_cell(request):
    if request.method == 'POST':
        row_id = request.POST.get('row_id')
        field = request.POST.get('field')
        value = request.POST.get('value')
        model_name = request.POST.get('tableName')
        
        # Update the data in the database using your Django model
        try:
            print('0')
            model = apps.get_model(app_label = 'MainApp', model_name = model_name)
            print('1')
            item = model.objects.get(id=row_id)
            print('2')
            #item = tableName.objects.get(id=row_id)
            setattr(item, field, value)
            item.save()
            return JsonResponse({'status': 'success'})
        except model.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        

########### Suppliers functions

def SuppliersView(request):
    supplierslist = Suppliers.objects.all()
    return render(request,'suppliers.html',{'supplierslist': supplierslist} )

def Suppliers_add_row(request):
    if request.method == 'POST':
        row_id = request.POST.get('row_id')
        SupplierName = request.POST.get('SupplierName')
        MobileNumber = request.POST.get('MobileNumber')
        FromAddress = request.POST.get('FromAddress')
        
        # Save the data to the database using your Django model
        new_row = Suppliers(
            #row_id=row_id,
            SupplierName=SupplierName,
            MobileNumber=MobileNumber,
            FromAddress=FromAddress,
        )
        new_row.save()

        # Redirect back to the table view
        return redirect(SuppliersView)
    else:
        # Handle other HTTP methods as needed
        return redirect(SuppliersView)
    
############ Buyes funcation 

def BuyersView(request):
    buyerslist = Buyers.objects.all()
    return render(request,'buyers.html',{'buyerslist': buyerslist} )

def Buyers_add_row(request):
    if request.method == 'POST':
        row_id = request.POST.get('row_id')
        BuyerName = request.POST.get('BuyerName')
        MobileNumber = request.POST.get('MobileNumber')
        FromAddress = request.POST.get('FromAddress')
        
        # Save the data to the database using your Django model
        new_row = Buyers(
            #row_id=row_id,
            BuyerName=BuyerName,
            MobileNumber=MobileNumber,
            FromAddress=FromAddress,
        )
        new_row.save()

        # Redirect back to the table view
        return redirect(BuyersView)
    else:
        # Handle other HTTP methods as needed
        return redirect(BuyersView)
    
############ Mandi Expenses funcation 

def MandiExpensesView(request):
    expenseslist = MandiExpenses.objects.all()
    return render(request,'mandiExpenses.html',{'expenseslist': expenseslist} )

def MandiExpenses_add_row(request):
    if request.method == 'POST':
        row_id = request.POST.get('row_id')
        VehicleRent = request.POST.get('VehicleRent')
        AssociationFund = request.POST.get('AssociationFund')
        Coolie = request.POST.get('Coolie')
        Charity = request.POST.get('Charity')
        WastageInKG = request.POST.get('WastageInKG')
        MandiServiceChargeinPercentage = request.POST.get('MandiServiceChargeinPercentage')
        
        # Save the data to the database using your Django model
        new_row = MandiExpenses(
            #row_id=row_id,
            VehicleRent=VehicleRent,
            AssociationFund=AssociationFund,
            Coolie=Coolie,
            Charity=Charity,
            WastageInKG=WastageInKG,
            MandiServiceChargeinPercentage=MandiServiceChargeinPercentage,
        )
        new_row.save()

        # Redirect back to the table view
        return redirect(MandiExpensesView)
    else:
        # Handle other HTTP methods as needed
        return redirect(MandiExpensesView)