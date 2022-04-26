from django.contrib import admin
from .models import *

# Register your models here.
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('account_no', 'account_type', 'account_balance')
    
admin.site.register(Accounts)
admin.site.register(Transaction)
admin.site.register(Report)

