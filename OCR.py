#Import Required Libraries:
# - Pillow library (PIL) for image manipulation
# - Pytesseract library for linking to Tesseract OCR library (must be installed separately)
# = tkinter for interactive window to choose image file
# - os for file manipulation

from PIL import Image
import pytesseract
import tkinter.filedialog
import os as os

#Define the Path Location of the Tesseract Install

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#Open file selection window with tkinter and choose image file
image_path = tkinter.filedialog.askopenfilename()

#Alternatively, you may define the path location of the image file to read via line below
#image_path = r"FILENAME.EXT"

#Open image with Pillow
img = Image.open(image_path)

#Define location fo Tesseract install
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

#Employ Tesseract image_to_string function to extract text
# - For pytesseract image_to_string, config = '-- psm x' denotes page segmentation mode settings as follows:<br>
#     0    Orientation and script detection (OSD) only. <br>
#     1    Automatic page segmentation with OSD. <br>
#     2    Automatic page segmentation, but no OSD, or OCR.<br>
#     3    Fully automatic page segmentation, but no OSD. (Default)<br>
#     4    Assume a single column of text of variable sizes.<br>
#     5    Assume a single uniform block of vertically aligned text.<br>
#     6    Assume a single uniform block of text.<br>
#     7    Treat the image as a single text line.<br>
#     8    Treat the image as a single word.<br>
#     9    Treat the image as a single word in a circle.<br>
#    10    Treat the image as a single character.<br>
#    11    Sparse text. Find as much text as possible in no particular order.<br>
#    12    Sparse text with OSD.<br>
#    13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.
text = pytesseract.image_to_string(img, config = '-c tessedit_char_whitelist=123456789 --psm 3')

#Preview extracted text
print(text[:-1])

#Get filename of processed image and remove period
file_name = os.path.basename(image_path)
file_name_M = file_name.replace(".","")

#Write extracted text to a new file designated by the original filename
txt_name = ("{file}_Output.txt").format(file = file_name_M)
f = open(txt_name, "a")
f.write(text)
f.close()