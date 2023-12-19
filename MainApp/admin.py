from django.contrib import admin
from django.db.models import ManyToManyField, ForeignKey
from .models import Buyers, ImportedGoods, MandiExpenses, Suppliers, goods
#from admin_row_actions import BaseRowActions
from django_admin_row_actions import AdminRowActionsMixin

# Register your models here.


# https://stackoverflow.com/questions/57341155/set-django-admin-to-display-all-the-columns-of-the-database





class goodsAdmin(admin.ModelAdmin):
    list_display = ('id','GoodsName', 'GoodsQuality','GoodsPrice')
    list_editable = ('GoodsPrice',)
    list_display_links = ('id','GoodsName',)
    ordering = ['id']
    class Media:
        js = ('StaticStyles/js/custom_admin.js',)
    #list_display = [field.name for field in goods._meta.get_fields() if not (field.many_to_many or isinstance(field, ForeignKey))]




admin.site.register(goods, goodsAdmin)
admin.site.register(Suppliers)
admin.site.register(Buyers)
admin.site.register(MandiExpenses)
admin.site.register(ImportedGoods)    