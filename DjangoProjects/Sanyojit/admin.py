from django.contrib import admin
from .forms import StockCreateForm

# Register your models here.
#import
from .models import Stock

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity','last_updated']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']
#to register it with admin
admin.site.register(Stock, StockCreateAdmin)
