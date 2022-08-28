from django.contrib import admin
from .models import Report

admin.site.site_header = "Citas Cuba v 3.0.2"
admin.site.site_title = "Citas Cuba v 3.0.2"
admin.site.index_title = "Bienvenidos al sistema Citas Cuba v 3.0.2"

class ReportAdmin(admin.ModelAdmin):
    list_display=('name','last_name','is_authorized')
    search_fields = ['name']


admin.site.register(Report, ReportAdmin)
