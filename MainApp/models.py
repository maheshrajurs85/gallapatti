from datetime import date
from pyexpat import model
from django.db import models
from django_admin_row_actions import AdminRowActionsMixin

# Create your models here.https://docs.djangoproject.com/en/5.0/ref/models/fields/#default"
class goods(models.Model):
    GoodsName = models.CharField(max_length=50)
    FirstQualityPrice = models.IntegerField(default=0, blank=True, null=True)
    SecondQualityPrice = models.IntegerField(default=0, blank=True, null=True)
    RippedQualityPrice = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        ordering = ['GoodsName'] #oder/sort by 

class Suppliers(models.Model):
    SupplierName = models.CharField(max_length=30)
    MobileNumber = models.CharField(max_length=15)
    FromAddress = models.CharField(max_length=100)
    class Meta:
        ordering = ['SupplierName'] #oder/sort by 
    
class Buyers(models.Model):
    BuyerName = models.CharField(max_length=30)
    MobileNumber = models.CharField(max_length=15)
    FromAddress = models.CharField(max_length=100)
    class Meta:
        ordering = ['BuyerName'] #oder/sort by
    
# models.py

class MandiBillSummary(models.Model):
    BillNumber = models.CharField(default='0',max_length=50)
    TotalAmount = models.IntegerField(default=0, blank=True, null=True)
    Hire = models.IntegerField(default=0, blank=True, null=True)
    Cooly = models.IntegerField(default=0, blank=True, null=True)
    AssociationFund = models.IntegerField(default=50, blank=True, null=True)
    Charity = models.IntegerField(default=100, blank=True, null=True)
    CashInPercentage = models.IntegerField(default=0, blank=True, null=True)
    MandiTotalExpenses = models.IntegerField(default=0, blank=True, null=True)
    NetTobePaidToSupplier = models.IntegerField(default=0, blank=True, null=True)
    BalanceToBePaid = models.IntegerField(default=0, blank=True, null=True)
    SoldStatus = models.BooleanField(default=False)
    BillingStatus = models.BooleanField(default=False)
    DatePaid = models.DateField(auto_now_add=False, null=True)
    Comments = models.TextField(default='', blank=True, null=True, help_text='Enter your comment here...')
    
class ImportedGoods(models.Model):
    #BillNumber = models.ForeignKey(MandiBillSummary, on_delete=models.DO_NOTHING)
    BillNumber = models.CharField(default='0',max_length=50)
    SupplierID = models.ForeignKey(Suppliers, on_delete=models.DO_NOTHING)
    ImportDate = models.DateField(auto_now_add=True, null=True)
    GoodsNameAndQuality = models.CharField(max_length=50, null=True)
    GoodsQuantity = models.IntegerField(default=0, blank=True, null=True)
    MeasurementUnits = models.CharField(default='Creats',max_length=50)
    InKgs = models.IntegerField(default=0, blank=True, null=True)
    NetInKgs = models.IntegerField(default=0, blank=True, null=True)
    GoodsPrice = models.IntegerField(default=0, blank=True, null=True)
    Amount = models.IntegerField(default=0, blank=True, null=True)
    Comments = models.TextField(default='', blank=True, null=True, help_text='Enter your comment here...')
    class Meta:
        ordering = ['id'] #oder/sort by

    def save(self, *args, **kwargs):
        # Your custom logic before saving (if needed)
        super().save(*args, **kwargs)
    
class ExportedGoods(models.Model):
    ImportedGoodID = models.ForeignKey(ImportedGoods, on_delete=models.DO_NOTHING)
    BuyerID = models.ForeignKey(Buyers,on_delete=models.DO_NOTHING)
    ExportDate = models.DateField(auto_now_add=True, null=True)
    CretesCount = models.IntegerField(default=0, blank=True, null=True)
    inKGs = models.IntegerField(default=0, blank=True, null=True)
    SellingPrice = models.IntegerField(default=0, blank=True, null=True)   #stores initially from goods table price value and later can be modified
    TotalAmount = models.IntegerField(default=0, blank=True, null=True)
    MandiExpenses = models.IntegerField(default=0, blank=True, null=True)
    TobeReceivedFromSupplier = models.IntegerField(default=0, blank=True, null=True)
    BalanceToBeReceived = models.IntegerField(default=0, blank=True, null=True)
    BillingStatus = models.BooleanField()
    PaymentReceivedDate = models.DateField(auto_now_add=False, null=True)
    Comment = models.TextField(default='', blank=True, null=True, help_text='Enter your comment here...')
    
class MandiExpenses(models.Model):
    
    VehicleRent = models.IntegerField(default=10, blank=True, null=True)
    AssociationFund = models.IntegerField(default=50, blank=True, null=True)
    Coolie = models.IntegerField(default=10, blank=True, null=True)
    Charity = models.IntegerField(default=100, blank=True, null=True)
    WastageInKG = models.IntegerField(default=4, blank=True, null=True)
    MandiServiceChargeinPercentage = models.IntegerField(default=10, blank=True, null=True)
    
class  BalanceSheet(models.Model):
    ThatDay = models.DateField(auto_now_add=True, null=True)
    OpeningBalance = models.IntegerField(default=0, blank=True, null=True)
    TotalPaymentReceived = models.IntegerField(default=0, blank=True, null=True)
    TotalPaymentGiven = models.IntegerField(default=0, blank=True, null=True)
    TodayIncome = models.IntegerField(default=0, blank=True, null=True)
    ToBank = models.IntegerField(default=0, blank=True, null=True)
    ClosingBalance = models.IntegerField(default=0, blank=True, null=True)
    Comment = models.TextField(default='', blank=True, null=True, help_text='Enter your comment here...')


    


    
    

    
    