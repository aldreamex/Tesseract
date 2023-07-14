# import pytesseract
from PIL import Image
import pytesseract

#img = Image.open('phone_number.png')
#img = Image.open('statya.png')
img = Image.open('rus.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split('.')[0]


#custom_config = r'--open 3 --psm 13'
custom_config = r'--open 3 --psm 6'

text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
print(text)

# with open('phone_number.txt', 'w') as text_file:
#     text_file.write(text)


with open(f'{file_name}.txt', 'w') as text_file:
      text_file.write(text)
