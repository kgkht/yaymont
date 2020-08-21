from django.contrib import admin
from .models import Ordering
# Register your models here.
@admin.register(Ordering)
class OrderingAdmin(admin.ModelAdmin):
    list_display = ('p_type','p_count','name', 'completed', 'pub_date')
