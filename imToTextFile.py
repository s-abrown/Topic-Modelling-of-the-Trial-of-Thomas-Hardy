############################################## TO EXTRACT TEXT FROM IMAGES ##############################################


from PIL import Image 
from pytesseract import pytesseract 

############################################## IMAGE TO TEXT/STRING ##############################################

# I. Defining paths to tesseract.exe and the images we will be using 
#(I don't need the path as the img file is in this present working directory)
# Making variable that will contain the entirety of the text of the trial of Thomas Hardy
thomas_hardy_trial_full_text = ""

# II. Making a loop to parse through each page created by PDF_to_JPEG.py, to then extract the text from each and append them/collect them in "file.txt"

# 613 pages/images total in Hardy's trial.
for i in range(1, 614):
# Small samples tester:
#for i in range(312,313):
    image_path = "Thomas_Hardy_Trial_Indiv_pages/page_"+str(i)+".jpg"
    # Opening the image & storing it in an image object 
    image = Image.open(image_path) 
    # Passing the image object to image_to_string() function. This function will extract the text from the image 
    text = pytesseract.image_to_string(image)
    # " " + text is so that there is a space between the final word of each page and the first word of the page that follows 
    thomas_hardy_trial_full_text += " " + text
    # "progess tracker" to keep track of things when script is running:
    print("Page : ", i)


############################################## SENDING OUTPUT STRING/TEXT TO ITS OWN TEXT FILE ##############################################

### Module 2: Sending the output string to its own text file.

# Opening the python file, to write the output and save it as a new file. It's written anew each time, bc it's through "write":
with open('file.txt', 'w') as file:
    file.write(thomas_hardy_trial_full_text)

