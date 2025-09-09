from django.contrib import admin
from .models import Prescription

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor_name', 'created_at')
    search_fields = ('patient_name', 'doctor_name')
    list_filter = ('created_at',)