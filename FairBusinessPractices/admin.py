from django.contrib import admin

# Register your models here.

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'dob', 'violation', 'office', 'comments', 'is_verified', 'created_ts', 'updated_ts']
    ordering = ['last_name', 'first_name', 'dob']
    search_fields = ['last_name', 'dob']
    list_per_page = 50

admin.site.register(Patient, PatientAdmin)