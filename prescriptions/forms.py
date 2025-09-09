from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_name', 'doctor_name', 'prescription_image']

    def clean_prescription_image(self):
        image = self.cleaned_data.get('prescription_image')
        if image:
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Only PNG, JPG, and JPEG files are allowed.")
            if image.size > 5 * 1024 * 1024:  # 5 MB limit
                raise forms.ValidationError("File size must be less than 5 MB.")
        return image