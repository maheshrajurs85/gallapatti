# Generated by Django 5.0 on 2024-01-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_alter_importedgoods_billingstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MandiBillSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillNumber', models.CharField(default='0', max_length=50)),
                ('TotalAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('Hire', models.IntegerField(blank=True, default=0, null=True)),
                ('Cooly', models.IntegerField(blank=True, default=0, null=True)),
                ('AssociationFund', models.IntegerField(blank=True, default=0, null=True)),
                ('Charity', models.IntegerField(blank=True, default=0, null=True)),
                ('CashInPercentage', models.IntegerField(blank=True, default=0, null=True)),
                ('MandiTotalExpenses', models.IntegerField(blank=True, default=0, null=True)),
                ('NetTobePaidToSupplier', models.IntegerField(blank=True, default=0, null=True)),
                ('BalanceToBePaid', models.IntegerField(blank=True, default=0, null=True)),
                ('SoldStatus', models.BooleanField(default=False)),
                ('BillingStatus', models.BooleanField(default=False)),
                ('DatePaid', models.DateField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='importedgoods',
            old_name='TotalAmount',
            new_name='Amount',
        ),
        migrations.RemoveField(
            model_name='importedgoods',
            name='BalanceToBePaid',
        ),
        migrations.RemoveField(
            model_name='importedgoods',
            name='BillingStatus',
        ),
        migrations.RemoveField(
            model_name='importedgoods',
            name='DatePaid',
        ),
        migrations.RemoveField(
            model_name='importedgoods',
            name='MandiExpenses',
        ),
        migrations.RemoveField(
            model_name='importedgoods',
            name='SoldStatus',
        ),
        migrations.RemoveField(
            model_name='importedgoods',
            name='TobePaidToSupplier',
        ),
        migrations.AddField(
            model_name='importedgoods',
            name='BillNumber',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='importedgoods',
            name='InKgs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='importedgoods',
            name='NetInKgs',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
