from django.contrib import admin
from financial.models import Fund

# Register your models here.

class FundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fund_id', 'description')

admin.site.register(Fund, FundAdmin)
