# Generated by Django 5.0 on 2023-12-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mandiexpenses',
            name='MandiServiceCharge',
        ),
        migrations.RemoveField(
            model_name='mandiexpenses',
            name='Wastage',
        ),
        migrations.AddField(
            model_name='mandiexpenses',
            name='AssociationFund',
            field=models.IntegerField(blank=True, default=50, null=True),
        ),
        migrations.AddField(
            model_name='mandiexpenses',
            name='MandiServiceChargeinPercentage',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name='mandiexpenses',
            name='VehicleRent',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name='mandiexpenses',
            name='WastageInKG',
            field=models.IntegerField(blank=True, default=4, null=True),
        ),
        migrations.AlterField(
            model_name='mandiexpenses',
            name='Charity',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AlterField(
            model_name='mandiexpenses',
            name='Coolie',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
