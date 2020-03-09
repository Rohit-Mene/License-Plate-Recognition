
#import cv2
#import pytesseract
##   print(pytesseract.image_to_string(images))
#image = cv2.imread("img.jpg")
#oc(image)


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# # Simple image to string
config = ('-l eng --oem 1 --psm 3')
str = pytesseract.image_to_string(Image.open('img.jpg'))
print(str)
