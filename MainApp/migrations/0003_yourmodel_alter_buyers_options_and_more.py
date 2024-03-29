# Generated by Django 5.0 on 2023-12-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_remove_mandiexpenses_mandiservicecharge_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='buyers',
            options={'ordering': ['BuyerName']},
        ),
        migrations.AlterModelOptions(
            name='suppliers',
            options={'ordering': ['SupplierName']},
        ),
    ]
