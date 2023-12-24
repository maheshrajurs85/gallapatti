import http
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from MainApp.models import Buyers, ImportedGoods, MandiExpenses, Suppliers, goods
from django.db.models import Q

# Create your views here.

######################## goods funcations ###############################################################
# 
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
    



################################################ Editing and saving existing table data#########################


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
        

################################################### Suppliers functions #####################################################

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
   
    

######################################################## Buyes funcation ################################################################

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
    


############ Mandi Expenses funcation  #########################################################################

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
    


############################################ Imported Goods funcation ############################################################################


def ImportedGoodsView(request):
    imported_goods_list = ImportedGoods.objects.all()
    return render(request,'importedgoods.html',{'imported_goods_list': imported_goods_list} )



# funcation to provide input suggestions 

def get_supplier_suggestions(request):
    #print("1")
    input_value = request.GET.get('input_value', '')
    print(input_value)
    #print("2")
    # Fetch matching suppliers from the database
    suggestions = Suppliers.objects.filter(
        Q(SupplierName__icontains=input_value) | Q(MobileNumber__icontains=input_value)
    )[:5]
    print(suggestions)
    # Create a list of supplier names
    suggestion_list = [{'id': supplier.id, 'name': supplier.SupplierName, 'mobileNumber':supplier.MobileNumber, 'address':supplier.FromAddress} for supplier in suggestions]
    print(suggestion_list)
    print('inViews')
    # Return the suggestions as JSON
    return JsonResponse({'suggestions': suggestion_list})


def get_goods_suggesions(request):
    input_value = request.GET.get('input_value', '')
    
    # Fetch matching goods from the database
    suggestions = goods.objects.filter(
        Q(GoodsName__icontains=input_value) |
        Q(FirstQualityPrice__icontains=input_value) |
        Q(SecondQualityPrice__icontains=input_value) |
        Q(RippedQualityPrice__icontains=input_value)
    )[:5]

    # Create a list of goods
    suggestion_list = [
        {
            'id': good.id,
            'name': good.GoodsName,
        }
        for good in suggestions
    ]

    # Return the suggestions as JSON
    return JsonResponse({'suggestions': suggestion_list})




def ImportedGoods_add_row(request):
    if request.method == 'POST':
        row_id = request.POST.get('row_id')
        SupplierID = request.POST.get('SupplierID')
        ImportDate = request.POST.get('ImportDate')
        GoodsID = request.POST.get('GoodsID')
        CreatsCount = request.POST.get('CreatsCount')
        InKGs = request.POST.get('InKGs')
        GoodsPrice = request.POST.get('GoodsPrice')
        TotalAmount = request.POST.get('TotalAmount')
        MandiExpenses = request.POST.get('MandiExpenses')
        TobePaidToSupplier = request.POST.get('TobePaidToSupplier')
        BalanceToBePaid = request.POST.get('BalanceToBePaid')
        SoldStatus = request.POST.get('SoldStatus')
        BillingStatus = request.POST.get('BillingStatus')
        DatePaid = request.POST.get('DatePaid')
        Comment = request.POST.get('Comment')
        
        # Save the data to the database using your Django model
        new_row = ImportedGoods(
            SupplierID=SupplierID,
            ImportDate=ImportDate,
            GoodsID=GoodsID,
            CreatsCount=CreatsCount,
            InKGs=InKGs,
            GoodsPrice=GoodsPrice,
            TotalAmount=TotalAmount,
            MandiExpenses=MandiExpenses,
            TobePaidToSupplier=TobePaidToSupplier,
            BalanceToBePaid=BalanceToBePaid,
            SoldStatus=SoldStatus,
            BillingStatus=BillingStatus,
            DatePaid=DatePaid,
            Comment=Comment,
        )
        new_row.save()

        # Redirect back to the table view
        return redirect(ImportedGoodsView)
    else:
        # Handle other HTTP methods as needed
        return redirect(ImportedGoodsView)
