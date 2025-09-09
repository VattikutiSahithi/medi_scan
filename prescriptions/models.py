from django.db import models

class Prescription(models.Model):
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    prescription_image = models.ImageField(upload_to='prescriptions/')
    extracted_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor_name}"
