from django import forms
from .models import Ordering

class OrderForm(forms.ModelForm):
    class Meta:
        model = Ordering
        fields = '__all__'
        exclude = ['order_id', 'time', 'completed']
