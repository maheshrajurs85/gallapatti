from django import forms
from django.forms import formset_factory
from .models import goods1

class GoodsForm(forms.ModelForm):
    class Meta:
        model = goods1
        fields = ['GoodsName', 'FirstQualityPrice', 'SecondQualityPrice']

GoodsFormSet = formset_factory(GoodsForm, extra=1, can_delete=True)
