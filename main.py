import cv2
import pytesseract
from PIL import Image

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract_executable>'

def preprocess_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding or other preprocessing techniques
    # (Add your preprocessing steps here as needed)
    
    return gray

def ocr(image_path):
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(preprocessed_image)
    
    return text

# Example usage
user_image_path = input("Enter the path to the image: ")
text = ocr(user_image_path)
print("Extracted Text:", text)
