try:
    from PIL import Image
except ImportError:
    import Image 

import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text=pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('TEST1.jpg')
print(info)

file = open("New.txt", "a") #a means append

file.write(info)
file.close()
print("Write Successful")

