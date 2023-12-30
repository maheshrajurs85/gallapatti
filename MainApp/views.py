import http
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from MainApp.models import Buyers, ImportedGoods, MandiExpenses, Suppliers, goods
from django.db.models import Q
from django.forms import formset_factory
from .forms import GoodsFormSet, ImportGoodsFormSet


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



from .forms import ImportGoodsFormSet

def importgoods(request):
    if request.method == 'POST':
        print(request.POST);
        

        import_date = request.POST[f'importGoods-{0}-ImportDate'];
        supplier_details = request.POST[f'importGoods-{0}-SupplierDetails'];
        supplier_id = request.POST[f'importGoods-{0}-SupplierID'];
        print(f'importGoods-{0}-ImportDate: {import_date}');
        print(f'importGoods-{0}-SupplierDetails: {supplier_details}');
        print(f'importGoods-{0}-SupplierID: {supplier_id}');
        
       

        for i in range(int(request.POST['importGoods-TOTAL_FORMS'])):
            goods_name_and_quality_i = request.POST[f'importGoods-{i}-GoodsNameAndQuality']
            goods_quantity_i = request.POST[f'importGoods-{i}-GoodsQuantity']
            measurement_units_i = request.POST[f'importGoods-{i}-MeasurementUnits']
            print(f'importGoods-{i}-GoodsNameAndQuality: {goods_name_and_quality_i}')
            print(f'importGoods-{i}-GoodsQuantity: {goods_quantity_i}')
            print(f'importGoods-{i}-MeasurementUnits: {measurement_units_i}')
            print('-' * 30)  # Separator for better readability
            



        mutable_post = request.POST.copy();

                # Add a new entry
        if ((int(request.POST['importGoods-TOTAL_FORMS'])) > 1):
            for i in range(1, int(request.POST['importGoods-TOTAL_FORMS'])):
                new_key = f'importGoods-{i}-SupplierID';
                new_value = request.POST[f'importGoods-0-SupplierID'];
                mutable_post[new_key] = new_value;

        formset = ImportGoodsFormSet(mutable_post, prefix='importGoods')
        if formset.is_valid():
            print('valid : mutable_post', mutable_post);
            for form in formset:
                # print('formmmm', form)
                print('supplier name :',form.cleaned_data.get('SupplierID', 0));
                print('supplier details : ',form.cleaned_data.get('SupplierDetails', 0));
                print('Goods Name And Quality :',form.cleaned_data.get('GoodsNameAndQuality', 0));
                print('hiddenGoodsCellName',form.cleaned_data.get('hiddenGoodsCellName', 0));
                print('GoodsQuantity', form.cleaned_data.get('GoodsQuantity', 0));
                print('MeasurementUnits', form.cleaned_data.get('MeasurementUnits', 0));
                print('date printed:',form.cleaned_data.get('ImportDate', 0));
                instance = form.save(commit=False)

                # Assign the sum to 'RippedQualityPrice'
                instance.GoodsPrice = 0
                instance.TotalAmount = 0
                instance.MandiExpenses = 0
                instance.TobePaidToSupplier = 0
                instance.BalanceToBePaid = 0
                instance.Comment = 'no Comments'
                
                

                # Save the instance
                instance.save()
                print('out side if');
            # Your processing logic here
            print('formmmm end');
            return redirect('http://127.0.0.1:8000/importgoods/')  # Replace with your actual success URL
        else:
            print('errorrrr invalid', formset.errors)
            return redirect('http://127.0.0.1:8000/importgoods/')
    else:
        formset = ImportGoodsFormSet(prefix='importGoods')

    return render(request, 'importgoods.html', {'formset': formset})





################## TEStng ######################

from django.shortcuts import render, redirect
from .forms import GoodsFormSet

def goods_formset_view(request):
    print(request);
    if request.method == 'POST':
        
        formset = GoodsFormSet(request.POST, prefix='goods')
        print(formset);
        if formset.is_valid():
            # print('request555', request);
            # print('validddd');
            # print('formset555', formset);
            for form in formset:
                # print('Form Errors:', form.errors)
                # print('form 1')
                # Calculate the sum of 'FirstQualityPrice' and 'SecondQualityPrice'
                first_quality_price = form.cleaned_data.get('FirstQualityPrice', 0)
                second_quality_price = form.cleaned_data.get('SecondQualityPrice', 0)
                ripped_quality_price = first_quality_price + second_quality_price
                print('variable:', first_quality_price,second_quality_price, ripped_quality_price)
                # Create an instance of the model
                instance = form.save(commit=False)

                # Assign the sum to 'RippedQualityPrice'
                instance.RippedQualityPrice = ripped_quality_price

                # Save the instance
                instance.save()

            return redirect('http://127.0.0.1:8000/goods-formset/')  # Replace 'success_url' with your actual success URL
        else:
            print('formsetttt invalid', formset)
            print('errorrrr invalid', formset.errors)
            print(formset.errors)
    else:
        formset = GoodsFormSet(prefix='goods')

    return render(request, 'test_forms.html', {'formset': formset})




