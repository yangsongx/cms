from django.contrib import admin
from financial.models import Fund, Investment

# Register your models here.

class FundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fund_id', 'description')

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fund', 'base_money', 'when', 'description')

admin.site.register(Fund, FundAdmin)
admin.site.register(Investment, InvestmentAdmin)
