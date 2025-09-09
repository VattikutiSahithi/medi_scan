from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from prescriptions.forms import PrescriptionForm
from prescriptions.models import Prescription
from scripts.ocr_model import extract_text  # Import OCR function

def home(request):
    """Landing page - displays latest prescription if available."""
    latest_prescription = Prescription.objects.order_by("-id").first()
    return render(request, "home.html", {"prescription": latest_prescription})

@csrf_exempt
def upload_and_extract_text(request):
    """Handles prescription image upload, processes it, extracts text, and saves it."""
    if request.method == "GET":
        form = PrescriptionForm()
        return render(request, "upload.html", {"form": form})

    if request.method == "POST" and request.FILES.get("prescription_image"):
        form = PrescriptionForm(request.POST, request.FILES)
        if form.is_valid():
            prescription = form.save()  # Save prescription instance
            image_path = prescription.prescription_image.path  # Get image path

            try:
                extracted_text = extract_text(image_path)  # Process image for OCR
                prescription.extracted_text = extracted_text
                prescription.save()  # Save extracted text to database
                return render(request, "upload.html", {"form": form, "prescription": prescription})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

def prescription_detail(request, pk):
    """Displays details of a single prescription, including extracted text."""
    prescription = get_object_or_404(Prescription, pk=pk)
    return render(request, "detail.html", {"prescription": prescription})
