from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from django.apps import apps

from .models import *
app = apps.get_app_config('business')

# for model in app.get_models():
#     admin.site.register(model)


class DomainResource(resources.ModelResource):
    class Meta:
        model = Domain


class DomainAdmin(ImportExportModelAdmin):
    resource_class = DomainResource


admin.site.register(Domain, DomainAdmin)


class LenderResource(resources.ModelResource):
    class Meta:
        model = Lender


class LenderAdmin(ImportExportModelAdmin):
    resource_class = LenderResource


admin.site.register(Lender, LenderAdmin)


class ShortTermLoanResource(resources.ModelResource):
    class Meta:
        model = ShortTermLoan
        exclude = ('id', 'created_at', 'updated_at')


class ShortTermLoanAdmin(ImportExportModelAdmin):
    resource_class = ShortTermLoanResource


admin.site.register(ShortTermLoan, ShortTermLoanAdmin)


class InvoiceFactoringResource(resources.ModelResource):
    class Meta:
        model = InvoiceFactoring
        exclude = ('id', 'created_at', 'updated_at')


class InvoiceFactoringAdmin(ImportExportModelAdmin):
    resource_class = InvoiceFactoringResource


admin.site.register(InvoiceFactoring, InvoiceFactoringAdmin)


class InvoiceFinancingResource(resources.ModelResource):
    class Meta:
        model = InvoiceFinancing
        exclude = ('id', 'created_at', 'updated_at')


class InvoiceFinancingAdmin(ImportExportModelAdmin):
    resource_class = InvoiceFinancingResource


admin.site.register(InvoiceFinancing, InvoiceFinancingAdmin)


class EquipmentFinancingResource(resources.ModelResource):
    class Meta:
        model = EquipmentFinancing
        exclude = ('id', 'created_at', 'updated_at')


class EquipmentFinancingAdmin(ImportExportModelAdmin):
    resource_class = EquipmentFinancingResource


admin.site.register(EquipmentFinancing, EquipmentFinancingAdmin)


class LinesOfCreditResource(resources.ModelResource):
    class Meta:
        model = LinesOfCredit
        exclude = ('id', 'created_at', 'updated_at')


class LinesOfCreditAdmin(ImportExportModelAdmin):
    resource_class = LinesOfCreditResource


admin.site.register(LinesOfCredit, LinesOfCreditAdmin)


class SbaLoanResource(resources.ModelResource):
    class Meta:
        model = SbaLoan
        exclude = ('id', 'created_at', 'updated_at')


class SbaLoanAdmin(ImportExportModelAdmin):
    resource_class = SbaLoanResource


admin.site.register(SbaLoan, SbaLoanAdmin)


