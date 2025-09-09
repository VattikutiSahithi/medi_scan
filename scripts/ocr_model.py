import os
import cv2
import pytesseract

# Set Tesseract OCR executable path (Modify this for your OS)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """Load and preprocess an image for OCR using OpenCV."""
    if not os.path.exists(image_path):
        raise ValueError(f"⚠️ Error: File does not exist - {image_path}")

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("⚠️ Error: Could not load image.")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding (helps with handwritten text)
    processed = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10
    )

    return processed

def extract_text(image_path):
    """Extract handwritten text from a prescription image using Tesseract OCR."""
    processed_image = preprocess_image(image_path)  # Preprocess image for better OCR

    # Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(processed_image, config="--psm 6").strip()

    return extracted_text
