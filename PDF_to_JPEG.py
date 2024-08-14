from pdf2image import convert_from_path
from PIL import Image 


# Defining path to the PDF file to convert to JPEG files
pdf_path = "Cobbett_s_Complete_Collection_of_State_T.pdf"

#Convert PDF to images: 1 JPEG per PDF page
images = convert_from_path(pdf_path)

# Save each image as a JPEG file
for i, image in enumerate(images):
    image.save(f'Thomas_Hardy_Trial_Indiv_pages/page_{i+1}.jpg', 'JPEG') 
