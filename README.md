# OCR (Optical Character Recognition) Project

This project is a simple Optical Character Recognition (OCR) system that extracts text from images using the Tesseract OCR engine and OpenCV for image preprocessing.

## Description

This program provides a basic OCR functionality by extracting text from images. It loads an image, preprocesses it using OpenCV (grayscale conversion, and optional preprocessing steps), and then performs OCR using the Tesseract OCR engine. The extracted text is then printed to the console.

## Getting Started

### Dependencies

* Tesseract OCR
* OpenCV
* Python 3.x

### Installing

1. Install Tesseract OCR. You can download it from the [Tesseract GitHub repository.](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file)
2. Install OpenCV using pip:
```
pip install opencv-python
```
3. Install the pytesseract library:
```
pip install pytesseract
```

### Executing program

1. Clone the repository or download the Python script.
2. Ensure you have an image file (e.g., JPEG, PNG) containing text.
3. Run the script:
```
python ocr_script.py
```
4. Paste in the path to your image file when prompted by the terminal.


## Authors

* Andrew Reyes
* Github: [@areyes42](https://github.com/areyes42)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details