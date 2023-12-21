# Generated by Django 5.0 on 2023-12-20 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ThatDay', models.DateField(auto_now_add=True, null=True)),
                ('OpeningBalance', models.IntegerField(blank=True, default=0, null=True)),
                ('TotalPaymentReceived', models.IntegerField(blank=True, default=0, null=True)),
                ('TotalPaymentGiven', models.IntegerField(blank=True, default=0, null=True)),
                ('TodayIncome', models.IntegerField(blank=True, default=0, null=True)),
                ('ToBank', models.IntegerField(blank=True, default=0, null=True)),
                ('ClosingBalance', models.IntegerField(blank=True, default=0, null=True)),
                ('Comment', models.TextField(blank=True, default='', help_text='Enter your comment here...', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BuyerName', models.CharField(max_length=30)),
                ('MobileNumber', models.CharField(max_length=15)),
                ('FromAddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GoodsName', models.CharField(max_length=50)),
                ('FirstQualityPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('SecondQualityPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('RippedQualityPrice', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['GoodsName'],
            },
        ),
        migrations.CreateModel(
            name='MandiExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coolie', models.IntegerField(blank=True, default=0, null=True)),
                ('Charity', models.IntegerField(blank=True, default=0, null=True)),
                ('Wastage', models.IntegerField(blank=True, default=0, null=True)),
                ('MandiServiceCharge', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupplierName', models.CharField(max_length=30)),
                ('MobileNumber', models.CharField(max_length=15)),
                ('FromAddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImportedGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImportDate', models.DateField(auto_now_add=True, null=True)),
                ('creatsCount', models.IntegerField(blank=True, default=0, null=True)),
                ('inKGs', models.IntegerField(blank=True, default=0, null=True)),
                ('GoodsPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('TotalAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('MandiExpenses', models.IntegerField(blank=True, default=0, null=True)),
                ('TobePaidToSupplier', models.IntegerField(blank=True, default=0, null=True)),
                ('BalanceToBePaid', models.IntegerField(blank=True, default=0, null=True)),
                ('SoldStatus', models.BooleanField()),
                ('BillingStatus', models.BooleanField()),
                ('DatePaid', models.DateField(null=True)),
                ('Comment', models.TextField(blank=True, default='', help_text='Enter your comment here...', null=True)),
                ('GoodsID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.goods')),
                ('SupplierID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='ExportedGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExportDate', models.DateField(auto_now_add=True, null=True)),
                ('CretesCount', models.IntegerField(blank=True, default=0, null=True)),
                ('inKGs', models.IntegerField(blank=True, default=0, null=True)),
                ('SellingPrice', models.IntegerField(blank=True, default=0, null=True)),
                ('TotalAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('MandiExpenses', models.IntegerField(blank=True, default=0, null=True)),
                ('TobeReceivedFromSupplier', models.IntegerField(blank=True, default=0, null=True)),
                ('BalanceToBeReceived', models.IntegerField(blank=True, default=0, null=True)),
                ('BillingStatus', models.BooleanField()),
                ('PaymentReceivedDate', models.DateField(null=True)),
                ('Comment', models.TextField(blank=True, default='', help_text='Enter your comment here...', null=True)),
                ('BuyerID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.buyers')),
                ('ImportedGoodID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MainApp.importedgoods')),
            ],
        ),
    ]
