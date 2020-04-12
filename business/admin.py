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

