from PIL import Image 
from pytesseract import pytesseract 

# Defining paths to tesseract.exe 
# and the image we would be using 
#(I don't need the path as the img file is in the working directory)
image_path = r"image_to_text_test_sample.jpeg"

# Opening the image & storing it in an image object 
img = Image.open(image_path) 

# Providing the tesseract executable 
# location to pytesseract library 
#pytesseract.tesseract_cmd = path_to_tesseract 

# Passing the image object to image_to_string() function 
# This function will extract the text from the image 
text = pytesseract.image_to_string(img) 

# Displaying the extracted text 
print(text[:-1])


