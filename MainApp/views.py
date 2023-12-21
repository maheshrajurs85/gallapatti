import http
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from MainApp.models import goods

# Create your views here.
def index(request):
    goodslist = goods.objects.all()
    return render(request,'index.html',{'goodslist': goodslist} )

# Goods - Adding new row to the database 
def save_row(request):
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
        return redirect(index)
    else:
        # Handle other HTTP methods as needed
        return redirect(index)
    

# Goods - Editing and saving existing table data

@csrf_exempt  # Use this decorator for simplicity; consider using csrf tokens in production
def update_cell(request):
    if request.method == 'POST':
        row_id = request.POST.get('row_id')
        field = request.POST.get('field')
        value = request.POST.get('value')

        # Update the data in the database using your Django model
        try:
            item = goods.objects.get(id=row_id)
            setattr(item, field, value)
            item.save()
            return JsonResponse({'status': 'success'})
        except goods.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})