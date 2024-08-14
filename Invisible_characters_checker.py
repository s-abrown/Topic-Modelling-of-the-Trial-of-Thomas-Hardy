import string

def find_invisible_chars(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    for i, char in enumerate(text):
        if char not in string.printable:
            print(f'Non-printable character {repr(char)} found at index {i}')


# "quote_sample does not exist in this repository, but this script is useful in case OCR_Cleaning.py contains hidden characters"
find_invisible_chars('quotes_sample.txt')
