from django.contrib import admin
from financial.models import Fund, Investment, Summary, MoneyDetails, Outcoming
from financial.views import summary_entry

# Register your models here.

class FundAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fund_id', 'description')

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fund', 'base_money', 'when', 'description')

class OutcomingAdmin(admin.ModelAdmin):
    list_display = ('id', 'fund', 'base_money', 'who', 'when')

class MoneyDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fund', 'price', 'count', 'when')

# try override the standard admin framework
@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return summary_entry(request)

admin.site.register(Fund, FundAdmin)
admin.site.register(Investment, InvestmentAdmin)
admin.site.register(MoneyDetails, MoneyDetailsAdmin)
admin.site.register(Outcoming , OutcomingAdmin)
