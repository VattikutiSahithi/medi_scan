from django.urls import path
from . import views  

app_name = "prescriptions"  # Namespacing the app

urlpatterns = [
    path("", views.home, name="prescriptions_home"),  # Landing page
    path("upload/", views.upload_and_extract_text, name="upload_prescription"),  # Upload & OCR processing
    path("detail/<int:pk>/", views.prescription_detail, name="prescription_detail"),  # Prescription details page
]
