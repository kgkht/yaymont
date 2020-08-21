from django.db import models
from django.urls import reverse
# Create your models here.


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

    

class Ordering(models.Model):
    YMONT_TYPES = [
        ('S', 'ရိုးရိုး'),
        ('E', 'ကြက်ဉ'),
        ]
    
    order_id = models.AutoField(primary_key=True)
    p_type = models.CharField(
        'ရိုးရိုး လား ကြက်ဉလား',
        max_length=1,
        choices=YMONT_TYPES,
        default='S',
        help_text="Simple or Egg ?",
    )
    p_count = IntegerRangeField('အရေအတွက်',default=1, min_value=1, max_value=15,help_text="How Many ?")
    name = models.CharField('နာမည်အပြည့်အစုံ', max_length=120, help_text="နာမည်ဖြည့်ပါ")
    phone = models.CharField('ဖုန်းနံပါတ်', max_length=13, help_text="ဖုန်းနံပါတ်ထည့်ပေးပါ")
    completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('frontend:itemUpdate', kwargs={'pk':self.order_id})
