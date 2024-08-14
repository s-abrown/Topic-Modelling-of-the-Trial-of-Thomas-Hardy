import re


############################################## STEP 1 : LINE BY LINE CLEANING ##############################################


input_filename = 'file.txt'
output_filename = 'header_filtering_test.txt'

# Open the input file and read line by line
with open(input_filename, 'r') as input_file:
    lines = input_file.readlines()

    # Parsing through the lines...
    # For "GEORGE" headers
    filtered_lines = [line for line in lines if "GEORGE" not in line]
    filtered_lines = [line for line in lines if "597}" not in line] 
    filtered_lines = [line for line in lines if "35 GRORGE Ill" not in line] 
    # Variations of "A. D." headers
    filtered_lines = [line for line in lines if "ALD." not in line]
    filtered_lines = [line for line in filtered_lines if "A. D" not in line]
    filtered_lines = [line for line in filtered_lines if "A.D" not in line]
    filtered_lines = [line for line in filtered_lines if "A, D" not in line]
    filtered_lines = [line for line in filtered_lines if "ASD" not in line]
    filtered_lines = [line for line in filtered_lines if "Ae B." not in line]
    filtered_lines = [line for line in filtered_lines if "Ae De" not in line]
    # Variations of "VOL" headers
    filtered_lines = [line for line in filtered_lines if "VOL " not in line]
    filtered_lines = [line for line in filtered_lines if "VOL." not in line]
    filtered_lines = [line for line in filtered_lines if "VOL," not in line]
    # # Variations of "trial of thomas hardy" headers
    filtered_lines = [line for line in filtered_lines if "Trial of Th" not in line] # 
    filtered_lines = [line for line in filtered_lines if "Phomas" not in line]
    filtered_lines = [line for line in filtered_lines if "Chomas" not in line]
    filtered_lines = [line for line in filtered_lines if "Fhomas H" not in line]
    filtered_lines = [line for line in filtered_lines if "iat of Tho" not in line]
    filtered_lines = [line for line in filtered_lines if "Yrial" not in line]
    filtered_lines = [line for line in filtered_lines if "‘vial " not in line]
    filtered_lines = [line for line in filtered_lines if "Frial" not in line]
    filtered_lines = [line for line in filtered_lines if "Triai" not in line]
    filtered_lines = [line for line in filtered_lines if "Lrial" not in line] 
    filtered_lines = [line for line in filtered_lines if "Triak" not in line]
    # Variations of "for High Treason" & some more "A. D." variations
    filtered_lines = [line for line in filtered_lines if "High Tr" not in line] # I changed it to High Tr instead of High T
    filtered_lines = [line for line in filtered_lines if "or High" not in line]
    filtered_lines = [line for line in filtered_lines if "$75)" not in line]
    filtered_lines = [line for line in filtered_lines if "A. 'D" not in line]
    filtered_lines = [line for line in filtered_lines if " D. 1794" not in line]
    filtered_lines = [line for line in filtered_lines if "D. 1794" not in line] 
    filtered_lines = [line for line in filtered_lines if "179%" not in line]
    # Variations of misc. stuff
    filtered_lines = [line for line in filtered_lines if "Google" not in line]
    filtered_lines = [line for line in filtered_lines if "1287]" not in line]
    filtered_lines = [line for line in filtered_lines if "1373" not in line]
    filtered_lines = [line for line in filtered_lines if "748" not in line]
    filtered_lines = [line for line in filtered_lines if "Taken in short-hand by Joseph Gurncy" not in line]
    # Variations of Vol. for footnotes
    filtered_lines = [line for line in filtered_lines if "See Vol." not in line]
    filtered_lines = [line for line in filtered_lines if "of this Collection" not in line]
    filtered_lines = [line for line in filtered_lines if "See it in" not in line]
    filtered_lines = [line for line in filtered_lines if "See his trial" not in line]
    filtered_lines = [line for line in filtered_lines if "See the Trial" not in line]
    filtered_lines = [line for line in filtered_lines if "See Mr." not in line]
    filtered_lines = [line for line in filtered_lines if "ante," not in line]
    filtered_lines = [line for line in filtered_lines if "See Mr." not in line] # Vol., Vol, See sir Walter, * I have been indulged, 's trial, 
    filtered_lines = [line for line in filtered_lines if "As to this see" not in line]
    filtered_lines = [line for line in filtered_lines if "son was then" not in line]
    filtered_lines = [line for line in filtered_lines if "ante Vol." not in line]
    filtered_lines = [line for line in filtered_lines if "ante Baek" not in line]
    filtered_lines = [line for line in filtered_lines if "See Lord Chief Justice" not in line]
    filtered_lines = [line for line in filtered_lines if "See lord" not in line] 
    filtered_lines = [line for line in filtered_lines if "See Burke" not in line]
    filtered_lines = [line for line in filtered_lines if "See the case" not in line]
    filtered_lines = [line for line in filtered_lines if "See his" not in line]
    filtered_lines = [line for line in filtered_lines if "et seq." not in line]
    filtered_lines = [line for line in filtered_lines if "see also" not in line]
    filtered_lines = [line for line in filtered_lines if "Sec the Debate" not in line]
    filtered_lines = [line for line in filtered_lines if "Parl. Hist." not in line]
    filtered_lines = [line for line in filtered_lines if "See also" not in line]
    filtered_lines = [line for line in filtered_lines if "Burke’s Works" not in line]
    filtered_lines = [line for line in filtered_lines if "Burke's Works" not in line]
    filtered_lines = [line for line in filtered_lines if "1908. are" not in line]
    filtered_lines = [line for line in filtered_lines if "the Sheriffs of Bristol" not in line]
    filtered_lines = [line for line in filtered_lines if "8vo. ed. " not in line]
    filtered_lines = [line for line in filtered_lines if "in this Collection" not in line]
    filtered_lines = [line for line in filtered_lines if "see the speech" not in line]
    filtered_lines = [line for line in filtered_lines if "ante, " not in line]
    filtered_lines = [line for line in filtered_lines if "case of captain Johnston" not in line]
    filtered_lines = [line for line in filtered_lines if "A. &cott, p. 383." not in line]
    filtered_lines = [line for line in filtered_lines if "Hinchcliffe, Shipley." not in line]
    filtered_lines = [line for line in filtered_lines if "See it" not in line]
    filtered_lines = [line for line in filtered_lines if "Sce also" not in line]
    filtered_lines = [line for line in filtered_lines if "Dammaree’s case" not in line]
    filtered_lines = [line for line in filtered_lines if "p. 975" not in line]
    filtered_lines = [line for line in filtered_lines if "cited by Mr." not in line]
    filtered_lines = [line for line in filtered_lines if "P.C. " not in line]
    filtered_lines = [line for line in filtered_lines if "Cro. Car" not in line]
    filtered_lines = [line for line in filtered_lines if " ant," not in line]
    filtered_lines = [line for line in filtered_lines if " Vol. " not in line]
    filtered_lines = [line for line in filtered_lines if "bis trial" not in line]
    filtered_lines = [line for line in filtered_lines if "Bee his" not in line]
    filtered_lines = [line for line in filtered_lines if "CoHeetion" not in line] 
    filtered_lines = [line for line in filtered_lines if "Perens" not in line]
    filtered_lines = [line for line in filtered_lines if "Mr. Gibbs fainted" not in line]
    filtered_lines = [line for line in filtered_lines if "minutes having recovered" not in line]
    filtered_lines = [line for line in filtered_lines if "oe a ec ae" not in line]
    filtered_lines = [line for line in filtered_lines if "See-Vol. 9, p. 608" not in line]
    filtered_lines = [line for line in filtered_lines if "9, p. 636," not in line]
    filtered_lines = [line for line in filtered_lines if "j Pemberton." not in line]
    filtered_lines = [line for line in filtered_lines if "* Sir John Mitford." not in line]
    filtered_lines = [line for line in filtered_lines if "Sce the case of lord" not in line]
    filtered_lines = [line for line in filtered_lines if "See the speech of" not in line]
    filtered_lines = [line for line in filtered_lines if "1410, 1411." not in line]
    filtered_lines = [line for line in filtered_lines if "See the Proceedings against king Ed" not in line]
    filtered_lines = [line for line in filtered_lines if "See the Articles of Accusation against" not in line]
    filtered_lines = [line for line in filtered_lines if "Vol. 1, p. 135." not in line]
    filtered_lines = [line for line in filtered_lines if "p. 47." not in line]
    filtered_lines = [line for line in filtered_lines if "ee ee" not in line]
    filtered_lines = [line for line in filtered_lines if "Here Mr. Solicitor General was inter" not in line]
    filtered_lines = [line for line in filtered_lines if "by a flow of tears." not in line]
    filtered_lines = [line for line in filtered_lines if "abitants wish to" not in line]
    filtered_lines = [line for line in filtered_lines if "Foster's Crown Law" not in line]
    filtered_lines = [line for line in filtered_lines if "chap. 1, sec. 2, p. 194," not in line]
    filtered_lines = [line for line in filtered_lines if "Hale’s Pleas of the Crown" not in line]
    filtered_lines = [line for line in filtered_lines if "Foster’s Crown Law" not in line]
    filtered_lines = [line for line in filtered_lines if "sect. 3." not in line]
    filtered_lines = [line for line in filtered_lines if "ed. of 1778" not in line]
    filtered_lines = [line for line in filtered_lines if "In 1803 appointed Recorder of Bombay" not in line]
    filtered_lines = [line for line in filtered_lines if "which occasion he received the honour" not in line]
    filtered_lines = [line for line in filtered_lines if "knighthood. :" not in line]
    filtered_lines = [line for line in filtered_lines if "Vol. " not in line]
    filtered_lines = [line for line in filtered_lines if "391, :" not in line]
    filtered_lines = [line for line in filtered_lines if "p. 283," not in line]
    filtered_lines = [line for line in filtered_lines if "———$ $e" not in line]
    filtered_lines = [line for line in filtered_lines if "The case of Sayre v. the earl of Roch" not in line]
    filtered_lines = [line for line in filtered_lines if "ford is reported in Vol, 20," not in line] #! warning: could not capture "lection. ;"
    filtered_lines = [line for line in filtered_lines if "416, 1 28, after know tnsert what," not in line]
    filtered_lines = [line for line in filtered_lines if "P. 411.1. 24 from bottom, after paragraph" not in line]
    filtered_lines = [line for line in filtered_lines if "insert by paragraph. ~" not in line]
    filtered_lines = [line for line in filtered_lines if "p. 1299." not in line]
    filtered_lines = [line for line in filtered_lines if "trial and conviction for perjury, p. 1166," not in line]
    filtered_lines = [line for line in filtered_lines if "p. 1315." not in line]
    filtered_lines = [line for line in filtered_lines if "the New Parliament" not in line]
    filtered_lines = [line for line in filtered_lines if "aera eine eee" not in line]
    filtered_lines = [line for line in filtered_lines if "Vol," not in line]
    filtered_lines = [line for line in filtered_lines if "3A ." not in line]
    filtered_lines = [line for line in filtered_lines if "0. ." not in line]
    filtered_lines = [line for line in filtered_lines if "p. 1333." not in line]
    filtered_lines = [line for line in filtered_lines if "a ah cee" not in line]
    filtered_lines = [line for line in filtered_lines if "p. 577." not in line]
    filtered_lines = [line for line in filtered_lines if "[lor" not in line]
    filtered_lines = [line for line in filtered_lines if "p. 659." not in line]
    filtered_lines = [line for line in filtered_lines if "cross-examination of George" not in line]
    filtered_lines = [line for line in filtered_lines if "digg 9" not in line]
    filtered_lines = [line for line in filtered_lines if "ADOW98 STA" not in line]
    #filtered_lines = [line for line in filtered_lines if "" not in line]

    # Looping through the text to find all lines which DO NOT contain "GEORGE" and other header variations etc.
    filtered_lines_without_GEORGE = []

    for line in filtered_lines:
        if "GEORGE" not in line:
            filtered_lines_without_GEORGE += [line]
            # Write the filtered lines to the output file

# /!\ Care with indentation here – keep out of OUT OF THE GEORGE LOOP            
with open(output_filename, 'w') as file:
# filtered_lines_
    file.writelines(filtered_lines_without_GEORGE)

print("     /✓\        LINE BY LINE CLEANING COMPLETE --> See header_filtering_test.txt for raw output")




############################################## STEP 2 : REGEX CLEANING ##############################################


# Define the function to clean the content using Regex
def cleanWithRegex(text_content):
    # Define Regex for matching the pattern you want to remove
    cleaned_content = text_content
    #? Pattern 1 blank test pattern
    #regex_pattern1 = r''
    #cleaned_content = re.sub(regex_pattern1, '', cleaned_content)
    # Pattern 2
    regex_pattern2 = r'^\s\d{3}\].*$'
    cleaned_content = re.sub(regex_pattern2, '', cleaned_content, flags=re.MULTILINE) #* works in cleaned_with_Regex.txt
    # Pattern 3
    regex_pattern3 = r'^[A-Za-z0-9]\.$'
    cleaned_content = re.sub(regex_pattern3, '', cleaned_content, flags=re.MULTILINE) #* idem
    # Pattern 4
    regex_pattern4 = r'\s\d{3}\).*'
    cleaned_content = re.sub(regex_pattern4, '', cleaned_content) #*
    # Pattern 5
    regex_pattern5 = r'\s\d{3}(\)|\}.*)'
    cleaned_content = re.sub(regex_pattern5, '', cleaned_content) #*
    # Pattern 6
    regex_pattern6 = r'^\[\d+.*$'
    cleaned_content = re.sub(regex_pattern6, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 7 #? for digit-only lines:
    regex_pattern7 = r"^\d+$"
    cleaned_content = re.sub(regex_pattern7, '', cleaned_content, flags=re.MULTILINE)  #*
    # Pattern 8
    regex_pattern8 = r"^.\.$"
    cleaned_content = re.sub(regex_pattern8, '', cleaned_content, flags=re.DOTALL) #*
    # Pattern 9 #? to delete all random single characters/symbols/digits on lines
    regex_pattern9 = r"^.$"
    cleaned_content = re.sub(regex_pattern9, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 10 #? for variations of single digit and capital letter
    regex_pattern10 = r'^\d{1}[A-Z]$'
    cleaned_content = re.sub(regex_pattern10, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 11
    regex_pattern11 = r"©\s"
    cleaned_content = re.sub(regex_pattern11, '', cleaned_content) #*
    # Pattern 12
    regex_pattern12 = r"©"
    cleaned_content = re.sub(regex_pattern12, '', cleaned_content) #*
    # Pattern 13 
    regex_pattern13 = r"§"
    cleaned_content = re.sub(regex_pattern13, '', cleaned_content) #*
    # Pattern 14
    regex_pattern14 = r"%"
    cleaned_content = re.sub(regex_pattern14, '', cleaned_content) #*
    # Pattern 15
    regex_pattern15 = r"^\d+s$" 
    cleaned_content = re.sub(regex_pattern15, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 16 #? was a spare free space so I'm popping this here
    regex_pattern16 = r"(evidence)\.~-(he says)"
    cleaned_content = re.sub(regex_pattern16, r"\1, \2", cleaned_content) #*
    # Pattern 17
    regex_pattern17 = r"^[0,9999]\.$"
    cleaned_content = re.sub(regex_pattern17, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 18 #? for correcting spelling of Thomas Hardy
    #regex_pattern18 = r"T([a-z]{3})as\sHarpy"
    #cleaned_content = re.sub(regex_pattern18, 'Thomas Hardy', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 19 #? for correcting spelling of Thomas Hardy  Also there's an instance of it spelled "Happy"
    #regex_pattern19 = r"\sHarpy"
    #cleaned_content = re.sub(regex_pattern19, ' Hardy', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 20 
    regex_pattern20 = r"^\[.*\]$"
    cleaned_content = re.sub(regex_pattern20, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 21 
    regex_pattern21 = r"^\[.*(\}|\))$"
    cleaned_content = re.sub(regex_pattern21, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 22
    regex_pattern22 = r'\s¢\s'
    cleaned_content = re.sub(regex_pattern22, '', cleaned_content) #*
    # Pattern 23
    regex_pattern23 = r'\*¢\s'
    cleaned_content = re.sub(regex_pattern23, '', cleaned_content) #*
    # Pattern 24
    regex_pattern24 = r'_\s' 
    cleaned_content = re.sub(regex_pattern24, '', cleaned_content) #*
    # Pattern 25
    regex_pattern25 = r'\s_\s' 
    cleaned_content = re.sub(regex_pattern25, '', cleaned_content) #*
    # Pattern 26
    regex_pattern26 = r'\s_' 
    cleaned_content = re.sub(regex_pattern26, '', cleaned_content) #*
    # Pattern 27
    regex_pattern27 = r'__' 
    cleaned_content = re.sub(regex_pattern27, '', cleaned_content) #*
    # Pattern 28 #? _ often mistakenly placed instead of \s hence why it's here replaced with a whitespace
    regex_pattern28 = r'_'
    cleaned_content = re.sub(regex_pattern28, ' ', cleaned_content) #*
    # Pattern 29 #? Making executive decision to delete all > there is no discernible pattern when it comes to its mistaken inclusion by OCR
    regex_pattern29 = r'>'
    cleaned_content = re.sub(regex_pattern29, '', cleaned_content) #*
    # Pattern 30 #? to correct some answers given in "dialog" with witnesses or other scenarios 
    regex_pattern30 = r'>—'
    cleaned_content = re.sub(regex_pattern30, '—', cleaned_content) #*
    # Pattern 31
    regex_pattern31 = r'<' #? idem as 29
    cleaned_content = re.sub(regex_pattern31, '', cleaned_content) #*
    # Pattern 32
    regex_pattern32 = r'\\'
    cleaned_content = re.sub(regex_pattern32, '', cleaned_content) #*
    # Pattern 33 #? too many –– (2 – dashes) with \s
    regex_pattern33 = r'\s(—{2,})\s'
    cleaned_content = re.sub(regex_pattern33, '', cleaned_content) #*
    # Pattern 34 #? stray noise
    regex_pattern34 = r'^.\]$'
    cleaned_content = re.sub(regex_pattern34, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 35
    regex_pattern35 = r'\s=\s'
    cleaned_content = re.sub(regex_pattern35, '', cleaned_content) #*
    # Pattern 36
    regex_pattern36 = r'\s=='
    cleaned_content = re.sub(regex_pattern36, '', cleaned_content) #*
    # Pattern 37
    regex_pattern37 = r'='
    cleaned_content = re.sub(regex_pattern37, '', cleaned_content) #*
    # Pattern 38
    regex_pattern38 = r'¢a'
    cleaned_content = re.sub(regex_pattern38, 'ca', cleaned_content)
    # Pattern 38b
    regex_pattern38b = r'¢o\s'
    cleaned_content = re.sub(regex_pattern38b, 'to ', cleaned_content)
    # Pattern 38c
    regex_pattern38c = r'\s¢\s'
    cleaned_content = re.sub(regex_pattern38c, '', cleaned_content)
    # Pattern 38c
    regex_pattern38d = r'¢([A-Z])'
    cleaned_content = re.sub(regex_pattern38d, '\1', cleaned_content)
    # Pattern 38c
    regex_pattern38e = r'¢ohcessions'
    cleaned_content = re.sub(regex_pattern38e, 'concessions', cleaned_content)
    # Pattern 38c
    regex_pattern38c = r'¢o'
    cleaned_content = re.sub(regex_pattern38c, 'do', cleaned_content)
    # Pattern 39
    regex_pattern39 = r'\s°'
    cleaned_content = re.sub(regex_pattern39, '', cleaned_content) #*
    # Pattern 40
    regex_pattern40 = r'°'
    cleaned_content = re.sub(regex_pattern40, '', cleaned_content) #*
    # Pattern 41
    regex_pattern41 = r'\s®\s'
    cleaned_content = re.sub(regex_pattern41, '', cleaned_content) #*
    # Pattern 42
    regex_pattern42 = r'®'
    cleaned_content = re.sub(regex_pattern42, '', cleaned_content) #*
    # Pattern 43 #? to correct single [ which replaced I
    regex_pattern43 = r'\s\[\s'
    cleaned_content = re.sub(regex_pattern43, 'I', cleaned_content) #*
    # Pattern 44 #? idem for { replacing I
    regex_pattern44 = r'\s\{\s' 
    cleaned_content = re.sub(regex_pattern44, '', cleaned_content) #*
    # Pattern 45 #? to correct "I am"
    regex_pattern45 = r'\s\|\sam'
    cleaned_content = re.sub(regex_pattern45, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 46
    regex_pattern46 = r'\s\|\s' 
    cleaned_content = re.sub(regex_pattern46, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 47
    regex_pattern47 = r'\s\|$'
    cleaned_content = re.sub(regex_pattern47, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 48
    regex_pattern48 = r'\s\|(\.|,)'
    cleaned_content = re.sub(regex_pattern48, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 49
    regex_pattern49 = r'\s\|'
    cleaned_content = re.sub(regex_pattern49, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 50
    regex_pattern50 = r'\s\.$'
    cleaned_content = re.sub(regex_pattern50, '', cleaned_content, flags=re.MULTILINE) #*
    #! Pattern 51
    #!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #regex_pattern51 = r'^\*\s' #! careful
    #cleaned_content = re.sub(regex_pattern51, '', cleaned_content, flags=re.MULTILINE)
    # Pattern 52 #? to fix some full stops, replace with single .
    regex_pattern52 = r'\.\s\.\s\.'
    cleaned_content = re.sub(regex_pattern52, '.', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 53 #? idem, replace with single .
    regex_pattern53 = r'\.\s\.$'
    cleaned_content = re.sub(regex_pattern53, '.', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 54 #? idem, replacing with single .
    regex_pattern54 = r'\.\s\.'
    cleaned_content = re.sub(regex_pattern54, '.', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 55 #? to DELETE floating full stops so NO replacing with .
    regex_pattern55 = r'\s\.$'
    cleaned_content = re.sub(regex_pattern55, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 56 #? to DELETE full stops at start of lines
    regex_pattern56 = r'^\.\s'
    cleaned_content = re.sub(regex_pattern56, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 57 #? to DELETE full stops at start of lines
    regex_pattern57 = r'^\.\s'
    cleaned_content = re.sub(regex_pattern57, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 58 #? to delete TM
    regex_pattern58 = r'.\s™\s'
    cleaned_content = re.sub(regex_pattern58, '', cleaned_content) #*
    # Pattern 59 #? to delete TM
    regex_pattern59 = r'\s™'
    cleaned_content = re.sub(regex_pattern59, '', cleaned_content) #*
    # Pattern 60 #? to delete TM
    regex_pattern60 = r'™'
    cleaned_content = re.sub(regex_pattern60, '', cleaned_content) #*
    # Pattern 61 #? to DELETE full stop at start of lines again
    regex_pattern61 = r'\.\s\.'
    cleaned_content = re.sub(regex_pattern61, '', cleaned_content) #*
    # Pattern 62
    regex_pattern62 = r'^\)\s'
    cleaned_content = re.sub(regex_pattern62, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 63
    regex_pattern63 = r'^\}\s'
    cleaned_content = re.sub(regex_pattern63, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 64
    regex_pattern64 = r'^\]\s'
    cleaned_content = re.sub(regex_pattern64, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 65 #? single letter on line (lowercaps)
    regex_pattern65 = r'^([a-z])$'
    cleaned_content = re.sub(regex_pattern65, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 66 #? single letter on line (all caps)
    regex_pattern66 = r'^([A-Z])$'
    cleaned_content = re.sub(regex_pattern66, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 67
    regex_pattern67 = r'^\(\d+'
    cleaned_content = re.sub(regex_pattern67, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 67
    regex_pattern67 = r'^\{\d+'
    cleaned_content = re.sub(regex_pattern67, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 68 #? replacing some whitespaces that had been corrupted
    regex_pattern68 = r'\s\+\s'
    cleaned_content = re.sub(regex_pattern68, ' ', cleaned_content) #*
    # Pattern 69
    regex_pattern69 = r'\s\+$'
    cleaned_content = re.sub(regex_pattern69, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 70
    regex_pattern69 = r'(?![A-Za-z])\+'
    cleaned_content = re.sub(regex_pattern69, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 71
    regex_pattern71 = r'\$\s'
    cleaned_content = re.sub(regex_pattern71, '', cleaned_content) #*
    # Pattern 72
    regex_pattern72 = r'£\s'
    cleaned_content = re.sub(regex_pattern72, '', cleaned_content) #*
    # Pattern 73
    regex_pattern73 = r'£v1'
    cleaned_content = re.sub(regex_pattern73, '', cleaned_content) #*
    # Pattern 74
    regex_pattern74 = r'£'
    cleaned_content = re.sub(regex_pattern74, '', cleaned_content) #*
    # Pattern 75
    regex_pattern75 = r'\.\.\.'
    cleaned_content = re.sub(regex_pattern75, '.', cleaned_content) #*
    # Pattern 76
    regex_pattern76 = r'\s/\s'
    cleaned_content = re.sub(regex_pattern76, '', cleaned_content) #*
    # Pattern 77
    regex_pattern77 = r'/'
    cleaned_content = re.sub(regex_pattern77, '', cleaned_content) #*
    # Pattern 78
    regex_pattern78 = r'@'
    cleaned_content = re.sub(regex_pattern78, 'a', cleaned_content) #*
    # Pattern 79
    regex_pattern79 = r'é'
    cleaned_content = re.sub(regex_pattern79, 'e', cleaned_content) #*
    # Pattern 80 #? replaced by space given the context
    regex_pattern80 = r'\s»\s'
    cleaned_content = re.sub(regex_pattern80, ' ', cleaned_content) #*
    # Pattern 81
    regex_pattern81 = r'»\s(?![A-Z])'
    cleaned_content = re.sub(regex_pattern81, '', cleaned_content) #*
    # Pattern 82 #? replaced by space given the context
    regex_pattern82 = r'»'
    cleaned_content = re.sub(regex_pattern82, '', cleaned_content) #*
    # Pattern 82 #? replaced by space given context
    regex_pattern82 = r'\s«\s'
    cleaned_content = re.sub(regex_pattern82, ' ', cleaned_content) #*
    # Pattern 83 #? floating lower cap and high cap
    regex_pattern83 = r'^(aA|oO)$'
    cleaned_content = re.sub(regex_pattern83, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 84 
    regex_pattern84 = r'^(Ee|Ss)$'
    cleaned_content = re.sub(regex_pattern84, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 85 #? Deleting full stops at start of lines
    regex_pattern85 = r'^\.'
    cleaned_content = re.sub(regex_pattern85, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 86
    regex_pattern86 = r'\s#\s'
    cleaned_content = re.sub(regex_pattern86, 'a', cleaned_content) #*
    # Pattern 87
    regex_pattern87 = r'\s#'
    cleaned_content = re.sub(regex_pattern87, '', cleaned_content) #*
    # Pattern 88
    regex_pattern88 = r'#\s'
    cleaned_content = re.sub(regex_pattern88, '', cleaned_content) #*
    # Pattern 89
    regex_pattern89 = r'#'
    cleaned_content = re.sub(regex_pattern89, '', cleaned_content) #*
    # Pattern 90 #? for : at start of lines 
    regex_pattern90 = r'^:\s'
    cleaned_content = re.sub(regex_pattern90, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 91 #? correcting some full stops (replacing with full stop)
    regex_pattern91 = r'\.:$'
    cleaned_content = re.sub(regex_pattern91, '.', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 92 #? commas at start of lines
    regex_pattern92 = r'^,\s'
    cleaned_content = re.sub(regex_pattern92, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 93 #? deleting random commas and ;
    regex_pattern93 = r'\s,\s;'
    cleaned_content = re.sub(regex_pattern93, '', cleaned_content) #*
    # Pattern 94 #? deleting at start of line
    regex_pattern94 = r'^,'
    cleaned_content = re.sub(regex_pattern94, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 95 #? deleting full stops at start of lines
    regex_pattern95 = r'^\.'
    cleaned_content = re.sub(regex_pattern95, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 96 #? deleting full stops at start of lines
    regex_pattern96 = r'^\.\s'
    cleaned_content = re.sub(regex_pattern96, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 97 #? deleting floating double low caps letters on single line
    regex_pattern97 = r'^([a-z])\1$'
    cleaned_content = re.sub(regex_pattern97, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 98 #? deleting floating double low caps letters on single line
    regex_pattern98 = r'^([A-Z])$' 
    cleaned_content = re.sub(regex_pattern98, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 99
    regex_pattern99 = r'^([a-z])$'
    cleaned_content = re.sub(regex_pattern99, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 100
    regex_pattern100 = r'^ost,' 
    cleaned_content = re.sub(regex_pattern100, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 101
    regex_pattern101 = r'^post\.$' 
    cleaned_content = re.sub(regex_pattern101, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 102
    regex_pattern102 = r'\{.*\}' 
    cleaned_content = re.sub(regex_pattern102, '', cleaned_content) #*
    # Pattern 103
    regex_pattern103 = r'\{' 
    cleaned_content = re.sub(regex_pattern103, '', cleaned_content) #*
    # Pattern 104
    regex_pattern104 = r'^art\sin' 
    cleaned_content = re.sub(regex_pattern104, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 105
    regex_pattern105 = r'^em$' 
    cleaned_content = re.sub(regex_pattern105, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 106
    regex_pattern106 = r'^fl$' 
    cleaned_content = re.sub(regex_pattern106, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 106 #? Correcting "sce" to see - recurring error
    regex_pattern107 = r'\ssce\s' 
    cleaned_content = re.sub(regex_pattern107, 'see', cleaned_content, flags=re.DOTALL) #*
    # Pattern 107
    regex_pattern107 = r'\$' 
    cleaned_content = re.sub(regex_pattern107, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 108
    regex_pattern108 = r'€\s' 
    cleaned_content = re.sub(regex_pattern108, '', cleaned_content) #*
    # Pattern 109
    regex_pattern109 = r'€' 
    cleaned_content = re.sub(regex_pattern109, '', cleaned_content) #*
    # Pattern 110 #? To correct -1 to -I
    regex_pattern110 = r'-1' 
    cleaned_content = re.sub(regex_pattern110, '-I', cleaned_content, flags=re.DOTALL) #*
    # Pattern 111 #? will be esp relevant later when we fix em dashes, this is pre-emptive cleaning
    regex_pattern111 = r'~-' 
    cleaned_content = re.sub(regex_pattern111, '–', cleaned_content, flags=re.DOTALL) #*
    # Pattern 112 #? Correcting HYPHENATED words for future when they'll need to be joined on the same line
    regex_pattern112 = r'(?<=[a-z])~\n' 
    cleaned_content = re.sub(regex_pattern112, '-\n', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 113 #? More correcting of hyphens
    regex_pattern113 = r'-~\n' 
    cleaned_content = re.sub(regex_pattern113, '-\n', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 114 #? Correcting future anchors around speakers aka em dashes
    regex_pattern114 = r'\.-~' 
    cleaned_content = re.sub(regex_pattern114, '.—', cleaned_content, flags=re.DOTALL) #TODO: change to em dash?
    # Pattern 115 #? idem
    regex_pattern115 = r'Mr\.\sErskine\s-~' 
    cleaned_content = re.sub(regex_pattern115, 'Mr. Erskine.—', cleaned_content) #*
    # Pattern 116
    regex_pattern116 = r'^~\s' 
    cleaned_content = re.sub(regex_pattern116, '', cleaned_content, flags=re.MULTILINE) #*
    # Pattern 117
    regex_pattern117 = r'~~' 
    cleaned_content = re.sub(regex_pattern117, '', cleaned_content) #*
    #? CORRECTING SPEAKER NAMES
    #? ATTORNEY (+ Solicitor n°126)
    # Pattern 118
    regex_pattern118 = r"(\sA)[^t](torney)"
    cleaned_content = re.sub(regex_pattern118, r"\1t\2", cleaned_content, flags=re.MULTILINE) #* 
    # Pattern 119
    regex_pattern119 = r"(\sAt)[^t](orney)"
    cleaned_content = re.sub(regex_pattern119, r"\1t\2", cleaned_content, flags=re.MULTILINE)
    # Pattern 120
    regex_pattern120 = r"(\sAtt)[^o](rney)"
    cleaned_content = re.sub(regex_pattern120, r"\1o\2", cleaned_content, flags=re.MULTILINE)
    # Pattern 121
    regex_pattern121 = r'(\sAtt)[^o](rney)' 
    cleaned_content = re.sub(regex_pattern121, r"\1o\2", cleaned_content)
    # Pattern 122
    regex_pattern122 = r'(\sAttor)[^n](ey)' 
    cleaned_content = re.sub(regex_pattern122, r"\1n\2", cleaned_content)  
    # Pattern 123
    regex_pattern123 = r'(\sAttorn)[^e](y)' 
    cleaned_content = re.sub(regex_pattern123, r"\1e\2", cleaned_content) 
    # Pattern 124
    regex_pattern124 = r"Att\sGeneral"
    cleaned_content = re.sub(regex_pattern124, 'Attorney General', cleaned_content, flags=re.MULTILINE) #* 
    # Pattern 125
    regex_pattern125 = r'(Attorney)-(General)'
    cleaned_content = re.sub(regex_pattern125, r'\1 \2', cleaned_content) #* 
    # Pattern 126
    regex_pattern126 = r'-General'
    cleaned_content = re.sub(regex_pattern126, ' General', cleaned_content)
    # Pattern 127
    regex_pattern127 = r"(Solicitor)-(General)"
    cleaned_content = re.sub(regex_pattern127, r'\1 \2', cleaned_content, flags=re.MULTILINE) #* 
    # Pattern 128
    regex_pattern128 = r'(G)[^e](neral)' 
    cleaned_content = re.sub(regex_pattern128, r"\1e\2", cleaned_content) #*
    # Pattern 129
    regex_pattern129 = r'(Ge)[^n](eral)' 
    cleaned_content = re.sub(regex_pattern129, r"\1n\2", cleaned_content) #*
    # Pattern 130
    regex_pattern130 = r'(Gen)[^e](ral)'
    cleaned_content = re.sub(regex_pattern130, r"\1e\2", cleaned_content) #*
    # Pattern 131
    regex_pattern131 = r'(\sGener)[^a](l)'  
    cleaned_content = re.sub(regex_pattern131, r"\1a\2", cleaned_content) #*
    #? ERSKINE
    # Pattern 132
    regex_pattern132 = r'(\sE)[^r](skine)'  
    cleaned_content = re.sub(regex_pattern132, r"\1r\2", cleaned_content)
    # Pattern 133
    regex_pattern133 = r'(\sEr)[^s](kine)'  
    cleaned_content = re.sub(regex_pattern133, r"\1s\2", cleaned_content)
    # Pattern 134
    regex_pattern134 = r'(\sErsk)[^i](ne)'  
    cleaned_content = re.sub(regex_pattern134, r"\1i\2", cleaned_content)
    # Pattern 135
    regex_pattern135 = r'(\sErski)[^n](e)'  
    cleaned_content = re.sub(regex_pattern135, r"\1n\2", cleaned_content)
    # Pattern 136
    regex_pattern136 = r'(\sErskin)[^e]()'  
    cleaned_content = re.sub(regex_pattern136, r"\1e\2", cleaned_content)
    # Pattern 137
    regex_pattern137 = r'()[^E](rskine)'  
    cleaned_content = re.sub(regex_pattern137, r"\1 E\2", cleaned_content)
    #? LORD CHIEF
    # Pattern 138
    regex_pattern138 = r'[^L](ord\sChief)'  
    cleaned_content = re.sub(regex_pattern138, 'Lord Chief', cleaned_content)
    # Pattern 139
    regex_pattern139 = r'(L)[^o](rd\s)'  
    cleaned_content = re.sub(regex_pattern139, r"\1o\2", cleaned_content)
    # Pattern 140
    regex_pattern140 = r'Jord'  
    cleaned_content = re.sub(regex_pattern140, 'Lord', cleaned_content)
    # Pattern 141
    regex_pattern141 = r'(\sChi)[^e](f)'  
    cleaned_content = re.sub(regex_pattern141, r"\1e\2", cleaned_content)
    # Pattern 142
    regex_pattern142 = r'(\sChie)[^f]()'  
    cleaned_content = re.sub(regex_pattern142, r"\1f\2", cleaned_content)
    # Pattern 143
    regex_pattern143 = r'Chef'  
    cleaned_content = re.sub(regex_pattern143, 'Chief', cleaned_content)
    # Pattern 144
    regex_pattern144 = r"Lord\SChief"
    cleaned_content = re.sub(regex_pattern144, 'Lord Chief', cleaned_content, flags=re.MULTILINE)
    #? JUSTICE
    # Pattern 144
    regex_pattern144 = r'(\sJusti)[^c](e)'  
    cleaned_content = re.sub(regex_pattern144, r"\1c\2", cleaned_content)
    # Pattern 145
    regex_pattern145 = r'(\sJustic)[^e](\s)'  
    cleaned_content = re.sub(regex_pattern145, r"\1e\2", cleaned_content)
    # Pattern 146
    regex_pattern146 = r'Justie'  
    cleaned_content = re.sub(regex_pattern146, 'Justice', cleaned_content)
    #? EYRE
    # Pattern 147
    regex_pattern147 = r'(\s)[^E](yre)'  
    cleaned_content = re.sub(regex_pattern147, r"\1E\2", cleaned_content)
    # Pattern 148
    regex_pattern148 = r'(\sE)[^y](re)'  
    cleaned_content = re.sub(regex_pattern148, r"\1y\2", cleaned_content)
    # Pattern 149
    regex_pattern149 = r'Eye'  
    cleaned_content = re.sub(regex_pattern149, 'Eyre', cleaned_content)
    #? GIBBS
    # Pattern 150
    regex_pattern150 = r'(\sG)[^i](bbs)'  
    cleaned_content = re.sub(regex_pattern150, r"\1i\2", cleaned_content)
    # Pattern 151
    regex_pattern151 = r'(\sGi)[^b](bs)'  
    cleaned_content = re.sub(regex_pattern151, r"\1b\2", cleaned_content)
    # Pattern 152
    regex_pattern152 = r'(\sGib)[^b](s)'  
    cleaned_content = re.sub(regex_pattern152, r"\1b\2", cleaned_content)
    # Pattern 153
    regex_pattern153 = r'(\sGibb)[^s]()'  
    cleaned_content = re.sub(regex_pattern153, r"\1s\2", cleaned_content)
    #? HARDY
    # Pattern 154
    regex_pattern154 = r'(\s)[^H](ardy)'  
    cleaned_content = re.sub(regex_pattern154, r"\1H\2", cleaned_content)
    # Pattern 155
    regex_pattern155 = r'(\sH)[^a](rdy)'  
    cleaned_content = re.sub(regex_pattern155, r"\1a\2", cleaned_content)
    # Pattern 156
    regex_pattern156 = r'(\sHa)[^r](dy)'  
    cleaned_content = re.sub(regex_pattern156, r"\1r\2", cleaned_content)
    # Pattern 157
    regex_pattern157 = r'(\sHard)[^y](y)'  
    cleaned_content = re.sub(regex_pattern157, r"\1y\2", cleaned_content)
    #? THOMAS
    # Pattern 158
    regex_pattern158 = r'[^T](homas)'  
    cleaned_content = re.sub(regex_pattern158, r"T\1", cleaned_content)
    # Pattern 159
    regex_pattern159 = r'(T)[^h](omas)'  
    cleaned_content = re.sub(regex_pattern159, r"\1h\2", cleaned_content)
    # Pattern 160
    regex_pattern160 = r'Thoma\s'  
    cleaned_content = re.sub(regex_pattern160, 'Thomas ', cleaned_content)
    #? GARROW
    # Pattern 161
    regex_pattern161 = r'(G)[^a](rrow)'  
    cleaned_content = re.sub(regex_pattern161, r"\1a\2", cleaned_content)
    # Pattern 162
    regex_pattern162 = r'(Garr)[^o](w)'  
    cleaned_content = re.sub(regex_pattern162, r"\1o\2", cleaned_content)
    #? HORNE TOOKE
    # Pattern 163
    regex_pattern163 = r'(\s)[^T](ooke\s)'  
    cleaned_content = re.sub(regex_pattern163, r"\1T\2", cleaned_content)
    #? ADAIR
    # Pattern 164
    regex_pattern164 = r'(Ad)[^a](ir)'  
    cleaned_content = re.sub(regex_pattern164, r"\1a\2", cleaned_content)
    #? BOWER
    # Pattern 165
    regex_pattern165 = r'(Mr\.\s)[^B](ower)'  
    cleaned_content = re.sub(regex_pattern165, r"\1B\2", cleaned_content)
    # Pattern 166
    regex_pattern166 = r'(Mr\.\sB)[^o](wer)'  
    cleaned_content = re.sub(regex_pattern166, r"\1o\2", cleaned_content)
    # Pattern 167
    regex_pattern167 = r'(Mr\.\sBow)[^e](r)'  
    cleaned_content = re.sub(regex_pattern167, r"\1e\2", cleaned_content)
    #? BEARCROFT
    # Pattern 168
    regex_pattern168 = r'(Bearcro)[^f](t)'  
    cleaned_content = re.sub(regex_pattern168, r"\1f\2", cleaned_content)
    #? LAW
    # Pattern 169
    regex_pattern169 = r'(Mr.\sL)[^a](w)'  
    cleaned_content = re.sub(regex_pattern169, r"\1a\2", cleaned_content)
    # Pattern 170
    regex_pattern170 = r'(Mr.\sL)[^a](w\.|-|–|—|,)'  
    cleaned_content = re.sub(regex_pattern170, r"\1a\2", cleaned_content)
    # Pattern 171
    regex_pattern171 = r'(Mr\.\sL)[^a](w\W)'  
    cleaned_content = re.sub(regex_pattern171, r"a", cleaned_content)
    # Pattern 172
    regex_pattern172 = r'Mr\.\sLaz:'  
    cleaned_content = re.sub(regex_pattern172, r"Mr. Law", cleaned_content)
    # Pattern 173
    regex_pattern173 = r'(L)[^a](w(,|\.))'  
    cleaned_content = re.sub(regex_pattern173, r"\1a\2", cleaned_content)
    # Pattern 174
    regex_pattern174 = r'Mr\.\sLawo'  
    cleaned_content = re.sub(regex_pattern174, 'Mr. Law', cleaned_content)
    #? GRANT
    # Pattern 175
    regex_pattern175 = r'(Ale)[^x](ander\sGrant\s)'  
    cleaned_content = re.sub(regex_pattern175, r"x", cleaned_content)
    #? BULLER
    # Pattern 176
    regex_pattern176 = r'(e\sBu)[^l](ler)'  
    cleaned_content = re.sub(regex_pattern176, r"\1l\2", cleaned_content)
    #? MR.
    #? OVERALL/GENERAL FIXES
    # Pattern 177
    regex_pattern177 = r'(Mr)(\s[A-Z]\w*)'  
    cleaned_content = re.sub(regex_pattern177, r"Mr.\2", cleaned_content)
    # Pattern 178
    regex_pattern178 = r'(Mr)([^.\w\s])(\s[A-Z]\w*)'  
    cleaned_content = re.sub(regex_pattern178, r"Mr.\3", cleaned_content)
    #? FOR WILLIAM CAMAGE & other witnesses
    # Pattern 179
    regex_pattern179 = r'm Cameage'  
    cleaned_content = re.sub(regex_pattern179, r"William Camage", cleaned_content)
    # Pattern 179b
    regex_pattern179b = r'Cammage'  
    cleaned_content = re.sub(regex_pattern179b, r"Camage", cleaned_content)
    # Pattern 179c
    regex_pattern179c = r'Juseph'  
    cleaned_content = re.sub(regex_pattern179c, r"Joseph", cleaned_content)
    #? FOR MR. ERSKINE
    # Pattern 180
    regex_pattern180 = r'(M)[^r](\.\sErskine)'  
    cleaned_content = re.sub(regex_pattern180, r"\1r\2", cleaned_content)
    # Pattern 181 (should have put it above in spelling correction for Attorney but had a spare here)
    regex_pattern181 = r'Alturney'  
    cleaned_content = re.sub(regex_pattern181, 'Attorney', cleaned_content)
    # Pattern 182
    regex_pattern182 = r'^\w{1}(\.|,)\sErskine' 
    cleaned_content = re.sub(regex_pattern182, 'Mr. Erskine', cleaned_content, flags=re.MULTILINE) #TODO: useful logic check for others
    # Pattern 183
    regex_pattern183 = r'^\w{3}(\.|,)\sErskine' 
    cleaned_content = re.sub(regex_pattern183, 'Mr. Erskine', cleaned_content, flags=re.MULTILINE)
    # Pattern 184
    regex_pattern184 = r'\b((?!Mr)\w{2})[\.,]\sErskine\b'  
    cleaned_content = re.sub(regex_pattern184, 'Mr. Erskine', cleaned_content)
    # Pattern 185
    regex_pattern185 = r'a Erskine'  
    cleaned_content = re.sub(regex_pattern185, 'Mr. Erskine', cleaned_content)
    # Pattern 186 #? to correct some mispellings
    regex_pattern186 = r'(Mr(\.|,)\s)(?!Erskine)\bE\w{6}\b\.'  
    cleaned_content = re.sub(regex_pattern186, r"Mr. Erskine.", cleaned_content)
    # Pattern 187
    regex_pattern187 = r'Mr\.\.Erskine'  
    cleaned_content = re.sub(regex_pattern187, r"Mr. Erskine", cleaned_content)
    # Pattern 188
    regex_pattern188 = r"((Me\sErskine)|(t\sErskine))"
    cleaned_content = re.sub(regex_pattern188, r"Mr. Erskine", cleaned_content)
    #? FOR MR. ATTORNEY GENERAL 
    # Pattern 189
    regex_pattern189 = r'\b(Mrs|Msr)(\.)\s(Attorney)\b'  
    cleaned_content = re.sub(regex_pattern189, r'Mr. Attorney', cleaned_content) 
    # Pattern 190
    regex_pattern190 = r'Myr,\sAttorney General'  
    cleaned_content = re.sub(regex_pattern190, r'Mr. Attorney General.', cleaned_content) 
    # Pattern 191
    regex_pattern191 = r'[^\s|\w](Attorney)' 
    cleaned_content = re.sub(regex_pattern191, r'Attorney General', cleaned_content)
    # Pattern 192 to correct spelling
    regex_pattern192 = r'‘ General' 
    cleaned_content = re.sub(regex_pattern192, r'General', cleaned_content)
    # Pattern 193
    regex_pattern193 = r'\b(Ir|Me|hr)\.\sAttorney General' 
    cleaned_content = re.sub(regex_pattern193, 'Mr. Attorney General', cleaned_content)
    # Pattern 193b
    regex_pattern193b = r'(Mr\.\s)(?!(Attorney|Solicitor))(\w+)(\sGeneral)' 
    cleaned_content = re.sub(regex_pattern193b, r'\1Attorney\4', cleaned_content)
    #? FOR MR. SOLICITOR GENERAL
    # Pattern 194
    regex_pattern194 = r'(?<!Mr\.|the|The)\s(Solicitor General|Solicitor-General)' 
    cleaned_content = re.sub(regex_pattern194, 'Mr. Solicitor General', cleaned_content)
    #? FOR MR. GARROW 
    # Pattern 195
    regex_pattern195 = r'\b(?!Mr\b)\w{1,2}[^a-zA-Z0-9]\sGarrow' 
    cleaned_content = re.sub(regex_pattern195, 'Mr. Garrow', cleaned_content)
    # Pattern 196
    regex_pattern196 = r'Mr\.\sGers:' 
    cleaned_content = re.sub(regex_pattern196, 'Mr. Garrow.', cleaned_content) 
    #? FOR MR. GIBBS
    # Pattern 197
    regex_pattern197 = r'\b(?!Mr\b)\w{1,2}[^a-zA-Z0-9]\sGibbs' 
    cleaned_content = re.sub(regex_pattern197, r'Mr. Gibbs', cleaned_content)
    # Pattern 198
    regex_pattern198 = r'(Mr)[^\.](\sGibbs)'  
    cleaned_content = re.sub(regex_pattern198, r"\1. \2", cleaned_content) 
    # Pattern 199
    regex_pattern199 = r"‘ir\sGibbs.—-Does your"
    cleaned_content = re.sub(regex_pattern199, "Mr. Gibbs.—Does your", cleaned_content)
    # Pattern 200 
    regex_pattern200 = r'(.*)[^Mr\.](.Gibbs)' 
    cleaned_content = re.sub(regex_pattern200, 'Mr. Gibbs', cleaned_content)
    # Pattern 201
    regex_pattern201 = r'Mr\.\sGibs' 
    cleaned_content = re.sub(regex_pattern201, 'Mr. Gibbs', cleaned_content)
    # Pattern 202
    regex_pattern202 = r'by\sMr\.\nMr.\sGibbs.' 
    cleaned_content = re.sub(regex_pattern202, 'by Mr. Gibbs.', cleaned_content)
    # Pattern 203
    regex_pattern203 = r'Guibbs' 
    cleaned_content = re.sub(regex_pattern203, 'Gibbs', cleaned_content)
    #? FOR MR. LAW
    # Pattern 204
    regex_pattern204 = r'ir,\sLaw'  
    cleaned_content = re.sub(regex_pattern204, "Mr. Law", cleaned_content)
    #? FOR MR. BOWER
    # Pattern 205
    regex_pattern205 = r'(M)[^r](\.\sBower)'  
    cleaned_content = re.sub(regex_pattern205, r'\1r\2', cleaned_content)
    # Pattern 206
    regex_pattern206 = r'(.*)(?<!Mr\.)\sBower'  
    cleaned_content = re.sub(regex_pattern206, 'Mr. Bower', cleaned_content)
    #? FOR Misc.
    # Pattern 207
    regex_pattern207 = r'Mfr.'  
    cleaned_content = re.sub(regex_pattern207, 'Mr.', cleaned_content)
    # Pattern 208
    regex_pattern208 = r'by\sAfr\.'  
    cleaned_content = re.sub(regex_pattern208, 'by Mr.', cleaned_content)
    #? EXAMINED BY VARIATIONS
    # Pattern 209
    regex_pattern209 = r'by\nr v. eT.'  
    cleaned_content = re.sub(regex_pattern209, 'by Mr. Bower.', cleaned_content)
    # Pattern 210
    regex_pattern210 = r'-examined\sb\nErskine'  
    cleaned_content = re.sub(regex_pattern210, '-examined by Mr. Erskine', cleaned_content)
    # Pattern 211 #? A relevant line
    regex_pattern211 = 'Then I do not un-'  
    cleaned_content = re.sub(regex_pattern211, 'Then I do not understand.', cleaned_content)
    #? Hyphens for Attorney and Solicitor General
    # Pattern 212
    regex_pattern212 = 'rney-'  
    cleaned_content = re.sub(regex_pattern212, 'rney ', cleaned_content)
    # Pattern 213
    regex_pattern213 = 'solicitor-'  
    cleaned_content = re.sub(regex_pattern213, 'solicitor ', cleaned_content)
    # Pattern 214
    regex_pattern214 = 'Solicitor-'  
    cleaned_content = re.sub(regex_pattern214, 'Solicitor ', cleaned_content)
    # Pattern 215
    regex_pattern215 = r'\]\shave\sgiven'  
    cleaned_content = re.sub(regex_pattern215, '. I have given', cleaned_content)
    #? Fixing full stops replacing whitespaces
    # Pattern 216
    regex_pattern216 = r'([a-z])\.([a-z])' 
    cleaned_content = re.sub(regex_pattern216, r"\1 \2", cleaned_content) 
    # Pattern 217 #? for commas
    regex_pattern217 = r'([a-z]),([a-z])' 
    cleaned_content = re.sub(regex_pattern217, r"\1, \2", cleaned_content) 
    # Pattern 218
    #regex_pattern218 = r'' 
    #cleaned_content = re.sub(regex_pattern218, r"", cleaned_content) 
    #? FIXING ANCHORS AFTER SPEAKER NAMES
    #? Fixing tildes + em dashes in anchors issues and Misc. issues in order to fix issues with anchors after speaker names subsequently
    # Pattern 219 
    regex_pattern219 = r'~—' 
    cleaned_content = re.sub(regex_pattern219, '—', cleaned_content) 
    # Pattern 220  
    regex_pattern220 = r'—1\s' 
    cleaned_content = re.sub(regex_pattern220, '—I ', cleaned_content) 
    # Pattern 221 
    regex_pattern221 = r'\?-~' 
    cleaned_content = re.sub(regex_pattern221, '?—', cleaned_content)
    # Pattern 222
    regex_pattern222 = r'\s~~' 
    cleaned_content = re.sub(regex_pattern222, '', cleaned_content)
    # Pattern 223 #? Fixing stray floating footers
    regex_pattern223 = r'^\d[A-Z]$'
    cleaned_content = re.sub(regex_pattern223, '', cleaned_content, flags=re.MULTILINE)
    # Pattern 224
    regex_pattern224 = r'\s:\s:'
    cleaned_content = re.sub(regex_pattern224, '', cleaned_content)
    # Pattern 225
    regex_pattern225 = r"\s,\s,"
    cleaned_content = re.sub(regex_pattern225, '', cleaned_content)
    # Pattern 226
    regex_pattern226 = r',---' 
    cleaned_content = re.sub(regex_pattern226, '.—', cleaned_content)
    # Pattern 227 
    regex_pattern227 = r"^'\s"
    cleaned_content = re.sub(regex_pattern227, '', cleaned_content, flags=re.MULTILINE) 
    # Pattern 228 #? replace with whitespace
    regex_pattern228 = r"\s'\s"
    cleaned_content = re.sub(regex_pattern228, ' ', cleaned_content, flags=re.MULTILINE)

    #? END ANCHORS AFTER SPEAKERS. Following convention in the text, speakers are followed by \.— (fullstop em dash) e.g: Mr. Erskine.—
    #? Placing full stops and em dashes after speaker names
    #* Note: rule is to first place fullstop (they're usually missing and sandwiched btw the names and either a minus, an en dash or an emdash (or others...))
    #? MR. ATTORNEY GENERAL.—
    # Pattern 229 #? at some point there's a General General that pops up and idk where so...
    regex_pattern229 = 'General General' 
    cleaned_content = re.sub(regex_pattern229, 'General', cleaned_content)
    # Pattern 230 #? Deleting this, not needed.
    regex_pattern230 = r'\s\(sir John Scott\)' 
    cleaned_content = re.sub(regex_pattern230, '', cleaned_content)
    # Pattern 231 #? fixing full stop em dash formatting
    regex_pattern231 = r'(\sGeneral),?\s*[-–—~]+' 
    cleaned_content = re.sub(regex_pattern231, r'\1.—', cleaned_content)
    # Pattern 231b #? fixing full stop em dash formatting
    regex_pattern231b = 'Examined by.'
    cleaned_content = re.sub(regex_pattern231b, 'Examined by', cleaned_content)
    # Pattern 231c #? fixing "examined by .—" specific
    regex_pattern231c = r'examined\sby\sMr\.\nalttorney\sGeneral,\n\n' 
    cleaned_content = re.sub(regex_pattern231c, 'examined by Mr. Attorney General.— ', cleaned_content)
    # Pattern 231d #? fixing "examined by .—"
    regex_pattern231d = r'(exami)[^n](ed\s)' 
    cleaned_content = re.sub(regex_pattern231d, r'\1n\2', cleaned_content)
    # Pattern 231e #? fixing "examined by .—"
    regex_pattern231e = r'(Examine)[^d](\s)' 
    cleaned_content = re.sub(regex_pattern231e, r'\1d\2', cleaned_content)
    # Pattern 231f #? fixing full stop em dash formatting
    regex_pattern231f = r'(\sGeneral\.)\s*[-–—~]{2,}' 
    cleaned_content = re.sub(regex_pattern231f, r'\1—', cleaned_content)
    # Pattern 231g #? fixing full stop em dash formatting
    regex_pattern231g = r'by\sMr\.\sAttorney\nGeneral\.\n\n' 
    cleaned_content = re.sub(regex_pattern231g, 'by Mr. Attorney General.—', cleaned_content)
    # Pattern 231h #? manual fix
    regex_pattern231h = r'out\swith\sthem\s\?-.' 
    cleaned_content = re.sub(regex_pattern231h, 'out with them?— No.', cleaned_content)
    # Pattern 231i #? 
    regex_pattern231i = r'(examined|Examined)\sby\s*Mr\.(\W+)Attorney\W*General([\W\d]+)' 
    cleaned_content = re.sub(regex_pattern231i, r'\1 by Mr. Attorney General.—', cleaned_content)
    # Pattern 231j #? 
    regex_pattern231j = r'byMr\.\sAt-\ntorney\sGeneral\.\W*' 
    cleaned_content = re.sub(regex_pattern231j, 'by Mr. Attorney General.—', cleaned_content)
    # Pattern 231k #? 
    regex_pattern231k = r'General\.\s—' 
    cleaned_content = re.sub(regex_pattern231k, 'General.—', cleaned_content)
    #? MR. ERSKINE.—
    # Pattern 232 #? fixing full stop em dash formatting
    regex_pattern232 = r'(\sErskine),?\s*[-–—~]+' 
    cleaned_content = re.sub(regex_pattern232, r'\1.—', cleaned_content)
    # Pattern 232b #? fixing full stop em dash formatting
    regex_pattern232b = r'(\sErskine\.)\s*[-–—~]{2,}' 
    cleaned_content = re.sub(regex_pattern232b, r'\1—', cleaned_content)
    # Pattern 233 #? Correcting manually
    regex_pattern233 = 'Erskine, I admit' 
    cleaned_content = re.sub(regex_pattern233, 'Erskine.— I admit', cleaned_content)
    # Pattern 234 #? fixing examined by...
    regex_pattern234 = r"M'Ewan\scross-examined\sby\sMr\.\n\nErskine,"
    cleaned_content = re.sub(regex_pattern234, "M'Ewan cross-examined by Mr. Erskine.—", cleaned_content)
    # Pattern 235 #? fixing examined by...
    regex_pattern235 = r"(examined|Examined)\sby\s*Mr\.\n*\sErskine([\W\d]+)"
    cleaned_content = re.sub(regex_pattern235, r'\1 by Mr. Erskine.— ', cleaned_content) 
    # Pattern 235b #? a double Mr. to fix
    regex_pattern235b = r"\sby\sMr\.\nMr\.\sErskine\.\n"
    cleaned_content = re.sub(regex_pattern235b, ' by Mr. Erskine.—', cleaned_content)
    # Pattern 235c
    regex_pattern235c = r"Erskine\.\s—"
    cleaned_content = re.sub(regex_pattern235c, 'Erskine.—', cleaned_content)
    #? MR. GIBBS.—
    # Pattern 236 #? fixing full stop em dash formatting
    regex_pattern236 = r'(\sGibbs),?\s*[-–—~]+' 
    cleaned_content = re.sub(regex_pattern236, r'\1.—', cleaned_content)
    # Pattern 236b #? fixing full stop em dash formatting
    regex_pattern236b = r'(\sGibbs\.)\s*[-–—~]{2,}' 
    cleaned_content = re.sub(regex_pattern236b, r'\1—', cleaned_content)
    # Pattern 237 #? fixing examined by...
    regex_pattern237 = r'(examined|Examined)\sby\s*Mr\.\n*\sGibbs([\W\d]+)'
    cleaned_content = re.sub(regex_pattern237, r'\1 by Mr. Gibbs.— ', cleaned_content)
    # Pattern 237b
    regex_pattern237b = r'(examined|Examined)\sby\sMr\.\n*\sibbs[.,]?\n{1,3}' 
    cleaned_content = re.sub(regex_pattern237b, r'\1 by Mr. Gibbs.— ', cleaned_content)
    # Pattern 237c
    regex_pattern237c = r'(examined|Examined)\sby\s*Mr\.\n*\sGubds([\W\d]+)' 
    cleaned_content = re.sub(regex_pattern237c, r'\1 by Mr. Gibbs.— ', cleaned_content)
    # Pattern 237d
    regex_pattern237d = r'(examined|Examined)\sby\s*Mr\.\n*\sibbs([\W\d]+)' 
    cleaned_content = re.sub(regex_pattern237d, r'\1 by Mr. Gibbs.— ', cleaned_content)
    # Pattern 237e
    regex_pattern237e = r'Examined!\)\nMr\.\sGibbs\.\n\n' 
    cleaned_content = re.sub(regex_pattern237e, r'Examined by Mr. Gibbs.—', cleaned_content)
    #? MR. EYRE.—
    # Pattern 238 #? fixing full stop em dash formatting
    regex_pattern238 = r'(\sEyre),?\s*[-–—~]+' 
    cleaned_content = re.sub(regex_pattern238, r'\1.—', cleaned_content)
    # Pattern 238b #? fixing full stop em dash formatting
    regex_pattern238b = r'(\sEyre\.)\s*[-–—~]{2,}' 
    cleaned_content = re.sub(regex_pattern238b, r'\1—', cleaned_content)
    # Pattern 238c #? fixing full stop em dash formatting
    regex_pattern238c = r'LordChiefJustice Eyre' 
    cleaned_content = re.sub(regex_pattern238c, 'Lord Chief Justice Eyre', cleaned_content)
    # Pattern 238d #? Motion by....
    regex_pattern238d = r'(A motion from)\W*(Lord)' 
    cleaned_content = re.sub(regex_pattern238d, r'\1 \2', cleaned_content)
    # Pattern 238e
    regex_pattern238e = r'(Eyre|Garrow)\.\s—' 
    cleaned_content = re.sub(regex_pattern238e, r'\1.—', cleaned_content)
    #? No need for fixing examined by... for Eyre.
    #? MR. LAW.—
    # Pattern 238 #? fixing full stop em dash formatting
    regex_pattern238 = r'(\sLaw),?\s*[-–—~]+' 
    cleaned_content = re.sub(regex_pattern238, r'\1.—', cleaned_content)
    # Pattern 239 #? for fixing examined by...
    regex_pattern238 = 'encen Examined by Mr.' 
    cleaned_content = re.sub(regex_pattern238, 'sworn, Examined by Mr. Law.', cleaned_content)
    # Pattern 240 #? fixing examined by...
    regex_pattern240 = r'(examined|Examined)\sby\s*Mr\.\n*\sLaw([\W\d]+)'
    cleaned_content = re.sub(regex_pattern240, r'\1 by Mr. Law.— ', cleaned_content)
    # Pattern 240b #? fixing full stop em dash formatting
    regex_pattern240b = r'(\sLaw\.)\s*[-–—~]{2,}' 
    cleaned_content = re.sub(regex_pattern240b, r'\1—', cleaned_content)
    # Pattern 240c #? fixing full stop em dash formatting
    regex_pattern240c = r'by\sMr\.\n\nww.\n\n' 
    cleaned_content = re.sub(regex_pattern240c, 'by Mr. Law.— ', cleaned_content)
    # Pattern 240d #? fixing full stop em dash formatting
    regex_pattern240d = r'\soe\scaeaitinel\sby\sMr\.\n\nle\n\n' 
    cleaned_content = re.sub(regex_pattern240d, 'cross-examined by Mr. Law.— ', cleaned_content)
    # Pattern 240e
    regex_pattern240e = r'^r. Law' 
    cleaned_content = re.sub(regex_pattern240e, 'Mr. Law', cleaned_content, flags=re.MULTILINE)
    #? MR. BOWER.—
    #? No need to fix em dash formatting for Bower.
    # Pattern 241 #? fixing for examined by...
    regex_pattern241 = r'Mr\.\ner.' 
    cleaned_content = re.sub(regex_pattern241, 'Mr. Bower.', cleaned_content)
    # Pattern 242 #? fixing examined by...
    regex_pattern242 = r'(examined|Examined)\sby\s*Mr\.\n*\sBower([\W\d]+)'
    cleaned_content = re.sub(regex_pattern242, r'\1 by Mr. Bower.—', cleaned_content)
    # Pattern 243 #? fixing full stop em dash formatting
    regex_pattern243 = r'(\sBower\.)\s*[-–—~]{2,}' 
    cleaned_content = re.sub(regex_pattern243, r'\1—', cleaned_content)
    # Pattern 243b
    regex_pattern243b = 'toaer' 
    cleaned_content = re.sub(regex_pattern243b, 'Bower', cleaned_content)
    # Pattern 243c #? fixing byMr.\n...
    regex_pattern243c = r'\sbyMr\.\n*Bower([\W]+)' 
    cleaned_content = re.sub(regex_pattern243c, ' by Mr. Bower.—', cleaned_content)
    # Pattern 243d 
    regex_pattern243d = r'\sbyMr\.\n*Bouer([\W]+)' 
    cleaned_content = re.sub(regex_pattern243d, ' by Mr. Bower.—', cleaned_content)
    # Pattern 243e
    regex_pattern243e = r'(Jane Rickman sworn.— Examined byMr.).*(—liam.)' 
    cleaned_content = re.sub(regex_pattern243e, ' Jane Rickman sworn.— Examined by Mr. Bower.—You are the wife of Thomas Clio Rickman?—I am.', cleaned_content, flags=re.DOTALL)
    #? MR. GARROW.—
    # Pattern 244 #? fixing full stop em dash formatting
    regex_pattern244 = r'(\sGarrow),?\s*[-–—~]+' 
    cleaned_content = re.sub(regex_pattern244, r'\1.—', cleaned_content)
    # Pattern 245 #? fixing full stop em dash formatting
    regex_pattern245 = r'(\sGarrow\.)\s*[-–—~]{2,}' 
    cleaned_content = re.sub(regex_pattern245, r'\1—', cleaned_content)
    # Pattern 246 #? fixing examined by...
    regex_pattern246 = r'(examined|Examined)\sby\W*Mr\.\W*\n*\sGarrow([\W\d]+)' 
    cleaned_content = re.sub(regex_pattern246, r'\1 by Mr. Garrow.—', cleaned_content)
    # Pattern 246b 
    regex_pattern246b = r'byM\.\n\nGarrow\.\n\n' 
    cleaned_content = re.sub(regex_pattern246b, 'by Mr. Garrow.—', cleaned_content)
    # Pattern 246c
    regex_pattern246c = r'Examin-\ned.*ow\.\n\n' 
    cleaned_content = re.sub(regex_pattern246c, 'Examined by Mr. Garrow.—', cleaned_content)
    #? MR. BULLER.—
    # Pattern 247 #? fixing full stop em dash formatting
    regex_pattern247 = r'(\sBuller),?\s*[-–—~]+' 
    cleaned_content = re.sub(regex_pattern247, r'\1.—', cleaned_content)
    #? No need to fix examined by for Buller.
    #? MR. BEARCROFT.— 
    #? /
    #? MR. WOOD.—
    # Pattern 247b #? for byMr\.\n...
    regex_pattern247b = r'(examined|Examined)\sby\s*Mr\.\W*\n*\sWood([\W\d]+)' 
    cleaned_content = re.sub(regex_pattern247b, r' by Mr. Wood.—', cleaned_content)
    #? MR. ADAIR.—
    #? /
    #?################################ END NAME AND ANCHORS FORMATTING - #######################################
    #? CORRECTING EM DASHES FOR IN TESTIMONIES/ GENERAL EM DASH FORMATTING
    #? Fixing em dashes after question marks 
    # Pattern 248 #? Correcting responses to answers "anchors"/em dashes.
    regex_pattern248 = r'\?[-–—~]{2,}(?=[A-Z])' 
    cleaned_content = re.sub(regex_pattern248, '?—', cleaned_content) #* Seems like there's never any \s between the — and the next word so...
    # Pattern 249 #? Fixing Ps which have replaced ?
    regex_pattern249 = r'\sP[-–—]+' 
    cleaned_content = re.sub(regex_pattern249, '?—', cleaned_content) #* no space...
    # Pattern 250 #? For 2 or more of the below
    regex_pattern250 = r'(\?\s*)([-–—~,.]{2,})([l|f|t])' 
    cleaned_content = re.sub(regex_pattern250, r'\1—I', cleaned_content)
    # Pattern 250b 
    regex_pattern250b = r'(\?\s*)([-–—~,.]{2,})a' 
    cleaned_content = re.sub(regex_pattern250b, r'\1—A', cleaned_content)  #* starting issue was this: (\?\s*)([-–—~,.]{2,})
    # Pattern 250c
    regex_pattern250c = r'(\?\s*)([-–—~,.]{2,})\n(T )' 
    cleaned_content = re.sub(regex_pattern250c, r'\1—I ', cleaned_content)
    # Pattern 250d
    regex_pattern250d = r'(\?\s*)([-–—~,.]{2,})\n([A-Z])' 
    cleaned_content = re.sub(regex_pattern250d, r'\1—\3 ', cleaned_content)  
    # Pattern 250e
    regex_pattern250e = r'(\?\s*)([-–—~,.]{2,})\n\n‘' 
    cleaned_content = re.sub(regex_pattern250e, r'\1—', cleaned_content)
    # Pattern 250f
    regex_pattern250f = r'(\?\s*)([-–—~,.]{2,})\n(\n\nThose)' 
    cleaned_content = re.sub(regex_pattern250f, r'\1—No.\3', cleaned_content)
    # Pattern 250g
    regex_pattern250g = r'(\?\s*)([-–—~,.]{2,})\n\n(Mr)' 
    cleaned_content = re.sub(regex_pattern250g, r'\1—\3', cleaned_content)
    # Pattern 250h
    regex_pattern250h = r'(\?\s*)([-–—~,.]{2,})\n\n(es\.)(.*)$' 
    cleaned_content = re.sub(regex_pattern250h, r'\1—Y\3', cleaned_content, flags=re.MULTILINE)
    # Pattern 250i
    regex_pattern250i = r'(\?\s*)([-–—~,.]{2,})\n\n(only)' 
    cleaned_content = re.sub(regex_pattern250i, r'\1—I \3', cleaned_content)
    # Pattern 250j
    regex_pattern250j = r'(\?\s*)([-–—~,.]{2,})\n\ntis' 
    cleaned_content = re.sub(regex_pattern250j, r'\1—His', cleaned_content)
    # Pattern 250k
    regex_pattern250k = r'((y|) )(.*\?\s*)([-–—~,.]{2,})\nes.' 
    cleaned_content = re.sub(regex_pattern250k, r'\3—Yes.', cleaned_content)
    # Pattern 250l
    regex_pattern250l = r'(\?\s*)([-–—~,.]{2,})\n([a-z])' 
    cleaned_content = re.sub(regex_pattern250l, r'\1—I', cleaned_content)
    # Pattern 250m
    regex_pattern250m = r'(Smithfield\.)\s(.*\?\s*)([-–—~,.]{2,})\n\s(.*)\ns\s(.*)\n(.*)\n-\s(.*)\n(.*)\ns(.*)-\n(.*)\n;\s(.*)\n(.*)\n(.*)---\n;\s(.*)\n(.*al\.)(.*)-\n“\s(.*)\n\nft( .*)\n(.*ad)-\s(.*)\s\}' 
    cleaned_content = re.sub(regex_pattern250m, r'\1\n\n\2—\4\n\n\5 \6\n\n\7 \8\9\10\n\n\11 \12\n\n\13—\14\n\n\15—\16\17\n\n[It\18 \19\20]', cleaned_content)
    # Pattern 250n
    regex_pattern250n = r'deing(\?\s*)([-–—~,.]{2,})\s(.*)\n(.*)' 
    cleaned_content = re.sub(regex_pattern250n, r'doing\1—Yes, at times there were.', cleaned_content)
    # Pattern 250o
    regex_pattern250o = r'\..*fortwighh\n\n\n(montb)(.*)-\n(.*)\n(.*)\s~\n\n(.*t)-.-was\n(.*)' 
    cleaned_content = re.sub(regex_pattern250o, r' a fortnight, a month\2\3 \4\n\n\5, was it once a week?—No.', cleaned_content)
    # Pattern 250p
    regex_pattern250p = r'\?-— ”' 
    cleaned_content = re.sub(regex_pattern250p, r'?”', cleaned_content)
    # Pattern 250q
    regex_pattern250q = r'(.*)\n\n(.*)4(.*that)\n\n\n\n(.*)\n(.*)-\n(.*)aans(.*)-\n(.*)-— ‘.*\n(.*)\)—(.*)\n(.*)\n(.*)\n(.*)–(.*)\n(.*)\n(.*)--(.*)\n(.*)\n(.*)\*(.*)' 
    cleaned_content = re.sub(regex_pattern250q, r'\1 \2a\3 \4 \5\6ons\7\8 Upon your oath; look \9. \10 \11 \12 \13 \14k \15 \16; \17 \18 \19\20', cleaned_content)
    # Pattern 250r
    regex_pattern250r = r'(I believe)\nha(.*)\n\n(.*)\n(.*)-\n(.*)\n(.*)\n.*(I.*)\n(.*)' 
    cleaned_content = re.sub(regex_pattern250r, r'\1 you\2 I \3 \4\5 go\6 society?—\7 kind.', cleaned_content)
    # Pattern 250s
    regex_pattern250s = r'(\?\s*)([-–—~,.]{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern250s, r'\1—\3', cleaned_content)
    # Pattern 250t
    regex_pattern250t = r'(\?\s*)([-–—~,.]{2,})(\s[A-Z].*er\.)\s(.*)\n(.*)\n(.*)\n\nlay.' 
    cleaned_content = re.sub(regex_pattern250t, r'\1—\3\n\n\4 \5\n\nW\6 May.\n', cleaned_content)
    # Pattern 250u
    regex_pattern250u = r'(\?\s*)([-–—~,.]{2,})(\s[A-Z].*\n)(.*)(\.|,)$' 
    cleaned_content = re.sub(regex_pattern250u, r'\1—\3\4.', cleaned_content, flags=re.MULTILINE)
    # Pattern 250v
    regex_pattern250v = r'(\?\s*)([-–—~,.]{2,})(\s[A-Z].*)(\.|,)$' 
    cleaned_content = re.sub(regex_pattern250v, r'\1—\3.', cleaned_content, flags=re.MULTILINE)
    # Pattern 250w
    regex_pattern250w = r'(— WaT 18 THE LAW UPON\nTHIS MOMENTOUS SUBJECT\? ---)' 
    cleaned_content = re.sub(regex_pattern250w, r'WHAT IS THE LAW UPON THIS MOMENTOUS SUBJECT?', cleaned_content)
    # Pattern 250x
    regex_pattern250x = r'(\?\s*)([-–—~,.]{2,})(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern250x, r'\1—\3', cleaned_content)
    # Pattern 250y
    regex_pattern250y = r'(there)\s(—We\s)' 
    cleaned_content = re.sub(regex_pattern250y, r'\1?\2', cleaned_content)
    # Pattern 250z
    regex_pattern250z = r'\s—We\s' 
    cleaned_content = re.sub(regex_pattern250z, r'? We ', cleaned_content)
    # Pattern 250z2
    regex_pattern250z2 = r'(\?\s*)([-–—~,.]{2,})“' 
    cleaned_content = re.sub(regex_pattern250z2, r'\1 “', cleaned_content)
    # Pattern 250z3
    regex_pattern250z3 = r'(\?\s*)([-–—~,.]{2,})' 
    cleaned_content = re.sub(regex_pattern250z3, r'\1—', cleaned_content)
    # Pattern 251 
    regex_pattern251 = r'(strong\?\s)-' 
    cleaned_content = re.sub(regex_pattern251, r'\1', cleaned_content)
    # Pattern 251b 
    regex_pattern251b = r'(_|-|\*)*(Mr. Law\.)[^—]([A-z])' 
    cleaned_content = re.sub(regex_pattern251b, r'\2—\3', cleaned_content)
    # Pattern 251c
    regex_pattern251c = r'^((_|-|\*)*)(Mr.\sLaw.)' 
    cleaned_content = re.sub(regex_pattern251c, r'\3', cleaned_content, flags=re.MULTILINE)
    # Pattern 251d
    regex_pattern251d = r'coms\nlain\sof\s\?~w' 
    cleaned_content = re.sub(regex_pattern251d, r'complain of? W', cleaned_content)
    # Pattern 251e 
    regex_pattern251e = r'(\?)\s~\n' 
    cleaned_content = re.sub(regex_pattern251e, r'\1', cleaned_content) 
    # Pattern 251f
    regex_pattern251f = r'(\?)\s~' 
    cleaned_content = re.sub(regex_pattern251f, r'\1—', cleaned_content) 
    # Pattern 251g
    regex_pattern251g = r'\?\s*[-–~]\n*(?=[a-zA-Z]\w*)' 
    cleaned_content = re.sub(regex_pattern251g, r'?—', cleaned_content)
    # Pattern 252
    regex_pattern252 = r'\?-\[\n' 
    cleaned_content = re.sub(regex_pattern252, "?—I ", cleaned_content)
    # Pattern 253 #? En dashes to em dashes:
    regex_pattern253 = r'\?–' 
    cleaned_content = re.sub(regex_pattern253, r'?—', cleaned_content)
    # Pattern 254 #? ?—Yes answers with \n+
    regex_pattern254 = r'\?—\n+es([\.,\s‘:;])+' 
    cleaned_content = re.sub(regex_pattern254, r'?—Yes.\n\n', cleaned_content) 
    #? Correcting ?—Yes. answers.
    # Pattern 255 
    regex_pattern255 = r'(\?—Yes)((,|:))\n+(?!Mr|I\s)([A-Z]\w*)' 
    cleaned_content = re.sub(regex_pattern255, r'\1.\n\n\4', cleaned_content)
    # Pattern 255b 
    regex_pattern255b = r'(\?—Yes,)\n(I was there),' 
    cleaned_content = re.sub(regex_pattern255b, r'\1 \2.', cleaned_content)
    # Pattern 255c
    regex_pattern255c = r'(\?—Yes,)\n+(?!Mr)([A-Z]\w*)' 
    cleaned_content = re.sub(regex_pattern255c, r'?\1.\n\n\2', cleaned_content)
    # Pattern 255d
    regex_pattern255d = r'(\?—Yes),\n+([A-Z]\w*)' 
    cleaned_content = re.sub(regex_pattern255d, r'\1.\n\n\2', cleaned_content)
    # Pattern 256 
    regex_pattern256 = r'(\?—\s*Yes[^\.])\n+(?!I|He)([A-Z]\w*)' 
    cleaned_content = re.sub(regex_pattern256, r'?—Yes.\n\n\2', cleaned_content)
    # Pattern 257 #? There are some "I"s missing
    regex_pattern257 = r'(\?—\s*Yes)[^\.]\n+\s*(was|have|believe)(.*)(\.*|,)'
    cleaned_content = re.sub(regex_pattern257, r'\1, I \2.', cleaned_content)
    # Pattern 258 
    regex_pattern258 = r'(\?—\s*Yes,\n\n‘\s)' 
    cleaned_content = re.sub(regex_pattern258, '?—Yes.\n\n', cleaned_content)
    # Pattern 259 
    regex_pattern259 = r'(\?—Yes\.)([^\w\n])([\Wea]+)$' 
    cleaned_content = re.sub(regex_pattern259, r'\1\n', cleaned_content, flags=re.MULTILINE)
    # Pattern 260 
    regex_pattern260 = r'^as\sthe\sprisoner\sat\sthe\sbar\sone\sof\sthem\?—Yes\.\swe' 
    cleaned_content = re.sub(regex_pattern260, r'Was the prisoner at the bar one of them?—Yes.', cleaned_content, flags=re.MULTILINE)
    # Pattern 260b
    regex_pattern260b = r'\?—es\.' 
    cleaned_content = re.sub(regex_pattern260b, '?—Yes.', cleaned_content)
    # Pattern 260c 
    regex_pattern260c = r'\?\W+—\W*Yes\.\W*$' 
    cleaned_content = re.sub(regex_pattern260c, r'?—Yes.\n', cleaned_content, flags=re.MULTILINE)
    # Pattern 260d #? 
    regex_pattern260d = r'(\?—)\n{2,}(Yes|No)' 
    cleaned_content = re.sub(regex_pattern260d, r'\1 \2', cleaned_content, flags=re.MULTILINE)
    #? Correcting ?—No. answers
    # Pattern 261 #? 
    regex_pattern261 = r'\?—[\W+\n]+(No)([\W]*)$' 
    cleaned_content = re.sub(regex_pattern261, '?—No.\n', cleaned_content, flags=re.MULTILINE)
    # Pattern 262 #? 
    regex_pattern262 = r'\?[^—][\W+\n]+(No)([\W]*)$' 
    cleaned_content = re.sub(regex_pattern262, '?—No.\n', cleaned_content, flags=re.MULTILINE)
    # Pattern 263 #? 
    regex_pattern263 = r'(\?—\s*No[^\.])(\n{2,})([A-Z]\w*)' 
    cleaned_content = re.sub(regex_pattern263, r'?—No.\n\n\3', cleaned_content)
    # Pattern 264 #? 
    regex_pattern264 = r'—No,\nDid' 
    cleaned_content = re.sub(regex_pattern264, '—No.\n\nDid', cleaned_content)
    # Pattern 265 #? 
    regex_pattern265 = r'(\?—No\.)([^\w\n])([\W]+)$' 
    cleaned_content = re.sub(regex_pattern265, r'\1\n', cleaned_content, flags=re.MULTILINE)
    #? Correcting questions marks
    # Pattern 265 #? 
    regex_pattern265 = r'\?P—' 
    cleaned_content = re.sub(regex_pattern265, '?—', cleaned_content)
    # Pattern 265b #? 
    regex_pattern265b = r'P—' 
    cleaned_content = re.sub(regex_pattern265b, '?—', cleaned_content)
    # Pattern 265c #? 
    regex_pattern265c = r'(\.|\?)—(f|l|T|E|F|J|K|L)\s' 
    cleaned_content = re.sub(regex_pattern265c, r'\1—I ', cleaned_content)
    # Pattern 265d #? 
    regex_pattern265d = r'\)—\n([A-Z])' 
    cleaned_content = re.sub(regex_pattern265d, r'?—\1', cleaned_content)
    # Pattern 265e
    regex_pattern265e = r'\?\s~\s' 
    cleaned_content = re.sub(regex_pattern265e, '?—', cleaned_content)
    #? CORRECTING SWORN.—
    # Pattern 266
    regex_pattern266 = r'\ssworn\W+(examined|Examined)' 
    cleaned_content = re.sub(regex_pattern266, r' sworn.— \1', cleaned_content)
    # Pattern 267
    regex_pattern267 = r'(John Coatessworn—Examined)' 
    cleaned_content = re.sub(regex_pattern267, 'John Coates sworn.— Examined', cleaned_content)
    # Pattern 268 #? this one needs comma not .—
    regex_pattern268 = r'sworn—' 
    cleaned_content = re.sub(regex_pattern268, 'sworn, ', cleaned_content)
    # Pattern 268b
    regex_pattern268b = r'swomm.—' 
    cleaned_content = re.sub(regex_pattern268b, 'sworn.— ', cleaned_content)
    # Pattern 268c
    regex_pattern268c = r'\(sworn\)—Examined' 
    cleaned_content = re.sub(regex_pattern268c, 'sworn.— Examined', cleaned_content)
    #? MORE EM DASH FORMATTING
    # Pattern 269 #? Fixing tripple hyphen  replacing em dashes
    regex_pattern269 = r'\.---' 
    cleaned_content = re.sub(regex_pattern269, '.—', cleaned_content)
    # Pattern 269b correcting to em dash
    regex_pattern269b = r'\.\.--' 
    cleaned_content = re.sub(regex_pattern269b, ".—", cleaned_content) 
    # Pattern 270
    regex_pattern270 = r',--you' 
    cleaned_content = re.sub(regex_pattern270, ", ", cleaned_content) 
    # Pattern 271
    regex_pattern271= r',-—' 
    cleaned_content = re.sub(regex_pattern271, ", ", cleaned_content) 
    # Pattern 272 correcting to full stop and whitespace
    regex_pattern272 = r'\.–-' 
    cleaned_content = re.sub(regex_pattern272, ". ", cleaned_content) 
    # Pattern 273 correcting to em dash
    regex_pattern273 = r'\.–([A-Z])' 
    cleaned_content = re.sub(regex_pattern273, r".—\1", cleaned_content) 
    # Pattern 274 correcting to em dash
    regex_pattern274 = r'\.-\.-' 
    cleaned_content = re.sub(regex_pattern274, '.—', cleaned_content) 
    # Pattern 275 correcting ; formatting to include the em dash as in rest of document
    regex_pattern275 = r';---' 
    cleaned_content = re.sub(regex_pattern275, '; ', cleaned_content) 
    # Pattern 276 
    regex_pattern276 = r';--' 
    cleaned_content = re.sub(regex_pattern276, '; ', cleaned_content) 
    # Pattern 277 
    regex_pattern277 = r';-—-' 
    cleaned_content = re.sub(regex_pattern277, '; ', cleaned_content) 
    # Pattern 278
    regex_pattern278 = r';-—' 
    cleaned_content = re.sub(regex_pattern278, '; ', cleaned_content) 
    # Pattern 279
    regex_pattern279 = r';-~*' 
    cleaned_content = re.sub(regex_pattern279, ';—', cleaned_content) 
    # Pattern 280
    regex_pattern280 = r';–-' 
    cleaned_content = re.sub(regex_pattern280, '; ', cleaned_content) 
    # Pattern 281
    regex_pattern281 = r';–' 
    cleaned_content = re.sub(regex_pattern281, '; ', cleaned_content)
    # Pattern 282
    regex_pattern282 = r';—-' 
    cleaned_content = re.sub(regex_pattern282, '; ', cleaned_content) 
    # Pattern 283
    regex_pattern283 = r'\.\.-' 
    cleaned_content = re.sub(regex_pattern283, '.—', cleaned_content)
     # Pattern 284 #? deleting 
    regex_pattern284 = r'^---' 
    cleaned_content = re.sub(regex_pattern284, '', cleaned_content, flags=re.MULTILINE) 
    # Pattern 285
    regex_pattern285 = r'\.~' 
    cleaned_content = re.sub(regex_pattern285, '.—', cleaned_content) 
    # Pattern 286
    regex_pattern286 = r'([a-z])~([a-z])' 
    cleaned_content = re.sub(regex_pattern286, r"\1 \2", cleaned_content) 
    # Pattern 287
    regex_pattern287 = r'([a-z])~([A-Z])' 
    cleaned_content = re.sub(regex_pattern287, r'\1. \2', cleaned_content) 
    #? TILDAS
    # Pattern 288
    regex_pattern288 = r'\?([\W]*)~([A-Z])' 
    cleaned_content = re.sub(regex_pattern288, r'?—\2', cleaned_content) 
    # Pattern 288b
    regex_pattern288b = r'were([-–—])~([A-Z])' 
    cleaned_content = re.sub(regex_pattern288b, r'were?—I', cleaned_content)
    # Pattern 288c
    regex_pattern288c = r'nat\nnow-([-–—])~([A-Z])' 
    cleaned_content = re.sub(regex_pattern288c, r'not know, I', cleaned_content)
    # Pattern 288d
    regex_pattern288d = r'prisonet-\n([-–—])~([A-Z]).*prisonct\.\nabout' 
    cleaned_content = re.sub(regex_pattern288d, r'prisoner?— I have known Mr. Hardy, the prisoner, for about', cleaned_content)
    # Pattern 288e
    regex_pattern288e = r'\n([-–—])~([A-Z])' 
    cleaned_content = re.sub(regex_pattern288e, r'. I', cleaned_content)
    # Pattern 289
    regex_pattern289 = r'\s~\s'
    cleaned_content = re.sub(regex_pattern289, '', cleaned_content)  
    # Pattern 290
    regex_pattern290 = r'(?<=\w)~(\s|$)'
    cleaned_content = re.sub(regex_pattern290, '-', cleaned_content, flags=re.MULTILINE)
    # Pattern 291
    regex_pattern291 = r'\s~' 
    cleaned_content = re.sub(regex_pattern291, ' ', cleaned_content)
    # Pattern 291b
    regex_pattern291b = r'~' 
    cleaned_content = re.sub(regex_pattern291b, '', cleaned_content) #*
    # Pattern 292
    regex_pattern292 = r'\s\}—' 
    cleaned_content = re.sub(regex_pattern292, "?—", cleaned_content) 
    # Pattern 293
    regex_pattern293 = r',-' 
    cleaned_content = re.sub(regex_pattern293, ", ", cleaned_content) 
    # Pattern 294
    regex_pattern294 = r'\.--' 
    cleaned_content = re.sub(regex_pattern294, ".—", cleaned_content)
    # Pattern 295
    regex_pattern295 = r'\.-—(I\s[^am])' 
    cleaned_content = re.sub(regex_pattern295, r".—\1", cleaned_content)
    # Pattern 296
    regex_pattern296 = r'(\w)\.-—' 
    cleaned_content = re.sub(regex_pattern296, r"\1. ", cleaned_content)
    # Pattern 297
    regex_pattern297 = r'\.-—' 
    cleaned_content = re.sub(regex_pattern297, " ", cleaned_content)
    # Pattern 298
    regex_pattern298 = r'\b([a-z]+)---([a-z]+)\b' 
    cleaned_content = re.sub(regex_pattern298, r'\1, \2', cleaned_content)
    # Pattern 299
    regex_pattern299 = r'(\n{2})(?!794)\d+\W(\n+)' 
    cleaned_content = re.sub(regex_pattern299, r'\n\n', cleaned_content)
    # Pattern 300
    regex_pattern300 = r'\.—\.' 
    cleaned_content = re.sub(regex_pattern300, '.', cleaned_content)
    # Pattern 301
    regex_pattern301 = r'(Mr\..*?)\.-([A-Z])' 
    cleaned_content = re.sub(regex_pattern301, r'\1.—\2', cleaned_content)
    # Pattern 302
    regex_pattern302 = 'the Jury.-' 
    cleaned_content = re.sub(regex_pattern302, 'the Jury.—', cleaned_content)
    # Pattern 303
    regex_pattern303 = '‘ EvipENcE FOR THE CRowN.' 
    cleaned_content = re.sub(regex_pattern303, 'EVIDENCE FOR THE CROWN.', cleaned_content)
    # Pattern 304
    regex_pattern304 = '3.1L' 
    cleaned_content = re.sub(regex_pattern304, '', cleaned_content)
    #? ¥ 
    # Pattern 305
    regex_pattern305 = r'¥\ses' 
    cleaned_content = re.sub(regex_pattern305, 'Yes', cleaned_content)
    # Pattern 306
    regex_pattern306 = r'—¥es,$' 
    cleaned_content = re.sub(regex_pattern306, '—Yes.', cleaned_content, flags=re.MULTILINE)
    # Pattern 307
    regex_pattern307 = r'—¥es' 
    cleaned_content = re.sub(regex_pattern307, '—Yes', cleaned_content)
    # Pattern 308
    regex_pattern308 = r'—¥ou' 
    cleaned_content = re.sub(regex_pattern308, '—You', cleaned_content)
    # Pattern 309
    regex_pattern309 = r'—¥' 
    cleaned_content = re.sub(regex_pattern309, '—I', cleaned_content) 
    # Pattern 310
    regex_pattern310 = r'¥\s(have|will|think|do)' 
    cleaned_content = re.sub(regex_pattern310, r'—I \1', cleaned_content) 
    # Pattern 311
    regex_pattern311 = r'^¥\s([A-Z])' 
    cleaned_content = re.sub(regex_pattern311, r'\1', cleaned_content, flags=re.MULTILINE) 
    # Pattern 312
    regex_pattern312 = r'¥\s([A-Z])' 
    cleaned_content = re.sub(regex_pattern312, r'? \1', cleaned_content) 
    # Pattern 313
    regex_pattern313 = r'\?(\W*)es\.$' 
    cleaned_content = re.sub(regex_pattern313, r'?—Yes. \1', cleaned_content, flags=re.MULTILINE) 
    # Pattern 314
    regex_pattern314 = r'\W*\n\nes\.$' 
    cleaned_content = re.sub(regex_pattern314, r'?—Yes.', cleaned_content, flags=re.MULTILINE) 
    # Pattern 315
    regex_pattern315 = r'!\nes,$' 
    cleaned_content = re.sub(regex_pattern315, r'?—Yes.', cleaned_content, flags=re.MULTILINE) 
    # Pattern 316
    regex_pattern316 = r'not\n\now.$' 
    cleaned_content = re.sub(regex_pattern316, r'not know.', cleaned_content, flags=re.MULTILINE)     
    # Pattern 317
    regex_pattern317 = r'\s¥$' 
    cleaned_content = re.sub(regex_pattern317, '', cleaned_content, flags=re.MULTILINE)
    # Pattern 318
    regex_pattern318 = r'¥$' 
    cleaned_content = re.sub(regex_pattern318, '', cleaned_content, flags=re.MULTILINE)   
    # Pattern 319
    regex_pattern319 = r'\n¥es' 
    cleaned_content = re.sub(regex_pattern319, 'Yes', cleaned_content, flags=re.MULTILINE)   
    # Pattern 320
    regex_pattern320 = r'^¥ou' 
    cleaned_content = re.sub(regex_pattern320, 'You', cleaned_content, flags=re.MULTILINE) 
    # Pattern 321
    regex_pattern321 = r'—\n¥' 
    cleaned_content = re.sub(regex_pattern321, ' I', cleaned_content, flags=re.MULTILINE) 
    # Pattern 322
    regex_pattern322 = '¥arm' 
    cleaned_content = re.sub(regex_pattern322, 'Farm', cleaned_content) 
    # Pattern 323
    regex_pattern323 = r'—I\sdo\n\n¥\s—I\sdonot\.\n' 
    cleaned_content = re.sub(regex_pattern323, '—I do not.', cleaned_content) 
    # Pattern 324
    regex_pattern324 = r'^¥\s' 
    cleaned_content = re.sub(regex_pattern324, '', cleaned_content, flags=re.MULTILINE) 
    # Pattern 325
    regex_pattern325 = r'^¥' 
    cleaned_content = re.sub(regex_pattern325, 'ti', cleaned_content, flags=re.MULTILINE) 
    # Pattern 326
    regex_pattern325 = 'r1¥z' 
    cleaned_content = re.sub(regex_pattern325, 'LIFE', cleaned_content) 
    # Pattern 327
    regex_pattern327 = '¥ treason' 
    cleaned_content = re.sub(regex_pattern327, 'of treason', cleaned_content) 
    # Pattern 328
    regex_pattern328 = '¥4¢' 
    cleaned_content = re.sub(regex_pattern328, 'which', cleaned_content) 
    # Pattern 329
    regex_pattern329 = '¥as' 
    cleaned_content = re.sub(regex_pattern329, 'was', cleaned_content) 
    # Pattern 330
    regex_pattern330 = '¥—We' 
    cleaned_content = re.sub(regex_pattern330, '? We', cleaned_content)
    # Pattern 331
    regex_pattern331 = '¥ ant' 
    cleaned_content = re.sub(regex_pattern331, 'parlia-', cleaned_content) 
    # Pattern 332
    regex_pattern332 = r'ved,\sa3\sclear\sas\sday-light,\sthat\she\s¥\s\nnae\s‘ina\splot\.\sAnd\smin\sa\sway\stheif\sof\n\nYrying' 
    cleaned_content = re.sub(regex_pattern332, 'proved, as clear as day-light, that he was concerned in a plot. And what a way this is of trying', cleaned_content) 
    # Pattern 333
    regex_pattern333 = '\s¥' 
    cleaned_content = re.sub(regex_pattern333, '', cleaned_content) 
    # Pattern 334
    regex_pattern334 = 'VI¥Ith' 
    cleaned_content = re.sub(regex_pattern334, 'VIIIth', cleaned_content) 
    # Pattern 335
    regex_pattern335 = '-\.-' 
    cleaned_content = re.sub(regex_pattern335, ', ', cleaned_content) 
    # Pattern 336
    regex_pattern336 = ',\.-' 
    cleaned_content = re.sub(regex_pattern336, ', ', cleaned_content)
    # Pattern 337
    regex_pattern337 = 'Compton.-\sstreet.' 
    cleaned_content = re.sub(regex_pattern337, 'Compton street.', cleaned_content)
    # Pattern 338
    regex_pattern338 = r'\.-\n\nF' 
    cleaned_content = re.sub(regex_pattern338, ' F', cleaned_content)
    # Pattern 339
    regex_pattern339 = r'\.-\n' 
    cleaned_content = re.sub(regex_pattern339, '.\n', cleaned_content)
    # Pattern 340
    regex_pattern340 = r'\.-\s' 
    cleaned_content = re.sub(regex_pattern340, '—', cleaned_content)
    # Pattern 341
    regex_pattern341 = r'\.-' 
    cleaned_content = re.sub(regex_pattern341, '. ', cleaned_content)
    #? -— (hyphen en dash) to correct
    # Pattern 342
    regex_pattern342 = r'-—\s' 
    cleaned_content = re.sub(regex_pattern342, ', ', cleaned_content)
    # Pattern 343
    regex_pattern343 = r'you\?r-—Yes.' 
    cleaned_content = re.sub(regex_pattern343, 'you?—Yes.', cleaned_content)
    # Pattern 344 #? Linking lines for questions & answers.
    regex_pattern344 = r'\?\n—[^Y]es,' 
    cleaned_content = re.sub(regex_pattern344, '?—Yes.', cleaned_content)
    # Pattern 345 #? Linking lines for questions & answers.
    regex_pattern345 = r'\?\n—([A-Z])' 
    cleaned_content = re.sub(regex_pattern345, r'?—\1', cleaned_content)
    # Pattern 346 #? Linking lines for questions & answers.
    regex_pattern346 = r'\?\n—[a-z]([A-Z])' 
    cleaned_content = re.sub(regex_pattern346, r'?—\1', cleaned_content)
    # Pattern 347
    regex_pattern347 = r'\?—Yes$' 
    cleaned_content = re.sub(regex_pattern347, r'?—Yes.', cleaned_content, flags=re.MULTILINE)
    # Pattern 348 
    regex_pattern348 = r'([a-z])-—(?!Citizen|Matthew|He)([A-Z])' 
    cleaned_content = re.sub(regex_pattern348, r'\1. \2', cleaned_content)
    # Pattern 348 
    regex_pattern348 = r'([a-z])-—([A-Z])' 
    cleaned_content = re.sub(regex_pattern348, r'\1, \2', cleaned_content)
    # Pattern 349
    regex_pattern349 = r'([a-z])-—([a-z])' 
    cleaned_content = re.sub(regex_pattern349, r'\1, \2', cleaned_content)
    # Pattern 350
    regex_pattern350 = r'-—\W+$' 
    cleaned_content = re.sub(regex_pattern350, r'.\n', cleaned_content, flags=re.MULTILINE)
    # Pattern 351
    regex_pattern351 = r'\?\.\n-—(Mr\.\sHorne)' 
    cleaned_content = re.sub(regex_pattern351, r'?—\1', cleaned_content)
    # Pattern 352
    regex_pattern352 = r'-—([A-Z])' 
    cleaned_content = re.sub(regex_pattern352, r'\1', cleaned_content)
    # Pattern 353
    regex_pattern353 = r'-—([A-Z])' 
    cleaned_content = re.sub(regex_pattern353, r'\1', cleaned_content)
    # Pattern 354
    regex_pattern354 = r'^-—-' 
    cleaned_content = re.sub(regex_pattern354, r'', cleaned_content, flags=re.MULTILINE)
    # Pattern 355
    regex_pattern355 = r'\w-—-\w' 
    cleaned_content = re.sub(regex_pattern355, r', ', cleaned_content)
    # Pattern 356
    regex_pattern356 = r'-—-' 
    cleaned_content = re.sub(regex_pattern356, r'', cleaned_content)
    # Pattern 357
    regex_pattern357 = r'-—(“)' 
    cleaned_content = re.sub(regex_pattern357, r' \1', cleaned_content)
    # Pattern 358
    regex_pattern358 = r'-—‘' 
    cleaned_content = re.sub(regex_pattern358, r' “', cleaned_content)
    # Pattern 359
    regex_pattern359 = r'Lisehood”-—' 
    cleaned_content = re.sub(regex_pattern359, r'falsehood”—', cleaned_content)
    # Pattern 360
    regex_pattern360 = r'^-—([a-z])' 
    cleaned_content = re.sub(regex_pattern360, r'\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 361
    regex_pattern361 = r'([a-z])\W*-—\W*([a-z])' 
    cleaned_content = re.sub(regex_pattern361, r'\1, \2', cleaned_content)
    # Pattern 362
    regex_pattern362 = r'(\))-–' 
    cleaned_content = re.sub(regex_pattern362, r'\1—', cleaned_content)
    # Pattern 363
    regex_pattern363 = r'-–' 
    cleaned_content = re.sub(regex_pattern363, ', ', cleaned_content)
    # Pattern 364
    regex_pattern364 = r'\]\scannot' 
    cleaned_content = re.sub(regex_pattern364, 'I cannot ', cleaned_content)
    #? en dashes left to correct
    # Pattern 365
    regex_pattern365 = r'–$' 
    cleaned_content = re.sub(regex_pattern365, ', ', cleaned_content, flags=re.MULTILINE)
    # Pattern 366
    regex_pattern366 = r'^–' 
    cleaned_content = re.sub(regex_pattern366, '', cleaned_content, flags=re.MULTILINE)
    # Pattern 367 
    regex_pattern367 = 'e–you had a. violent ' 
    cleaned_content = re.sub(regex_pattern367, 'e, you had a violent ', cleaned_content)
    # Pattern 368
    regex_pattern368 = '3–' 
    cleaned_content = re.sub(regex_pattern368, ', ', cleaned_content)
    # Pattern 369
    regex_pattern369 = '(Man\?”)——' 
    cleaned_content = re.sub(regex_pattern369, r'\1— ', cleaned_content) # ? inside “” (specifically these, not "" or '' etc.)
    # Pattern 370
    regex_pattern370 = r'”–(?!Burnett)' 
    cleaned_content = re.sub(regex_pattern370, r'” ', cleaned_content)
    # Pattern 371
    regex_pattern371 = r'–((?!Burnett)([A-Z]))' 
    cleaned_content = re.sub(regex_pattern371, r', \2', cleaned_content)
    # Pattern 372
    regex_pattern372 = r'([a-z])–' 
    cleaned_content = re.sub(regex_pattern372, r'\1 ', cleaned_content)
    # Pattern 373
    regex_pattern373 = r':–' 
    cleaned_content = re.sub(regex_pattern373, r': ', cleaned_content)
    #? Hyphen cleaning
    # Pattern 374
    regex_pattern374 = r'^-\s' 
    cleaned_content = re.sub(regex_pattern374, r'', cleaned_content, flags=re.MULTILINE)
    # Pattern 375
    regex_pattern375 = r'(\.\n)-([A-Z])' 
    cleaned_content = re.sub(regex_pattern375, r'\1\n\2', cleaned_content)
    # Pattern 376
    regex_pattern376 = r'^-([A-Z])' 
    cleaned_content = re.sub(regex_pattern376, r'\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 377
    regex_pattern377 = r'(,\n)-([a-z])' 
    cleaned_content = re.sub(regex_pattern377, r'\1\2', cleaned_content)
    # Pattern 378
    regex_pattern378 = r'(-\n)-([a-z])' 
    cleaned_content = re.sub(regex_pattern378, r'\1\2', cleaned_content)
    # Pattern 379
    regex_pattern379 = r'(—\n)-([a-z])' 
    cleaned_content = re.sub(regex_pattern379, r', \2', cleaned_content)
    # Pattern 380
    regex_pattern380 = r'^--\s' 
    cleaned_content = re.sub(regex_pattern380, r'', cleaned_content, flags=re.MULTILINE)
    # Pattern 381
    regex_pattern381 = r'\?”\n--\[' 
    cleaned_content = re.sub(regex_pattern381, r'”?—I', cleaned_content)
    # Pattern 382
    regex_pattern382 = r'(\?—)\[\s' 
    cleaned_content = re.sub(regex_pattern382, r'\1I ', cleaned_content)
    # Pattern 383
    regex_pattern383 = r'(\?—)\[fe' 
    cleaned_content = re.sub(regex_pattern383, r'\1He', cleaned_content)
    # Pattern 384
    regex_pattern384 = r'(—)\[\(' 
    cleaned_content = re.sub(regex_pattern384, r'\1[', cleaned_content)
    # Pattern 385 #? linking answers to questions
    regex_pattern385 = r'(\?—)\n(Y)' 
    cleaned_content = re.sub(regex_pattern385, r'\1\2', cleaned_content)
    # Pattern 386 #? same
    regex_pattern386 = r'(\?—)\n(N)' 
    cleaned_content = re.sub(regex_pattern386, r'\1\2', cleaned_content)
    # Pattern 387 #? same
    regex_pattern387 = r'(\?—)\n([A-Z])' 
    cleaned_content = re.sub(regex_pattern387, r'\1\2', cleaned_content)
    # Pattern 388
    regex_pattern388 = r'^--' 
    cleaned_content = re.sub(regex_pattern388, r'', cleaned_content, flags=re.MULTILINE)
    # Pattern 389
    regex_pattern389 = r'((?!\s|:)(\W*))--([a-z])' 
    cleaned_content = re.sub(regex_pattern389, r', \3', cleaned_content)
    # Pattern 390
    regex_pattern390 = r'sworns--([A-Z])' 
    cleaned_content = re.sub(regex_pattern390, r'sworn.— \1', cleaned_content)
    # Pattern 391
    regex_pattern391 = r'(\n‘s)--([A-Z])' 
    cleaned_content = re.sub(regex_pattern391, r'—\2', cleaned_content)
    # Pattern 392
    regex_pattern392 = r'([a-z])--([A-Z])' 
    cleaned_content = re.sub(regex_pattern392, r'\1, \2', cleaned_content)
    # Pattern 393
    regex_pattern393 = r'\n\W*--([A-Z])' 
    cleaned_content = re.sub(regex_pattern393, r'—\1', cleaned_content)
    # Pattern 394
    regex_pattern394 = r'(\?”)(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern394, r'” ?—\3', cleaned_content)
    # Pattern 395
    regex_pattern395 = r':(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern395, r': \2', cleaned_content)
    # Pattern 396
    regex_pattern396 = r'”(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern396, r'” \2', cleaned_content)
    # Pattern 397
    regex_pattern397 = r't\s(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern397, r't?— \2', cleaned_content)
    # Pattern 398
    regex_pattern398 = 'first At the first' 
    cleaned_content = re.sub(regex_pattern398, 'first?— At the first', cleaned_content)
    # Pattern 399
    regex_pattern399 = r'([a-z])(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern399, r'\1, \3', cleaned_content)
    # Pattern 400
    regex_pattern400 = r'!(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern400, r'! \2', cleaned_content)
    # Pattern 401
    regex_pattern401 = r'7(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern401, r'?—\2', cleaned_content)
    # Pattern 402
    regex_pattern402 = r'(\]|\})(-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern402, r']—\3', cleaned_content)
    # Pattern 403
    regex_pattern403 = r';\sdid\syou\sreceive\n1t2(—-{2,})([A-Z])' 
    cleaned_content = re.sub(regex_pattern403, r'. Did you receive it?—\2', cleaned_content)
    # Pattern 404
    regex_pattern404 = r'([a-z])(—-)([a-z])' 
    cleaned_content = re.sub(regex_pattern404, r'\1, \3', cleaned_content)
    # Pattern 405
    regex_pattern405 = r':(—-)([a-z])' 
    cleaned_content = re.sub(regex_pattern405, r': \2', cleaned_content)
    # Pattern 406
    regex_pattern406 = r'"(—-)([a-z])' 
    cleaned_content = re.sub(regex_pattern406, r'" \2', cleaned_content)
    # Pattern 407
    regex_pattern407 = r',(—-)([a-z])' 
    cleaned_content = re.sub(regex_pattern407, r', \2', cleaned_content)
    # Pattern 408
    regex_pattern408 = r'(—-)([a-z])' 
    cleaned_content = re.sub(regex_pattern408, r' \2', cleaned_content)
    # Pattern 409
    regex_pattern409 = r'(”)(—-)$' 
    cleaned_content = re.sub(regex_pattern409, r'\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 410
    regex_pattern410 = r'(”)(—-)' 
    cleaned_content = re.sub(regex_pattern410, r'\1 ', cleaned_content)
    # Pattern 411
    regex_pattern411 = r'(e\.")(—-)' 
    cleaned_content = re.sub(regex_pattern411, r'\1?— ', cleaned_content)
    # Pattern 412
    regex_pattern412 = r'([a-z])\n+(—-)' 
    cleaned_content = re.sub(regex_pattern412, r'\1?—', cleaned_content)
    # Pattern 413
    regex_pattern413 = r'(\.\})(—-)' 
    cleaned_content = re.sub(regex_pattern413, r'-]— ', cleaned_content)
    # Pattern 414
    regex_pattern414 = r'\}(—-)' 
    cleaned_content = re.sub(regex_pattern414, r'— ', cleaned_content)
    # Pattern 415
    regex_pattern415 = r'(Johnson)\.(—-)' 
    cleaned_content = re.sub(regex_pattern415, r'\1.—', cleaned_content)
    # Pattern 416
    regex_pattern416 = r'(king)\.(—-)' 
    cleaned_content = re.sub(regex_pattern416, r'\1?— ', cleaned_content)
    # Pattern 417
    regex_pattern417 = r'!(—-)N' 
    cleaned_content = re.sub(regex_pattern417, r'!— N', cleaned_content)
    # Pattern 418
    regex_pattern418 = r'!(—-)' 
    cleaned_content = re.sub(regex_pattern418, r'! ', cleaned_content)
    # Pattern 419
    regex_pattern419 = r'(\.|:)(—-)$' 
    cleaned_content = re.sub(regex_pattern419, r'\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 420
    regex_pattern420 = r'(\.|:)(—-)' 
    cleaned_content = re.sub(regex_pattern420, r'\1 ', cleaned_content)
    # Pattern 421
    regex_pattern421 = r',(—-)' 
    cleaned_content = re.sub(regex_pattern421, r', ', cleaned_content)
    # Pattern 422
    regex_pattern422 = r'(\s)(—-)' 
    cleaned_content = re.sub(regex_pattern422, r' ', cleaned_content)
    # Pattern 423
    regex_pattern423 = r'Nu(—-I never did,)' 
    cleaned_content = re.sub(regex_pattern423, r'No, I never did.', cleaned_content)
    # Pattern 424
    regex_pattern424 = r'f(—-)([A-Z])' 
    cleaned_content = re.sub(regex_pattern424, r'?— \2', cleaned_content)
    # Pattern 425
    regex_pattern425 = "'—-No" 
    cleaned_content = re.sub(regex_pattern425, '?— No', cleaned_content)
    # Pattern 426
    regex_pattern426 = r'(\W)—-' 
    cleaned_content = re.sub(regex_pattern426, r'\1 ', cleaned_content)
    # Pattern 427
    regex_pattern427 = r'(were)—-\n' 
    cleaned_content = re.sub(regex_pattern427, r'\1?— ', cleaned_content)
    # Pattern 428
    regex_pattern428 = 'Hanly' 
    cleaned_content = re.sub(regex_pattern428, 'Hardy', cleaned_content)
    # Pattern 429
    regex_pattern429 = r'—-I\n\n3;' 
    cleaned_content = re.sub(regex_pattern429, r'?—', cleaned_content)
    # Pattern 430
    regex_pattern430 = r'—-$' 
    cleaned_content = re.sub(regex_pattern430, r'', cleaned_content)  
    # Pattern 431
    regex_pattern431 = r'—-$' 
    cleaned_content = re.sub(regex_pattern431, r', ', cleaned_content, flags=re.MULTILINE)  
    # Pattern 432 wich has no full stop
    regex_pattern432 = r'—-([A-Z])' 
    cleaned_content = re.sub(regex_pattern432, r'. \1', cleaned_content) 
    # Pattern 433
    regex_pattern433 = r'—-' 
    cleaned_content = re.sub(regex_pattern433, r'', cleaned_content)  
    # Pattern 434
    regex_pattern434 = r'–' 
    cleaned_content = re.sub(regex_pattern434, r' ', cleaned_content) 
    # Pattern 435
    regex_pattern435 = r'^Groves\.—' 
    cleaned_content = re.sub(regex_pattern435, r'Mr. Groves.—', cleaned_content, flags=re.MULTILINE)  
    #? ;— issues (; em dash)
    # Pattern 436
    regex_pattern436 = r'\s;—\n{2,}ow' 
    cleaned_content = re.sub(regex_pattern436, r', how', cleaned_content)  
    # Pattern 437
    regex_pattern437 = r'draught\s30\sinterlined\s;—\n\n\nonday\n\nto\sconsider\sof\sthe\suti-\n\noriginal\smaa\sprepared\sfor\sthe\spurpose\sof\n\n\n\n' 
    cleaned_content = re.sub(regex_pattern437, r'draught so interlined, ', cleaned_content)  
    # Pattern 438
    regex_pattern438 = 'stand.—Do ' 
    cleaned_content = re.sub(regex_pattern438, 'stand. Do ', cleaned_content) 
    # Pattern 439
    regex_pattern439 = r';—\n{2,}' 
    cleaned_content = re.sub(regex_pattern439, r':\n\n', cleaned_content)  
    # Pattern 440
    regex_pattern440 = r'([a-z])\s;—\n' 
    cleaned_content = re.sub(regex_pattern440, r'\1, ', cleaned_content)  
    # Pattern 441
    regex_pattern441 = r'([a-z])\s;—([A-Z])' 
    cleaned_content = re.sub(regex_pattern441, r'\1, \2', cleaned_content)  
    # Pattern 442
    regex_pattern442 = r'([a-z])\s;—([a-z])' 
    cleaned_content = re.sub(regex_pattern442, r'\1; \2', cleaned_content)  
    # Pattern 443
    regex_pattern443 = r'([a-z])\s;—\s' 
    cleaned_content = re.sub(regex_pattern443, r'\1; ', cleaned_content)  
    # Pattern 444
    regex_pattern444 = r'([a-z])\s;—“' 
    cleaned_content = re.sub(regex_pattern444, r'\1; “', cleaned_content)  
    # Pattern 445
    regex_pattern445 = r'(\s;)—' 
    cleaned_content = re.sub(regex_pattern445, r'; ', cleaned_content)  
    # Pattern 446
    regex_pattern446 = r'([a-z]);—([a-z])' 
    cleaned_content = re.sub(regex_pattern446, r'\1; \2', cleaned_content)  
    # Pattern 447
    regex_pattern447 = r'([a-z]);—([A-Z])' 
    cleaned_content = re.sub(regex_pattern447, r'\1; \2', cleaned_content)  
    # Pattern 448
    regex_pattern448 = r'([a-z]);—\n' 
    cleaned_content = re.sub(regex_pattern448, r'\1; ', cleaned_content)  
    # Pattern 449
    regex_pattern449 = r'([a-z]);—\s' 
    cleaned_content = re.sub(regex_pattern449, r'\1; ', cleaned_content) 
    # Pattern 450
    regex_pattern450 = r';—‘‘' 
    cleaned_content = re.sub(regex_pattern450, r'; “', cleaned_content)  
    # Pattern 450b
    regex_pattern450b = r'‘‘' 
    cleaned_content = re.sub(regex_pattern450b, r'“', cleaned_content)  
    # Pattern 451
    regex_pattern451 = r';—([a-z])' 
    cleaned_content = re.sub(regex_pattern451, r'; \1', cleaned_content)  
    # Pattern 452
    regex_pattern452 = r';—' 
    cleaned_content = re.sub(regex_pattern452, r'; ', cleaned_content)
    #? Fixing unlinked questions (\?—\n+) (and mistakes if possible)   
    # Pattern 453
    regex_pattern453 = r'\*~I\shad\sa\smavic' 
    cleaned_content = re.sub(regex_pattern453, r'?— I had a magic', cleaned_content)  
    # Pattern 454
    regex_pattern454 = r'^The\sInstructions\sread\.\]' 
    cleaned_content = re.sub(regex_pattern454, r'[The instructions read.]', cleaned_content)  
    # Pattern 455
    regex_pattern455 = r'there\seleven\sfone:' 
    cleaned_content = re.sub(regex_pattern455, r'there eleven months.', cleaned_content)  
    # Pattern 456
    regex_pattern456 = r'pack\?—Where ' 
    cleaned_content = re.sub(regex_pattern456, r'pack? Where ', cleaned_content)  
    # Pattern 457
    regex_pattern457 = r'How\scame\syou\sto\stalk\sabout\scavalry\s\?—' 
    cleaned_content = re.sub(regex_pattern457, r'\n\nHow came you to talk about cavalry?—', cleaned_content)  
    # Pattern 458
    regex_pattern458 = r'\nit\swas\swhen\she\swas\stalking\sabout\sthe\suse\nof\sit,' 
    cleaned_content = re.sub(regex_pattern458, r' It was when he was talking about the use of it.', cleaned_content)  
    # Pattern 459
    regex_pattern459 = r'\?—\n\ncannot\.' 
    cleaned_content = re.sub(regex_pattern459, r'?— I cannot.', cleaned_content)  
    # Pattern 460
    regex_pattern460 = r'continued\sto\sbe\stheir\sobject\sduring\smy\ssecre-\n\?—' 
    cleaned_content = re.sub(regex_pattern460, r'continued to be their object during my secreatryship.', cleaned_content)  
    # Pattern 461
    regex_pattern461 = r'\?—\n\n\n\n(You)' 
    cleaned_content = re.sub(regex_pattern461, r'?—No.\n\n\1', cleaned_content)  
    # Pattern 462
    regex_pattern462 = r'\?—\n\n\n\n(Were)' 
    cleaned_content = re.sub(regex_pattern462, r'?—No.\n\n\1', cleaned_content)  
    # Pattern 463
    regex_pattern463 = r'\?—\n\n\n\n(We)' 
    cleaned_content = re.sub(regex_pattern463, r'?—\1', cleaned_content)  
    # Pattern 464
    regex_pattern464 = r'\?—\n\n\n\n(After)' 
    cleaned_content = re.sub(regex_pattern464, r'?—No.\n\n\1', cleaned_content)  
    # Pattern 465
    regex_pattern465 = r'\?—\n\n\n\n(When)' 
    cleaned_content = re.sub(regex_pattern465, r'?—No.\n\n\1', cleaned_content)  
    # Pattern 466
    regex_pattern466 = r'\?—\n\n\n(Was)' 
    cleaned_content = re.sub(regex_pattern466, r'?—No.\n\n\1', cleaned_content)  
    # Pattern 467
    regex_pattern467 = r'\?—\n\n\n(Did)' 
    cleaned_content = re.sub(regex_pattern467, r'?—No.\n\n\1', cleaned_content)  
    # Pattern 468
    regex_pattern468 = r'pikes\?—No.\n\nmever\.' 
    cleaned_content = re.sub(regex_pattern468, r'pikes?—No; never.\n', cleaned_content)  
    # Pattern 469
    regex_pattern469 = r'\?—\n\n\n(I)' 
    cleaned_content = re.sub(regex_pattern469, r'?—\1', cleaned_content)  
    # Pattern 470
    regex_pattern470 = r'\?—\n\n\n(Those)' 
    cleaned_content = re.sub(regex_pattern470, r'?—No.\n\n\1', cleaned_content)  
    # Pattern 471
    regex_pattern471 = r'-(notes of all that passed\s\?—)\n\n‘' 
    cleaned_content = re.sub(regex_pattern471, r'\1', cleaned_content)  
    # Pattern 472
    regex_pattern472 = r'\?—\n\nJo\.\s;' 
    cleaned_content = re.sub(regex_pattern472, r'?—No.\n\n', cleaned_content)  
    # Pattern 473
    regex_pattern473 = r'2\s(him in the ordinary course of business\s\?—)\n\noO\.\s-' 
    cleaned_content = re.sub(regex_pattern473, r'of \1No.\n', cleaned_content)  
    # Pattern 474
    regex_pattern474 = r'\?—\n\n(The\s)' 
    cleaned_content = re.sub(regex_pattern474, r'?—\1', cleaned_content)  
    # Pattern 475
    regex_pattern475 = r'\?—\n\n(T\s)' 
    cleaned_content = re.sub(regex_pattern475, r'?—I ', cleaned_content)
    # Pattern 476
    regex_pattern476 = r'\?—\n\n(Mr. F)' 
    cleaned_content = re.sub(regex_pattern476, r'?—\1', cleaned_content)  
    # Pattern 477
    regex_pattern477 = r'(any)\n\nceedings( of the )Correspondimg( Society \?—)\n\n(do not know.)' 
    cleaned_content = re.sub(regex_pattern477, r'\1 proceedings\2Corresponding\3 I \4', cleaned_content)  
    # Pattern 478
    regex_pattern478 = r'(your oath \?—)\n\n(only,)' 
    cleaned_content = re.sub(regex_pattern478, r'\1 I \2', cleaned_content)  
    # Pattern 479
    regex_pattern479 = r'(fusees\?—)\n\n(They were all muskets),' 
    cleaned_content = re.sub(regex_pattern479, r'\1 \2.', cleaned_content)  
    # Pattern 480
    regex_pattern480 = r'Hew( long is it ago since you gave a note to)\nMr.\sLincolb, Mr.\sMavoaioares-\sAgent\s\?' 
    cleaned_content = re.sub(regex_pattern480, r"How\1 Mr Lincoln, Mc Macnamara's Agent?", cleaned_content)  
    # Pattern 481
    regex_pattern481 = r'platoon\sin\sgi—Yes\s:' 
    cleaned_content = re.sub(regex_pattern481, r'platoon firing?— Yes.', cleaned_content)  
    # Pattern 482
    regex_pattern482 = r'were\s2' 
    cleaned_content = re.sub(regex_pattern482, r'were a', cleaned_content)  
    # Pattern 483
    regex_pattern483 = r'\s7:' 
    cleaned_content = re.sub(regex_pattern483, r'', cleaned_content)  
    # Pattern 484
    regex_pattern484 = r'ee( you kept up that representation)\s\?—' 
    cleaned_content = re.sub(regex_pattern484, r'sation,\1?— I did.', cleaned_content)  
    # Pattern 485
    regex_pattern485 = r'(your division \?—)\n\n0\.\s2,' 
    cleaned_content = re.sub(regex_pattern485, r'\1 Number 2.', cleaned_content)  
    # Pattern 486
    regex_pattern486 = r'(are)\n\ning( to give me a description of him\?—)\n\ntis' 
    cleaned_content = re.sub(regex_pattern486, r'\1 going\2 His', cleaned_content)  
    # Pattern 487
    regex_pattern487 = r',\s\n(Let us have nothing)' 
    cleaned_content = re.sub(regex_pattern487, r'.\n\n\1', cleaned_content)  
    # Pattern 488
    regex_pattern488 = r'aflerwards\s\?—\n\n(My)' 
    cleaned_content = re.sub(regex_pattern488, r'afterwards?— \1', cleaned_content)  
    # Pattern 489
    regex_pattern489 = r'\sfe-\nspecting' 
    cleaned_content = re.sub(regex_pattern489, r' respecting', cleaned_content)  
    # Pattern 490
    regex_pattern490 = r'\?—\n\nwhen( I did attend, )1( attended the division)\nVo\.\s8,' 
    cleaned_content = re.sub(regex_pattern490, r'?— When\1I\2 Number 8.', cleaned_content)  
    # Pattern 491
    regex_pattern491 = r'(private \?—)\n\n(was),' 
    cleaned_content = re.sub(regex_pattern491, r'\1 I \2.', cleaned_content)  
    # Pattern 492
    regex_pattern492 = r'conversatien\n' 
    cleaned_content = re.sub(regex_pattern492, r'conversation ', cleaned_content)  
    # Pattern 493
    regex_pattern493 = r'(any conversation with him \?)—' 
    cleaned_content = re.sub(regex_pattern493, r'\1', cleaned_content)  
    # Pattern 494
    regex_pattern494 = r'(You have said)\n\n(you thought he did put confidence in you)\?r—\n(There was one particular occasion)' 
    cleaned_content = re.sub(regex_pattern494, r'\1 \2?— \3.', cleaned_content) 
    #? Misc (brackets) Will have to sort ed notes brackets later but for now this can stay up here.
    # Pattern 495
    regex_pattern495 = r'long,\s\]' 
    cleaned_content = re.sub(regex_pattern495, r'long.]', cleaned_content)  
    # Pattern 496
    regex_pattern496 = r'(Mr\.\sDundas)\?—\[Showing\sit\sto\sthe\switness\.\s\]--\n(This is the letter.)\s:' 
    cleaned_content = re.sub(regex_pattern496, r'\1 [Showing it to the witness.] ?— \2', cleaned_content)  
    # Pattern 497
    regex_pattern497 = r'Mar-\n\n\n\ngarot' 
    cleaned_content = re.sub(regex_pattern497, r'Margarot', cleaned_content)  
    #? Misc
    # Pattern 498
    regex_pattern498 = r'(parts)——\s—\s—\nynom.—l(I could obliterate them with )3\n(pen sont talk, Dus these is no erasure, to my)\nnowledge(, as they stand now.)' 
    cleaned_content = re.sub(regex_pattern498, r'\1.\n\nMr. Lynam.— I could obliterate them with a pen and ink, but there is no erasure, to my knowledge, as they stand now.\n', cleaned_content)  
    # Pattern 499
    regex_pattern499 = r'Lo\sChief' 
    cleaned_content = re.sub(regex_pattern499, r'Lord Chief', cleaned_content)  
    # Pattern 500
    regex_pattern500 = r'ful]' 
    cleaned_content = re.sub(regex_pattern500, r'full', cleaned_content)
    # Pattern 501
    regex_pattern501 = r'regularly\n\nkept.' 
    cleaned_content = re.sub(regex_pattern501, r'regularly kept.\n', cleaned_content)  
    # Pattern 502
    regex_pattern502 = r'Sheftield;\n—Yes.' 
    cleaned_content = re.sub(regex_pattern502, r'Sheffield?—Yes.', cleaned_content)  
    # Pattern 503
    regex_pattern503 = r'(You knew Maurice )Mar;\n—(Yes, I saw him in the)\nburgh.' 
    cleaned_content = re.sub(regex_pattern503, r'\1Margarot, did not you?—\2 Tolbooth, in Edinburgh.', cleaned_content)  
    # Pattern 504
    regex_pattern504 = r'(Are you a member of the society there\?—Yes.)\s\s—\n\n\n' 
    cleaned_content = re.sub(regex_pattern504, r'\n\1\n', cleaned_content)  
    # Pattern 505
    regex_pattern505 = r'(What did you hear at the third meeting)' 
    cleaned_content = re.sub(regex_pattern505, r'\n\1', cleaned_content)  
    # Pattern 506
    regex_pattern506 = r'eight---' 
    cleaned_content = re.sub(regex_pattern506, r'eight,', cleaned_content)  
    # Pattern 507
    regex_pattern507 = r'Pau( staid)' 
    cleaned_content = re.sub(regex_pattern507, r'And\1', cleaned_content)  
    # Pattern 508
    regex_pattern508 = r'there--\nthey' 
    cleaned_content = re.sub(regex_pattern508, r'there; they', cleaned_content)
    #? Fixing double and triple em dashes + minus signs. For the former, a lot of those are to [REDACT] names/words/etc.
    #! To wit: it seems there is a such a thing as a 3-em dash: "This type of dash is usually used to omit a person's name or signify a word has been redacted."
    #? The correction/formatting/dealing with 3-em dash or any combinations of en/em/minuses depends heavily on context given in the text and in the rest of the formatting found within Cobbett's State Trials. 
    #? for now, I am going to replace the 3-em dashes with [REDACTED] along with cases which point to redactions when verifying the original texts/pdf files/imgs.
    #? Other instances of dashes/minuses not related to redactions are usually to signal interruptions or formatting stuff.
    # Pattern 509
    regex_pattern509 = r'\s—————' 
    cleaned_content = re.sub(regex_pattern509, r'[REDACTED]', cleaned_content)  
    # Pattern 510
    regex_pattern510 = r'(arise)\s————' 
    cleaned_content = re.sub(regex_pattern510, r'\1.', cleaned_content)  
    # Pattern 511
    regex_pattern511 = r'B——— —' 
    cleaned_content = re.sub(regex_pattern511, r'B[REDACTED]', cleaned_content)  
    # Pattern 512
    regex_pattern512 = r'(the )————' 
    cleaned_content = re.sub(regex_pattern512, r'\1 [REDACTED]', cleaned_content)  
    # Pattern 513
    regex_pattern513 = r'be—————' 
    cleaned_content = re.sub(regex_pattern513, r'be.', cleaned_content)  
    # Pattern 514
    regex_pattern514 = r'(this)—————' 
    cleaned_content = re.sub(regex_pattern514, r'\1.', cleaned_content)  
    # Pattern 515
    regex_pattern515 = r'\n\n(it)—————' 
    cleaned_content = re.sub(regex_pattern515, r' \1.', cleaned_content)  
    # Pattern 516
    regex_pattern516 = r'(Mr. )————' 
    cleaned_content = re.sub(regex_pattern516, r'\1[REDACTED]', cleaned_content)  
    # Pattern 517
    regex_pattern517 = r'' 
    cleaned_content = re.sub(regex_pattern517, r'', cleaned_content)  
    # Pattern 518
    regex_pattern518 = r'———\W*$' 
    cleaned_content = re.sub(regex_pattern518, r'.\n', cleaned_content, flags=re.MULTILINE)  
    # Pattern 519
    regex_pattern519 = r'thing——ust' 
    cleaned_content = re.sub(regex_pattern519, r'thing, must', cleaned_content)  
    # Pattern 520
    regex_pattern520 = r'([a-z])——([a-z])' 
    cleaned_content = re.sub(regex_pattern520, r'\1, \2', cleaned_content)  
    # Pattern 521
    regex_pattern521 = r'(Grose)——(I)' 
    cleaned_content = re.sub(regex_pattern521, r'\1.—\2', cleaned_content)  
    # Pattern 522
    regex_pattern522 = r'([a-z])——(I)' 
    cleaned_content = re.sub(regex_pattern522, r'\1; \2', cleaned_content)  
    # Pattern 523
    regex_pattern523 = r'([a-z])——([A-Z])' 
    cleaned_content = re.sub(regex_pattern523, r'\1. \2', cleaned_content)  
    # Pattern 524
    regex_pattern524 = r'his\slite' 
    cleaned_content = re.sub(regex_pattern524, r'his life', cleaned_content)  
    # Pattern 525
    regex_pattern525 = r'([a-z])——(\n\n)' 
    cleaned_content = re.sub(regex_pattern525, r'\1.\2', cleaned_content)  
    # Pattern 526
    regex_pattern526 = r'(united )th——' 
    cleaned_content = re.sub(regex_pattern526, r'\1th[REDACTED]', cleaned_content)  
    # Pattern 527
    regex_pattern527 = r'(you h)——' 
    cleaned_content = re.sub(regex_pattern527, r'\1[REDACTED]', cleaned_content)  
    # Pattern 528
    regex_pattern528 = r'(may heaven avert)' 
    cleaned_content = re.sub(regex_pattern528, r'\1 [REDACTED]', cleaned_content)  
    # Pattern 529
    regex_pattern529 = r'P\s(Mr. Bower.)' 
    cleaned_content = re.sub(regex_pattern529, r'\1', cleaned_content)  
    # Pattern 530
    regex_pattern530 = r'(the contents)—(did it)\nes( to you to publish the Rights of Man\?)\n\n\n' 
    cleaned_content = re.sub(regex_pattern530, r'\1, \2 happen\3— No.', cleaned_content)  
    # Pattern 531
    regex_pattern531 = r'(How many copies)—(I do not ask you to)\n(within a thousand,)—(but about how many do)\n\nyqu( think you sold)\s\?' 
    cleaned_content = re.sub(regex_pattern531, r'\1, \2 \3 \4 you\5?', cleaned_content)  
    # Pattern 532
    regex_pattern532 = r'(to answer that ques)-\n\ntion\?\n' 
    cleaned_content = re.sub(regex_pattern532, r'\1tion?\n\n', cleaned_content)
    #? (\.)\s:$
    # Pattern 533 
    regex_pattern533 = r'\s-\s(\.)\s:' 
    cleaned_content = re.sub(regex_pattern533, r'', cleaned_content)  
    # Pattern 534
    regex_pattern534 = r'(in the)\n\n(custody)' 
    cleaned_content = re.sub(regex_pattern534, r'\1 \2', cleaned_content)  
    # Pattern 535
    regex_pattern535 = r'Cam-\nffen(.*)\n(.*)\n\n(general)' 
    cleaned_content = re.sub(regex_pattern535, r'Camden\1 \2 \3', cleaned_content)  
    # Pattern 536
    regex_pattern536 = r'(them\?)—Doesnot he,' 
    cleaned_content = re.sub(regex_pattern536, r'\1 Does not he,', cleaned_content)  
    # Pattern 537
    regex_pattern537 = r"(people)\n\ntoassuctate( for that public good, and, )pia\s(as)-'\nlord\n\n"
    cleaned_content = re.sub(regex_pattern537, r'\1 to associate\2being \3', cleaned_content)  
    # Pattern 538
    regex_pattern538 = r'\n(Camden tells them are not likely to be re)-\njected\}.*\n\n\n\*\s' 
    cleaned_content = re.sub(regex_pattern538, r' lord \1jected?\n\n“', cleaned_content)  
    # Pattern 539
    regex_pattern539 = r'(mankind\.)\s:' 
    cleaned_content = re.sub(regex_pattern539, r'\1', cleaned_content)  
    # Pattern 540
    regex_pattern540 = r"‘(Gentlemen, the )‘(king in his parliament)\n\n\n(could)" 
    cleaned_content = re.sub(regex_pattern540, r'\1\2 \3', cleaned_content)  
    # Pattern 541
    regex_pattern541 = r'(\.)\s:(\n\nMr)' 
    cleaned_content = re.sub(regex_pattern541, r'\1\2', cleaned_content)  
    # Pattern 542
    regex_pattern542 = r'(\.)\s:(\n\nGent)' 
    cleaned_content = re.sub(regex_pattern542, r'1\1\2', cleaned_content)  
    # Pattern 543
    regex_pattern543 = r'(\.)\s:(\n\n“)' 
    cleaned_content = re.sub(regex_pattern543, r'\1\2', cleaned_content)  
    # Pattern 544
    regex_pattern544 = r'(world\.)\s:(\n\n)' 
    cleaned_content = re.sub(regex_pattern544, r'\1', cleaned_content)  
    # Pattern 545
    regex_pattern545 = r'informed\s\]\n' 
    cleaned_content = re.sub(regex_pattern545, r'informed ', cleaned_content)  
    # Pattern 546
    regex_pattern546 = r"(lette):\n(among Mr. Adams's papers.)\s:\n\n\n"
    cleaned_content = re.sub(regex_pattern546, r'\1r \2', cleaned_content) 
    # Pattern 547
    regex_pattern547 = r'(now to )readthe’\n(answer of the Birmingham Society, dated 25th)\n(March, 1798, to this communication of )‘(the)\n(Constitutional )Socicty\.' 
    cleaned_content = re.sub(regex_pattern547, r'\1red the \2 \3\4 \5Society.', cleaned_content)  
    # Pattern 548
    regex_pattern548 = r'(“ Birmingham, March 25th, 1793.)' 
    cleaned_content = re.sub(regex_pattern548, r'\n\1', cleaned_content)  
    # Pattern 549
    regex_pattern549 = r'Ictter' 
    cleaned_content = re.sub(regex_pattern549, r'letter', cleaned_content)  
    # Pattern 550
    regex_pattern550 = r'William\n\nSkirving' 
    cleaned_content = re.sub(regex_pattern550, r'William Skirving', cleaned_content)  
    # Pattern 551
    regex_pattern551 = r'(Solomon\.)\s:\n' 
    cleaned_content = re.sub(regex_pattern551, r'\1', cleaned_content)
    # Pattern 552 
    regex_pattern552 = r'(\.)\s:(\W{2,})$' 
    cleaned_content = re.sub(regex_pattern552, r'\1', cleaned_content, flags=re.MULTILINE)  
    # Pattern 553 #* Up to here I've been doing case-by-case fixes to check that I won't accidentally delete stuff that is important like I have in the past so this is it here.
    regex_pattern553 = r'(\.)\s:$' 
    cleaned_content = re.sub(regex_pattern553, r'\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 553b
    regex_pattern553b = r'(\.)\s;$' 
    cleaned_content = re.sub(regex_pattern553b, r'\1', cleaned_content, flags=re.MULTILINE)  
    #? Back to triple em-dashes etc. 
    # Pattern 554
    regex_pattern554 = r'\n\n(an)——\s:' 
    cleaned_content = re.sub(regex_pattern554, r' \1[REDACTED].', cleaned_content)  
    # Pattern 555
    regex_pattern555 = r'(Richmond his)\n\n(uestion, without stating, by a preamble, why)\n\n(e asks it.\n\n)‘' 
    cleaned_content = re.sub(regex_pattern555, r'\1 q\2 h\3', cleaned_content)
    # Pattern 556
    regex_pattern556 = r'(Wharton)——\s:' 
    cleaned_content = re.sub(regex_pattern556, r'\1.', cleaned_content)  
    # Pattern 557
    regex_pattern557 = r'"——' 
    cleaned_content = re.sub(regex_pattern557, r'”.', cleaned_content)  
    # Pattern 558
    regex_pattern558 = r'(code)\s:”——(\n\n)(Mr. )Tauzun' 
    cleaned_content = re.sub(regex_pattern558, r'\1.”\2\3Lauzun', cleaned_content)  
    # Pattern 559
    regex_pattern559 = r'([a-z])——\.' 
    cleaned_content = re.sub(regex_pattern559, r'|1.', cleaned_content)
    # Pattern 560
    regex_pattern560 = r'(legis)-\n\n(lature)' 
    cleaned_content = re.sub(regex_pattern560, r'\1\2', cleaned_content)  
    # Pattern 561
    regex_pattern561 = r'(his ma)-\n\n(jesty)\s\?' 
    cleaned_content = re.sub(regex_pattern561, r'\1\2?', cleaned_content)  
    # Pattern 562
    regex_pattern562 = r'(were those)\n\n(terms of )' 
    cleaned_content = re.sub(regex_pattern562, r'\1 \2', cleaned_content)  
    # Pattern 563
    regex_pattern563 = r'(the House)\n\n(of Lo)' 
    cleaned_content = re.sub(regex_pattern563, r'\1 \2', cleaned_content)
    # Pattern 564
    regex_pattern564 = r'(legislature \?—I have)' 
    cleaned_content = re.sub(regex_pattern564, r'\1.', cleaned_content)  
    # Pattern 565
    regex_pattern565 = r'(What did he say about the House of Lords\?)\n\n(—He said )' 
    cleaned_content = re.sub(regex_pattern565, r'\1\2', cleaned_content)  
    # Pattern 566
    regex_pattern566 = r'(Did he recommend the abolition of any of)\n\n(those parts\?—A new modellation he recom).\n(mended.)' 
    cleaned_content = re.sub(regex_pattern566, r'\1 \2\3', cleaned_content)  
    # Pattern 567
    regex_pattern567 = r'(In what manner did he recommend them)\n\n(to be new modelled)' 
    cleaned_content = re.sub(regex_pattern567, r'\1 \2', cleaned_content)
    # Pattern 568
    regex_pattern568 = r'(How to be taken \?—By annual parliaments)\n\n(and universal suffrage.)' 
    cleaned_content = re.sub(regex_pattern568, r'\1 \2', cleaned_content)  
    # Pattern 569
    regex_pattern569 = r'(Do you know the prisoner at the bar)!' 
    cleaned_content = re.sub(regex_pattern569, r'\1?', cleaned_content)  
    # Pattern 570
    regex_pattern570 = r'(How long have you known him\?—)Abat\nfifleen( years.)' 
    cleaned_content = re.sub(regex_pattern570, r'\1 About fitfteen\2\n', cleaned_content)  
    # Pattern 571
    regex_pattern571 = r'(How long ago did he cease to be a )serra:\n(of yours\?—About three years.)"(\n\n)y\s' 
    cleaned_content = re.sub(regex_pattern571, r'\1servant \2\3', cleaned_content)
    # Pattern 572
    regex_pattern572 = r'(Richard Brindsley Sheridan, esq. swo)m—\n' 
    cleaned_content = re.sub(regex_pattern572, r'\1rn.— ', cleaned_content)  
    # Pattern 573
    regex_pattern573 = r'(that you )9' 
    cleaned_content = re.sub(regex_pattern573, r'\1saw', cleaned_content)  
    # Pattern 574
    regex_pattern574 = r'(the societies )w!\n(were then )sy\sised( to be promoting )seditna\n(or treason in the country)' 
    cleaned_content = re.sub(regex_pattern574, r'\1which \2supposed\3sedition \4.', cleaned_content)  
    # Pattern 575
    regex_pattern575 = r'Epes\sthat( occasion did you send for )Mt.' 
    cleaned_content = re.sub(regex_pattern575, r'Upon what\1Mr.', cleaned_content)
    # Pattern 576
    regex_pattern576 = r'him.” I will' 
    cleaned_content = re.sub(regex_pattern576, r'him. I will', cleaned_content)  
    # Pattern 577
    regex_pattern577 = r'1s mate' 
    cleaned_content = re.sub(regex_pattern577, r'is material', cleaned_content)
    # Pattern 577b
    regex_pattern577b = r'(stand from the conversation which pas)' 
    cleaned_content = re.sub(regex_pattern577b, r'\1ed,', cleaned_content)    
    # Pattern 578
    regex_pattern578 = r'nox$' 
    cleaned_content = re.sub(regex_pattern578, r'notice', cleaned_content, flags=re.MULTILINE)  
    # Pattern 579
    regex_pattern579 = r'soc\nties' 
    cleaned_content = re.sub(regex_pattern579, r'societies', cleaned_content)
    # Pattern 580
    regex_pattern580 = r'(ay:)' 
    cleaned_content = re.sub(regex_pattern580, r'myself', cleaned_content)  
    # Pattern 581
    regex_pattern581 = r'(sup a,)' 
    cleaned_content = re.sub(regex_pattern581, r'suppposed', cleaned_content)  
    # Pattern 582
    regex_pattern582 = r'(were stat)\n' 
    cleaned_content = re.sub(regex_pattern582, r'\1ed ', cleaned_content)  
    # Pattern 583
    regex_pattern583 = r'suppost' 
    cleaned_content = re.sub(regex_pattern583, r'supposed to be', cleaned_content)
    # Pattern 584
    regex_pattern584 = r'(be brewing in this society.)—(I conve)' 
    cleaned_content = re.sub(regex_pattern584, r'\1 \2rsed with', cleaned_content)  
    # Pattern 585
    regex_pattern585 = r'(a gentleman upon the subject; he )veg' 
    cleaned_content = re.sub(regex_pattern585, r'\1among', cleaned_content)  
    # Pattern 586
    regex_pattern586 = r"(other modes of inquiry, named to me )Fr\n(Hardy, and he stated him as a person)\n(he conceived incapable of giving into )an\n(plans, and who, he thought, could give )aid\n(every information upon )subject.\s1\n\n(I should be glad to see him: Mr. Hardy )\*\n\n\n‘" 
    cleaned_content = re.sub(regex_pattern586, r'\1Mr. \2 whom \3any such \4me \5the subject. I said \6ac', cleaned_content)  
    # Pattern 587
    regex_pattern587 = r'(tion, not)\.' 
    cleaned_content = re.sub(regex_pattern587, r'\1', cleaned_content)
    #? Dashes
    # Pattern 588
    regex_pattern588 = r'([A-Z])——' 
    cleaned_content = re.sub(regex_pattern588, r'\1[REDACTED]', cleaned_content)  
    # Pattern 589
    regex_pattern589 = r'(Did he recommend any particular )ineans( of)' 
    cleaned_content = re.sub(regex_pattern589, r'\1means\2', cleaned_content)  
    # Pattern 590
    regex_pattern590 = r'(understood him right, his meaning was)——\s\*\s(Did you ever hear him mention a conven)-\n' 
    cleaned_content = re.sub(regex_pattern590, r'\1.\n\n\2', cleaned_content)  
    # Pattern 591
    regex_pattern591 = r'([a-z])——\s;\nlod( Chief)' 
    cleaned_content = re.sub(regex_pattern591, r'\1.\n\nLord\2', cleaned_content)
    # Pattern 592
    regex_pattern592 = r'(it calum)-\nzat( the society he belonged to, and its)\needings.' 
    cleaned_content = re.sub(regex_pattern592, r'\1nniated\2 proceedings.', cleaned_content)
    #? There are em-dashes in between words. 
    # Pattern 593
    regex_pattern593 = r'(L)[^a](uzun)' 
    cleaned_content = re.sub(regex_pattern593, r'\1a\2', cleaned_content)  
    # Pattern 594
    regex_pattern594 = r'(La)[^u](zun)' 
    cleaned_content = re.sub(regex_pattern594, r'\1u\2', cleaned_content)  
    # Pattern 595
    regex_pattern595 = r'(Lau)[^z](un)' 
    cleaned_content = re.sub(regex_pattern595, r'\1z\2', cleaned_content)
    # Pattern 596
    regex_pattern596 = r'(Lauzu)[^n]()' 
    cleaned_content = re.sub(regex_pattern596, r'\1n\2', cleaned_content)  
    # Pattern 597
    regex_pattern597 = r'(Ed)[^w](ard)' 
    cleaned_content = re.sub(regex_pattern597, r'\1w\2', cleaned_content)  
    # Pattern 598 
    regex_pattern598 = r'——\nWe(are accused of pressing).( hard upon the)\n(prisoner for addressing Paine.)—(Did not this)\n\n\n\n(Norwich)' 
    cleaned_content = re.sub(regex_pattern598, r' We \1\2 \3 \4 \5', cleaned_content)  
    # Pattern 599
    regex_pattern599 = r'Paine\.—' 
    cleaned_content = re.sub(regex_pattern599, r'Paine. ', cleaned_content)
    # Pattern 600
    regex_pattern600 = r'(”)——' 
    cleaned_content = re.sub(regex_pattern600, r'\1 ', cleaned_content)
    # Pattern 601
    regex_pattern601 = r'( )[^g](entlemen)' # No such case for Cap G.
    cleaned_content = re.sub(regex_pattern601, r'\1g\2', cleaned_content)
    # Pattern 601b
    regex_pattern601b = r'(Ge)[^n](tlemen)' 
    cleaned_content = re.sub(regex_pattern601b, r'\1n\2', cleaned_content)
    # Pattern 601c
    regex_pattern601c = r'(Gent)[^l](emen)' 
    cleaned_content = re.sub(regex_pattern601c, r'\1l\2', cleaned_content)
    # Pattern 601d
    regex_pattern601d = r"(Gentleme)ry( this, and numberless )obt\n(letters of the same description, which I )mp\n(observe upon, clearly and distinctly, )\n(seems to me, show the principles, the )ve\*s\n(and the intentions of the persons )views\n(gaged in this transaction ; and the )age\n(which they meant finally to)-accomplishintentions—(I think that we may fairly )jai\n(of the views and intentions, and )evel\sa\n(principles of )aman(, not only by what he)!\n(self declares, )‘(but by the principles )thse\n(company he keeps; by the )principieso\n(whose character, and whose acts he )Pil\n—(by the principles of his publications)—\n(am told I)(am not to judge of me)\sby\n(opinions but by their actions, )ep\n(must frequently judge of the object)\n(actions by their opinions.)\s—s\srig" 
    cleaned_content = re.sub(regex_pattern601d, r'\n\1n,\2other \3might \4as it \5views, \6who are en\7means by \8 accomplish those intentions. \9judge \10even of the \11a man\12 him\13\14of the \15principles of those \16approves, \17, I \18 \19n by their \20I answer, I \21 of their \22\n', cleaned_content)
    # Pattern 601e
    regex_pattern601e = r"(Suppose the Roman Catholics, in the)\n\n\n\n\n\na(of king Willlam, had set about a reform of)\n\*'\sy(eligion, and for that purpose had attempted to)(assemble a convention, to act as a conven)-\n“2\s(tion of the )(le, for the reform of religion.)\n‘\*\s(Could you have had a doubt what sort)(of a)\n\n(reform they meant to effect\? Could you have)\n‘t\s(had a doubt that they meant to establish)\n’\s(Popery \? Would a doubt of it have existed in)\n( the )mutd( of any man\? And one great reason)\n\n(why you could not have had a doubt of it,)\n(would be, the intolerant principles of Popery)( though perhaps not of the Roman Catholic)\n(religion, for I know they make a great dis)-\n\s(tinction, and a distinction in some degree well)\n( founded, between Papists and Roman Catho)-\n(lics; but the great majority of Roman Catho)-\n(lics in England, at least in former times, were)\n\n(Papists, if they are not so now.)"
    cleaned_content = re.sub(regex_pattern601e, r'\1 reign \2 r\3 \4\5peop\6 \7 \8 \9 \10 \11\12mind\13 \14 \15,\16 \17\18\19\20\21 \22', cleaned_content)
    # Pattern 601f
    regex_pattern601f = r'^ntlemen'
    cleaned_content = re.sub(regex_pattern601f, r'Gentlemen', cleaned_content, flags=re.MULTILINE)
    # Pattern 601g
    regex_pattern601g = r'(intolerant in their political principles as the)\n\n(Papists ever were in their religious princi)-\n\n(ples. They willnot endure any other sort of go)-\s\sY(ernment to exist in the world, but their own)\n\n'
    cleaned_content = re.sub(regex_pattern601g, r'\1 \2\3v\4', cleaned_content)
    #? double-em dashes
    # Pattern 602
    regex_pattern602 = r'(-\n——\nSee sir Walter Raleigh’s case in this Col-\n\n)' 
    cleaned_content = re.sub(regex_pattern602, r'', cleaned_content)
    # Pattern 603
    regex_pattern603 = r'——\n' 
    cleaned_content = re.sub(regex_pattern603, r'', cleaned_content)
    # Pattern 604
    regex_pattern604 = r'(thought proper, not only to call itself a Con)-\n(vention of the People)—(a British Convention of)\n(.*)\n(island)—but—Tue( BRITISH CONVENTION, ONE)\n(AND INDIVISIBLE)—(and to date their transac)-\n(.*)\n(One and Indivisible.)——(What could this be)' 
    cleaned_content = re.sub(regex_pattern604, r'\1\2, \3 \4 \5, but the\6 \7, \8\9 \10 \11', cleaned_content)
    # Pattern 605
    regex_pattern605 = r'(elsewhere),—— (Now,)' 
    cleaned_content = re.sub(regex_pattern605, r'\1. \2', cleaned_content)
    # Pattern 606
    regex_pattern606 = r'(\n\npected the people, was not intended to be a \})( abolition of the slave trad)c,' 
    cleaned_content = re.sub(regex_pattern606, r'\2e.', cleaned_content)
    # Pattern 607
    regex_pattern607 = r'(petition.)’ ——' 
    cleaned_content = re.sub(regex_pattern607, r'\1” ', cleaned_content)
    # Pattern 608
    regex_pattern608 = r'aad( enumerating a long list of grievances\?)\n(— Yes),' 
    cleaned_content = re.sub(regex_pattern608, r'And\1\2.', cleaned_content)
    # Pattern 609
    regex_pattern609 = r'pe( we would be able to take the lead)\n——(the associations with you are no more, I)\n(fear)—(excuse my freedom)—(than an aristocracy)' 
    cleaned_content = re.sub(regex_pattern609, r'England,\1, \2 \3, \4, \5', cleaned_content)
    # Pattern 610
    regex_pattern610 = r'(\W)[^I]( have not)' 
    cleaned_content = re.sub(regex_pattern610, r'\1I\2', cleaned_content)
    # Pattern 611
    regex_pattern611 = r':——' 
    cleaned_content = re.sub(regex_pattern611, r': ', cleaned_content)
    # Pattern 612
    regex_pattern612 = r'(\.)——([A-Z])' 
    cleaned_content = re.sub(regex_pattern612, r'\1 \2', cleaned_content)
    # Pattern 613
    regex_pattern613 = r':\n——([A-Z])' 
    cleaned_content = re.sub(regex_pattern613, r'. \1', cleaned_content)
    # Pattern 614
    regex_pattern614 = r'ansve,\n——([A-Z])' 
    cleaned_content = re.sub(regex_pattern614, r'answer.\n\1', cleaned_content)
    # Pattern 615
    regex_pattern615 = r'(\.|,)\n——([A-Z])' 
    cleaned_content = re.sub(regex_pattern615, r'.\n\2', cleaned_content) 
    # Pattern 616 
    regex_pattern616 = r'\n——(the enclosed paper, which I, )‘(previous to)' 
    cleaned_content = re.sub(regex_pattern616, r', \1\2', cleaned_content)
    #? Starting to deal with the quotation marks etc...
    #? First  get rid of the incorrect apostrophes (‘) while correcting misc stuff that I see as I go.
    # Pattern 617
    regex_pattern617 = r'(\.\n)‘([A-Z])' 
    cleaned_content = re.sub(regex_pattern617, r'\1\2', cleaned_content)
    # Pattern 618
    regex_pattern618 = r'(\.\n)‘([h])' 
    cleaned_content = re.sub(regex_pattern618, r'\1T\2', cleaned_content)
    # Pattern 619
    regex_pattern619 = r'(is, therefore, with the utmost)\n(that )\[(ask you a few plain questions, )arismg\neut' 
    cleaned_content = re.sub(regex_pattern619, r'\1 confidence \2I \3arising out', cleaned_content)
    # Pattern 620
    regex_pattern620 = r'—(In the first place, then)' 
    cleaned_content = re.sub(regex_pattern620, r'\1', cleaned_content)
    # Pattern 621
    regex_pattern621 = r'(when they)\n\n(knew )' 
    cleaned_content = re.sub(regex_pattern621, r'\1 \2', cleaned_content)
    # Pattern 622
    regex_pattern622 = r'—(I ask you)\n((He afterwards succeeded lord Erskine in)\n((.*\n){10})(.*))' 
    cleaned_content = re.sub(regex_pattern622, r'\1 ', cleaned_content)
    # Pattern 623
    regex_pattern623 = r'e:\n(geration.)—\s\[(ask you )tarther(, whether if the pro)-\n' 
    cleaned_content = re.sub(regex_pattern623, r'exag\1 I \2rather\3', cleaned_content)
    # Pattern 624
    regex_pattern624 = r'(followed had their birth.)—(I ask you, lastly,)' 
    cleaned_content = re.sub(regex_pattern624, r'\1 \2', cleaned_content)
    # Pattern 625
    regex_pattern625 = r'(thinking)\n\ni¢\sDot' 
    cleaned_content = re.sub(regex_pattern625, r'\1 it is not', cleaned_content)
    # Pattern 626
    regex_pattern626 = r'i¢' 
    cleaned_content = re.sub(regex_pattern626, r'ic', cleaned_content)
    # Pattern 626b
    regex_pattern626b = r'¢o(n|m)' 
    cleaned_content = re.sub(regex_pattern626b, r'co\1', cleaned_content)
    # Pattern 627
    regex_pattern627 = r'(Adam,)\*\n(.*)\n\nges' 
    cleaned_content = re.sub(regex_pattern627, r'\1 \2 Judges', cleaned_content)
    # Pattern 628
    regex_pattern628 = r'‘The\shis-toryofmankinod(never furnished an instance, nor)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)\n(.*)—(in that)\n(they might be mistaken),( I am)(not arguing)\n(that point at present: if they are hereafter)(indicted for a misdemeanor, and )(Counsel).\n.(in that cause, I will then tell you what I)\n.(think of it:).(sufficient for the day is thegood or evil of it,).(it is sufficient, for the)\n(present one, that the legality or illegality)(of the business has no relation to the crime)\n(.*)' 
    cleaned_content = re.sub(regex_pattern628, r'The history of mankind \1 \2 \3 \4 \5 \6 \7 \8 \9 \10;\11 \12 \13 \14I am \15 \16 \17 \18 \19 \20 \21 \22', cleaned_content)
    # Pattern 629
    regex_pattern629 = r'\n\n(3 P 2)\n\n\n' 
    cleaned_content = re.sub(regex_pattern629, r' ', cleaned_content)
    # Pattern 630
    regex_pattern630 = r'(treason|action|ness|sovereign|whole|basis)\.—(Gentlemen)' 
    cleaned_content = re.sub(regex_pattern630, r'\1. \2', cleaned_content)
    # Pattern 631
    regex_pattern631 = r'(contents,)\n(now look at the contents.—)i\sbave( looked at)\n\nem\.' 
    cleaned_content = re.sub(regex_pattern631, r'\1 \2I have\3 them.', cleaned_content)
    # Pattern 632 
    regex_pattern632 = r'(Lord Chief Justice Eyre.—Was this a)\n(meeting of delegates)\s\s(Yes.)' 
    cleaned_content = re.sub(regex_pattern632, r'\n\1 \2?—\3', cleaned_content)
    # Pattern 633
    regex_pattern633 = r'(—)ey\n\n(You)' 
    cleaned_content = re.sub(regex_pattern633, r'\1 \2', cleaned_content)
    # Pattern 634
    regex_pattern634 = r'‘(Lynam)' 
    cleaned_content = re.sub(regex_pattern634, r'Mr. \1', cleaned_content)
    # Pattern 635
    regex_pattern635 = r'‘Froncis' 
    cleaned_content = re.sub(regex_pattern635, r'Francis', cleaned_content)
    # Pattern 636
    regex_pattern636 = r'Society —Yes.' 
    cleaned_content = re.sub(regex_pattern636, r'Society?—Yes.', cleaned_content)
    # Pattern 637 #? Deleting mistakenly added apostrophes (‘)
    regex_pattern637 = r'(\b\n)‘' 
    cleaned_content = re.sub(regex_pattern637, r'\1', cleaned_content)
    # Pattern 638
    regex_pattern638 = r'L( have no doubt o)t its being the same.\s‘' 
    cleaned_content = re.sub(regex_pattern638, r'I\1f it being the same.', cleaned_content)
    # Pattern 639
    regex_pattern639 = r'(If it is, )Eyreuny\n' 
    cleaned_content = re.sub(regex_pattern639, r'\1tyranny ', cleaned_content)
    # Pattern 640
    regex_pattern640 = r'‘Lord' 
    cleaned_content = re.sub(regex_pattern640, r'Lord', cleaned_content)
    # Pattern 641
    regex_pattern641 = r'‘onstitutional' 
    cleaned_content = re.sub(regex_pattern641, r'Constitutional', cleaned_content)
    # Pattern 642
    regex_pattern642 = r'that\n\n‘ou\s' 
    cleaned_content = re.sub(regex_pattern642, r'that you', cleaned_content)
    # Pattern 643
    regex_pattern643 = r'\npruntes may copy it, mg.' 
    cleaned_content = re.sub(regex_pattern643, r' printer may copy it.', cleaned_content)
    # Pattern 644 #? Checking around Mr\.\sSiaseast\sTyp(.*)\n\n‘(.*)\n\n (aka p. 520)
    regex_pattern644 = r'(Mr. )Juhason\.— W\shat(is the date in the title)-\n(page\?)' 
    cleaned_content = re.sub(regex_pattern644, r'\1Johnson.—What \2 \3', cleaned_content)
    # Pattern 645
    regex_pattern645 = r'lJo' 
    cleaned_content = re.sub(regex_pattern645, r'Do', cleaned_content)
    #! Pattern 646 Fixing the anchor point before Erskine's long Defence Speech.
    regex_pattern646 = r'The\sHonourable\sThomas\sErskine\.\*—Gen-\ntlemen' 
    cleaned_content = re.sub(regex_pattern646, r'Mr. Erskine.—Gentlemen', cleaned_content)
    # Pattern 647
    regex_pattern647 = r'(Mr. )Siaseast Typ (have already said, that you)(believe that to be one of the copies of the)\n\n(.*)\n(.*)\n(.*)\n\n(.*)\n(.*)\n(.*)' 
    cleaned_content = re.sub(regex_pattern647, r'\1Garrow.—You \2 \3 \4 \5 \6 \7 \8 \9', cleaned_content)
    # Pattern 648
    regex_pattern648 = r'(to)-(the Addressers\?—I beg leave to address)\n(the Court).—(My lord, this publication )hae\n(been deemed a )if' 
    cleaned_content = re.sub(regex_pattern648, r'\1 \2 \3; \4has \5libel.', cleaned_content)
    # Pattern 649
    regex_pattern649 = r'(—Symonds),' 
    cleaned_content = re.sub(regex_pattern649, r'\1.', cleaned_content)
    # Pattern 650
    regex_pattern650 = r'‘(\b[a-z]+\?)' 
    cleaned_content = re.sub(regex_pattern650, r'\1', cleaned_content)
    # Pattern 651
    regex_pattern651 = r'(not)\n\n‘o.\s‘(Their)' 
    cleaned_content = re.sub(regex_pattern651, r'\1 go. \2', cleaned_content)
    # Pattern 652
    regex_pattern652 = r'-\n‘(\b[a-z]+\.)' 
    cleaned_content = re.sub(regex_pattern652, r'\1', cleaned_content)
    # Pattern 653
    regex_pattern653 = r'dissp-\n\n‘oved.' 
    cleaned_content = re.sub(regex_pattern653, r'disapproved.', cleaned_content)
    # Pattern 654
    regex_pattern654 = r'(\w)’\n—I' 
    cleaned_content = re.sub(regex_pattern654, r'\1?—I', cleaned_content)
    # Pattern 655
    regex_pattern655 = r'’\n(—I)' 
    cleaned_content = re.sub(regex_pattern655, r'\1', cleaned_content)
    # Pattern 656 
    regex_pattern656 = r'\s’—I' 
    cleaned_content = re.sub(regex_pattern656, r'?—I', cleaned_content)
    # Pattern 657 #? Fixing single quotations marks back to double after noticing (finally) their pattern...
    regex_pattern657 = r'’—I' 
    cleaned_content = re.sub(regex_pattern657, r'”—I', cleaned_content)
    #? Fixing Witness names for the dictionary in "Speech_extractor.py" and list with misc fixes along the way
    #? quick fix I noticed
    # Pattern 658
    regex_pattern658 = r'(Mr. Erskine.—Meaning me, gentleme)t.' 
    cleaned_content = re.sub(regex_pattern658, r'\1n.\n', cleaned_content)
    #? Alexander Grant
    # Pattern 659
    regex_pattern659 = r'(Ale)[^x](ander)' 
    cleaned_content = re.sub(regex_pattern659, r'\1x\2', cleaned_content)
    # Pattern 660
    regex_pattern660 = r'(Alexa)[^n](der)' 
    cleaned_content = re.sub(regex_pattern660, r'\1n\2', cleaned_content)
    #? John Gurnell
    # Pattern 661
    regex_pattern661 = r'(Gur)[^n](ell)' 
    cleaned_content = re.sub(regex_pattern661, r'\1n\2', cleaned_content)
    # Pattern 662
    regex_pattern662 = r'Gurneli(—I found this letter i)a\n\n(Mr. Hardy\'s desk),\n\nI' 
    cleaned_content = re.sub(regex_pattern662, r'Gurnell.\1n \2.\n\n[I', cleaned_content)
    #? James Davidson
    # Pattern 663
    regex_pattern663 = r'(Da)[^v](idson)' 
    cleaned_content = re.sub(regex_pattern663, r'\1v\2', cleaned_content)
    #? Richard Williams
    # Pattern 664
    regex_pattern664 = r'\s(Wil)[^l](iams)' 
    cleaned_content = re.sub(regex_pattern664, r'\1l\2', cleaned_content)
    #? Samuel Jordan
    # Pattern 665
    regex_pattern665 = r'Lordan' 
    cleaned_content = re.sub(regex_pattern665, r'Jordan', cleaned_content)
    #? Joseph Johnson
    # Pattern 666
    regex_pattern666 = r'(J)[^o](seph)' 
    cleaned_content = re.sub(regex_pattern666, r'\1o\2', cleaned_content)
    #? William Huskisson, esq.
    # Pattern 667
    regex_pattern667 = r'pee( Huskisson delivered into court, Eng)e\n(lish translations of the French papers.\])' 
    cleaned_content = re.sub(regex_pattern667, r'[Mr.\1\2', cleaned_content)
    #? John Thompson
    # Pattern 668
    regex_pattern668 = r'Thomson' 
    cleaned_content = re.sub(regex_pattern668, r'Thompson', cleaned_content)
    #? William Broomhead
    # Pattern 669
    regex_pattern669 = r'Broonhead' 
    cleaned_content = re.sub(regex_pattern669, r'Broomhead', cleaned_content)
    # Pattern 670
    regex_pattern670 = r'^(Broomhead\.—)' 
    cleaned_content = re.sub(regex_pattern670, r'Mr. \1', cleaned_content, flags=re.MULTILINE)
    #? George Widdison
    # Pattern 671
    regex_pattern671 = r'(Widdiso)[^n]' 
    cleaned_content = re.sub(regex_pattern671, r'\1n', cleaned_content)
    #? John Coates
    # Pattern 672
    regex_pattern672 = r'Coutes' 
    cleaned_content = re.sub(regex_pattern672, r'Coates', cleaned_content)
    #? Arthur McEwan
    # Pattern 673
    regex_pattern673 = r'M‘Ewan' 
    cleaned_content = re.sub(regex_pattern673, r'McEwan', cleaned_content)
    # Pattern 674
    regex_pattern674 = r'M’Ewan' 
    cleaned_content = re.sub(regex_pattern674, r'McEwan', cleaned_content)
    #? James Clerke 
    # Pattern 675
    regex_pattern675 = r'‘o Mr. Clerke' 
    cleaned_content = re.sub(regex_pattern675, r'To Mr. Clerk.', cleaned_content)
    # Pattern 676
    regex_pattern676 = r'Clerke(\W)' 
    cleaned_content = re.sub(regex_pattern676, r'Clerk\1', cleaned_content)
    #? Francis Downling
    # Pattern 677
    regex_pattern677 = r'(Dowling)\s(—When Mr. Horne Tooke was i)t\n(the)\'(chair.)' 
    cleaned_content = re.sub(regex_pattern677, r'Mr. \1.\2n \3 \4', cleaned_content)
    # Pattern 678
    regex_pattern678 = r'(Dowling.—If)' 
    cleaned_content = re.sub(regex_pattern678, r'Mr. \1', cleaned_content)
    #? Daniel Stuart
    # Pattern 679
    regex_pattern679 = r'(the same)\n\n‘' 
    cleaned_content = re.sub(regex_pattern679, r'\1', cleaned_content)
    # Pattern 680
    regex_pattern680 = r'(the same)\n\nMr.\n\n' 
    cleaned_content = re.sub(regex_pattern680, r'\1 ', cleaned_content)
    # Pattern 681
    regex_pattern681 = r'attorn ogre' 
    cleaned_content = re.sub(regex_pattern681, r'attorney general', cleaned_content)
    #? John Carr
    # Pattern 682
    regex_pattern682 = r'(John Carr called)\.\n\n.*\n\n.*\n.*\n.*\n\n.*\n\n.*\n.*\n.*\n.*\n\nE' 
    cleaned_content = re.sub(regex_pattern682, r'\1, e', cleaned_content)
    #? James Stevens
    # Pattern 683
    regex_pattern683 = r'(The rev. James Stevens called)\.\n\n.*\n.*\n\n.*\n.*\n.*\n.*\n\nE' 
    cleaned_content = re.sub(regex_pattern683, r'\1, e', cleaned_content)
    #? Peter Macbean
    # Pattern 684
    regex_pattern684 = r'Muchean' 
    cleaned_content = re.sub(regex_pattern684, r'Macbean', cleaned_content)
    #? John Bogue
    # Pattern 685
    regex_pattern685 = r'(John Bogue, called).\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n\nE' 
    cleaned_content = re.sub(regex_pattern685, r'\1, e', cleaned_content)
    # Pattern 686
    regex_pattern686 = r'(How long have you known Mr. Hardy)’—\n' 
    cleaned_content = re.sub(regex_pattern686, r'\1?—', cleaned_content)
    #? Edward Oakes
    # Pattern 687
    regex_pattern687 = r'(Oakes.—To be elected members)\sP' 
    cleaned_content = re.sub(regex_pattern687, r'Mr. \1?', cleaned_content)
    #? William Dewsnap
    # Pattern 688
    regex_pattern688 = r'(William Dewsnap)(cross-examined by Mr. Law.— You have said that it was)-(your object to ob)-\n\n\n\n\n.*\n.*\n.*' 
    cleaned_content = re.sub(regex_pattern688, r'\1 \2 \3tain a reform by petitioning parliament, was it your object all along to obtain a reform by petitioning parliament?—It was.', cleaned_content)
    #? Duke of Richmond
    # Pattern 689
    regex_pattern689 = r'Itichmond' 
    cleaned_content = re.sub(regex_pattern689, r'Richmond', cleaned_content)
    # Pattern 690
    regex_pattern690 = r'Richrmond’s' 
    cleaned_content = re.sub(regex_pattern690, r"Richmond's", cleaned_content)
    # Pattern 691
    regex_pattern691 = r'(Richm)[^o](nd)' 
    cleaned_content = re.sub(regex_pattern691, r'\1o\2', cleaned_content)
    # Pattern 692
    regex_pattern692 = r'(Richmo)[^n](d)' 
    cleaned_content = re.sub(regex_pattern692, r'\1n\2', cleaned_content)
    # Pattern 693
    regex_pattern693 = r'soeiety\s\?—\sYes,\n\n.*\n.*\nof\.' 
    cleaned_content = re.sub(regex_pattern693, r'society?— Yes, frequently stated, and a number of the duke of', cleaned_content)
    #? Richard Brindsley Sheridan, esq.
    # Pattern 694
    regex_pattern694 = r'(Sher)[^i](dan)' 
    cleaned_content = re.sub(regex_pattern694, r'\1i\2', cleaned_content)
    #? earl of Lauderdale
    # Pattern 695
    regex_pattern695 = r'c(arl(s*)\s)' 
    cleaned_content = re.sub(regex_pattern695, r'e\1', cleaned_content)
    # Pattern 696
    regex_pattern696 = r'Laxderdale' 
    cleaned_content = re.sub(regex_pattern696, r'Lauderdale', cleaned_content)
    # Pattern 697
    regex_pattern697 = r'(nor do they afford)\n\n(.*)-\n\n\n.*\n\n' 
    cleaned_content = re.sub(regex_pattern697, r'\1 \2', cleaned_content)
    # Pattern 698
    regex_pattern698 = r'(That is for the)\n\n(.*)\n3\s(.*)\n(.*)-\n\n(.*)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern698, r'\1 \2\n\n\3\4 \5 \6', cleaned_content)
    #? One of the Jury
    # Pattern 699
    regex_pattern699 = r'(but I would rather go)\n\n(.*)\n\n.*\n.*\n.*' 
    cleaned_content = re.sub(regex_pattern699, r'\1 h\2', cleaned_content)
    # Pattern 700
    regex_pattern700 = r'\*\s(Did you )' 
    cleaned_content = re.sub(regex_pattern700, r'\1', cleaned_content)
    #? Philip Francis, esq.
    # Pattern 701
    regex_pattern701 = r'cross-exarained( by Mr.)\n(.*)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern701, r'cross-examined\1 \2— \3', cleaned_content)
    # Pattern 702
    regex_pattern702 = r'(forms of the)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern702, r'\1 \2', cleaned_content)
    # Pattern 703
    regex_pattern703 = r'(could give)\n\n\n\n.*\n\n' 
    cleaned_content = re.sub(regex_pattern703, r'', cleaned_content)
    # Pattern 704
    regex_pattern704 = r'(Philip Francis, )a( sworm.—Examined )hy\n\n(.*)\n\n(.*)\]\n(.*)' 
    cleaned_content = re.sub(regex_pattern704, r'\1esq.\2by \3— \4?— I \5', cleaned_content)
    #? Baron Hotham
    # Pattern 705
    regex_pattern705 = r'Mr.’(.*)\n\n(.*)\n\n(.*)\nSyte(.*)\n\n' 
    cleaned_content = re.sub(regex_pattern705, r'Mr.\1 o\2 c\3 fit to\4', cleaned_content)
    #? Mr. Justice Buller
    # Pattern 706
    regex_pattern706 = r'Buler' 
    cleaned_content = re.sub(regex_pattern706, r'Buller', cleaned_content)
    # Pattern 707
    regex_pattern707 = r'nizht(.*)\n(.*)-\n\n(.*)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern707, r'night\1 \2gr\3d\4', cleaned_content)
    # Pattern 708
    regex_pattern708 = r'Tiatice' 
    cleaned_content = re.sub(regex_pattern708, r'Justice', cleaned_content)
    # Pattern 709
    regex_pattern709 = r'(whic)\!\n\naE\n\n' 
    cleaned_content = re.sub(regex_pattern709, r'\1h ', cleaned_content)
    #? Felix Vaughan
    # Pattern 710
    regex_pattern710 = r'[^V](aughan)' 
    cleaned_content = re.sub(regex_pattern710, r'V\1', cleaned_content)
    #? Joseph White, esq.
    # Pattern 711
    regex_pattern711 = r'B(r. White.—It was not found among his)\n\n(.*)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern711, r'M\1 \2 ha\3', cleaned_content)
    # Pattern 712
    regex_pattern712 = r'(Mr. White)—' 
    cleaned_content = re.sub(regex_pattern712, r'\1.—', cleaned_content)
    #? William Scott
    # Pattern 713
    regex_pattern713 = r'(S)[^c](ott)' 
    cleaned_content = re.sub(regex_pattern713, r'\1c\2', cleaned_content)
    # Pattern 714
    regex_pattern714 = r'(Scott)\s—' 
    cleaned_content = re.sub(regex_pattern714, r'\1.—', cleaned_content)
    # Pattern 715
    regex_pattern715 = r'N(r\. William Scott again called)\.\n\n(.*)\n\n(.*)\n(.*)' 
    cleaned_content = re.sub(regex_pattern715, r'M\1, examined by \2 \3\n\n[\4', cleaned_content)

    #? "again called"/ "called" variations
    # Pattern 716
    regex_pattern716 = r'(Mr. Edward Lauzun again called)\.\n(.*)' 
    cleaned_content = re.sub(regex_pattern716, r'\n\1, examined by \2', cleaned_content)
    # Pattern 717
    regex_pattern717 = r'(Mr. Edward Lauzun called)\.\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern717, r'\1, examined by Mr. Garrow.— \2', cleaned_content)
    # Pattern 718
    regex_pattern718 = r'(Frederic Polydore Nodder called in again)\.\n\nE' 
    cleaned_content = re.sub(regex_pattern718, r'\1, e', cleaned_content)
    # Pattern 719
    regex_pattern719 = r'(Mr. John Gurnell called)\.\n\n' 
    cleaned_content = re.sub(regex_pattern719, r'\1, examined by Mr. Attorney General.—', cleaned_content)
    # Pattern 720
    regex_pattern720 = r'(Mr. Edward Lauzun called again)\.\n\n' 
    cleaned_content = re.sub(regex_pattern720, r'\1, examined by ', cleaned_content)
    # Pattern 721
    regex_pattern721 = r'(Mr. Willian Walker called again)\.\n\n' 
    cleaned_content = re.sub(regex_pattern721, r'\1, examined by ', cleaned_content)
    # Pattern 722
    regex_pattern722 = r'(Evan Evans again called)\.\n\n' 
    cleaned_content = re.sub(regex_pattern722, r'\1, examined by ', cleaned_content)
    # Pattern 723
    regex_pattern723 = r'(Mr. Daniel Stuart called again)\.\n\n' 
    cleaned_content = re.sub(regex_pattern723, r'\1, examined by ', cleaned_content)
    # Pattern 724
    regex_pattern724 = r'(Mr. Daniel Stuart, called in again,)\n\n' 
    cleaned_content = re.sub(regex_pattern724, r'\1 examined by ', cleaned_content)

    #? SPEAKER to SPEAKER instances
    # Pattern 725
    regex_pattern725 = r'T(o Mr. Lockhart)' 
    cleaned_content = re.sub(regex_pattern725, r'Mr. Garrow t\1', cleaned_content)
    # Pattern 726
    regex_pattern726 = r'T(o Mr. William Scott)' 
    cleaned_content = re.sub(regex_pattern726, r'Lord Chief Justice Eyre t\1', cleaned_content)
    # Pattern 727
    regex_pattern727 = r'(Mr. Garrow to Mr. Lockhart.—Open the)\n\n\n.*\n\n\n\n' 
    cleaned_content = re.sub(regex_pattern727, r'\1 ', cleaned_content)
    # Pattern 728
    regex_pattern728 = r'T(o Mr. Clerk)' 
    cleaned_content = re.sub(regex_pattern728, r'Mr. Garrow t\1', cleaned_content)
    # Pattern 729
    regex_pattern729 = r'(Mr. Garrow to William Broomhead.)' 
    cleaned_content = re.sub(regex_pattern729, r'\1—', cleaned_content)
    # Pattern 730
    regex_pattern730 = r'(Mr. Garrow to Mr. Johnson)\s' 
    cleaned_content = re.sub(regex_pattern730, r'\1.', cleaned_content)
    # Pattern 731
    regex_pattern731 = r'(Did you mark the papers you had seized?—Yes.)' 
    cleaned_content = re.sub(regex_pattern731, r'\n\1', cleaned_content)
    # Pattern 732
    regex_pattern732 = r'(Is this one of the papers you seized\?—)es,' 
    cleaned_content = re.sub(regex_pattern732, r'\1Yes.\n', cleaned_content)
    # Pattern 733
    regex_pattern733 = r'(hand-writing\?)\s—' 
    cleaned_content = re.sub(regex_pattern733, r'\1—', cleaned_content)
    # Pattern 734
    regex_pattern734 = r"T(o Alexander Grant.—Is this the prisoner's)"
    cleaned_content = re.sub(regex_pattern734, r'Mr. Bower t\1', cleaned_content)
    # Pattern 735
    regex_pattern735 = r'\(T(o Alexander Grant.)\s\)' 
    cleaned_content = re.sub(regex_pattern735, r'Lord Chief Justice Eyre t\1', cleaned_content)
    # Pattern 736
    regex_pattern736 = r'Leusun' 
    cleaned_content = re.sub(regex_pattern736, r'Lauzun', cleaned_content)
    #? Fixing start of speeches
    # Pattern 737
    regex_pattern737 = r'(Mr. Attorney General.—)\n(May it please your )' 
    cleaned_content = re.sub(regex_pattern737, r'\1 \2', cleaned_content)
    # Pattern 738
    regex_pattern738 = r'(Mr. Gibbs.—May it please your Lordships;)\n\n.*\n\n\n\n\n' 
    cleaned_content = re.sub(regex_pattern738, r'\1 Gentlemen of the jury; I need not state to', cleaned_content)
    # Pattern 739
    regex_pattern739 = r'Lord Chief’ ' 
    cleaned_content = re.sub(regex_pattern739, r'Lord Chief', cleaned_content)
    # Pattern 740
    regex_pattern740 = r'(Mr. Hardy —No, my lord.)' 
    cleaned_content = re.sub(regex_pattern740, r'Mr. Hardy.—No, my lord.', cleaned_content)
    #? Making sure that insances of SPEAKER.— are their own paragraph
    # Pattern 741
    regex_pattern741 = r'(Mr. Garrow.—This is one of the pamphlets)' 
    cleaned_content = re.sub(regex_pattern741, r'\n\1', cleaned_content)
    # Pattern 742
    regex_pattern742 = r"‘(\nMr. Erskine.—)"
    cleaned_content = re.sub(regex_pattern742, r'\n\1', cleaned_content)
    # Pattern 743
    regex_pattern743 = r'(Mr. Gurnell.—I found these papers in Mr.)' 
    cleaned_content = re.sub(regex_pattern743, r'\n\1', cleaned_content)
    # Pattern 744
    regex_pattern744 = r"‘(\nMr. Attorney General.—)"
    cleaned_content = re.sub(regex_pattern744, r'\n\1', cleaned_content)
    # Pattern 745
    regex_pattern745 = r'”(\nMr. Bower.—We will now read the Ad-)' 
    cleaned_content = re.sub(regex_pattern745, r'\n\1', cleaned_content)
    # Pattern 746
    regex_pattern746 = r'(Lauzun.—I found this paper in the pri-)' 
    cleaned_content = re.sub(regex_pattern746, r'\nMr. \1', cleaned_content)
    # Pattern 747
    regex_pattern747 = r'(Mr. Lauzun.—I found this paper in Mr.)' 
    cleaned_content = re.sub(regex_pattern747, r'\n\1', cleaned_content)
    # Pattern 748
    regex_pattern748 = r'(Mr. Garrow.—It is a letter addressed to)' 
    cleaned_content = re.sub(regex_pattern748, r'\n\1', cleaned_content)
    # Pattern 749
    regex_pattern749 = r'(Mr. Erskine.—My friend is not merely)' 
    cleaned_content = re.sub(regex_pattern749, r'\n\1', cleaned_content)
    # Pattern 750
    regex_pattern750 = r'(Mr. Garrow.—Do you know of your own)' 
    cleaned_content = re.sub(regex_pattern750, r'\n\1', cleaned_content)
    # Pattern 751
    regex_pattern751 = r'(Mr. Gurnell.—I found these papers in Mr.)' 
    cleaned_content = re.sub(regex_pattern751, r'\n\1', cleaned_content)
    # Pattern 752
    regex_pattern752 = r'(Mr. Law.—Io )' 
    cleaned_content = re.sub(regex_pattern752, r'\n\1', cleaned_content)
    # Pattern 753
    regex_pattern753 = r'(Mr. Erskine.—And )1' 
    cleaned_content = re.sub(regex_pattern753, r'\n\1I', cleaned_content)
    # Pattern 754
    regex_pattern754 = r'(Mr. Erskine.—Said by whom?)' 
    cleaned_content = re.sub(regex_pattern754, r'\n\1', cleaned_content)
    # Pattern 755
    regex_pattern755 = r'(Mr. Gibbs.—I wish it had; but I did not)' 
    cleaned_content = re.sub(regex_pattern755, r'\n\1', cleaned_content)
    # Pattern 756
    regex_pattern756 = r'(Mr. Gibbs.—I will not press the question)' 
    cleaned_content = re.sub(regex_pattern756, r'\n\1', cleaned_content)
    # Pattern 757
    regex_pattern757 = r'(Mr. Erskine.—You wrote this down at the)' 
    cleaned_content = re.sub(regex_pattern757, r'\n\1', cleaned_content)
    # Pattern 758
    regex_pattern758 = r'(Mr. Bower.—Did you receive that note from)' 
    cleaned_content = re.sub(regex_pattern758, r'\n\1', cleaned_content)
    # Pattern 759
    regex_pattern759 = r'(Mr. Erskine.—There seemed to be a sort of)' 
    cleaned_content = re.sub(regex_pattern759, r'\n\1', cleaned_content)
    # Pattern 760
    regex_pattern760 = r'(Mr. Erskine.—Supposing, for instance, that)' 
    cleaned_content = re.sub(regex_pattern760, r'\n\1', cleaned_content)
    # Pattern 761
    regex_pattern761 = r'(Mr. Erskine.—I shall only desire to look)' 
    cleaned_content = re.sub(regex_pattern761, r'\n\1', cleaned_content)
    # Pattern 762
    regex_pattern762 = r'pierChief' 
    cleaned_content = re.sub(regex_pattern762, r'Lord Chief', cleaned_content)
    # Pattern 763
    regex_pattern763 = r'(Mr. Gibbs.—This is certainly an informal)' 
    cleaned_content = re.sub(regex_pattern763, r'\n\1', cleaned_content)
    # Pattern 764
    regex_pattern764 = r'(Mr. Gibbs.—Did you ever see Mr. Martin)' 
    cleaned_content = re.sub(regex_pattern764, r'\n\1', cleaned_content)
    # Pattern 765
    regex_pattern765 = r'(Mr. Gibbs.—Because there was a direct)' 
    cleaned_content = re.sub(regex_pattern765, r'\n\1', cleaned_content)
    # Pattern 766
    regex_pattern766 = r'(Mr. Gibbs.—How long have you known the)' 
    cleaned_content = re.sub(regex_pattern766, r'\n\1', cleaned_content)
    # Pattern 767
    regex_pattern767 = r'(Mr. Attorney General.—It is not worth )u-\n\n.*' 
    cleaned_content = re.sub(regex_pattern767, r'\1arguing.', cleaned_content)
    # Pattern 768
    regex_pattern768 = r"(‘3 :)\n(.*)\n"
    cleaned_content = re.sub(regex_pattern768, r'\2', cleaned_content)
    # Pattern 769
    regex_pattern769 = r'(Mr. Erskine.—I1 have no wish to consume)\n\n' 
    cleaned_content = re.sub(regex_pattern769, r'\n\1 ', cleaned_content)
    # Pattern 770
    regex_pattern770 = r'(Mr. Bower.—As you desire to have it read,)\n\n(.*)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern770, r'\n\1 \2 \3', cleaned_content)
    # Pattern 771
    regex_pattern771 = r'(Mr. Erskine.—I said no sermon could be)' 
    cleaned_content = re.sub(regex_pattern771, r'\n\1', cleaned_content)
    # Pattern 772
    regex_pattern772 = r'(Mr. Attorney General.—It is matter of)' 
    cleaned_content = re.sub(regex_pattern772, r'\n\1', cleaned_content)
    # Pattern 773
    regex_pattern773 = r'(Mr. Erskine.—I hope you wil)\smtboffended' 
    cleaned_content = re.sub(regex_pattern773, r'\1\1l not be offended', cleaned_content)
    # Pattern 774
    regex_pattern774 = r'y(pon a cross-exami)-\n\n.*\n(.*)\s‘' 
    cleaned_content = re.sub(regex_pattern774, r'u\1nation.\n\n\2\n', cleaned_content)
    # Pattern 775
    regex_pattern775 = r'(Mr. Erskine.—I see you do not.)(Mr. Solicitor General.—The manner, sir,)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern775, r'\1\n\n\2 in which you have thought proper to con\3', cleaned_content)
    # Pattern 776
    regex_pattern776 = r'(Mr. Erskine.—We conceive that upon the)' 
    cleaned_content = re.sub(regex_pattern776, r'\n\1', cleaned_content)
    # Pattern 777
    regex_pattern777 = r'(Mr. Erskine.—I will state to your lordship)' 
    cleaned_content = re.sub(regex_pattern777, r'\n\1', cleaned_content)
    # Pattern 778
    regex_pattern778 = r'(Mr. Erskine.—I hope you wil)(Mr. Erskine.)' 
    cleaned_content = re.sub(regex_pattern778, r'\n\2', cleaned_content)
    # Pattern 779
    regex_pattern779 = r'(Lord Chief Justice Eyre.—Is it very )St\n.*' 
    cleaned_content = re.sub(regex_pattern779, r'\1fair to allude to them?\n', cleaned_content)
    # Pattern 780
    regex_pattern780 = r'(Mr. Gibbs.—I allude to them merely)\n.*\n.*\n\n.*\n\n.*\n\n\n' 
    cleaned_content = re.sub(regex_pattern780, r'\1 as ', cleaned_content)
    # Pattern 781
    regex_pattern781 = r'(Mr. Garrow \(to Mr. Huskisson\))' 
    cleaned_content = re.sub(regex_pattern781, r'Mr. Garrow to Mr. Huskisson', cleaned_content)
    # Pattern 782
    regex_pattern782 = r'x(called again)\.\n' 
    cleaned_content = re.sub(regex_pattern782, r'Alexander Grant \1, examined by ', cleaned_content)
    # Pattern 783
    regex_pattern783 = r'(I am very ready and wil)-\n\nng.' 
    cleaned_content = re.sub(regex_pattern783, r'\1ling.\n', cleaned_content)
    # Pattern 784
    regex_pattern784 = r'(Mr. Attorney General.—Suppose the Con)r\n\n\nS' 
    cleaned_content = re.sub(regex_pattern784, r'\n\1s', cleaned_content)
    # Pattern 785
    regex_pattern785 = r'(Mr. Attorney General.—I will repeat it.)' 
    cleaned_content = re.sub(regex_pattern785, r'\n\1', cleaned_content)
    # Pattern 786
    regex_pattern786 = r'(Mr. Attorney General.—I am sure I am consequence)' 
    cleaned_content = re.sub(regex_pattern786, r'\n\1', cleaned_content)
    # Pattern 787
    regex_pattern787 = r'(Mr. Attorney General.I heard said )‘(as)' 
    cleaned_content = re.sub(regex_pattern787, r'\n\1\2', cleaned_content)
    # Pattern 788
    regex_pattern788 = r'(Lord Chief Justice Eyre.—How many met)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern788, r'\1 \2\n', cleaned_content)
    # Pattern 789
    regex_pattern789 = r'(Mr. Attorney General.—The first time you)\n\n\n.*\n.*\n\n.*\n\n' 
    cleaned_content = re.sub(regex_pattern789, r'\1 were there; how many were they, to the best ', cleaned_content)
    # Pattern 790
    regex_pattern790 = r'(Mr. Attorney General.—I rise in the first)' 
    cleaned_content = re.sub(regex_pattern790, r'\n\1', cleaned_content)
    # Pattern 791
    #regex_pattern791 = r'[^(^\s*$)]\n(Mr\. Justice Buller)' 
    #cleaned_content = re.sub(regex_pattern791, r'', cleaned_content)
    # Pattern 792
    regex_pattern792 = r'(Lord Chief Justice Eyre.—I think this let-)' 
    cleaned_content = re.sub(regex_pattern792, r'\n\1', cleaned_content)
    # Pattern 793
    regex_pattern793 = r'(Lord Chief Justice Eyre.)( I wish it had)' 
    cleaned_content = re.sub(regex_pattern793, r'\n\1—\2', cleaned_content)
    # Pattern 794
    regex_pattern794 = r'(Robert Ferguson)\*(.*)\n‘(.*)' 
    cleaned_content = re.sub(regex_pattern794, r'\n\1\2\3\n', cleaned_content)
    # Pattern 795
    regex_pattern795 = r'(Lord Chief Justice Eyre.—What is this)\n\n(.*)\n.*\n\n\n\n\n' 
    cleaned_content = re.sub(regex_pattern795, r'\1 \2', cleaned_content)
    # Pattern 796
    regex_pattern796 = r'(Lord Chief Justice Eyre.— Recollecting)' 
    cleaned_content = re.sub(regex_pattern796, r'\n\1', cleaned_content)
    # Pattern 797
    regex_pattern797 = r'!\s(Mr. Erskine.—I am g)i\n(.*)\n(.*)\n(.*)-\n‘\sJ' 
    cleaned_content = re.sub(regex_pattern797, r'\1oing to prove the first \2 \3 \4', cleaned_content)
    # Pattern 798
    regex_pattern798 = r'([^(^\s*$)])\n(Lord Chief Justice Eyre)' 
    cleaned_content = re.sub(regex_pattern798, r'\1\n\n\2', cleaned_content)
    # Pattern 799
    regex_pattern799 = r'"(Lord Chief Justice Eyre.)' 
    cleaned_content = re.sub(regex_pattern799, r'\n\n\1', cleaned_content)
    # Pattern 800
    regex_pattern800 = r'(EVIDENCE FOR THE CROWN.)' 
    cleaned_content = re.sub(regex_pattern800, r'\1\n', cleaned_content)
    # Pattern 801
    #regex_pattern801 = r'([^(^\s*$)])\n(Mr\.\s(\b[A-Z][a-z]+ [A-Z][a-z]+\b))' 
    #cleaned_content = re.sub(regex_pattern801, r'', cleaned_content)
    # Pattern 802
    regex_pattern802 = r'(Mr. Edward L)ousun(.—I found this paper)\n(.*)(\n\n.*)J' 
    cleaned_content = re.sub(regex_pattern802, r'\n\1auzun\2 \3\4]', cleaned_content)
    # Pattern 803
    regex_pattern803 = r'(Mr. William Scott sworn).—( by)' 
    cleaned_content = re.sub(regex_pattern803, r'\n\1, examined\2', cleaned_content)
    # Pattern 804
    regex_pattern804 = r'x(said he believed it to be)' 
    cleaned_content = re.sub(regex_pattern804, r'Mr. Wood.—Alexander Grant \1', cleaned_content)
    # Pattern 805
    regex_pattern805 = r'\[A\sapes\sshow\sn\s(to Alexander Grant, which)\n(.*)-\n(.*):\n\n.*' 
    cleaned_content = re.sub(regex_pattern805, r"[A paper is shown \1 \2\3g.]\n", cleaned_content)
    # Pattern 806
    regex_pattern806 = r'(Mr. errow.—")(This seems the beginning of)\n(.*),\n(\n\n)' 
    cleaned_content = re.sub(regex_pattern806, r'Mr. Garrow.—\2 \3:\n', cleaned_content)
    # Pattern 807
    regex_pattern807 = r'(London Corres-)’' 
    cleaned_content = re.sub(regex_pattern807, r'\1', cleaned_content)
    # Pattern 808
    regex_pattern808 = r'(Corres)-\n\nndiog\sSuciety' 
    cleaned_content = re.sub(regex_pattern808, r'\1ponding Society', cleaned_content)
    # Pattern 809
    regex_pattern809 = r'\n\n(.*\n)(Mr. Daniel Stuart)' 
    cleaned_content = re.sub(regex_pattern809, r' \1\n\2', cleaned_content)
    # Pattern 810
    regex_pattern810 = r'(what return I have met with I leave to others)((.*\n){18})' 
    cleaned_content = re.sub(regex_pattern810, r'\1 who have heard it, to judge, without making any observartion upon it, because it is not for your lordship to redress it.\n', cleaned_content)
    # Pattern 811
    regex_pattern811 = r'\n\n‘(were upon cross-examinations, out of a proper ):\n\n(.*)\n(.*)\n(.*)\n(.*)Mr\.\n(.*)j\n\nS(.*)\n\n' 
    cleaned_content = re.sub(regex_pattern811, r' \1\2 \3 \4 \5 \6 s\7', cleaned_content)
    # Pattern 812
    regex_pattern812 = r'i( my own possession till )1( had marked them)\n\n(.*)' 
    cleaned_content = re.sub(regex_pattern812, r'in\1I\2 \3', cleaned_content)

    #? Questions starting with all cap has ‘ before them
    # Pattern 813
    regex_pattern813 = r'(Have you continued a member of the )-\n' 
    cleaned_content = re.sub(regex_pattern813, r'\1 so', cleaned_content)
    # Pattern 814
    regex_pattern814 = r'-\n\n(se of receiving a negative\?—)' 
    cleaned_content = re.sub(regex_pattern814, r'rpo\1', cleaned_content)
    # Pattern 815
    regex_pattern815 = r'(Yes)—(I might see it, but I r)-\n' 
    cleaned_content = re.sub(regex_pattern815, r'\1, \2e', cleaned_content)
    # Pattern 816
    regex_pattern816 = r'(fourteen )7\n\nThen‘' 
    cleaned_content = re.sub(regex_pattern816, r'\1years.\n\nThen ', cleaned_content)
    # Pattern 817
    regex_pattern817 = r'negetived\!—\n(.*)' 
    cleaned_content = re.sub(regex_pattern817, r'negatived?—\1\n', cleaned_content)
    # Pattern 818
    regex_pattern818 = r'j(o you know one Brown\?—Yes.)' 
    cleaned_content = re.sub(regex_pattern818, r'D\1\n', cleaned_content)
    # Pattern 819
    regex_pattern819 = r',\n(Do you know one Brown\?—Yes.)' 
    cleaned_content = re.sub(regex_pattern819, r'.\n\n\1', cleaned_content)
    # Pattern 820 #! I removed all of this (is found in "People_names.txt," in case)
    regex_pattern820 = r'(Mr. Erskine.—Undoubtedly they did think)\n((.*\n){4})' 
    cleaned_content = re.sub(regex_pattern820, r'', cleaned_content)
    # Pattern 821
    regex_pattern821 = r'(of the year 178\0?)\n\n' 
    cleaned_content = re.sub(regex_pattern821, r'\1', cleaned_content)
    #? Deleting superfluous starts and ends of court days during the trial
    # Pattern 822
    regex_pattern822 = r'(Adjourned \(it now being a quarter past)\n((.*\n){13})' 
    cleaned_content = re.sub(regex_pattern822, r'', cleaned_content)
    # Pattern 823
    regex_pattern823 = r"(It being now past twelve o'clock, a conversa)\n((.*\n){33})"
    cleaned_content = re.sub(regex_pattern823, r'', cleaned_content)
    # Pattern 824
    regex_pattern824 = r"(\[It now being half past one o’clock, om Fri-)\n((.*\n){16})"
    cleaned_content = re.sub(regex_pattern824, r'', cleaned_content)
    # Pattern 825
    regex_pattern825 = r"(\[It now being half past one o'clock, on)\n((.*\n){15})"
    cleaned_content = re.sub(regex_pattern825, r'', cleaned_content)
    # Pattern 826
    regex_pattern826 = r"(\[It being now twenty minutes past ).*\n((.*\n){12})"
    cleaned_content = re.sub(regex_pattern826, r'', cleaned_content)
    # Pattern 827
    regex_pattern827 = r'(Adjourned \(it now being twenty-five minutes)\n((.*\n){14})' 
    cleaned_content = re.sub(regex_pattern827, r'', cleaned_content)
    # Pattern 828
    regex_pattern828 = r'(It being now thirty-five minutes pastelevet)\n((.*\n){15})' 
    cleaned_content = re.sub(regex_pattern828, r'', cleaned_content)
    # Pattern 829
    regex_pattern829 = r'(ciation was a proper or an improper one, but)\n\n(.*)—' 
    cleaned_content = re.sub(regex_pattern829, r'\1 recom\2 ', cleaned_content)

    #? Deleting footnotes
    # Pattern 830
    regex_pattern830 = r'\n(SS— eee)\n\n.*\n\n\n' 
    cleaned_content = re.sub(regex_pattern830, r' grea', cleaned_content)
    # Pattern 831
    regex_pattern831 = r'(within the Kingdom,)\n\n.*\n\n\n' 
    cleaned_content = re.sub(regex_pattern831, r'\1 ', cleaned_content)
    # Pattern 832
    regex_pattern832 = r'\n\n(\* “ Holding a castle or fort against the)\n((.*\n){17})' 
    cleaned_content = re.sub(regex_pattern832, r' ', cleaned_content)
    # Pattern 833
    regex_pattern833 = r'\n\n(“It may be fairly questioned, whether)\n((.*\n){50})' 
    cleaned_content = re.sub(regex_pattern833, r' ', cleaned_content)
    # Pattern 834
    regex_pattern834 = r'\n\n(himself, with the same intent\? for the man-)\n((.*\n){45})' 
    cleaned_content = re.sub(regex_pattern834, r' ', cleaned_content)
    # Pattern 835
    regex_pattern835 = r'(whom they should not suffer to exist; and,)\n\n\n\n' 
    cleaned_content = re.sub(regex_pattern835, r'\1 ', cleaned_content)
    # Pattern 836
    regex_pattern836 = r'(letter, what were those plans for the remedy)\W*' 
    cleaned_content = re.sub(regex_pattern836, r'\1 ', cleaned_content)
    # Pattern 837
    regex_pattern837 = r'(To James Mackintosh,)\W*' 
    cleaned_content = re.sub(regex_pattern837, r'“\1 ', cleaned_content)
    # Pattern 838
    regex_pattern838 = r'(appointed delegate)\n\n.*\n' 
    cleaned_content = re.sub(regex_pattern838, r'\1 for Number 65; Mr. Richter, a party named in ', cleaned_content)
    # Pattern 839
    regex_pattern839 = r'(although the observations contained in this)\W*' 
    cleaned_content = re.sub(regex_pattern839, r'\1 ', cleaned_content)
    # Pattern 840
    regex_pattern840 = r'\n\n\n(vantages thereof equally with our-)\n((.*\n){15})' 
    cleaned_content = re.sub(regex_pattern840, r' ', cleaned_content)
    # Pattern 841
    regex_pattern841 = r'(solely to the war: enclosed you have a copy)\n((.*\n){5})' 
    cleaned_content = re.sub(regex_pattern841, r'\1 ', cleaned_content)
    # Pattern 842
    regex_pattern842 = r'(the)\n\n\n\nD' 
    cleaned_content = re.sub(regex_pattern842, r'\1 b', cleaned_content)
    # Pattern 843
    regex_pattern843 = r'(journmentin onecriminal case: but that was)a\W*' 
    cleaned_content = re.sub(regex_pattern843, r'\1 a ', cleaned_content)
    # Pattern 844
    regex_pattern844 = r'\n\n(lection.)\n\n' 
    cleaned_content = re.sub(regex_pattern844, r' ', cleaned_content)
    # Pattern 845
    regex_pattern845 = r'\n(eee See et ae)\W*' 
    cleaned_content = re.sub(regex_pattern845, r' ', cleaned_content)
    # Pattern 846
    regex_pattern846 = r'w(myself and,)\n\n' 
    cleaned_content = re.sub(regex_pattern846, r'\1 g', cleaned_content)
    # Pattern 847
    regex_pattern847 = r'(\[The Minutes of the convention at Edinburgh)\n((.*\n){15})' 
    cleaned_content = re.sub(regex_pattern847, r'', cleaned_content)
    # Pattern 848
    regex_pattern848 = r'(\[The Minutes of the convention at Edinburgh)\n((.*\n){21})' 
    cleaned_content = re.sub(regex_pattern848, r'', cleaned_content)
    # Pattern 849
    regex_pattern849 = r'(almost all the prominent characters in the)\W*"' 
    cleaned_content = re.sub(regex_pattern849, r'\1 ', cleaned_content)
    # Pattern 850
    regex_pattern850 = r'(Did any body attend that were not members)\W*' 
    cleaned_content = re.sub(regex_pattern850, r'\1 ', cleaned_content)
    # Pattern 900
    regex_pattern900 = r'\W*(15, p. 553.)\W*' 
    cleaned_content = re.sub(regex_pattern900, r' ', cleaned_content)
    # Pattern 901
    regex_pattern901 = r'(lesign, and a general plot, as clearly there)\W*' 
    cleaned_content = re.sub(regex_pattern901, r'\1 ', cleaned_content)
    # Pattern 902
    regex_pattern902 = r'(cerned; they are brought into one engage)-\W*' 
    cleaned_content = re.sub(regex_pattern902, r'\1 ', cleaned_content)
    # Pattern 903
    regex_pattern903 = r'(this question, is a material one; suppose an)\W*' 
    cleaned_content = re.sub(regex_pattern903, r'\1 ', cleaned_content)
    # Pattern 904
    regex_pattern904 = r'(that we view their ex)-\W*' 
    cleaned_content = re.sub(regex_pattern904, r'\1', cleaned_content)
    # Pattern 905
    regex_pattern905 = r'\W*(29th of July, 1814, he was sworn one of his ma-)\n((.*\n){10})' 
    cleaned_content = re.sub(regex_pattern905, r' \n', cleaned_content)
    # Pattern 906
    regex_pattern906 = r'\n*(\* See the proceedings against them before)\n((.*\n){4})\sAt' 
    cleaned_content = re.sub(regex_pattern906, r'\n\n“ At ', cleaned_content)
    # Pattern 907
    regex_pattern907 = r'(\?—The second time I)\W*' 
    cleaned_content = re.sub(regex_pattern907, r'\1 D', cleaned_content)
    # Pattern 908
    regex_pattern908 = r'\*\n\n(\* Mr. Burnett \(Treatise on various branches)\n((.*\n){11})' 
    cleaned_content = re.sub(regex_pattern908, r'', cleaned_content)
    # Pattern 909
    regex_pattern909 = r'otcasion\sres-\W*' 
    cleaned_content = re.sub(regex_pattern909, r'occasion res', cleaned_content)
    # Pattern 910
    regex_pattern910 = r'(with a)\n\n(i)' 
    cleaned_content = re.sub(regex_pattern910, r'\1 p\2', cleaned_content)
    # Pattern 911
    regex_pattern911 = r'(Yes)\W*(pamphlet, intituled “ Ecce Homo,” a. p. 1812,)\W*' 
    cleaned_content = re.sub(regex_pattern911, r'', cleaned_content)
    # Pattern 912
    regex_pattern912 = r'(mine on a cross-examination in the court in)\W*-(.*)\*\n((.*\n){11})' 
    cleaned_content = re.sub(regex_pattern912, r'\1 \2', cleaned_content)
    # Pattern 913
    regex_pattern913 = r'\W*(out to the witness the answer which is wished)\n((.*\n){18})' 
    cleaned_content = re.sub(regex_pattern913, r' ', cleaned_content)
    # Pattern 914
    regex_pattern914 = r'\W*(\* In 1812 created a baronet,)\W*' 
    cleaned_content = re.sub(regex_pattern914, r' ', cleaned_content)
    # Pattern 915
    regex_pattern915 = r'\W*j(oing on; that )' 
    cleaned_content = re.sub(regex_pattern915, r' g\1', cleaned_content)
    # Pattern 916
    regex_pattern916 = r'(hettess)\W*.*\W*' 
    cleaned_content = re.sub(regex_pattern916, r'letters ', cleaned_content)
    # Pattern 917
    regex_pattern917 = r'(\* See the Minutes of the British Conven-)\n((.*\n){6})' 
    cleaned_content = re.sub(regex_pattern917, r'', cleaned_content)
    # Pattern 918
    regex_pattern918 = r'(George Ross\* eset by Mr.)\n((.*\n){6})\W*' 
    cleaned_content = re.sub(regex_pattern918, r'George Ross sworn, examined by Mr. Garrow.— ', cleaned_content)
    # Pattern 919
    regex_pattern919 = r'\W*(23, p. 1167.)\n\n.*\W*' 
    cleaned_content = re.sub(regex_pattern919, r' ', cleaned_content)
    # Pattern 920
    regex_pattern920 = r'(naticn on the trial of David Downie, p. 61 of)\n((.*\n){4})Wo' 
    cleaned_content = re.sub(regex_pattern920, r'We', cleaned_content)
    # Pattern 921
    regex_pattern921 = r'\nJ( believe there were.)' 
    cleaned_content = re.sub(regex_pattern921, r'—I\1', cleaned_content)
    # Pattern 922
    regex_pattern922 = r'(e witness was sworn holding up his right)\n((.*\n){3})' 
    cleaned_content = re.sub(regex_pattern922, r'\n', cleaned_content)
    # Pattern 923
    regex_pattern923 = r'(See the trial of, John Stockdale ant2 Vol.)\n((.*\n){1})\s' 
    cleaned_content = re.sub(regex_pattern923, r'\n', cleaned_content)
    # Pattern 924
    regex_pattern924 = r'(determined)\!\W*' 
    cleaned_content = re.sub(regex_pattern924, r'\1 at ', cleaned_content)
    # Pattern 925
    regex_pattern925 = r'(gining the death of )i\n((.*\n){8})' 
    cleaned_content = re.sub(regex_pattern925, r'\1king William; and the overt acts charged, and principally relied on, were, first, the sending Mr. Charnock into France to king James, to desire him to persuade the French king to send forces over to Great Britain, to levy war against, and the depose the King, and that Mr. Charnock was actually sent; and, secondly, the preparing men to be levied to form a corps to assist in the restoartion to the Pretender, and the expulsion of king William, of which sir John ', cleaned_content)
    # Pattern 926
    regex_pattern926 = r'(to me, not only from the eminent services he)\W*' 
    cleaned_content = re.sub(regex_pattern926, r'\1 ', cleaned_content)
    # Pattern 927
    regex_pattern927 = r'\W*(lien ecm)\n((.*\n){4})' 
    cleaned_content = re.sub(regex_pattern927, r' ', cleaned_content)
    # Pattern 928
    regex_pattern928 = r'(such a negative of the intention, but they)\W*' 
    cleaned_content = re.sub(regex_pattern928, r'\1 ', cleaned_content)
    # Pattern 929
    regex_pattern929 = r'(\W*(Fa)\n\n.*\W*)' 
    cleaned_content = re.sub(regex_pattern929, r' ', cleaned_content)
    # Pattern 930
    regex_pattern930 = r'\n*(\* Mr. Charles Grey,).*\n((.*\n){10})' 
    cleaned_content = re.sub(regex_pattern930, r' ', cleaned_content)
    # Pattern 931
    regex_pattern931 = r'lesst ob\n((.*\n){6})ja' 
    cleaned_content = re.sub(regex_pattern931, r'least obvious sense against a poor shoemaker or any plain tradesman at a Sheffield club, while it is in', cleaned_content)
    # Pattern 932
    regex_pattern932 = r'(the strong-hold).\W*' 
    cleaned_content = re.sub(regex_pattern932, r'\1 ', cleaned_content)
    # Pattern 933
    regex_pattern933 = r'a cS RS\n\n' 
    cleaned_content = re.sub(regex_pattern933, r'', cleaned_content)
    # Pattern 934
    regex_pattern934 = r'(examined),\s;\nF' 
    cleaned_content = re.sub(regex_pattern934, r'\1\n\nT', cleaned_content)
    # Pattern 935
    regex_pattern935 = r'(of the: British cdnstitution; whbse cowmtry-)\W*' 
    cleaned_content = re.sub(regex_pattern935, r'of the British constitution; whose country', cleaned_content)
    # Pattern 936
    regex_pattern936 = r'\W*(Alluding, we believe, to Mr. Fox. Editor)\n((.*\n){9})' 
    cleaned_content = re.sub(regex_pattern936, r' ', cleaned_content)
    # Pattern 937
    regex_pattern937 = r'(and Mr. Burke seemed to question their right)\W*' 
    cleaned_content = re.sub(regex_pattern937, r'\1 ', cleaned_content)
    # Pattern 938
    regex_pattern938 = r'\W*(\* AssistantCounsel to the prisoners: a young)\n((.*\n){5})' 
    cleaned_content = re.sub(regex_pattern938, r' ', cleaned_content)
    # Pattern 939
    regex_pattern939 = r'(treason t—I am making no complaint)\n((.*\n){4})' 
    cleaned_content = re.sub(regex_pattern939, r'treason. I am making to complaint ', cleaned_content)
    # Pattern 940
    regex_pattern940 = r'( beyond their judicial pro)-\n((.*\n){5})' 
    cleaned_content = re.sub(regex_pattern940, r'\1', cleaned_content)
    # Pattern 941
    regex_pattern941 = r'\n\n(22, p. 357. org, :)\W*f' 
    cleaned_content = re.sub(regex_pattern941, r' t', cleaned_content)
    # Pattern 942
    regex_pattern942 = r'(pee that the prisoners were parties to it.—)\n((.*\n){51})' 
    cleaned_content = re.sub(regex_pattern942, r'', cleaned_content)
    # Pattern 943
    regex_pattern943 = r'\W*(collected and in parliament and pub-)\n((.*\n){49})' 
    cleaned_content = re.sub(regex_pattern943, r' ', cleaned_content)
    # Pattern 944
    regex_pattern944 = r'(Commons for his misdemeanour in)\W*' 
    cleaned_content = re.sub(regex_pattern944, r'\1 refusing ', cleaned_content)
    # Pattern 945
    regex_pattern945 = r'\s\!—(correct to re)-\W*cotd' 
    cleaned_content = re.sub(regex_pattern945, r', \1cord', cleaned_content)
    # Pattern 946
    regex_pattern946 = r'(as Dr. Johnson says,)\n\n' 
    cleaned_content = re.sub(regex_pattern946, r'\1 to expect that a great city might be drowned ', cleaned_content)
    # Pattern 947
    regex_pattern947 = r'(I have been eadeavour)-\n((.*\n){26})' 
    cleaned_content = re.sub(regex_pattern947, r'\1ing to support.\n', cleaned_content)
    # Pattern 948
    regex_pattern948 = r'\W*.*\nM(ou saw Mr. Hardy )' 
    cleaned_content = re.sub(regex_pattern948, r' up\n\nY\1', cleaned_content)
    # Pattern 949
    regex_pattern949 = r'\Weee\W*(Resolutions for conciliation with America, New)\W*' 
    cleaned_content = re.sub(regex_pattern949, r' ', cleaned_content)
    # Pattern 950
    regex_pattern950 = r'(Mr. Gibbs.—We think that every witness)\n((.*\n){8})' 
    cleaned_content = re.sub(regex_pattern950, r'\1 ', cleaned_content)
    # Pattern 951
    regex_pattern951 = r'(Did you never bear who were the editors)\W*' 
    cleaned_content = re.sub(regex_pattern951, r'\1 ', cleaned_content)
    # Pattern 952
    regex_pattern952 = r't(I have looked over the copy)\W*' 
    cleaned_content = re.sub(regex_pattern952, r'\1 ', cleaned_content)
    # Pattern 953
    regex_pattern953 = r'\W*(\* See the Debates in the New Parliamen-)\W*' 
    cleaned_content = re.sub(regex_pattern953, r' ', cleaned_content)
    # Pattern 954
    regex_pattern954 = r'-\n.*\W*(\*Hinchcliffe, Shipley.)\W*' 
    cleaned_content = re.sub(regex_pattern954, r'', cleaned_content)
    # Pattern 955
    regex_pattern955 = r'(\W*(gE aca a ca re PaO el)\W*)' 
    cleaned_content = re.sub(regex_pattern955, r' ', cleaned_content)
    # Pattern 956
    regex_pattern956 = r'\W*(charged with an act, with levying war; but)' 
    cleaned_content = re.sub(regex_pattern956, r' \1', cleaned_content)
    # Pattern 957
    regex_pattern957 = r'\W*(duty in those concerned for the crown, to a)' 
    cleaned_content = re.sub(regex_pattern957, r' \1', cleaned_content)
    # Pattern 958
    regex_pattern958 = r'T(ord Kenyon )' 
    cleaned_content = re.sub(regex_pattern958, r'L\1', cleaned_content)
    # Pattern 959
    regex_pattern959 = r'(an audience of the king, and tendered his ser)-\W*' 
    cleaned_content = re.sub(regex_pattern959, r'\1', cleaned_content)
    # Pattern 960
    regex_pattern960 = r'\W*(Russell declared so; )' 
    cleaned_content = re.sub(regex_pattern960, r'', cleaned_content)
    # Pattern 961
    regex_pattern961 = r'(sutix:)\W*y' 
    cleaned_content = re.sub(regex_pattern961, r'subject b', cleaned_content)
    # Pattern 962
    regex_pattern962 = r'(it is upon this )groasl\W*.*\W*.*\W*' 
    cleaned_content = re.sub(regex_pattern962, r'ground that ', cleaned_content)
    # Pattern 963
    regex_pattern963 = r'(kept regularly the fast of the 30th of January,)\W*' 
    cleaned_content = re.sub(regex_pattern963, r'\1 ', cleaned_content)
    # Pattern 964
    regex_pattern964 = r'\W*(214, 215. i)\n((.*\n){2})' 
    cleaned_content = re.sub(regex_pattern964, r' ', cleaned_content)
    # Pattern 965
    regex_pattern965 = r'\W*(Ny, p. 434.)\W*' 
    cleaned_content = re.sub(regex_pattern965, r' ', cleaned_content)
    # Pattern 966
    regex_pattern966 = r'\W*a\W*(C4)\W*' 
    cleaned_content = re.sub(regex_pattern966, r' ', cleaned_content)
    # Pattern 967
    regex_pattern967 = r'(The next is the case of Dammaree, )t that\W*f' 
    cleaned_content = re.sub(regex_pattern967, r'\1that familiar case ', cleaned_content)
    # Pattern 968
    regex_pattern968 = r'(many other cases I take it that words)\n((.*\n){27})' 
    cleaned_content = re.sub(regex_pattern968, r"\1 spoken by a man, not only at the time of the overt act, but before that time, are admissible, for tere is no limitation of time within which words spoken by a prisoner may not be given in eidence to explain the nature of an overt act, charged to be an overt act in the prosecution of his design of compassing the king's death\n\nNow if the crown may give evidence of the whole of a man's life, for the purpse of explaining an indifferent act, and giving it a crimial complexion, surely it follows, upon the principle of administering equal justice, that whatever he has said upon the same subject, tending to prove a differnt intention, an innocent intention, it should be copetent to him to give in evidence. I take the distinction to be this: if that which is charged upon a man to be an act, if it be a thing done, you cannot in any case give in evidence that the prisoner has denied that he did the thing. The crown in that case may give evidence, that the prisoner did at any time admit that he committed the act, that he did the thing, ", cleaned_content)
    # Pattern 969
    regex_pattern969 = r'(Lord Chief Justice Eyre.—Here the design)\W*(.*)\W*(.*)' 
    cleaned_content = re.sub(regex_pattern969, r'\1 \2 \3', cleaned_content)
    # Pattern 970
    regex_pattern970 = r'(passing the king’s death, is his consenting to)\W*' 
    cleaned_content = re.sub(regex_pattern970, r'', cleaned_content)
    # Pattern 971
    regex_pattern971 = r"\W*‘:\s(treason )"
    cleaned_content = re.sub(regex_pattern971, r' \1', cleaned_content)
    # Pattern 972
    regex_pattern972 = r'“(Mr. Gibbs.)' 
    cleaned_content = re.sub(regex_pattern972, r'\1', cleaned_content)
    # Pattern 973
    regex_pattern973 = r'\n\n(il)\n\n' 
    cleaned_content = re.sub(regex_pattern973, r' ', cleaned_content)
    # Pattern 974
    regex_pattern974 = r'(that there were associations for those pur)-\W*' 
    cleaned_content = re.sub(regex_pattern974, r'\1', cleaned_content)
    # Pattern 975
    regex_pattern975 = r'(ing it the right of the subject, upon all o)a\n((.*\n){11})' 
    cleaned_content = re.sub(regex_pattern975, r'\1cca', cleaned_content)
    # Pattern 976
    regex_pattern976 = r'(SO re err eee ree)\W*1\s' 
    cleaned_content = re.sub(regex_pattern976, r'', cleaned_content)
    # Pattern 977
    regex_pattern977 = r'(if you believe that,)\W*i' 
    cleaned_content = re.sub(regex_pattern977, r'\1 you', cleaned_content)
    # Pattern 978
    regex_pattern978 = r'\W*(clusion, but it is always a question whether)' 
    cleaned_content = re.sub(regex_pattern978, r'', cleaned_content)
    # Pattern 979
    regex_pattern979 = r'\s(spiring to raise rebellion agains the king be,)\W*' 
    cleaned_content = re.sub(regex_pattern979, r' ', cleaned_content)
    # Pattern 980
    regex_pattern980 = r'\W*(erson ef the king, and more than that from)' 
    cleaned_content = re.sub(regex_pattern980, r'p\1', cleaned_content)
    # Pattern 981
    regex_pattern981 = r'(they cannot find it to bea true charge, but)\W*' 
    cleaned_content = re.sub(regex_pattern981, r'\1 when the jury has found it, their verdict does pass for the truth, we are bound by the ver', cleaned_content)
    # Pattern 982
    regex_pattern982 = r'(We are to)r:\W*' 
    cleaned_content = re.sub(regex_pattern982, r'\1 go ', cleaned_content)
    # Pattern 983
    regex_pattern983 = r'(general opinion of the people was for this re)-\W*' 
    cleaned_content = re.sub(regex_pattern983, r'\1f', cleaned_content)
    # Pattern 984
    regex_pattern984 = r'(kid held in Scotland, before the time we held)\W*' 
    cleaned_content = re.sub(regex_pattern984, r'\1th', cleaned_content)
    # Pattern 985
    regex_pattern985 = r'\W*(a Sir John Freind’s case, ante, Voi. 13,)\W*.*\W*' 
    cleaned_content = re.sub(regex_pattern985, r'', cleaned_content)
    # Pattern 986
    regex_pattern986 = r'\W*(porting this convention, when it should te)' 
    cleaned_content = re.sub(regex_pattern986, r'\1', cleaned_content)
    # Pattern 987
    regex_pattern987 = r'\W*(mayor of Nottingham, the first magistrate of)' 
    cleaned_content = re.sub(regex_pattern987, r' ', cleaned_content)
    # Pattern 988
    regex_pattern988 = r'^(attack),$' 
    cleaned_content = re.sub(regex_pattern988, r'\1.', cleaned_content, flags=re.MULTILINE)
    # Pattern 989
    regex_pattern989 = r'\W*(given in evidence a letter from one Davison)' 
    cleaned_content = re.sub(regex_pattern989, r' \1', cleaned_content)
    # Pattern 990
    regex_pattern990 = r'\W*(meant to provide this convention, or those)' 
    cleaned_content = re.sub(regex_pattern990, r' \1', cleaned_content)
    # Pattern 991
    regex_pattern991 = r'\W*(signify what they wanted, and if they hed)' 
    cleaned_content = re.sub(regex_pattern991, r' \1', cleaned_content)
    # Pattern 992
    regex_pattern992 = r'\W*(established government of the country, is the)' 
    cleaned_content = re.sub(regex_pattern992, r' \1', cleaned_content)
    # Pattern 993
    regex_pattern993 = r'(risoner, namely, that he has compassed the)\n(.*)' 
    cleaned_content = re.sub(regex_pattern993, r"p\1 king's death.\n", cleaned_content)
    # Pattern 994
    regex_pattern994 = r'\W*(going about the country, to corrupt the sol-)' 
    cleaned_content = re.sub(regex_pattern994, r' \1', cleaned_content)
    # Pattern 995
    regex_pattern995 = r'\W*(e spoke from notes he had taken, in which)' 
    cleaned_content = re.sub(regex_pattern995, r' h\1', cleaned_content)
    # Pattern 996
    regex_pattern996 = r'mectings\W*(merely)' 
    cleaned_content = re.sub(regex_pattern996, r'meetings \1', cleaned_content)
    # Pattern 997
    regex_pattern997 = r'\W*(Did not he think it material, at the time)\W*' 
    cleaned_content = re.sub(regex_pattern997, r'.\n\n\1 ', cleaned_content)
    # Pattern 998
    regex_pattern998 = r'\W*(drafted out from the House of Commons into)' 
    cleaned_content = re.sub(regex_pattern998, r' \1', cleaned_content)
    # Pattern 999
    regex_pattern999 = r'\W*(se, but for the press of deposing the)\W*' 
    cleaned_content = re.sub(regex_pattern999, r'po\1 k', cleaned_content)
    # Pattern 1000
    regex_pattern1000 = r'\W*(be connected in this plot, we countenanced a)\W*' 
    cleaned_content = re.sub(regex_pattern1000, r'\1 ', cleaned_content)
    # Pattern 1001
    regex_pattern1001 = r'\W*(Lilt)\W*' 
    cleaned_content = re.sub(regex_pattern1001, r', ', cleaned_content)
    # Pattern 1002
    regex_pattern1002 = r'te\n(Groves.s evidence)\W*' 
    cleaned_content = re.sub(regex_pattern1002, r'to \1.\n\n\n', cleaned_content)
    # Pattern 1003
    regex_pattern1003 = r'\W*(oes farther )' 
    cleaned_content = re.sub(regex_pattern1003, r' g\1', cleaned_content)
    # Pattern 1004
    regex_pattern1004 = r'em\n\ndeavouring' 
    cleaned_content = re.sub(regex_pattern1004, r'endeavouring', cleaned_content)
    # Pattern 1005
    regex_pattern1005 = r'\W*f\s(persons of his description.)(\n\n)T' 
    cleaned_content = re.sub(regex_pattern1005, r' \1\2I', cleaned_content)
    # Pattern 1006
    regex_pattern1006 = r'\W*(convention to which they sent delegates, was)\W*' 
    cleaned_content = re.sub(regex_pattern1006, r' \1 ', cleaned_content)
    # Pattern 1007
    regex_pattern1007 = r'(Derence.)\n' 
    cleaned_content = re.sub(regex_pattern1007, r'', cleaned_content)

    #? Deleting Editor's notes []
    # Pattern 1008
    regex_pattern1008 = r'\[(?!.*REDACTED).*?\]\W*$' 
    cleaned_content = re.sub(regex_pattern1008, r'', cleaned_content, flags=re.MULTILINE)
    # Pattern 1009
    regex_pattern1009 = r'\|(—No.)' 
    cleaned_content = re.sub(regex_pattern1009, r'\1', cleaned_content)
    # Pattern 1010
    regex_pattern1010 = r'(\[the king\])' 
    cleaned_content = re.sub(regex_pattern1010, r', the king, ', cleaned_content)
    # Pattern 1011
    regex_pattern1011 = r'([A-Za-z]*\[(.*?)\])' 
    cleaned_content = re.sub(regex_pattern1011, r'', cleaned_content)
    # Pattern 1012
    regex_pattern1012 = r'(\[The following entries were read from the)\n((.*\n){3})' 
    cleaned_content = re.sub(regex_pattern1012, r'\n', cleaned_content)
    # Pattern 1013
    regex_pattern1013 = r'\n(2N ,)\n\n' 
    cleaned_content = re.sub(regex_pattern1013, r'', cleaned_content)
    # Pattern 1014 #? \n\n\[[^\]]*\n[^\]]*\]\n\n
    regex_pattern1014 = r'(\[Read from “ An Address to the British Na-)\n((.*\n){2})' 
    cleaned_content = re.sub(regex_pattern1014, r'', cleaned_content)
    # Pattern 1015
    regex_pattern1015 = r'2(—I do\.)\n\n.*' 
    cleaned_content = re.sub(regex_pattern1015, r'?\1\n', cleaned_content)
    # Pattern 1016
    regex_pattern1016 = r'\n\n\[[^\]]*\n[^\]]*\]\n\n' 
    cleaned_content = re.sub(regex_pattern1016, r'\n\n', cleaned_content)
    # Pattern 1017
    regex_pattern1017 = r'(—If they thought proper.)' 
    cleaned_content = re.sub(regex_pattern1017, r'\1\n', cleaned_content)
    # Pattern 1018 
    regex_pattern1018 = r'V(e you at any time print any book for him\?—I di)' 
    cleaned_content = re.sub(regex_pattern1018, r'Hav\1d.', cleaned_content)
    # Pattern 1019
    regex_pattern1019 = r'(intituled Rights of:)\n\n.*' 
    cleaned_content = re.sub(regex_pattern1019, r'intitled Rights of Man.', cleaned_content)
    # Pattern 1020
    regex_pattern1020 = r'Pevou' 
    cleaned_content = re.sub(regex_pattern1020, r'You', cleaned_content)
    # Pattern 1021
    regex_pattern1021 = r'.*\n(the first part of the “ Rights of Man.”\))\n\n.*\W*' 
    cleaned_content = re.sub(regex_pattern1021, r'“ ', cleaned_content)
    #? Figured out smth about the quotes... “quotes”. Someone will typically be talking and —“ cite something”— (the spaces realy just depend...) but there seems to be emdashes
    #? —\* and \*— are OCR mistakes of these
    #? and there also the single quotes, —“for when someone is ‘quoting something’ inside what they are quoting”—
    # #? or it can just look like this r'(“ That a hundred thou)' 
    #? When a quote is separated by a new paragraph (such as 2 paragraphs from a letter being quoted), then there is NO closing quote sign” at the end of the paragraph block where that quote opens “.
    #? Instead, the next paragraph will simply start with an opening quote sign “And continue the quoted passages, sometimes over multiple paragraphs if it is a long quoted passage or a whote letter,
    #? “And keep going on over maybe some \n, until eventually the quote is ended and the closing quote sign is placed ”
    #? Note, that there can be punctuation in between these quotes and the text (eg full stop, —, comma, closing fullstop of the quote) 
    # Pattern 1022
    regex_pattern1022 = r'(resolutions.)\s—\*' 
    cleaned_content = re.sub(regex_pattern1022, r'\1', cleaned_content)
    # Pattern 1023
    regex_pattern1023 = r'(\s—)\*' 
    cleaned_content = re.sub(regex_pattern1023, r'\1“', cleaned_content)
    # Pattern 1024
    regex_pattern1024 = r'—\*' 
    cleaned_content = re.sub(regex_pattern1024, r'—“', cleaned_content)
    # Pattern 1025 
    regex_pattern1025 = r'(”)\*—' 
    cleaned_content = re.sub(regex_pattern1025, r'\1—', cleaned_content)
    # Pattern 1026
    regex_pattern1026 = r'\*—No' 
    cleaned_content = re.sub(regex_pattern1026, r' No', cleaned_content)
    # Pattern 1027
    regex_pattern1027 = r'(”).\*—' 
    cleaned_content = re.sub(regex_pattern1027, r'\1—', cleaned_content)
    # Pattern 1028
    regex_pattern1028 = r'DEATR' 
    cleaned_content = re.sub(regex_pattern1028, r'DEATH', cleaned_content)
    # Pattern 1029
    regex_pattern1029 = r'“(able, to remind you once again of the great)\npun(.*)\n(.*),\n\n.*\n\n' 
    cleaned_content = re.sub(regex_pattern1029, r'\1 prin\2 \3.', cleaned_content)
    # Pattern 1030
    regex_pattern1030 = r'\*—There' 
    cleaned_content = re.sub(regex_pattern1030, r' There', cleaned_content)
    # Pattern 1031
    regex_pattern1031 = r'\*—' 
    cleaned_content = re.sub(regex_pattern1031, r'?—', cleaned_content)
    # Pattern 1032
    regex_pattern1032 = r'(—“)\* ' 
    cleaned_content = re.sub(regex_pattern1032, r'\1 ', cleaned_content)
    # Pattern 1033
    regex_pattern1033 = r'“\*' 
    cleaned_content = re.sub(regex_pattern1033, r'“', cleaned_content)
    # Pattern 1034
    regex_pattern1034 = r'“.\*' 
    cleaned_content = re.sub(regex_pattern1034, r'“', cleaned_content)
    # Pattern 1035
    regex_pattern1035 = r'“\sT\s' 
    cleaned_content = re.sub(regex_pattern1035, r'“ I ', cleaned_content)
    # Pattern 1036
    regex_pattern1036 = r'“T' 
    cleaned_content = re.sub(regex_pattern1036, r'', cleaned_content)
    # Pattern 1037
    regex_pattern1037 = r'“(!?\s)\n' 
    cleaned_content = re.sub(regex_pattern1037, r'\n\n', cleaned_content)
    # Pattern 1038
    regex_pattern1038 = r'(\* J,)' 
    cleaned_content = re.sub(regex_pattern1038, r'“ I.', cleaned_content)
    # Pattern 1039
    regex_pattern1039 = r'Jeol ove boytec ' 
    cleaned_content = re.sub(regex_pattern1039, r'Look out for us.”', cleaned_content)          #? ”’— AND “, (aka “ and \W but not \S)
    # Pattern 1040
    regex_pattern1040 = r'& Resolved,' 
    cleaned_content = re.sub(regex_pattern1040, r'“ Resolved,', cleaned_content)
    # Pattern 1041
    regex_pattern1041 = r'‘\*(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern1041, r'“\1', cleaned_content)
    # Pattern 1042
    regex_pattern1042 = r'^\*(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern1042, r'“\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 1043
    regex_pattern1043 = r'^.\*(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern1043, r'“\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 1044
    regex_pattern1044 = r'\*\*(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern1044, r'“\1', cleaned_content)
    # Pattern 1045 
    regex_pattern1045 = r'(\.)\*(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern1045, r'\1\2', cleaned_content)
    # Pattern 1046
    regex_pattern1046 = r'(\s)\*(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern1046, r'\1“\2', cleaned_content)
    # Pattern 1047
    regex_pattern1047 = r'(”)\*(\s[A-Z])' 
    cleaned_content = re.sub(regex_pattern1047, r'\1\2', cleaned_content)
    # Pattern 1048
    regex_pattern1048 = r'-\n\n(.*)\*( Abingdon,)\n\n' 
    cleaned_content = re.sub(regex_pattern1048, r'\1 \2 P', cleaned_content)
    # Pattern 1049
    regex_pattern1049 = r'”’\*' 
    cleaned_content = re.sub(regex_pattern1049, r'”', cleaned_content)
    # Pattern 1050
    regex_pattern1050 = r'\n\n\n(.*)’\*' 
    cleaned_content = re.sub(regex_pattern1050, r' \1”', cleaned_content)
    # Pattern 1051
    regex_pattern1051 = r'(wich)\*\n' 
    cleaned_content = re.sub(regex_pattern1051, r'\1 ', cleaned_content)
    # Pattern 1052 #? (\W|\S)\*(\s[a-z]) 
    regex_pattern1052 = r'^o the London Corresponding Society.$' 
    cleaned_content = re.sub(regex_pattern1052, r'', cleaned_content, flags=re.MULTILINE)
    # Pattern 1053
    regex_pattern1053 = r'\*\*(\sge)' 
    cleaned_content = re.sub(regex_pattern1053, r'“ Ge', cleaned_content)
    # Pattern 1054
    regex_pattern1054 = r'\*(\sge)' 
    cleaned_content = re.sub(regex_pattern1054, r'\nGe', cleaned_content)
    # Pattern 1055
    regex_pattern1055 = r'(,\s)\*(\s[a-z])' 
    cleaned_content = re.sub(regex_pattern1055, r'\1\2', cleaned_content)
    # Pattern 1056
    regex_pattern1056 = r'\W{2}\(tus\W*' 
    cleaned_content = re.sub(regex_pattern1056, r'', cleaned_content)
    # Pattern 1057
    regex_pattern1057 = r'(\* and December, 1792.)\n.*' 
    cleaned_content = re.sub(regex_pattern1057, r'', cleaned_content)
    # Pattern 1058
    regex_pattern1058 = r'-\n\*\s([a-z])' 
    cleaned_content = re.sub(regex_pattern1058, r'\1', cleaned_content)
    # Pattern 1059
    regex_pattern1059 = r'([a-z])\n\*\s([a-z])' 
    cleaned_content = re.sub(regex_pattern1059, r'\1 \2', cleaned_content)
    # Pattern 1060
    regex_pattern1060 = r'(D)\n\*\s([a-z])' 
    cleaned_content = re.sub(regex_pattern1060, r'Representa\2', cleaned_content)
    # Pattern 1061 #that is an emdash
    regex_pattern1061 = r'—\n\*\s([a-z])' 
    cleaned_content = re.sub(regex_pattern1061, r'—“ \1', cleaned_content)
    # Pattern 1062
    regex_pattern1062 = r'(\n\n)(“ That the speeches”—)(Gentlemen)' 
    cleaned_content = re.sub(regex_pattern1062, r'”\1\3', cleaned_content)
    # Pattern 1063
    regex_pattern1063 = r'(society\.)\s-' 
    cleaned_content = re.sub(regex_pattern1063, r'\1', cleaned_content)
    # Pattern 1064
    regex_pattern1064 = r'-\n\n\*\s([a-z])' 
    cleaned_content = re.sub(regex_pattern1064, r'\1', cleaned_content)
    # Pattern 1065
    regex_pattern1065 = r'([a-z])\n\n\*\s([a-z])' 
    cleaned_content = re.sub(regex_pattern1065, r'\1 \2', cleaned_content)
    # Pattern 1066
    regex_pattern1066 = r'\W*.*\n\n(\* societ;)\W*' 
    cleaned_content = re.sub(regex_pattern1066, r' ', cleaned_content)
    # Pattern 1067
    regex_pattern1067 = r'(whe)t\n\n\n\*(.*)-\n\n' 
    cleaned_content = re.sub(regex_pattern1067, r'\1n\2', cleaned_content)
    # Pattern 1068
    regex_pattern1068 = r'(whe)t\n\n' 
    cleaned_content = re.sub(regex_pattern1068, r'\1n ', cleaned_content)
    # Pattern 1069
    regex_pattern1069 = r'([a-z],|;)\n\n\*\s([a-z])' 
    cleaned_content = re.sub(regex_pattern1069, r'\1 \2', cleaned_content)
    # Pattern 1070
    regex_pattern1070 = r'(\s)\*(\s[a-z])' 
    cleaned_content = re.sub(regex_pattern1070, r'\1\2', cleaned_content)
    # Pattern 1071
    regex_pattern1071 = r'(,)\*(\s[a-z])' 
    cleaned_content = re.sub(regex_pattern1071, r'\1\2', cleaned_content)
    # Pattern 1072
    regex_pattern1072 = r'esq\.\*' 
    cleaned_content = re.sub(regex_pattern1072, r'esq.', cleaned_content)
    # Pattern 1073
    regex_pattern1073 = r'(”)\*(\s[a-z])' 
    cleaned_content = re.sub(regex_pattern1073, r'\1\2', cleaned_content)
    # Pattern 1074
    regex_pattern1074 = r'(;)\*(\s[a-z])' 
    cleaned_content = re.sub(regex_pattern1074, r'\1\2', cleaned_content)
    # Pattern 1075
    regex_pattern1075 = r'([a-z])\*(\s[a-z])' 
    cleaned_content = re.sub(regex_pattern1075, r'\1\2', cleaned_content)
    # Pattern 1076
    regex_pattern1076 = r'(\W)\*(\s[a-z])' 
    cleaned_content = re.sub(regex_pattern1076, r'\1\2', cleaned_content)
    # Pattern 1077
    regex_pattern1077 = r'\)\*' 
    cleaned_content = re.sub(regex_pattern1077, r')', cleaned_content)
    # Pattern 1078
    regex_pattern1078 = r'””\*' 
    cleaned_content = re.sub(regex_pattern1078, r'”', cleaned_content)
    # Pattern 1079
    regex_pattern1079 = r'”' 
    cleaned_content = re.sub(regex_pattern1079, r'', cleaned_content)
    # Pattern 1080
    regex_pattern1080 = r'1( therefore consider the case of lord)\sG\n' 
    cleaned_content = re.sub(regex_pattern1080, r'I\1 ', cleaned_content)
    # Pattern 1081
    regex_pattern1081 = r'([a-z])\*([a-z])' 
    cleaned_content = re.sub(regex_pattern1081, r'\1\2', cleaned_content)
    # Pattern 1082
    regex_pattern1082 = r'([a-z])\*\s' 
    cleaned_content = re.sub(regex_pattern1082, r'\1 ', cleaned_content)
    # Pattern 1083
    regex_pattern1083 = r'([a-z])\*' 
    cleaned_content = re.sub(regex_pattern1083, r'\1', cleaned_content)
    # Pattern 1084
    regex_pattern1084 = r'(\.)\*' 
    cleaned_content = re.sub(regex_pattern1084, r'\1', cleaned_content)
    # Pattern 1085
    regex_pattern1085 = r'(;)\*' 
    cleaned_content = re.sub(regex_pattern1085, r'\1', cleaned_content)
    # Pattern 1086
    regex_pattern1086 = r'\s\*\s—\ne8\.' 
    cleaned_content = re.sub(regex_pattern1086, r'—Yes.', cleaned_content)
    # Pattern 1087
    regex_pattern1087 = r'\.\s\*' 
    cleaned_content = re.sub(regex_pattern1087, r'.', cleaned_content)
    # Pattern 1088
    regex_pattern1088 = r'\s\*\n—Itis.' 
    cleaned_content = re.sub(regex_pattern1088, r'?—It is.', cleaned_content)
    # Pattern 1089
    regex_pattern1089 = r'\s\*‘' 
    cleaned_content = re.sub(regex_pattern1089, r' “', cleaned_content)
    # Pattern 1090
    regex_pattern1090 = r'‘\s\*' 
    cleaned_content = re.sub(regex_pattern1090, r'”', cleaned_content)
    # Pattern 1091
    regex_pattern1091 = r'\s\*' 
    cleaned_content = re.sub(regex_pattern1091, r'', cleaned_content)
    # Pattern 1092
    regex_pattern1092 = r'\[*\*' 
    cleaned_content = re.sub(regex_pattern1092, r'', cleaned_content)
    # Pattern 1093
    regex_pattern1093 = r'\n\n(friends and fellow-labourers),\n..\n*.*\n*.*\n.*' 
    cleaned_content = re.sub(regex_pattern1093, r'\1.', cleaned_content)
    # Pattern 1094
    regex_pattern1094 = r'Lauzisn' 
    cleaned_content = re.sub(regex_pattern1094, r'Lauzun', cleaned_content)
    # Pattern 1095
    regex_pattern1095 = r'\.\s;\s\n“' 
    cleaned_content = re.sub(regex_pattern1095, r'.\n\n“', cleaned_content)
    # Pattern 1096
    regex_pattern1096 = r'”(\s\n)' 
    cleaned_content = re.sub(regex_pattern1096, r'”\1', cleaned_content)
    
    #? a big hyphen joining
    # Pattern 1097
    regex_pattern1097 = r'([a-z])-(\n{2,})([a-z])' 
    cleaned_content = re.sub(regex_pattern1097, r'\1\3', cleaned_content)
    #? and joining 
    # Pattern 1098
    regex_pattern1098 = r'([a-z])(\n{2,})([a-z])' 
    cleaned_content = re.sub(regex_pattern1098, r'\1 \3', cleaned_content)
    #? and for commas
    # Pattern 1099
    regex_pattern1099 = r'([a-z],)(\n{2,})([a-z])' 
    cleaned_content = re.sub(regex_pattern1099, r'\1 \3', cleaned_content)
    # Pattern 1100
    regex_pattern1100 = r',(\n{2,})(Gentlemen)' 
    cleaned_content = re.sub(regex_pattern1100, r'.\1\2', cleaned_content)
    # Pattern 1101
    regex_pattern1101 = r'-(\n{2,})(Gentlemen)' 
    cleaned_content = re.sub(regex_pattern1101, r'\1\2', cleaned_content)
    # Pattern 1102
    regex_pattern1102 = r'([a-z])(\n{2,})([a-z])' 
    cleaned_content = re.sub(regex_pattern1102, r'\1\3', cleaned_content)
    # Pattern 1103
    regex_pattern1103 = r'\n‘“—' 
    cleaned_content = re.sub(regex_pattern1103, r'—', cleaned_content)
    # Pattern 1104
    regex_pattern1104 = r'“—I' 
    cleaned_content = re.sub(regex_pattern1104, r'“ I', cleaned_content)
    # Pattern 1105
    regex_pattern1105 = r'\n“—c' 
    cleaned_content = re.sub(regex_pattern1105, r'? C', cleaned_content)
    # Pattern 1106
    regex_pattern1106 = r'i(d you any views)' 
    cleaned_content = re.sub(regex_pattern1106, r'Ha\1', cleaned_content, flags=re.MULTILINE)
    # Pattern 1107
    regex_pattern1107 = r'g(l to you to adhere to that object\?—Yes)\.\W*' 
    cleaned_content = re.sub(regex_pattern1107, r'tel\1, ', cleaned_content)
    # Pattern 1108
    regex_pattern1108 = r'“edly(.*)\n' 
    cleaned_content = re.sub(regex_pattern1108, r'“Secondly\1 ', cleaned_content)
    # Pattern 1109
    regex_pattern1109 = r'\W*(‘ ’ )' 
    cleaned_content = re.sub(regex_pattern1109, r' ', cleaned_content)
    # Pattern 1110
    regex_pattern1110 = r'\n(‘Bt )' 
    cleaned_content = re.sub(regex_pattern1110, r' by ', cleaned_content)
    # Pattern 1111
    regex_pattern1111 = r',\n\n‘([A-Z])' 
    cleaned_content = re.sub(regex_pattern1111, r', \1', cleaned_content)
    # Pattern 1112
    regex_pattern1112 = r'\n\n(794),' 
    cleaned_content = re.sub(regex_pattern1112, r'1\1.', cleaned_content)
    # Pattern 1113
    regex_pattern1113 = r',(—.)(that,.*)\nu(.*)\nri(.*)\W*' 
    cleaned_content = re.sub(regex_pattern1113, r', \2 n\3 they\4 did.\n\n', cleaned_content)
    # Pattern 1114
    regex_pattern1114 = r'\n\n(‘It be etee ot arms themselves.)' 
    cleaned_content = re.sub(regex_pattern1114, r' better to arm themselves.\n', cleaned_content)
    # Pattern 1115
    regex_pattern1115 = r'(hat people \?—)(.*)\n(.*)( si id)' 
    cleaned_content = re.sub(regex_pattern1115, r'W\1\2 \3', cleaned_content)
    # Pattern 1116
    regex_pattern1116 = r'«“' 
    cleaned_content = re.sub(regex_pattern1116, r'“', cleaned_content)
    # Pattern 1117
    regex_pattern1117 = r'“«' 
    cleaned_content = re.sub(regex_pattern1117, r'“', cleaned_content)
    # Pattern 1118
    regex_pattern1118 = r'([a-z])«$' 
    cleaned_content = re.sub(regex_pattern1118, r'\1-', cleaned_content, flags=re.MULTILINE)
    # Pattern 1119
    regex_pattern1119 = r'([a-z])\W*«\n' 
    cleaned_content = re.sub(regex_pattern1119, r'\1?— ', cleaned_content)
    # Pattern 1120
    regex_pattern1120 = r'—(I desire to be understood,)\W*(.*)\n«' 
    cleaned_content = re.sub(regex_pattern1120, r'\1 \2 ', cleaned_content)
    # Pattern 1121
    regex_pattern1121 = r'\W*“(them to say \?—)' 
    cleaned_content = re.sub(regex_pattern1121, r' \1', cleaned_content)
    # Pattern 1122
    regex_pattern1122 = r'«mischief' 
    cleaned_content = re.sub(regex_pattern1122, r'mischief', cleaned_content)
    # Pattern 1123 #? ([a-z])\n« AND [^\?|\.]—[A-Z]
    regex_pattern1123 = r':—' 
    cleaned_content = re.sub(regex_pattern1123, r': ', cleaned_content)
    # Pattern 1124
    regex_pattern1124 = r'(a copy.\])' 
    cleaned_content = re.sub(regex_pattern1124, r'', cleaned_content)
    # Pattern 1125
    regex_pattern1125 = r'\[produ.*' 
    cleaned_content = re.sub(regex_pattern1125, r'', cleaned_content)



#?############################################### KNOWN/UNRESOLVED DATA CLEANING ISSUES FOR STEP 2 ################################################

    #? long, ] --> fix the punctuation to fullstop (I checked in book). Also beware cases like: (No Signature.] “ SECe
    # #TODO: also do smth abt stuff in between brackets or parenthesis 
  
    #? regarding quotes/things read out.... The correct one is the english one so: “” I will have to triple check this and then replace them all.
    #? Quotes placed within quotes (ex: When a letter is read--> “Sometimes a quote will contain ‘another imbedded quote’ in this way.”)
    #? Beware: this (‘) is an apostrophe. It might have come to replace to single quotes.
    #* list of cases where the apostrophe must be deleted, separated by commas: ‘The name of Mr. , 
    #? Check: :—“*       (eg: ? They then go on to say :—“ From bosoms)
    #? Note for QUOTATION MARKS: Notice in the example of “I have not a higher wish in the present --> There's no closing quote in the para before it (ST 24 p. 335)
    #? Example of a WRONG stray single quotation mark here: ‘edition\? (p.521)
    #* convention’
    #—I                 #? Basically seems like ’\n— instead of \?—

    #? also &c. is supposed to be etc.
    #? ———
    #? for the ed notes in brackets: there's a novel one I found in the style of [Extracts read from...]
    #TODO: I am getting to the point where I seriously need to get rid of the editor's notes.... as in the long ones I have marked out with yellow post its. Figure out where in the code to put it.
    #? saying,—I
    #? that means I could do a sweep check for weird puncutation (ending punctuations) to see if there are any doubles etc where salvageable.
    #? Then another scary one will be the quotes...... like read letters and evidence etc. See the quotes is not the is not the below
    #? ” is not the same as " is not the same as ' is not the same as ´ is not the same as ‘ is not the same as " is not the same as “ is not the same as ” is not the same as „ is not the same as « is not the same as »
    #? ()—————  --> This one belongs to the "triple and double em dadsh + minus signs sections" (abt #510). Might need a lot of work or I might not gaf
    #? triple and double minuses and en or em dashes in between words/dialog. Theres no fullstop but lowcap letters
    #? ¢ --> Can spellcheck just deal with this there's 65 instances of this
    #? } replacing Is, ] are replacing Is too. Check for ) too in code I may have deleted it...?
    #? Some * are replacing “ (eg: * Resttved (purposefully picked a badly spelled example))
    #TODO: And from here the dash formatting is for them ONLY (in theory)
    #? wtf is this —-- is it the same as this ---J 
    #? also check —] but beware bc there's context in those (sometimes) also check --[
    #? }---I
    #? ?—[showing
    #? it tb the witness]---In Mr. Thelwall’s
    #? ---I
    #? ---
    #? -—
    
    

    
   
    return cleaned_content
    

# Define the input and output file names
#? Remember that here, the input file is 'header_filtering_test.txt' which above is = output_filename. 
#? Reminder: output_filename_2 = 'cleaned_with_regex.txt'

# Define the line ranges to exclude #TODO: I can use this method to exclude large ranges of superfluous footnotes AND CAN ONLY BE DONE ONCE I'VE DELETED THE MAX IN STEP 1
excluded_ranges = [(3829, 3830), ]  # List of tuples, each tuple is a range of lines to exclude

# Open the file and read all the lines into a list
with open(output_filename, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# Filter out the lines in the excluded ranges #TODO: Check before finalizing data cleaning that the lines are correct
for start, end in excluded_ranges:
    del lines[start - 1:end]  # Python uses 0-based indexing
    # Slice the list to get only the lines you want
    start_line = 3130  # Content will start from line 3131 #? This is to delete superfluous text from the start of the document which didn't take place during the trial (a tract, the charge by chief justice Eyre)
    end_line = 93090  # Content will end at line 93090 #? To delete the addendum at the end of the book
    selected_lines = lines[start_line - 1:end_line]  # Python uses 0-based indexing

# Join the selected lines back into a single string
text_content = ''.join(selected_lines)

# Clean the file content using the defined function
cleaned_text = cleanWithRegex(text_content)

# Write the cleaned text to the new file
with open("cleaned_with_Regex.txt", "w") as cleanedRegex:
    cleanedRegex.write(cleaned_text)

    print("     /✓\        REGEX CLEANING COMPLETE --> SEE cleaned_with_Regex.txt for raw output")





#?############################################# UNUSED — STEP 3: Passages to delete too complex/long to capture with either regex or line by line ##############################################

#input_filename3 = "cleaned_with_Regex.txt"
#output_filename3 = "passages_gone_test.txt"

# #the text 
# def remove_specific_passages(text, passages):
#     for passage in passages:
#         text = text.replace(passage, '')  # Simple string replacement
#     return text

# # List of exact texts to remove
# passages_to_remove = [
#     #? Deleting the end of the trial of Downie
#     """crowd. In this manner they proceeded till
# they joined the magistrates, when the mili-
# tary returned to the Castle, and then the
# procession was conducted in the following
# order :—The city constables; town officers
# bare-hcaded; bailie Lothian, and bailie Dal-
# rymple; Rev. Principal Baird; Mr. Sheriff
# Clerk, and Mr. Sheriff Davidson ; a number
# of country constables; the hurdle painted
# black, and drawo by a white horse; a num-
# ber of country constables. The city guard,
# lined the streets to keep off the crowd.

# * When they hadreached the Tolbooth door,
# the prisoner was taken from the hurdle, and
# conducied into the prison, where a conside-
# rable time was spent in devotional exercises.
# The prisoner then came out upon the plat-
# form, attended by the magistrates, the she-
# tiffs, Principal Baird, &c. Some time was


# then spent in prayer and singing psalms;
# after ohh ihe poaonet neni. the drop-
# beard, and was launched into eternity.

# “ When the body was taken down, it was
# stretched upon a table, and the executioner,
# with two blows of the ase, severed off the
# head, which was received into a basket, and
# then held up to the multitude, while the
# executioner called aloud ‘ This is the head of * traitor, and so perish all treitors.’”—New
# Ann. Reg., 1794, p. 58. That part of the
# sentence which relates to being quartered,
# ecc. had been previously remitted.

# David Downie, in consequence of the re-
# commendation of the jury y whom he was
# tried, received his Majesty’s Pardon,

# Court holden under a Special Commission of Oyer and
# Terminer, at the Sessions House in the Old Bailey, on the
# 28th, 29th, 390th, and 31st days of October, and the Ist, 3d,
# Ath, and 5th days of November: 35 Georce III. a. p.

# 1794.*""",
#     #? Deleting the charge of chief justice Eyre (taken in shorthand)
#     """ON the tenth day of September, 1794, a
# special commission of Oyer and Terminer
# was issued under the Great Seal of Great
# Britain to inquire of certain high treasons and
# misprisions of treason within the county of
# Middlesex.

# On Thursday, the second of October, the
# special commission was opened at the Session
# house in Clerkenwell :

# Present,—the right honourable sir James
# Eyre, knt., lord chief justice of his majesty’s
# court of Common pleas ; the right honguratle
# sir Archibald Macdonald, knt. lord chief baron
# of his majesty’s court of Exchequer; the ho-
# nourable sir Beaumont Hotham, knt. one of
# the barons of his majesty’s court of Exche-
# quer; the honourable sir Francis Buller, bt.
# one of the justices of his majesty’s court of
# Common pleas; the honourable sir Nash
# Grose, knt. one of the justices of his majesty’s
# coutt of King’s-bench; the honourable sir
# Soulden Lawrence, knt. one of the justices of
# his majesty’s court of King’s-bench; and
# others his majesty’s justices, &c,

# After the commission had been read, the
# sheriff delivered in the panel of the grand
# jury, which was called over, when the follow-
# ing gentlemen were sworn :—



# a THE GRAND aa ‘

# Benj. Winthrop, esq, Samuel Hawkins, esq.
# J. fia Schneider, - George Ward, a
# Edw. Ironside, esq.Thomas Boddam, esq.
# Benj. Kenton, esq. Jos. Lancaster, esq.
# R. H. Boddam, esq. Robt. Wilkinson, esq.
# John Aris, esq. G. G. Mills, esq.

# Wm. P. Allet, esq. Henry Wright, esq.
# John Perry, aig Joho Matchett,H. P. Kuff, es R. Stevenson, esq.

# Thos. Winslow, esq. John Campbell, esq.

# Thomas Cole, esq.

# Lord Chief Justice Eyre.—Gentlemen of
# the Grand Inquest; — You are assembled
# under the authority of the king’s commission,
# which has been issued for the hearing and de-
# termining of the offences of high treason, and
# misprisions of treason against the persun and
# authority of the king.

# That which hath given occasion for this
# commission is that which is declared by a late
# statute, namely, “ That a traitorous and de-
# testahle conspiracy has heen formed for sub-
# verting the existing laws and constitution, and
# for introducing the system of many and
# confusion, which has so lately prevailed in
# France;” acrime of that deep malignity which
# loudly calls upon the justice of the nation to
# interpose, “ for the better preservation of his
# majesty’s sacred person, and for securing the
# peace and the laws and liberties of this pa
# dom.”



# The first and effective pt Kea on agin
# the ordinary criminal proceedings, is, that a
# grand jury of the country should make public
# Inquisition for the king, shoutd diligently in-
# quire, discover, and bring forward to the view
# of the criminal magistrate, those offences
# which it is the object of this special commbis-
# sion to hear and to determine.

# Youare jurors for our sovereign lord the
# king; you are so styled in every indictment
# which is presented; but let the true nature
# of this service be understood. The king com-
# mands you to enter upon this inquiry; but
# the royal authority in this, as in all its other
# functions, is exerted, and operates ultimately
# for the benefit of his people. It is the king’s
# object, his duty, to vindicate his peace, his
# crown, and dignity, because his peace, his
# crown, and dignity, are the subjects’ protec-
# tion, their security, and their happiness.

# It is ultimately for them that the laws have
# thrown extraordinary fences around the per-
# son and authority of the king, and that all
# attempts against the one or the other are con-
# sidered a3 the highest crimes which can be
# committed, and are punished with a severity
# which rothing but the salus populi can
# justify. :

# The business of this day calls upon me (in
# order that you may the better understand the
# subject which is to come before you) to open
# to you the nature of that offence, which I have
# before spoken of in general.

# An ancient statute, 25 Edward Srd, has de-
# clared and defined it. I shall state to you so
# yauch of that declaration and definition as ap-
# pears to me to have any probable relation to
# the business of this day.

# By that statute it is declared to he high trea-
# son to compass or imagine the death of the
# king, provided such compassing and imagi-
# nation be manifested by some act or acts
# proved (by two witnesses) to have been done

# y the party accused in prosecution of that
# compassing and imagination; that is, from
# the moment that this wicked imagination of
# the heart is acted upon, that any steps are
# taken in any manner conducing to the bring-
# ing about and effecting the design, the inten-
# tion becomes the crime, and the measure of
# it is full.

# These acts or steps are technically deno-
# minated overt acts; and the forms of pro-
# ceeding in cases of this nature, tequire that
# these overt acts should be particularly set
# forth in every indictment of treason; and,
# from the nature of them, they must consti-
# tute the principal head of inquiry for the grand
# jury.

# ‘These overt acts involve them in two
# distinct considerations; 1st, the matter of
# fact, of which they consist; in the next
# place, the relation of that fact tu the design.

# With respect to the mere miatter of fact, it
# willbe for the grand jury to inquire into the
# true state of it; and I can have very little to
# offer to your consideration respecting it: and,


# with respect to the question, whether the fact
# has relation to the design, so ss to constitute
# an overt act of this species of treason, which:
# involves considerations botly of fact and of haw,
# it is impossible that any certain rule should be
# laid down for your government ; overt acts
# being in their nature all the possible means
# which may be used in the prosecution of the
# end proposed; they can be no otherwise
# defined, aod must remain for ever infnitely
# various.

# Thus far, I can inform you: that occasions
# have unhappily, but too frequently, brought
# overt acts of this species of treason under com
# sideration; in consequence of which we are
# furnished with judicial opinions upon man
# of them? and we are also furnished with epi-
# nions (drawn from these sources) of text
# writers—some of the wisest and most enlight-
# ened men of their time, whose integrity has
# Leen always considered as the most promi-
# nent feature of their character, and whose
# doctrines do now form great land-marks, b:
# which posterity will be enabled to trace, wit!
# a great degree of certainty, the boundary
# lines between high treason, and offences of a
# lower order and degree.

# It is a fortunate circumstance that we are
# thus assisted; for it is not to be dissembled
# that, though the crime of high treason is
# “ the greatest crime against faith, duty, and
# human society,” and though, “ the public is
# deeply interested in every prosecution of this
# kind well founded,” there hath been, in the
# best times, a considerable degree of jealousy
# on the subject of prosecutions for high trea-
# son ; they are state prosecutions, and the con-
# sequences to the party accused are penal in
# the extreme.

# Jurors and judges ought to feel an extradrdi-
# nary anxiety that prosecutions of this nature
# should proceed upon solid grounds. I can
# easily conceive, therefore, that it must be a
# great relief to jurors placed in the responsible
# situation in which you now stand bound tode
# justice to their country and to the persons
# accused, and anxious to discharge this trust
# faithfully ; sure I am that it is consolation and-
# comfort to us, whe have upon us the respori-
# sibility of declaring what the law is, in cases
# in which the public and the individual are so
# deeply interested; to have such men as the
# great sir Matthew Hale, and an eminent judge
# of our own times, who, with the experience
# of acentury concurs with him in opinion, sir
# Michael Foster, for our guides.

# To proceed by steps: from these writers
# upon the law of treason (who speak, as I
# have before observed, upon the authority of ad-
# judged cases) we learn, that not only acts of
# immediate aud direct attempt against the
# king's life are overt acts of compassing hit
# death, but that all the remoter steps, taken
# with a view to assist, to bring about the actual
# attempt, are equally overt acts of this species
# of treason ; even the ineeting and the consult-
# ing whet steps should be taken in order to

# bring about the end proposed, has been always
# deemed to be an act done in prosecution of
# the design, and as such an overt act of this
# treason—This is our first step in the present
# inquiry. I proceed to observe that the overt
# acts I have been nqw speaking of have refer-

# ence, nearer or more remote, to a direct and im-
# mediate attempt upon the life of the king; but
# that the same authority informs us that they
# who aim directly at the life of the king (such,
# for instance, as the persons who were con-
# cerned in the assassination plot, in the vag
# of king William) are not the only persons who
# can be said to compass or imagine the death
# of the king. The entering into measures
# which, in the nature of things, or in the com-
# mon experience of mankind, do obviously tend
# to bring the life of the king into danger, is
# also compassing and imagining the death of
# the king; and the measures which are taken
# will be at once evidence of the compassing,
# and overt acts of it,

# The instances which are put by sir Matthew
# Hale and sir Michael Foster (and upon which
# there have been adjudged cases) are of conspi-
# tacies to depose the king; to imprison him ;
# to get his person into the power of the conspi-
# rators ; to procure an invasion of the kingdom.
# The first of these, apparently the strongest
# case, and coming the nearest to the direct at-
# tempt against the life of the king; the last,
# the farthest removed from that direct attempt,
# but being a measure tending to destroy the
# public peace of the country to introduce hos-
# tilities, and the Benessily of resisting force by
# force, and where it is obvious, that the con-
# flict has an ultimate tendency to bring the

# rson and life of the king into jeopardy; it
# 1s taken’ to be a sound construction of the
# statute 25 Edward Srd, and the clear law of
# the land, that this is also compassing and
# imagining the death of the king.

# If a conspiracy to depose or to imprison
# the king, to get his person into the power-of
# the conspirators, or to procure an invasion of
# the kingdom, involves in it the compassing
# and imagining of his death and if steps taken
# in prosecution of such a conspiracy are rightly
# deemed overt acts of the treason of imaginin,
# and compassing the king’s death: need Ladd,
# that if it should appear that it has entered
# into the heart of any man who is a subject of
# this country, to design, to overthrow the
# whole government of the country, to pull
# down and to subvert from its very foundations
# the British monarchy, that glorious fabric
# which it has been the work of ages to erect,
# maintain and support, which has been ce-
# mented with the best blood of our ancestors ;
# to design such a horrible ruin and devastation,
# which no king could survive, a crime of such
# a magnitude that no lawgiver in this country
# hath ever ventured to contemplate itinits whole
# extent; need I add, I say, that the complica-
# tion and the enormous extent of such a de-
# sign will not prevent its being distinctly seen,
# that the compassing and imaginipg the death


# of the king is involved in it, is, in truth, of
# its very essence.

# This is too plain a case to require farther
# illustration from me. If any man of plain
# sense, but not conversant with subjects of
# this nature, should feel himself disposed to
# ask whether a conspiracy of this nature is to
# be reached by this medium only; whether it
# is a specific treason to compass and imagine
# the death of the king, and not a specific trea-
# son to conspire to subvert the monarchy
# itself; I answer, that the statute of Edward
# Srd, by which we are governed, hath not
# declared this (which in all just theory of
# treason is the greatest of all treasons) to be
# high treason.

# said no lawgiver had ever ventured : to
# contemplate it in its whole extent; the seditio
# regni, spoken of by some of our ancient
# writers, comes the nearest to it, but falls far
# short of it; perhaps if it were now a question
# whether ick a conspiracy should be made a
# specific treason, it might be argued to be un-
# necessary : that in securing the person and
# authority of the king from all danger, the
# monarchy, the religion and laws of our country -
# are incidentally secured ; that the constitution
# of our government is so framed, that the
# imperial crown of the realm is the common
# centre of the whole; that all traitorous at-
# tempts upon any part of it are instantly
# communicated to that centre, and felt there ;
# and that, as upon every principle of public
# policy and justice they are punishable as
# traitorous attempts against the king’s person
# or authority, and will, according to the parti-
# cular nature of the traitorous attempt, fall
# within one or other of the specific treasons
# against the king, declared by the statute of
# 25 Edward Srd ; this greatest of all treasons is
# sufficiently provided against by law.

# Gentlemen, I presume, I hardly need give
# you this caution, that though it has been ex-
# pressly declared, by the highest authority,
# that there do exist in this country men capable
# of meditating the destruction of the constitu-
# tion under which we live; that declaration,
# being extrajudicial, is not a ground upon which
# you ought to proceed.

# In consequence of that declarationit became
# a public and indispensable duty of his majesty
# to institute this solemn proceeding, and to
# impose upon you the painful task of examin- -
# ing the accusations which shall be brought
# before you; but it will be your duty to ex-
# amine them in a regular judicial course, that
# is, by hearing the evidence, and forming your -
# own judgment upon it. -

# And here, as I do not think it necessary to
# trouble you with observations upon the other
# branches of the statute 25 Edward $rd, the
# charge to the grand inquest might conclude ;
# had not the particular nature of the conspiracy,
# alleged to have been formed against the
# state, been disclosed, and made matter of -
# public notoriety by the reports of the two

# jouses of parliament, now in every one’s

# hands: but that being the case, I am appre-
# hensive that I shall not be thought to have
# fulfilled the duty, which the judge owes to
# the grand jury, when questions in the criminal
# law arise on new and extraordinary cases of
# fact, if I did not plainly and distinctly state
# what I conceive the law to be, or what doubts
# I conceive may arise in law, upon the facts
# which are likely to be laid before you, accord-
# ing to the different points of view in which
# those facts may appear to you.

# It is matter of public notoriety that there
# ‘have been associations formed in this county,
# and in other parts of the kingdom, the pro-
# fessed purpose of which has been a change in
# the constitution of the Commons House of
# Parliament, and the obtaining of annual par-
# liaments; and that to some of these associa-
# tions other purposes, hidden under this veil,

# “purposes the most traitorous, have been
# imputed; and that some of these associations
# have been supposed to have actually adopted
# measures of such a nature, and to have gone
# into such excesses, as will amount to the crime
# of high treason.

# If there be ground to consider the professed
# purpose of any of these associations, a reform
# in parliament, as mere colour, and as a pretext
# held out in order to cover deeper designs—
# designs against the whole constitution and
# government of the country ; the case of those
# embarked in such designs is that which I
# have already considered. Whether this be
# s0, or not, is mere matter of fact; as to which
# I shall only remind you, that an inquiry into
# acharge of this nature, which undertakes to
# make out that the ostensible purpose is a
# mere veil, under which is concealed a trai-
# torous conspiracy, requires cool and deliberate
# examination, and the most attentive conside-
# ation ; and that the result should be perfectly
# elear and satisfactory. In the affairs of com-
# mon life, no man is justified in imputing to
# another a meaning contrary to what he himself
# expresses, but upon the fullest evidence. On
# the other hand, where the charge can be
# made out, it is adding to the crime meditated
# the deepest dissimulation and treachery, with
# respect to those individuals, who may be
# drawn in to embark in the ostensible purpose,
# as well as to the public, against which this
# dark mystery of wickedness is fabricated.

# But if we suppose these associations to
# adhere to the professed purpose, and to have
# no other primary object, it may be asked, is it
# possible, and (if it be possible) by what pro-
# cess is it, that an association for the reform of
# pavement can work itself up to the crime of

# high treason? All men may, nay, all men

# must, if they possess the faculty of thinking,
# reason upon every thing which sufficiently
# interests them to become objects of their
# attention, and among the objects of the atten-
# tion of free men, the principles of govern-

# -ment, the constitution of particular govern-
# ments, and, above all, the constitution of the
# overmment under which they live, will natu-
 

# rally engage attention, and provoke speculg-
# tion. The power of communication of thoughts
# and opinionsisthe gift of God, and the freedons
# of it is the source of all science, the first fruits
# and the ultimate happiness of society ; and
# therefore it seems to fallow, that human laws
# ought not to interpose, nay, cannot interpose,
# to prevent the communication of sentiments
# and opinions in voluntary assemblies of men;
# all which is true, with this single reservation,
# that those assemblies are to be so composed,
# and so conducted, as not to endanger the
# public peace and good order of the government
# under which they live; and I shall not state
# to you that associations and assemblies of
# men, for the purpose of obtaining a reform in
# the interior constitution of the British parlia-
# ment, are simply unlawful; but, on the other
# hand, I must state to you, that they may but
# too easily degenerate, and become unlawful,
# in the highest degree, even to the enormous
# extent of the crime of high treason. i

# The process is very simple: let us imagine
# to ourselves this case: a few well meaning
# men conceive that they and their fellow
# subjects labour under some grievance; they
# assemble peaceably to deliberate on the means
# of obtaining redress; the numbers increase ;
# the discussion grows animated, eager, and
# violent ; a rash measure is proposed, adopted
# and acted upon; who can say where this shall
# stop, and that these men, who originally
# assembled peaceably, shall not finally, and
# suddenly too, involve themselves in the crime
# of high treason? It is apparent how easily
# an impetuous man may precipitate such as-
# semblies into crimes of unforeseen magnitude,
# and danger to the state; but, let it con-
# sidered, that bad men may also find their way
# into such assemblies, and use the innocent
# purposes of their association as the stalking

# jorse to their purposes of a very different
# complexion. How easy for such men to
# practise upon the credulity and the enthusiasm
# of honest men, lovers of their country, loyal
# to their prince, but eagerly bent upon some
# speculative improvements in the frame, and
# internal mechanism of the government? If
# we suppose bad men to have once gained an
# corenitice in an assembly of this description,
# popular in its constitution, and having popular
# objects ; how easy is it for such men to plunge
# such an assembly into the most criminal ex-
# cesses? Thus far I am speaking in general,
# merely to illustrate the proposition, that men
# who assemble in order to procure a reform of
# parliament may involve themselves in the
# guilt of high treason.

# The notoriety to which I have alluded leads
# me to suppose, that the project of a convention
# of the people to be assembled under the
# advice and direction of some of these societies,
# or of delegations from them, will be the lead-
# ing fact, which will be laid before you in evi-
# dence, respecting the conduct, and measures
# of these associations; a project, which. per-
# haps, in better times, would baye been hardly

# thought worthy of gas consideration; but,
# in these our days, having been attempted to
# be put in execution in a distant part of the
# united kingdoms, and, with the example of a
# neighbouring country before our eyes; is
# deservedly become an object of the jealousy
# of our laws: it will be your duty to examine
# the evidence on this head very carefully, and
# to sift it to the bottom ; to consider every part
# of it in itself, and as it stands connected with
# other parts of it, and to draw the conclusion
# of fact, as.to the existence, the nature, and
# the object of this project of a convention,
# from the whole.

# In the course of the evidence you will pro-
# bably hear of bodies of men having been col-
# Lectesl soxethies, of violent resolutions voted at
# these and at other meetings, of some prepara-
# tion of offensive weapons, and of the adoption
# ofthe language, and manner of proceeding of
# those conventions in France, which have pos-
# sessed themselves of the government of that
# country: I dwell not on these particulars,
# because I consider them, not as substantive
# treasons, but, as circumstances of evidence,
# tending to ascertain the true nature of the
# object which these persons had in view, and

# the true nature of this project of a con-
# vention, and to be considered by you in the
# mass of that evidence; which evidence it
# floes not fall within the province of the charge
# to, consider. in detail; my present duty is, to
# inform you what the law is upon the matter of
# fact, which in your judgment shall be the
# result of the evidence.

# i presume that I have sufficiently explained
# to you, that a project to bring the people
# togetber in convention, in imitation of those
# national conventions. which we have heard of
# in France, in order to usurp the government
# of the country, and any one step taken towards
# bringing it about, such as, for-instance, con-
# sultations, forming of committees to con-
# sider ef the means, acting in those committees,
# swould,be a case of no difficulty that it would
# be the cheateat, Hight treason 3 i woul be
# compassing and imagining the king’s death,
# and not only his ent; t the asks and
# destruction of all order, religion, laws, all
# pro , all security for the lives and liberties
# of tl king's subjects.

# That which remains to be considered is,
# the project of a convention having for its sole
# object the effecting a change in the mode of

# tation of the le in parliament,
# and the obtaining that parliaments should be
# held. annually; and here there is room to
# distinguish. Such a project of a convention,
# aaking it to be criminal, may be criminal in
# different degrees, according to the case in
# evidence, ‘from whence you are-to collect the
# drue nature and extent of the , and the
# manner in-which it is inte’ to operate ;
# and it will become a question of great impor-
# ome under what class ef crimes it-ought to

# ln eeialnibe upon. the-complexion and


# wality af this project of a convention,

# til lay down to yourselves one praciple
# which is never to be departed from, : that
# alterations.in the representation of the people
# in parliament, or in the law for holding par-
# liaments, can only be effected by the muthictty
# of the King, Lords, and Commons, in parlia-
# ment assembled. This being taken as a foun-
# dation, it seems to follow as a necessary
# consequence, that a project of a convention,
# which should have for its object the obtaining
# a parliamentary reform without the authority
# of parliament, and steps taken upon it, would
# be high treason in all the actors in it; for this
# is a conspiracy to overturn the government.
# The gocrament cannot be said to exist, if
# the functions of legislation are usu! fora
# moment; and it then becomes of little con-
# Sequence indeed, that the original conspira-
# tors, perhaps, had only meditated a plan of
# moderate reform : it is in the.nature of things,
# that the power should go out of their hands,
# and be Beyond the reach of their control.
# A conspiracy of this nature is therefore, at
# best, a conspiracy to overturn the govern-
# ‘ment, in order to new model it, which is, in
# effect, to introduce anarchy, and that which
# anarchy may chance to settle down into ;
# after the king may have been brought to the
# scaffold, and after the country may have
# suffered all the miseries which discord and
# civil war shall have produced.

# Whether the project of a. convention, hay-
# ing for its object the collecting together a
# power which should overawe the legislative
# body, and extort a parliamentary reform from
# it, if acted upon, will also amount to high
# treason, and to the specific treason of com-
# passing and imagining the king's death, is a
# more doubtful question. Thus far is clear;
# a force upon the parliament must.be immedi-
# ately directed against the king, who is an in-
# tegral part of it; it mugchreset the king, or it
# can have no effect at all. Laws are enacted
# in parliament by the king’s majesty, by and
# with the advice and consent of the pee and
# Commons, in parliament assembled. A force
# meditated against the parliament, is therefore
# a force meditated against the king, and seezns
# to fall within the case of a force meditated
# against the king, to compel him to ‘alter the
# measures of his government: but, in that
# case, it does not appear to.me that lam war-
# ranted by the authoritics to state to you, as
# clear law, that the mere conspiracy to raise
# such a force, and the gntering into consulta-
# tions respecting -it, will alone, and without
# actually raising the force, constitute the crime
# of high treason. What the law is in that
# case, and what will be the effect of the cir-
# cumstance of the force being meditated agai
# the king in parliament, against the king an
# the exercise of the royal function in a -point
# which is of the very essence of his monarchy,
# will be fit to be.solemaly considered, and de-
# termined when the case shall arise,

# ‘It may be stated toyouasclear, that the pro-
# ject of a convention, having for its sole object a
# dutiful and peaceable application to the wisdom
# of parliament on the subject of a wished-for
# ¥eform, which application should be entitled
# to weight and credit from the universality of
# -t, but should still leave to the parliament the
# freest exercise of its discretion to grant or to
# refuse the prayer of the petition (great as the
# responsibility will be on the persons concern-
# ed in it, in respect of the many probable, and
# all the possible, bad consequences of collect-
# ing a great number of people together, with
# Noo specific legal powers to be exercised, and
# under no government but that of their own
# discretion), cannot in itself merit to be ranked
# among that class of offences which we are
# now assembled to hear and determine.

# Upon this last statement of the fact of the
# ease, Fam not called upon, and therefore it
# -would not be proper for me to say more.

# Gentlemen, you will now proceed upon the
# several articles of inquiry, which have been

# ven you in charge; if you find that the par-~
# ties, who shall be accused before you, have
# been pursuing lawful ends by lawful means,
# or have been only indiscreet, or at the worst if
# eriminal, that they have not been criminal to
# the extent of those treasons to which our in-
# quiries are confined, then say, that the bills
# which shall be presented to you are not true
# bills; but, if any of the accused persons shalt
# appear to you to have been engaged in that
# traitorous and detestable conspiracy described
# in the preamble of the late statute ; or, if with-
# out any formed design to go the whole length
# of that conspiracy, they have yet acted upon
# the desperate imagination of bringing about
# alterations in the constitution of the commons
# ‘house of parliament, or in the manner ofholding parliaments without the authority of
# parliament, and, in defiance of it, by an usurp-
# power, which should, in that instance,
# suspend the lawful authority of the king, )
# Jords, and commons, in parliament assembled,
# and take upon itself the fanction of legisla-
# - tion (which imagination amounts to a eonspi-
# racy to subyert the exisiing laws and consti-
# tution, differing from the former only in the
# extent of its object), you will then do that
# which belongs to your office to do.

# In the third view of the case of the aceused
# persons; that is, if you find them involved in,
# and proceeding upon, a design to collect the
# people together against the legislative autho-

# rity of the country, for the purpose, not of
# asurping the functions of the legislature, but
# of overawing the parliament, and so compel-
# ling the king, lords, and commons, in par- !
# Hiament assembled, to enact a law for new
# modelling the commons house of parliament,
# or for holding annual parliaments; and that
# charges of high treason are offered to be main-
# tained agaiust them upon this ground only:
# perhaps it may be fitting that, in respect of
# the extraurdinary nature and dangerous ex-
# tent and very criminal complexion of such a
# conspiracy, that case, which J state to you as


# a new and 8 doubtful case, should be put into’
# a judicial course of inquiry, that it may receive
# a solemn adjudication, Meher will, or will
# not, amount to high treason, in order to which
# the bills must be found to be true bills.

# Gentlemen, I have not opened to you the
# law of misprision of treason, because I am
# not aware that there are any commitments
# for that offence ; and therefore I have no rea
# som to suppose that there will be any prose-
# cution for that offence. It consists of the
# concealment of treason committed by others
# (which undoubtedly it is every man’s duty to
# disclose), and the punishment is extremely
# severe; but the humanity of modern times
# hath usually interposed, and I trust that the
# necessities of the present hour will not de-
# mand, that the law of misprision of treason’
# should now be carried into execution.

# Gentlemen, I dismiss you with confident
# expectation that your judgment will be direct-
# ed to those conclusions which may clear in-
# nocent men from all suspicion of guilt, bring
# the guilty to condign punishment, preserve
# the life of our gracious sovereign, secure the
# stability of our government, abd maintain the
# public peace, in which comprehensive term is
# Included the welfare and happimess of the
# Freel under the protection of the laws and
# iberties of the kingdom.*

# Tren nenenenemnmenemenaeneend""",
# #? Deleting the tract version of the charge of chief justice Eyre (by Felix Vaughan)
# """* Immediately after the publication of this
# charge, appeared a short examination of the
# doctrines maintained in it, under the title of
# “ Cursory Strictures on the Charge delivered
# by lord chief justice Eyre to the Grand
# Jury, October 2, 1794.” This tract, although
# now somewhat scarce, drew much attention,
# and excited much interest at the time ; I have
# sufficient authority for stating that it was com-
# posed by the late Mr. Felix Se ye who it
# will be observed was appointed counsel for’
# one of the persons arraigned, and who acted
# as aasintantt counsel on his and the following
# trial.

# Tt is as follows:

# €vursory Strictures, &c.

# & special commission was opened on the
# second day of October, for the trial of certain
# persons apprehended upon suspicion of high
# treason, the greater part of whom were taken.
# into custody in the month of May, 1794,
# Upon this occasion a charge was delivered to
# the grand jury, by sir James Eyre, lord chief
# justice of the court of Common Pleas.

# Itis one of the first privileges ot’ an English-
# man, one of the first duties of a rational be-
# ing, to discuss with pertect freedom, all prin-
# ciples proposed to be enforced upon general
# observance, when those principles are first
# disclosed, and before they have yet, by any
# solemn and final proceeding, been made part
# ofa regular catablished system. The chief
# justice, in his charge to the jury, has delivered
# many new and extraordinary doctrines upon
# the subject of treason. These doctrines, now



# The sheriff returned into the court the
# panel of the petit jurors.

# On Monday, October the sixth, the grand
# jury returned a true bill against Thomas

# when they have been for the first time stated,
# it is fit we should examine. In that exami-
# nation, I shall deliver my opinions in a man-
# ner perfectly frank and explicit. No man
# should seek to offend high authorities and
# elevated magistracy ; but the object before us
# is of an importance paramount to these con-
# siderations. Decorum is an excellent thing ;
# but we ought not to sacrifice to the fastidious
# refinements of decorum, all that is most firm
# in security, or most estimable in social insti-
# tution.

# The chiefjustice has promised a publication
# of his charge, and I should have been glad to
# have waited for the opportunity of an authen-
# ticcopy. But thereare onlya few days remain-
# ing previous to the commencement of trials,
# of the highest expectation, and most unlimited
# importance. He who thinks, as I think, that
# the best principles of civil government, and
# all that our ancestors most affectionately
# Joved, are struck at in the most flagrant man-
# ner in this charge, will feel that there is not
# an hour to be lost. While I animadvert

# upon its enormitics, it is with some pleasure
# that I shall reflect upon the possibility of the
# enormities being aggravated or created by the
# imperfect and irregular form of the publica-
# tion before me. Every friend of his country
# will participate the Bigbeat satisfaction, at
# finding them answered, by a regular publica-
# tion of the charge to the grand jury, stripped
# of the illegal and destructive doctrines that
# now appear to pollute it.

# Among the various branches of the English
# constitution that have for centuries been a
# topic of unbounded praise, there is none, that
# has been more, or more deservedly, applauded,
# than that which relates to the law of treason.
# “The crime of igh treason,” says chief jus-
# tice Eyre,* “though the greatest crime against
# faith, duty, and human socicty, and though
# the public is deeply interested in every well-
# founded prosecution of this kind, has yet, at
# the best times, been the object of consider-
# able jealousy, in respect of the prosecutions
# instituted against it; they are state prosecu-
# tions.” Itis therefore of the utmost conse-
# quence, that the crime of high treason should
# be clearly defined, and the exquisite jea-
# Jousy allayed, which must otherwise arise in
# every benevolent mind. This has been done

# * “ He adds, ‘it is not to be dissembled,’
# —Will any one venture to say, that the judges
# of England would dissemble, if they could,
# in matters of the utmost value to the subject ;
# and that it is with reluctance they: confess
# any thing, that tends most to poured security,
# equity, and welfare ?”


# Hardy, John Horne Tooke, John Augustus
# Bonney, Stewart Kyd, Jeremiah Joyce, The
# mas Wardle, Thomas Holcroft, John Richter,
# Matthew Moore, John Thelwall, Richard
# Hodgson, and John Baxter, for high treason.

# by the act 25 Edward Srd, one of the great
# ladiums of the English constitution. ‘This
# law has been sanctioned by the experience of
# more than four centuries; and, though it has
# been repeatedly attacked by the encroach-
# ments of tyrannical princes, and the decisions
# of profligate judges, Englishmen have always
# found it necessary in the sequel to strip it of
# mischievous appendages and artificial glosses
# and restore it to its original simplicity and tus
# tre. By this law all treason, exclusively ofa
# few articles of little general concern, is con-
# fined to the ‘levying war against the king
# within the realm, and the compassing or
# imagining the death of the king.’ Nay, the
# wise framers of the law were not contented to
# stop here: they not only shut out the mis-
# chief of arbitrary and constructive treason for
# themselves, but inserted a particular clause,
# roviding thatif in any future time it might
# necessary to declare any new treasons, that
# should only be done by a direct proceeding of
# parliament for that special purpose.’ ”

# It is obvious upon the face of this wise and
# moderate law, that it made it extremely difi-
# cult for a bad king, or an unprincipled admi-
# nistration, to gratify their resentment against
# aa pertinacious opponent by instituting against
# him a charge of treason. Such kings and
# ministers would not fail to complain, that the
# law of Edward 3rd shut up the crime within
# too narrow bounds ; that a subtle adversary
# of the public peace would easily evade these
# gross and palpable definitions; and that
# crimes of the highest magnitude, and most
# dangerous tendency, might be committed,
# which could never be brought under these
# dry, short, and inflexible classes. It is not to
# be denied, that some mischief might arise
# from so careful, lenient, and unbloody a pro-
# vision. No doubt offences might be con-
# ceived, not less dangerous to the public wel-
# fare, than those described in the act under
# consideration. But our ancestors exposed
# themselves to this inconvenience, and tound
# it by no means such as was hard to be borne.
# They experienced a substantial benefit, a
# proud and liberal security, arising out of this
# Statute, which amply cumpensated for the
# mischief of such subterfuges as might occa-
# sionally be employed by a few insignificant
# criminals, If we part with their wisdom and
# policy, let us beware that we do not substitute
# a mortal venom in its stead.

# The chief justice has thought proper to
# confine himself to that article of the statute
# of king Edward Srd which treats of “ compas-
# sing and imagining the death of the king.”
# This compassing and imagining he very pro-
# perly observes, “ requires that jt should be
# manifested by overt acts;” and he adds,

# The bill ofindictment was not found against
# John Lovett.

# On Tuesday, October the seventh, Thomas

# «¢ that they who aim directly at the life of the
# king, are not the only persons, who may be
# said’ tocompass or imagine his death. The
# entering into measures, which in the nature
# ef things do obviously tend to bring the life
# of the king into danger, is also compassin
# and imagining the death of the king; an
# the measures which are taken, will be at once
# evidence of the compassing and overt acts of
# it. The instances which are put under this
# head by sir Michael Foster and sir Matthew
# Hale, and upon which there have been ad-
# judged cases, are [principally four, viz.] of a
# conspiracy to depose the king, to imprison
# hin, to get his person into the power of the
# conspirators, and to procure an invasion of
# the kingdom.” He farther states, “ that oc-
# casions have unhappily, but too frequently
# brought overt acts of this species of treason
# under consideration, in consequence of which
# we are furnished with judicial opinions upon
# many of them. We are also furnished with
# opinions drawn from these sources, ef text
# writers, some of the wisest and most enlight-
# ened men of their time, whose intcgrity has
# always been considered as the most prominent
# feature of their character, and whose doctrines
# do now form great land marks, by which pos-
# terity will be enabled to trace with consider-
# able certainty the boundary line between high
# treason, and offences of a lower order and de-
# gree. Itis a fortunate circumstance,” con-
# tinues the chief justice, “ that we are thus as-
# sisted. I can easily conceive that it must be
# a great relief to jurors, placed in the responsi-
# ble situation in which you now stand; and
# sure I am that it is a consolation and comfort
# to us, who have upon us the responsibility of
# declaring what the law is, in cases in which
# the public and the andividual are so deeply
# interested.”

# In all this preamble of the chief justice,
# there is certainly something extremely hu-
# mane and conmuletate. I trace init the lan-
# guage of a constitutional lawyer, a sound lo-
# gician, and a temperate, discreet, and honest
# man. I see rising to my view by just degrees
# ajudge resting upon the law as it is, and de-
# terminedly setting his face against new, un-
# preceentes and temporizing constructions.

# sec a judge who scorns to bend his neck to
# the yoke oh party, or any administration ;
# who expounds the unalterable principles of
# justice, and is prepared to try by them, and
# them only, the persons ‘that are brought be-
# fore him. I see him taking to himself, and
# holding out to the jury the manly consolation
# that they are to make no new law, and force
# no new interpretations; that they are to con-
# sult only the statutes of the realm, and the
# decisions of those writers who have been the
# luminaries of England,


# Holcroft voluntarily surrendered himself in
# court, and was committed to Newgate. :

# At the request.of the several prisoners the

# Meanwhile what would be said by our con-
# temporaries and by our posterity, if this picture
# were to be reversed; if these promises were
# made, only to render our disappointment
# more bitter ; if these high professions served
# merely as an introduction to.an unparalleled
# mass of arbitrary constructions, of new-fan-
# gled treasons, and doctrines equally inconsis-
# tent with history and themselves: I ho
# these appearances will not be found in
# the authentic charge. But whoever be the
# unprincipled impostor, that thus audaciously
# saps the vitals of human liberty and human
# happiness, be he printer, or be he judge, it is
# the duty of every friend to mankind to detect
# and expose his sophistries.

# Chief Justice Eyre, after having stated the
# treasons which are most strictly within the
# act of Edward 3rd, as well as those which are
# sanctioned by high law authorities, and upon
# which there have been adjudged cases, pro-
# ceeds to reason in the following manner ;

# “ If a cunspiracy to depose or imprison the
# king, to get his person into the power ot the
# conspirators, or procure an invasion of the
# kingdom, involves in it the compassing and
# imagining his death, and if steps taken in
# prosecution of such a conspiracy, are rightly.
# deemed overt acts of the treason of compas~
# sing the king’s death, what ought to be our
# judgment, if it should appear that'it had en-
# tered into the heart of any man, who is a sub-
# ject of this country, to design to overthrow the
# whole government of the country, to pull
# down and to subvert from its very foundations
# the British monarchy, that glorious fabric,
# which it has been the work of ages to erect,
# maintain, and support; which has been ce-
# mented with the best blood of our ancestors 5
# to design such a horrible ruin and devastation,
# which no king could survive.”.

# Here. we are presented with-a question
# which is no doubt of the utmost itude
# and importance. Is the proceeding thus de-
# scribed matter of high treason, or is it not?
# It confessedly does not come within the letter
# of 25 Edward Srd. It does not come within
# the remoter instances “ upon which there
# have been adjudged cases.” Chief Justice
# Eyre has already enumerated these, and, ha-
# ving finished that part of his subject, gone on
# to something confessedly different.

# Are we reasoning respecting law, or re~
# specting a state of society, which, having no
# fixed rules of law, is obliged to consult the
# dictates of its own discretion? Plainly the
# former. It follows, therefore, that the aggrae
# vations collected by the chief justice, are to-
# tally foreign to the question he had to con-
# sider. Let it be granted, that the crime, in
# the eye of reason and discretion, is the most
# enormous, that it can enter into the heart of

# following gentlemen were assigned by the
# Court as their counse) :—for,
# Thomas Hardy,—Mr. Erskine, Mr. Gibbs. John Horne Tooke,—Mr. Erskine, Mr.
# Gibbs.

# man to conceive, still I shall have a right to
# ask is it a crime against law? Show me the
# statute that describes it; refer me to the pre-
# cedent by which it is defined ; quote me the
# adjudged case in which a matter of such un-
# paralleled magnitude is settled.

# - Let us know the ground upon which we
# stand. Are we to understand that, under
# chief justice Eyre, and the other judges of the
# special commission, reasonings are to be ad-
# duced from the axioms and dictums of moral-
# ists and metaphysicians, and that men are to
# be convicted, sentenced, and executed, upon
# uhese? Are we to understand that hence-
# forth the man most deeply read in the laws
# of his country, and most assiduously conform
# ing his actions to them, shall be liable to be
# arraigned and capitally punished fora crime
# that no law describes, that no precedent or
# adjudged case ascertains, at the arbitrary
# pleasure of the administration for the time

# ing? Such a miserable miscellany of law
# and metaphysical maxims, would be ten thou-
# sand times worse, than if we bad no law to
# direct our actions. The law in that case
# would be a mere trap to delude us to our ruin
# greating a fancied security, an apparent clear-
# ness and definition, the better to cover the
# concealed pitfalls with which we are on eyery
# side surrounded.

# - The chief justice is by no means unaware
# of the tremendous consequences that would
# result from such an administration of criminal
# Jaw. He speaks respecting it, when the sub-
# ject is first started, with great temperance
# and caution. He says, “ That the crime of
# conspiring to overthrow the monarchy, is
# such an one, as no lawgiver in this conn
# has ever ventured to contemplate in its whole
# extent. Ifany man of plain sense, but not
# conversant with subjects of this nature, should
# feel himself disposed to ask, whether a con-
# spiracy of this extraordinary nature is to be
# teached by the statute of treasons, whether it
# is a specific treason to compass and imagine
# the death of the king, and not a specitic trea-
# son to conspire to subvert the monarchy it-
# self? I answer, that the statute of Edward 3rd.
# ‘by which we are bound, has not declari
# this, which undoubtedly in all just theory of
# treason is the greatest of all treasons, to be a
# specific high treason. I said, no lawgiver had
# ever ventured to contemplate it in its whole
# extent.” ‘

# The language here employed is no doubt
# manly and decisive. From hence it follows,
# with the most irresistible evidence, that that
# ‘‘ which the statute by which we are bound,
# has not declared to be treason,” that “ which
# no lawgiver has ever ventured to contem-
# plate,” can never be construed into treason,


# John Augustus Bonney, — Mr. Erskine,
# Mr. Gibbs.

# Stewart Kyd,—Mr. Erskine, Mr. Gibbs.

# Jeremiah Joyce,—Mr, Exskine, Mr. Felix
# Vaughan.

# Bl all law is feanslitated, and ol met
# of juris; ce trampled under foot
# ene ee

# No author has reasoned with greater aceu-
# racy, and in a more satisfactory manner upom
# this important branch of the English constita-
# tion than the celebrated David Hume, in his
# History of England. This author is well
# known to have been sufficiently favourable to
# the prerogative, yet his reasonings upon this
# subject, in the case of lord Strafforde, are as
# minutely applicable to the case before us, a9
# if he had written them with the proceedings
# of the special commission of October, 1794,
# lying before him upon his table.

# “Ofall species of guilt, the law of England
# has, with the most scrupulous exactness, de-
# fined that of treason; because on that side it
# was found most necessary to protect the sub-
# ject against the violence of the king and of
# his ministers. In the famous statute of Ed-
# ward Srd, all the kinds of treasons are enume-
# rated; and every other crime, beside such as
# are there expressly mentioned, is care!
# excluded from that appellation. But wi
# regard to this guilt. An endeavour to subvert
# the fundamental laws, the statute of treason is
# totally silent; and arbitrarily to introduce it
# into the fatal catalogue, is itself a subversion
# ofall law; and, under colour of defending li-
# berty, reverses a statute the best calcul
# for the security of liberty, that was ever enact-
# ed by an English parliament.” Vol. vi. chap,
# liy. p. 403.

# The following are a few sentences from the
# defence of lord Strafforde, as quoted by Mr.
# Hume, a nobleman, whom the republicans of
# that time so vehemently hated, and were so
# fixed to destroy, as to render them little scru~
# rou of overstepping the simple and up;

# ending provisions of the law.
# “ ere has this species of guilt lain sq
# long concealed? Where has this fire been
# so long buried, during so many centuri
# that no smoke should appear till it burst ou!
# at once to consume me and my children?
# Better it were to live under no law at all, and,
# by the maxims of cautious prudence, to con-
# form ourselves the best we can to the arbi-
# trary will of a master, than fancy we have s
# law on which we can rely, and tnd at last,
# that this law shall inflicta punishment prece-
# dent to the promulgation, and try us hy max-
# ims unheard of till the very moment of the
# prosecution, Where is the mark set u
# this crime?Where the token by which I
# should discover it? It has lain concealed ;
# and no human prudence, no human innocence,
# could save me from the destruction with
# which I am at present threatened.”

# “ It is now full two hundred and forty

# Thomas Holcroft,—Mr. Erskine, Mr. Gibbs.
# John Richter,—Mr. Erskine, Mr. Gibbs,
# John Thelwall,—Mr. Erskine, Mr. Gibbs,
# John Baxter,—Mr. Erskine, Mr, Gurney.

# ———
# years since treasons were defined. Let us becontent with what our fathers left us ; let not 4
# our ambition carry us to be more learned than
# they were, in these killing and destructive
# arts! To all my afBictions add not this, my
# Jords, the most severe of any, that I, for my
# other sins, not for my treasons, be the means
# of introducing a precedent so pernicious to
# the lame and liberties of my native country !”

# id.

# Chief Justice Free charge consists of three
# parts. The first five pages contain principally
# a sound and constitutional exposition of the
# Jaw of treason, as exhibited in the books. In!
# the two following pages we are presented with
# this portentous speculation, this new treason
# of “conspiring to subvert the monarchy ;”
# though the chief justice, as has already appear-
# ed, has qualified his speculation, with expres-
# sions, proving, by accumulated evidence, and
# in the most precise terms, that this new ima-
# ginary treason is no treason by the laws of

# gland

# Here, as the chief justice observes, the
# charge might have concluded. Here, if a
# proper regard had been paid to the essential
# principles of criminal justice, it would have
# concluded; if not in reality a little sooner.
# The remainder of the charge is made up of hy-
# pothesis, presumption, prejudication, and con-
# Jecture. There is scarcely a single line that
# is not deformed with such phrases as “ public
# notoriety,” “things likely,” “purposes im-
# puted,” “ measures supposed,” and “ imagin-

# cases.”

# The plain reason of all this is, that the
# chief justice suspected, that the treason de-
# scribed in the statute 25 Edward Srd, and
# those founded upon precedent, or deducible
# from adjudged cases, even with the addition
# of the chief justice’s new constructive treason,
# founded, as te confesses, upon no law, prece-
# dent, or case, and which therefore is in reality
# Ro treason, did not afford sufficient ground of
# crimination against the prisoners. He is
# therefore obliged to leave the plain road, and
# travel out of the record. No law, no deduc-
# tion, or construction of law, that could be for-
# ced or drawn out of a mere view of the sta-
# tute, would answer the purposes of the spe-
# cial commission. He is therefore obliged to
# indulge himself in conjecture, as to what the
# Prisoners may have done, and what are

# the facts likely to be laid before the jury.”
# Two ferent iniquities are included in this
# mode of preceeding. First, the chief justice
# implicitly confesses himself unable, by direct

# luctions of law, to show us what it is we
# ought to avoid, and is reduced to the neces-
# ay of reasoning, not forward from general
# s of action to the guilt or innocence of
# Particular men, but backward ffom actions al-


# ‘Thomas Wardle, Matthew Moore, and
# Richard Hodgson, were not in custody.

# On Monday, October the thirteenth, Mr.

# ready performed to the question, whether or
# no they shall fall under such or such provi-
# sions of law. Secondly, by this perverted
# mode of proceeding, he completely prejudges
# the case of the prisoners. He does not pro-
# ceed, as a judge ought to proceed, by explain-
# ing the law, and leaving the grand jury to fix
# its application upon individuals; but leads
# them to the selection of the individuals them-
# selves, and centres in his own person the pro-
# vinces of judge and accuser. It may be
# doubted whether, in the whole records of the,
# legal proceedings of England, another in-
# stance is to be found, of such wild conjecture,
# such premature presumption, imaginations so
# licentious, and dreams so full of sanguinary
# and tremendous prophecy.

# The conjectures of the chief justice respect-
# ing the protable guilt of the accused fall un-
# dertwo heads. First, “ associations, the pro-
# fessed purpose of which has been a change in
# the constitution of the Commons House of
# Parliament, and the obtaining of Annual par-
# liaments.” Secondly, “ the project of a con-
# vention to be assembled under the advice and
# direction of some of these associations.”

# The treasons which the chief justice ima-
# gines himself capable of fixing upon some of
# these associations for a parliamentary reform,
# are of two kinds.

# Before we enter upon these, let us pause a
# moment, and consider the unexplored country
# before us. Every paragraph now presents us
# with a new treason, real or imaginary, pre-
# tendedly direct, or avowedly constructive,
# Division and subdivision rise upon us, and al-
# most every one is concluded with the awful
# denunciation of treason. The chief justice
# is no longer contented with the plain treasons
# of 25 Edward 3rd, or the remoter treasons of
# Foster and Hale. His whole discourse hangs
# by one slender thread. He perpetually refers
# to the new and portentous treason of his own
# mere creation, “a conspiracy to subvert the
# “ monarchy ;” a treason, which he ingenu-
# ously avows “ no lawgiver in this country has
# ever ventured to contemplate,” and “the.
# statute of Edward 3rd, by which we are bound,
# has not declared.” Upon this self-constituted
# treason he hangs his other conjectures and
# novelties as well as he is able, by the help of
# forced constructions, of ambiguous and de-
# ceitful words, and all the delusions of a prac~
# tised sophister. Was it necessary for the de-
# struction of twelve private and untitled men,
# to create all this confusion, to luce all this
# ruin, to overturn every thing that is valuable
# in English liberty, and place us for time com-
# ing under the most atrocious and inexplicable
# despotism that the world ever saw?

# Let usattend to the opinion of judge Black-
# stone upon this subject.

# White, solicitor for the treasury, delivered to
# each of the prisonersa copy of the indictment,
# a list of the jurors impanelled by the sheriff,
# and a list of the witnesses to be produced by
# the crown for proving the said indictment.
#  By the ancient common law, there was a
# great latitude left in the breast of the judges,
# to determine what was treason or not so;
# whereby the creatures of tyrannical princes
# had opportunity to create abundance of con-
# structive treasons : that is, to raise, by forced
# andarbitrary constructions, offences into the
# crime and punishment of treason, which never
# were suspected to besuch. To prevent these
# inconveniences, the statute 25 Edward Srd,
# chap. 2, was made. [Book iv. chap. 6, p. TeThis is a great security to the public, a
# leaves a weighty memento to judges to be care-
# ful, and not overhasty in letting in treasons
# by construction or interpretation, especially
# in new cascs that have not been resolved and
# settled—The legislature was extremely libe-
# ral in declaring new treasons in the unfortu-
# nate reign of king Richard the second; but,
# in the first year of his successor’s reign, an
# act “‘ was passed, which at once swept away
# this whole load of extravagant treasons. Af-
# terwards, particularly in the bloody reign of
# Henry 8th, the spirit of inventing new and
# strange treasons was revived ; all which new-
# fangled crimes were totally abrogated by the
# statute 1 Mary, chap. 1; since which time the
# legislature has become more cautious upon
# this subject.” [P. 85, 86.]

# - The first mode in which, according to chief
# justice Eyre, an association for parliamentary
# reform, may incur the penalties of high trea-
# son, is when “ other purposes, besides those
# of parliamentary reform, and of the most trai-
# torous nature, are hidden under this veil.”
# The purposes he may be supposed to mean,
# are those of his new-fangled treason, of “ con-
# spiring to subvert the monarchy.” Thus,
# in the first place, we have an innocent purpose
# constituting the professed object of this sup-

# josed association ; and behind that the grand
# Tay are to discover, if they can, a secret. pur-
# pose, totally unlike that which the associators
# profess; and this purpose chief justice Eyre

# leclares to be treason, contrary, as he avow-
# edly confesses, to all law, precedent, and ad-
# judicated cases.

# The second mode, in which the chief justice
# is willing to pre-suppose high treason in an
# association for parliamentary reform is, by
# such an association, not in its own nature, as
# he says, “ simply unlawful, too easily degene-
# rating, and becoming unlawful in the highest
# degree.”

# t is difficult to comment upon this article
# with the gravity, that may seem due to a ma-
# gistrate, delivering his opinions from a bench
# of justice. “ An association for parliamentary
# reform ey degenerate, and become unlawful
# in the highest degree, even to the enormous
# extent of the crime of high treason.” Who




# ‘On Friday, October the 24th, Thomas
# Hardy, John Horne Tooke, John Augustus
# Bonney, Stewart Kyd, Jeremiah Joyce, John
# Richter and John Thelwall, were removed
# by habeas corpus from the Tower to New-
# gate.

# knows not that? Was it necessary that
# chief justice Eyre should come in 1794, so-
# lemnly to announce to us so irresistible aproposition? An association for parliamen-
# tary reform may desert its object, and be
# guilty of high treason. True: so may a card
# club, a bench of justices, or even a cabinet
# council. Does chief justice Eyre mean to in-
# sinuate, that there is something in the pur-
# pose of a parliamentary reform, so unhallow-
# ed, ambiguous, and unjust, as to render ts
# well-wishers ohjects of suspicion, rather than
# their brethren and fellow subjects? What
# can be more wanton, cruel, and inhuman,
# than thus gratuitously to single out the pur-
# pose of parliamentary reform, asif it were, of
# all others, most especially connected with de-
# generacy and treason?

# But what is principally worthy of observa-
# tion in both these cases, is, the easy and artful
# manner in which the idea of treason is in-
# troduced into them. First, there is a ‘ con-
# cealed purpose,” or an insensible “ degene-
# racy,” supposed to take place in these asso-
# ciations. Next, that “concealed purpose,”
# or insensible “ degeneracy,” is suppo:ed to
# tend directly to this end, the “ subversion of
# the monarchy.” Lastly, a “ conspiracy to
# subvert the monarchy,” is a treason, first
# discovered by chief justice Eyrein 1794, never
# contemplated by any lawgiver, or included in
# any statute. Deny the chief justice any one
# of his three assumptions, and his whole de-
# duction falls to the ground. Challenge him,
# or any man living, to prove any of them ; an
# you require of him an impossibility. And it
# 1s by this sort of logic, which would be scout-
# ed in the rawest graduate in either of our uni-
# versities, that Englishmen are to be brought
# under the penalties of treason!

# Of these assumptions, the most flagrant
# perhaps, if in reality there can be any grada~
# tion in such groundless assertions, is that
# which imputes to the associations a “ con-
# spiracy to subvert the “monarchy.” The
# chief justice knows, for no man is !gnorant,
# that there is not the shadow of evidence of
# such a conspiracy. If any man in England
# wishes the subversion of the monarchy, is
# there a man in England that does not feel, that
# such subversion, ifcftected at all, can only beef-
# fected by an insensible revolution of opinion?
# Did these associations plan the murder of the
# king, and the assassination of the royal fami-
# ly?” Where are the proofs of it? But the
# authors of the present prosecution probably
# hope, that the mere names of jacobin and re-
# pablieass will answer their purposes ; and that
# a jury of Englishmen can be found who will
# send every man to the gallows without exa-


# Sessions House in the Old Bailey, Saturday Oc-
# tober 25th, 1794,

# Present.—Lord chief justice Eyre; lord
# chief baron Macdonald ; Mr. baron Hotham;

# mination, to whom these appellations shall
# once have been attributed !
# If chief justice Eyre, or his majesty’s ser-
# vants, have any charge of high treason to ad-
# -vance, let them advance,it. The purpose of
# parliamentary reform, as the chiefjustice con-
# tesses, so far from being treasonable, is not
# “ simply unlawful.” If the persons now in
# confinement, have been guilty of high treason,
# that is the point to hich our attention is to
# be called. Their treason is-neither greater
# nor less, for their being engaged in a lawful
# object, the associating for a parliamentary re-
# form. Tell us what they have done that is
# criminal, and do not seek to excite extrajudi-
# cial prejudices against them for what is inno-
# cent.
# Having dismissed the immediate purpose of
# a parliamentary reform, the chief justice goes
# on in the last place to consider “the project
# of aconvention, to be assembled under the ad-
# vice and direction of some of these associa-
# tions.”
# and here it was impossible not to recollect,
# that conventions and meetings of delegates
# are by no means foreign to the English his-
# tory; and that twelve or fourteen years ago,
# many of his majesty’s present ministers were
# deeply engaged in a project of this nature.
# Accordin; f the chief justice takes a very me-
# morable distinction. He calls it “a project,
# which in better times would have been hardly
# thought worthy of grave consideration, but, in
# these, our days, when it has been attempted
# to be pat in execution in a distant part of the
# united kingdom, and with the example of a
# neighbouring country before our eyes, is de-
# scevedly become an object of jealousy to the
# w,”?
# This remark constitutes one of the most
# flagrant violations of the principles of executive
# justice, that was ever heard of or imagined.
# If the times require different measures of jus-
# tice, we are already instructed by the act 25
# Edward Srd, as to the proceeding fitting to
# be employed. “ The judge,” says the act,
# “ shall tarry, without going to judgment of
# the treason, till the cause be shown and de-
# clared before the Eine and his parliament,
# whether it ought to be judged treason or
# other felony.” Parliament, the legislative
# authority of the realm, may make new provi-
# sions of law in accommodation to circum-
# stances; but the judges, the bare expounders
# - of the law, are bound to maintain themselves
# 4n an atmosphere unaffected by the variations
# of popular clamour, ministerial vengeance, or
# the ever-changing nature of circumstances.


# Mr. justice Buller; Mr. justice Grose ; and
# others of his majesty’s justices, &c.

# Thomas Hardy, John Horne Tooke, John
# Augustus Bonney, Stewart Kyd, Jeremiah

# they are to find to day. An interpretation,
# shifting with every gale of accident, may pro-
# duce undefinable terrors in its miserable vic-
# tims, may devote its authors to eternal exe-
# cration, but can have none of the venerable
# features either of law or justice.

# Some of the dreadful consequences in-
# volved in this loose and fluctuating interpre-
# tation, show themsclves in the very next sen-
# tence.

# “ Tt will be your duty,” says the chief jus-
# tice to the jury, “ to examine the evidence
# on this head very caretully, and to sift
# it to the bottom: to consider every part of
# it in itself, and as it stands connected with
# other parts of it; and to draw the conclusion
# of fact, as to the existence, the nature and ob-
# ject of this proposed convention, from the
# whole.

# “In the course of the evidence you will
# probably hear of bodies of men having been
# collected together, of violent resolutions voted
# at this and other meetings, of some prepara
# tion of offensive weapons, and of the adoption
# of the language and manners of those con-
# ventions in France, which have possessed
# themselves of the government of that country.
# I dwell not on thers particulars, because I
# consider them not as substantive treasons,
# but as circumstances of evidence, tending to
# ascertain the true nature of the object which
# these persons had in view.”

# Here we have set before us, in the most
# unblushing and undisguised manner, that
# principle of constructive treason, which has
# upon all occasions formed an object of exe-
# cration in English history. Let us hear what
# Hume says upon the subject in the farther
# progress of that very passage which has been
# already quoted.

# “As is species of treason, discovered by
# the Commons, ‘ in the casc of lord Strafforde,’
# is entirely new and unknown to the laws; so
# is the species of proof by which they pretend
# to fix that guilt upon the prisoner. They
# have invented a kind of accumulative or con-
# structive evidence, by which many actions,
# either totally innocent in themselves, or cri-
# minal in a much inferior degree, shall, when
# united amount to treason, and subject the
# person to the highest penalties inflicted by
# the law. A hasty and unguarded word, a
# rash and passionate action, assisted by the
# malevolent fancy of the accuser, and tortured
# by doubtful constructions, is transmuted into
# the deepest guilt, and the lives and fortunes
# of the whole nation, no longer pratected by
# justice, are subjected to arbitrary will and

# They are to be severely and unalterably thepleasure” [p. 403.].

# same. The meaning they found in the sta-

# It is not easy to conceive of two passages

# tute yesterday, that meaning, and no other,more parallel to each other, than the doctrines

# Joyce, Thomas Holcroft, John Richter, John
# Thelwall, and John Baxter, were arraigned
# apo the following indictment, and severally
# pleaded Not Guilty.

# here delivered by chief justice Eyre, and the
# ‘condemnation pronounced upon them by
# way of anticipation by the illustrious Hume.
# Thus, “ a hasty and unguarded word,”— Adoption of the language of the convention
# in France,”—“ A rash and passionate action,”
# —* Violent resolutions voted at this and other
# ‘meetings — some preparation of offensive
# weapons,”—* Actions either totally innocent
# in themselves, or criminal in a much inferior
# degree”—“ I consider not these particulars
# as substantive treasons.”

# Can any thing be more atrocious, than the
# undertaking to measure the guilt of an indi-
# vidual, and the interpretation of a plain and
# permanent law, by the transitory example
# that may happen to exist “ before our eyes in
# a neighbouring country ?”

# The chief justice speaks of two sorts of
# convention. The first, “ a convention, in
# imitation of those which we have heard of in
# France, in order to usurp the government of
# the country.”

# There lurks a memorable ambiguity under
# this word convention. A convention ~ was
# held no long time ago, of delegates from the
# royal burghs in Scotland, to consider of a
# reformation in the administration of those
# burghs, Of this convention, the present lord
# advocate of Scotland, among others, was a
# member. A convention was proposed in
# 1780, of delegates from'the different county
# meetings held at that period. Both these
# conventions were considerably more formi-
# dable in their structure than that which is the
# subject of present animadversion. The royal
# burghs, and the meetings of freeholders in
# the several countics, consist of bodies more
# or less recognized by the constitution, and
# possessing a degree of inherent authority.
# The convention Proposed in the present in-
# stance, was simply of delegates from the dif-
# ferent societies, voluntarily associated for the
# purpose of parliamentary reform. They could
# possess no inherent authority. The per-
# sons who constituted them, must have been

# ‘actuated by the most perfect insanity, before

# they could have dreamed of usurping the
# government of the country. No delusion,
# therefore, can be more gross, than an attempt
# to style, as chief justice Eyre styles, such a
# convention “ a convention of the people.”

# In describing his first sort of convention,
# the chief juni roundly affirms, “ that the
# project of such a convention, and any one
# step taken towards bringing it about, such
# as, for instance, consultations, forming com-
# mittees to consider of the means, or acting in
# those committees, would be a case of no dif-
# ficulty : it would be the clearest high treason ;
# it would be compassing and imagining the
# King’s death ; and not only his death, but the

# INDICTMENT.
# Middleser, 2 BE it remembered that at 8

# to wit. special session of Oyer and

# death and destruction of all order, religion,
# and laws, of all property, and security for the
# lives and liberties of the king’s subjects.”

# There is a figure in speech, of the highest use
# to a designing and treacherous orator, which
# has not yet perhaps received a name in the la-
# bours of Aristotle, Quintillian, or Farnaby,
# I would call this figure encroachment. It is
# a proceeding, by which an affirmation is mo-
# destly insinuated at first, accompanied with
# considerable doubt and qualification ; repeated
# afterwards, unaccompanied with these quali-
# fications; and at. last asserted in the most
# perenne and arrogant terms. It is thus
# that chief justice Eyre expresses himself re-
# specting a “ conspiracy to overturn the mo-
# narchy.” It is first a treason, “ not declared
# by the statute 25 Edward 3rd;” a treasoa
# “which no lawgtver in this country has ever
# ventured to contemplate ;” a treason, “ not
# resting for its authority upon any law, pre-
# cedent, or adjudged case.” It 1s not this
# thing, nor it is not that; “ the seditio regai
# spoken of by some of our ancient writers, but
# which is no part of our law, seems to come the
# nearest to it,” but will not apply. ‘* the par-
# ticular nature of the traitorous attempt, will
# fall within one or other of the specific trea-
# sons of the statute of Edward 3rd.” A strange
# crime, which the judge knows is provided
# against by the first or the second principal
# clause, but is unable to determine whether it
# is by the former or the latter! Afterwards
# the chief justice speaks of it with less hesi-
# tation ; and at last, as we have seen, affirms
# it to be “a case of no difficulty,and the clearest
# high treason.”

# Can any play upon words be more con-
# temptible, than that by which the chief jus-
# tice, finding the king’s death the subject of
# one of the clauses, and determined to trace
# at least some remote analogy between that
# and the subversion of the monarchy, describes
# the latter by the appellation of “ the death
# and destruction of all order, religion, Sc. &c. t”

# The second sort of convention in chief jus-
# tice Eyre’s arrangement, isaconvention, which,
# not intending to usurp the government of the
# country, “ has for its sole object the effecting
# a change in the mode of representation o'
# the people in parliament, and the obtaining
# that parliaments should be held annually.
# And here,” says the chief justice, “ there ts
# room to distinguish. Such a project of con-
# vention, taking it to be criminal,”

# “Taking it to be criminal!” Was ever
# postulate, more extraordinary, or more intol-
# erable? Did ever judge, sitting upon the
# bench, previously to this instance, assume the
# whole question ; affirm at his ease, and with-
# out the shadow of an authority, scriptural or
# nuncupatory, statute or report, the whole cx-

# Terminer of our sovereign lord the king of and
# for the county of Middlesex holden at the
# Session House on Clerkenwell-green in the
# said county on Thursday the second day of
# October in the thirty-fourth year of the reign
# of our sovereign lord George the Third by the
# minality; and then proceed at his leisure to
# distribute the assumed criminality into all itsdifferent degrees? Meanwhile, after this loud
# and peremptory preamble, the chief justice isobliged to grant, that one sort of convention,one “ degree of criminality,” “ a convention,having for its sole object a dutiful and peace-
# able application to parliament by petition,
# cannot of itself be ranked among this class of
# offences.” He dares not affirm that it is tobe ranked among any class of offences what-
# ever.—But to proceed to the distinctions he
# undertakes to enunrerate.

# The first sort of “ Convention, which hasfor its object the obtaining a parliamentary
# teform, and that object only, is a convention,
# pepong to obtain it without the authority of
# parliament,” and for that purpose “ usurping,
# at least in this instance, the functions of legis-
# lation.” This the chief justice determines,
# upon just the same grounds as in the preced-
# ing instances, “ would be high treason in
# every one of the actors.”

# After this laborious discussion, chief justice
# Eyre is not yet satisfied that he has framed a
# construction, strong enough to ensnare the
# os now under confinement. He has

# ped distinction upon distinction. He has
# promulgated at least five or six different
# elasees of treason, not found in the direct
# ovisions of 25 Edward 3rd, or in the remoter
# stances of Foster and Hale; not supported,
# as he explicitly confesses, by any law, prece-
# dent, or adjudged case. But all this he does
# im the mere wantonness of his power. If any
# ef the prisoners now under confinement had
# acted according to all the as iereonns of his
# irmeginary cases, it may safely be affirmed,
# that, upon any sober trial pti a charge of
# high treason, they must infallibly be acquitted.
# But the chief justice implicitly confesses, that
# they have not acted according to any one of
# his cases. All this profusion of fiction, hypo-
# thesis, and prejudication, is brought forward
# for the sole purpose, either of convincin:
# of the unparalleled ingenuity of the lord chief
# justice of his majesty’s court of Common
# Pleas, or to bewilder the imaginations, to
# throw dust in the eyes, and confound the un-
# derstandings of the grand jury and the nation.
# If this last be the purpose conceived, and if
# it could possibly be supposed that it should be
# successful for a moment, early would be the

# ce, deep the remorse, and severe, it

# is to be feared, the retribution !
# The chief justice then, having hitherto
# talked of every thing that is not to the pur-
# comes at last to speak of the matter in
# Kind. Here he employs ali his ingenuity,
# exerts ail his arts, ail displays his utmost in-



# of God of Great Britain France and Ire-
# and king defender of the faith and so forth
# before the right honourable sir James Eyre
# knight chief justice of our said lord the king
# of his court of Commun Pleas the right ho-
# nourable sir Archibald Macdonald “knight

# trepidity of countenance. This part of the
# case is opened as follows :

# “ Whether the projectofaconvention, having
# for its object the cdllzeting togethera power
# which should overawe the legislative body,
# but not suspen it, or entirely determine its
# functions, if acted upon, will also amount to
# high treason, and to the specifi: treason of
# compassing and imagining the king’s death,
# is a more doubtful question. Thus far is
# clear‘ a force upon the parliament, must be
# immediately directed against the king. It
# must reach the king, or it can have no effect
# at all. The laws are enacted in parliament
# by the ksing’s majesty, by and with the advice
# and consent of the Lords and Commons in
# parliament assembled. A force meditated
# against the parliament, therefore, is a force
# meditated against the king, and seems to fall
# within the cases described.”

# Nothing can be more gross fo the view of
# any one who will attentively read this para-

# aph, than its total want ofall definite and
# intelligible meaning. The chief justice talks
# of “ collecting together a power,” and of “a
# force” exercised upon the parliament. What
# is here intended by the words power and
# force? Under the kindly ambiguity of these,
# words, the chief ghee seen very willing to
# slip upon us the idea of an armed power and
# amilitary force. But thiscan scarcely by any
# construction be reconciled to the idea ofa
# convention. An army of delegates was an
# idea reserved for chief justice Eyre to intros
# duce into the worl ell then: let us
# pose that arms and violence are not intended;
# yet the chief justice says, that the project of a
# convention has for its object ‘ the collecting
# together a power, which should overawe the
# legislative body.” This word is still more
# ambiguous than any of the rest. What are
# we to understand by the phrase “ to over-
# awe?” Awe in its true acceptation has always.
# been understood to mean deference or re-
# spect. It cannot mean any thing else here,
# since, as we have already seen, armed power
# and military force are out of the question,
# But in this sense what is the object of every
# species of convention or political association
# whatever? It is always intended to produce
# deference and respect. Thus the chief justice
# very properly observes, that “ a convention,
# having for its sole object a dutiful and peace-
# able application to parliament,” does not fail
# to find that application attended with “ re-
# spect and credit, in proportion to its univer.
# sality.” Indeed there can be no doubt, that
# there are but two ways of operating upon
# men’s conduct, the one, hy exhibiting argu-
# ments calculated to prevail upon their own

# chicf baron of our said lord the king of his
# court of Exchequer the honourable sir Beau-
# mont Hotham knight one of the barons of our
# said lord the king of his said cout of F.xche-
# quer the honcurable sir Francis Buller baronet

# one of the justices of our said lord the king of
# his said court of Common Pleas the henour- ;

# able sir Nash Grose knight one of the justices
# i of our said lord the king assigned to hol¢
# pleas before the king himself the honourable
# Soulden Lawrence knight one other of
# ‘ the justices of our said lord the king assigned
# to hold Pleas before the king himself and
# others their fclluws justices and commissioners

# inclinations and conviction, the uther a per-
# ceiving huw much the thing required accords
# with the sense of numerous bodies of men,
# and budics uf men entitled to eminent credit.
# * Such being the substance of the most ma-
# terial paragraph in the charge to the grand
# jury, let us see in what manner this paragraph

# is concluded, and what are the inferences
# drawn trom it. Whatis the treatment due
# to this force which is no force; thiscollecting
# together a power, unarmed, and entitled to
# credit only fur its universality? What shall
# be done to the men who thus overawe the
# legislative body, by exciting its deference and
# ; or, failing this, do not overawe it at
# all, inasmuch as they have no power to in-
# force their demands? “ Whether or no,” as
# chict justice Eyre sagaciously ubseives, the
# project of such a convention will amount to
# high treason, is a more doubtful question.”
# He adds, “ in this case it docs not appear to
# me, that warranted by the authorities, tu
# state to you as clear law, that the mere con-
# spiracy to raise such a force” (recollect what
# has been said upon the nature of this force],
# “ and the entering into consultations respect-
# ing it, will alone, and without actually raising
# the force, constitute the crime of high treason.

# What the law is in that case, and what will

# be the effect of the circumstance of the force
# being thus meditated, will be fit to be so-
# Jemnly considered and determined when the
# case shall arise.”

# Here the chief justice speaks with a proper
# degree of modesty and precaution, so far as
# relates to the supposed guilt of the persons
# under confinement; but when he has occasion

# to resume the subject, he, in his usual manner

# introduces a variation into the statement.

# “Tt may perhaps be fitting,” says he, “ if

# you find these persons involved in such a de-
# sign, and if the charges of high treason are
# oficred to be maintained against them upon
# that ground, that, in respect of the extraordi-
# Nary nature, the dangerous extent, and at
# the best, the very criminal complesion of such
# a-conspiracy, this case, which I state to you
# as a new and a duubtful case, should be put
# into a judicial course of inquiry, that it may
# receive a culemn adjudication, whether it will
# or will not amount to high treason.”

# "It is diflicult to conceive of any thing more
# abhorrent to the genuine principles of buma-
# nity, tian the ductrine here delivered. The
# chief justice, after having enumerated various
# sorts of treason, respecting which he speaks
# diflidently at first, and pcremptorily at last,
# but which are all the mere creatures of his
# own imagination, comes toa case upon which

# aver the procecding described in it to be trea-
# son, Well, then; what is the remedy he pro-

# poses? Surely anew act of parliament; the
# remedy prescribed by the act of Edward 3rd,
# * “in cases of treason, which may happen intime to come, but which could net then be
# thought of or declared.” No such thing.Upon this case, which he does not venture to
# pronounce to be treason, he directs the grand
# jury to findthe bills to be true bills! He
# tells them, “ that it is fitting that this case,”
# which he “ statcs as new and doubttul, shouid
# be put into a judicial course of inquiry, that
# it may receive a solemn adjudication, whether
# it will or will not amount to high treason !”‘The chief justice, in this instance, quits
# the character of acriminal judge and a civil
# magistrate, and assumes that of a natural
# philosopher or experimental anatomist. He
# is willing to dissect the persons that shall be
# brought before him, the better to ascertain
# the truth or falsehood of his preconceived
# conjectures, The plain English of his recom-
# mendation is this: “ Let these men be put
# upon trial fer their lives; let them and their
# friends, through the remotest strainers of
# connexion, be exposed to all the anxieties
# incident to so uncertain and fearful a condi-
# i tion; let them be exposed to ignominy, to
# obloquy, to the partialities, as it may happen,
# of'a prejudiced judge, and the perverseness of
# au ignorant jury: we shall then know how
# we ought to conceive of similar cases. By
# trampling upon their peace, throwing away
# their lives, or sporting wih their innocence,
# we shall obtain a basis upon which to proceed,
# and a precedent to guide our judgment in
# future instances,”

# This is a sort of language which it is im-
# i possible to recollect without horror, and
# which seems worthy of the judicial ministers
# of liberius or Nero. It argues, if the speaker
# understocd his own meaning, or if the paper
# before me has faithfully reported it, the most
# frigid indifference to human happiness and
# human life. According to this method of
# estimate. laws, precedents, cases, and reports
# j} are of high value, and the hanging a few
# individuals is a very cheap, economical and
# proper way of purchasing the decision of a
# doubtful speculation.

# Surely it would be worthy, if not of the
# ; judges, at least of the immediate ministers of
# the sovereign, to consider whether, if they
# mean to put us under a new rule of criminal
# Jaw, it be not better solemnly to originate
# that lawin the two Houses of Parliament,
# than to suffer it to be made out of new con-
# leven he hesitates to decide. He dares not



# of our said lord the king assigned by letters
# patent of our said lord the king under his
# great seal of Great Britain made to them and
# others and any three or more of thein (of
# whom one of them the aforesaid sir James
# Evre sir Archibald Macdonald sir Beaumont
# Hotham sir Francis Buller sir Nash Grose

# structions of old statutes, contrary to all law
# and precedent, and contrary to the security
# aul liberty of the subject.

# In Jreland, some time ago, it was thought
# pope to bring forward a convention-bill,
# declaring such proceedings, as are the subjects
# of the forced constructions of chief baron
# Eyre, to amount to high treason. When the
# Habeas Corpus act was suspended in England,
# wewere given to understand that this pro-

# ceeding was thought sufficient for the present, '

# and that a convention-bill, similar to the
# Trish, and other severe measures, were re-
# served to be adopted, as the case might
# require. This fallacious show of lenity, now
# turns out to be the most unprincipled tyranny.
# Mr. Dundas and others talked in the last
# session of parliament, of bringing home the
# Scottish principles of jurisprudence, if need
# were, to England, and rendering associations
# and conventions a subject of transportation to
# Botany Bay. They have since refined upon
# their plan, and carried the law of England,
# or what they are pleased to call so, into
# Scotland, rendering these offences, real or
# imaginary, a subject of the penalties of high
# treason. Such have been the incroachinents
# upon the constitution, by men who have the
# audacity to cali themselves its champions,
# that a man who should have pretended to
# foretel, from six months to six months, the
# measures they would think proper to pursue,
# would have been laughed at for the improba-
# bility and utter absurdity of his tale. Britons
# willat length awake, and the effects of reason
# and conviction upun them, will not be less
# formidable or Jess unacceptable to their op-
# pressors, than the effects that might flow
# trom a course of violence !

# I have hitherto abstained from saying anv
# thing respecting the personal characters of
# the men now under accusation. If their
# aoilities be as rare, and their merits as high as
# Lieir warmest admirers can conceive them, it
# would still be foreign to the question I propose
# to consider. If they be men, exceptionable
# in their character, ambiguous in their designs,
# and mischievous in their counsels, that also

# ought to be put out of the consideration. The
# English constitution is strong enough to dis-
# arm all the adversarics of the public peace,
# without its being necessary for that purpose
# to destroy its very essence. Twelve men are
# apparently concerned, but the liberties and
# happiness of all are at stake. If these new
# treasons be established, we may say, as the
# parliament of Henry the fourth did, speaking
# of the new-fangled treasons under Richard
# the second, that “ no man can know how he


# and sir Soulden Lawrence our said lord the
# king willed should be one) to inquire by the
# oath of good and lawful men of the county of
# Middlesex of all high treasons in compassing
# or imagining the death of our lord the king
# levying war against our lord the king in his’
# realm or in adiering to the enemics of our’
# fe eS
# ought to behave himself, to do, speak, or say,’
# for doubt of the pains of treason” [Black-
# stone, book iv, chap. 6, p. 86]. The construc
# tions of chiet justice Kyre, and the special
# commission, put a perpetual bar to all asso-’
# ciations, delegations, and consultings respect-
# ing any species of grievance. Will any man
# venture to say, that we shall never stand in
# need of these expedients ; or shall we consent
# for all time coming, to hold every possible
# retorm and amendment at the mere will of,
# the administration? If these principles be
# established, utterly subversive as they are of
# the principles of the English government,’
# who will say that we shall stop here? Chief
# justice Eyre says today, “ all men may, nay,’
# all men must, if they possess the faculty of
# thinking, reason upon every thing, that’
# sufficiently interests them to become an’
# object of their attention; and among the’
# ‘ objects of attention of freemen, the principles’
# of government, the constitution of particular’
# governments, and, above all, the constitution”
# of the government under which they live,‘
# will naturally engage attention and provoke‘
# speculation.” But who will say how long
# this liberty will be tolerated, if the principles,
# so alarmingly opened in the charge to thes
# grand jury, shall once be established? This’
# Is the most important crisis in the history of
# English liberty, that the world ever saw. If?
# men can be convicted of high treason, upon‘
# such constructions and implications as are
# contained in this charge, we may look with.
# conscious superiority upon the republican
# speculations of France, but we shall certainly:
# have reason to envy the milder tyrannies of
# ‘Turkey and Ispahan. i
# Krom what has been said it appears, that
# the whole proceedings intended in the present
# case, are of the nature of an er post facto law.
# ‘This is completely admitted by the chief
# j justice. In summing up the different parts
# ! of his charge, he enumerates three cases, in
# ' the first of which he directs the rand jury to’
# * throw outthe bills, and in that of the two last’
# to find them true bills. One of these two:
# [relates to chief justice Eyre’s new treason of
# “a conspiracy to subvert the monarchy,”a treason which, he says, is not declared by
# ‘ the statute of Edward 3d. and no lawgiver inthis country basever ventured to contemplate.The other, “that of overawing parliament,”
# he states to be a new and doubttul case, and
# ; Fecommends, that it should be “ put into a
# judicial course of enquiry, that it may receive
# a solemn adjudication whether it will or will
# not amount to high treason.” . :
# Thus it is fully admitted, respecting the



# said lord the king in his realm giving to them
# aid and comfort in his realm or elsewhere and
# ofall misprisions of such high treasons as afore-
# said or of any of them within the county afore-
# said (as well within liberties as without) by
# whomsvever and in what manner soever done
# committed or perpetrated when how and after
# what manner and of all otiver articles and cir-
# cumstances concerning the premisses and
# every or any of them in any manner what-
# soever and the said treason and misprisions of
# treasons according to the laws and customs
# of England for this time to hear and deter-
# mine by the oath of Benjamin Winthrop es-
# wire John Henry Schneider esquire Edward
# ronside esquire Benjamin Kenton esquire
# Rawson Hart Boddam esquire John Aris es-
# wre William Pardoe Allett esquire John
# erry esquire Henry Peter Khuff esquire
# Thomas Winslow esquire Thomas Cole es-
# quire Samuel Hawkins esquire George Ward
# esquire Thomas Boddam esquire Joseph Lan-
# caster esquire Rohert Wilkinson esquire
# George Galway Millis esquire Henry Wright
# esquire John Hatchet esquire Rowland
# persons now under accusation, that they.
# could find no reason, either in the books of :
# our law, or of any commentators of received '
# authority, to suppose that they were incurring
# the guilt of treason. “The mark set upon
# this crime, the token by which it could be
# discovered, lay entirely concealed; and no
# human prudence, no human innocence, could
# save them from the destruction with which ‘
# they are at present threatened” [Hume, vol.yi, ch. liv. p, 404.}.

# It is pretty generally admitted, that several
# of these persons, at least, were honest and

# phenson esquire and John Campbell esquire
# good and lawful men of the county aforesaid
# now here sworn and charged to iuquire for
# our said lord the king for the body of the said
# county, touching and concerning the pre-
# misses in the said letters patent mentioned It
# is presented in manner and form as fulloweth
# (that is to say)

# Middlesex to wit the jurors for our sove-
# reign lord the king upon their oath present
# that Thomas Hardy late of Westminster in
# the county of Middlesex shoemaker John
# Horne ‘tooke late of Wimbledon in the county
# of Surrey clerk John Augustus Bonney late of
# the parish of Saint Giles in the Fields in the
# county of Middlesex aforesaid gentleman
# Stewart Kyd late of London esquire Jeremiah
# Joyce late of the parish of Saint Mary-le-bone
# otherwise Marybone in the county of Middle-
# sex aforesaid pentieyaay Thomas Wardle late
# of London gentleman Thomas Holcroft late of
# the parish of Saint Mary-le-bone otherwise
# Marybone aforesaid in the county of Middle-
# sex aforesaid gentleman John Richter late of
# Westminster 1p the said county of Middlesex

# condemnation. If therefore he address them
# in the frank language of sincerity, he must
# say: “Six months ago you engaged in meay
# sures, which you believed conducive to the
# public good. You examined them in the
# sincerity of your hearts, and you admitted
# them with the full conviction of the under-
# standing. You adopted them from this ruling
# motive, the love of your country and man-
# kind. You had no warning that the measures
# in which you engaged were acts of high
# treason: no law told you so; no precedent
# recorded it; no man existing upon the face of

# well-intentioned, though mistaken men. ; the earth could have predicted such an inter-
# Punishment is awarded in human courts of pretation. You went to your beds with a
# justice, either according to the intention, orperfect and full conviction, that you had arted
# the mischief committed. If the intention be . upon the principles of immutable justice, and
# alone to be considered, then the men of , that you had offended no provision or statute

# whom I speak, however unguarded and preju-
# dicial their conduct'may be supposed to have
# been, must on that ground be infallibly ac-
# quitted. If, on the other hand, the mischief
# incurred be the sole measure of the punish-
# ment, we are bound by every thing that is
# sacred to proceed with reluctance and regret.
# Let it be supposed, that there are cases,
# where it shall be necessary, that a well
# designing man should be cut off, for the sake
# of the whole. The least consideration that
# we can pay in so deplorable a necessity, is, to
# warn him of his danger, and not suffer him to
# incur the penalty, without any previous cau-
# tion, without so much as the knowledge of
# ats existence.

# I anticipate the trials to which this charge
# is the prelude. I know that the judge will
# admit the good intention and honest design of

# that was ever devised. I, the judge sitting
# upon the bench, you, gentlemen of the jury,
# every inhabitant of the island of Great Britain,
# had just as much reason to conceive they were
# incurring the penalties of the law, as the pri-
# soners at the bar. This is the nature of the
# crime; these are the circumstances of the
# case, “

# “ And for this, the sentence of the court
# ; [but not of the law] is, That you, and each of
# yon, shall be taken from the bar, and con-
# veyed to the place from whence you came,
# and from thence be drawn ‘upon 8 hurdle to
# the place of execution, there to be hanged by
# the neck, but not until you are dead; you
# shall be taken down alive, your privy mem-
# bers shall be cut off, and your bowels shall be
# taken out and burnt before your faces; your
# heads shall be severed from your bodies, and

# several of the persons arraigned: it will beyour bodies shall then be divided into four
# impossible to deny it; it is notorious to thequarters, which are to be at the king’s dis-
# whole universe. He has already admitted,posal; and the Lord have mercy on your
# that there is no law or precedent for theirsouls!”

# gentleman Matthew Moore late of West- 1 said jurers unknown to cause and procure a
# ininster in the county of Middlesex aforesaidconvention and meeting of divers subjects of
# gentleman John Thelwall late of Westminsterour said lord the king to be assembied and
# in the county of Middlesex aforesaid gentle-held within this kingdom with intent and if
# man Rict.ard Hodgson late of Westminster inorder that the persons to be assembled at such

# the county of Middlesex aforesaid hatter and
# John Baxter late of the parish of Saint Leo-
# nard Shoreditch in the county of Middlesex '
# aforesaid labourer being subjects of our said
# lord the king not having the fear of God in
# their hearts nor weighing the duty of their
# allegiance but being moved and seduced by ;
# the instigation of the devil as false traitors
# against our said lord the king their supreme
# true lawful and undoubted ford and whollywithdrawing the cordial love and true and due
# obedience which every true and faithful sub-
# ject of our said lord the king should and of right
# ought to bear towards our said lord the kingand
# contriving and with all their strength intending
# traitorously to break and disturb the peace
# and common tranquillity of this kingdom of
# Great Britain and to stir move and excite
# insurrection rebellion and war against our
# said lord the king withia this kingdom and to
# subvert and alter the legislature rule and go-
# vernment now duly and happily established
# in this kingdom and to depose our said lord
# the king from the royal state title power and
# government of this kingdom and to bring and put our said lord the king to death on the first
# day of March in the thisty-third year of the
# reign of our sovereign lord the now kin
# and on divers other days and times as well
# before as after at the parish of Saint Gilesaforesaid in the county of Middlesex aforesaidmaliciously and traitorously with force and
# arms &c. did amongst themselves and together
# with divers other false traitors whose names
# are to the said jurors unknown conspire com-
# pass imagine and intend to stir up move andexcite insurrection rebellion and war against
# our said lord the king within this kingdom of
# Great Britain and to subvert and alter the le-
# islature rule and government now duly and
# appily established within this kingdom of
# Great Britain and to depose our said lord the
# king from the royal state title power and go-
# vernment of this kingdom and to bring and
# put our said lord the king to death And to
# fulfil perfect and bring to effect their most
# evil and wicked treason and treasonable com-
# passings and imaginations aforesaid they the
# said Thomas Hardy John Horne Tooke John
# Augustus Bonney Stewart Kyd Jeremiah Joyce
# Thomas Wardle Thomas Holcroft John Rich-
# ter Matthew Moore John Thelwall Richard
# Hodgson and John Baxter as such false trai-
# tors as aforesaid with force and arms on the‘said first day of March in the thirty-thirdyear aforesaid and on divers other days and
# times as well before as after at the parish of
# Saint Giles aforesaid in the county of Mid-
# dlesex aforesaid maliciously sn traitor-
# ously did meet conspire consult and agree
# among themselves and ther with divers
# other false traitors whose names are to the

# convention and meeting should and might
# wickedly and traitorously without and in de-
# fiauce of the authority and against the will of
# the parliament of this kingdom subvert and
# alter and cause to be subverted and altered
# the legislature rule and government now duly
# and happily established in this kingdom and
# depose and cause to be deposed our said lord the
# king from the royal state title power and go-
# vernment thereof And further to fulfil per-

# ‘fect and bring to effect their most evil and

# wicked treason and treasonable compassings
# and imaginations aforesaid and in urder the
# more readily and effectually to assemble such
# convention and meeting as aforesaid for the
# traitorous purposes aforesaid and thereby to
# accomplish the same purposes they the said
# Thomas Hardy John Horne Tooke John Au-
# gustus Bonney Stewart Kyd Jeremiah Joyce
# Thomas Wardle Thomas Holcroft John Rich-
# ter Matthew Moore John Thelwall Richard
# Hodgson and John Baxter as such false traitors
# as aforesaid together with divers other falsetrai-
# tors whose names are to the jurorsaforesaid un-
# known on the said first day of March in the
# thirty-third year aforesaid and on divers other
# days and times as well before asafter with force
# and arms at the parish of Saint Giles afore-
# said in the county of Middlesex aforesaid
# maliciously and traitorously did compose
# and write and did then and there maliciously
# and traitorously cause to be composed and
# written divers books pamphlets levers in-
# structions resolutions orders declarations ad-
# dresses and writings and did then and there
# maliciously and traitorously cause to be pub-
# lished divers other books pamphlets letters
# instructions resolutions orders declarations
# addresses and writings the said books pam.
# phlets letters instructions resolutions orders
# declarations addresses and writings so re-
# spectively composed written published and
# caused to be composed written and published
# purporting and containing therein among
# other things incitements encouragements and
# exhortations to move induce and persuade
# the subjects of our said lord the king to choose
# depute and send and cause to be chosen de-
# puted and sent persons as delegates to com-
# pose and constitute such convention and
# meeting as aforesaid to be so holden as afore-
# said for the traitorous purposes aforesaid And
# further to fulfil perfect and bring to effect
# their most evil and wicked treason and trea~
# sonable compassings and imaginations afore.
# said and in order the more reatily and effec-
# tually to assemble such convention and meet-
# ing as aforesaid for the traitorous panes
# siccosasd and thereby to accomplish the
# same purposes they the said Thomas Hardy
# Joba Horn Tooke John Augustus Bonney
# Stewart Kyd Jeremiah Joyce Thomas Wardle

# Thomas Holcroft John Richter Matthew Moore
# John Thelwall Richard Hodgson and John
# Baxter as such false traitors as aforesaid on
# the said first day of March in the thirty-third
# year atoresaid and on divers other days and
# times as well before as after with force and
# arms at the parish of Saint Giles aforesaid in
# the county of Middlesex aforesaid did meet
# consult and deliberate among themselves and
# together with divers other false traitors whose
# names are to the said jurors unknown of and
# concerning the calling and assembling such
# convention and meeting as aforesaid for
# the traitorous purposes aforesaid and how
# when and where such convention and
# meeting should be assembled and held and by
# what means the subjects of our said lord the
# king should and might be induced and moved
# tu send persons as delegates to compose and
# constitute the same And further to fulfil per-
# fect and bring to effect their most evil and
# wicked treason and treasonable compassings
# and imaginations aforesaid and in order the
# more readily and effectually to assemble such
# convention and meeting as aforesaid for the
# traitorous purposes aforesaid and thereby to
# accomplish the same purposes they the said
# ‘Thomas Hardy John Horne Tooke John Au-

# ustus Bonney Steward Kyd Jeremiah Joyce

# ‘homas Wardle Thomas Holcroft John Rich-
# ter Matthew Moore John Thelwall Richard
# Hodgson and John Baxteras such false traitors
# as aforesaid together with divers other false
# traitors whose names are to the jurors
# aforesaid unknown on the said first day of
# March in the thirty-third year aforesaid and
# on divers other days and times as well before
# as after with force and arms at the parish of
# Saint Giles aforesaid in the county of Middle-
# sex aforesaid maliciously and traitorously did
# consent and agree that the said Jeremiah
# Joyce John Augustus Bonney John Horne
# Tooke Thomas Wardle Matthew Moore John
# Thelwall John Baxter Richard Hodgson one
# John Lovett one William Sharp and one John
# Pearson should meet confer and co-operate
# among themselves and together with divers
# other false traitors whose names are to the
# said jurors unknown for and towards the call-
# ing and assembling such convention and
# meeting as aloresaid for the traitorous pur-
# poses aforesaid and further to fulfil perfect
# and bring to effect their most evil and wicked
# treason and treasonable compassings and ima-
# ginations aforesaid they the said Thomas
# Hardy John Horne Tooke John Augustus
# Bonney Stewart Kyd Jeremiah Joyce Thais
# Wardle Thomas Holcroft John Richter Mat-
# thew Moore John Thelwall. Richard Hodgson
# and John Baxter as such false traitors as
# aforesaid together with divers other false trai-
# tors whose names are to the jurors afore-
# said unknown on the first day of March in
# the thirty-third year aforesaid and on divers
# other days and times as well before as after
# with force and arms at the parish of St Giles


# maliciously and traitorously did cause and pro-
# cure to be made and provided and did then
# and therc maliciously and traitorously consent
# and agree to the making and providing of
# divers arms and offensive weapons to wit guns
# muskets pikes and axes for the purpose of
# arming divers subjects of our said lord the king
# in order and to the intent that the same sub-
# jects should and might unlawfully forcibly
# and traiturously oppose and withstand our said
# lord the king in the due and lawful exercise
# ot his royal power and authority in the execu-
# tion of the laws and statutes of this realm
# and should and might unlawtully forcibly and
# traitorously subvert and alter and aid and

# assist in subverting and altering without and
# in defiance of the authority and against the
# will of the parliament of this kingdom the
# legislature rule and government now duly and
# happily established in this kingdom and de-
# ee and aid and assist in deposing our said
# ord the king from the royal state title power
# and governinent of this kingdom and further
# to fulfil perfect and bring to effect their most
# evil and wicked treason and treasonable com-
# passings and imaginations aforesaid they the
# said Yhomas Hardy John Horne Tooke
# John Augustus Bonney Stewart Kyd Jere-
# miah Joyce Thomas Wardle Thomas Hol-
# croft John Richter Matthew Moore John
# Thelwall Richard Hodgson and John Baxter
# as such false traitors ‘as aforesaid with
# force and arms on the said first day of
# March in the thirty-third year aforesaid
# and on divers other days and times as well be-
# fore as after at the parish of Saint Giles afore-
# said in the county of Middlesex aforesaid ma-
# liciously and traitorously did meet conspire con-
# sult and agree among themselves and with di-
# vers other false traitors whose names are to the
# said jurors unknown to raise levy and make
# insurrection rebellion and war within this
# kingdom of Great Britain against our said
# lord the king and further to fulfil perfect and
# bring to effect their most evil and wicked trea-
# son and treasonable compassings and imagin-
# ations aforesaid they the said ‘Thomas Hardy
# John Horne Tooke John Augustus Bonney
# Stewart Kyd Jeremiah Joyce Thomas Wardle
# Thomas Holcroft John Richter Matthew
# Moore John Thelwall Richard Hodgson and
# John Baxter as such false traitors as aforesaid
# on the said first day of March in the thirty-
# third year aforesaid and on divers other days
# and times as well before as after at the parish
# of Saint Giles aforesaid in the county of
# Middlesex aforesaid with force and arms ma-~
# liciously and traitorously did meet conspire
# consult and agree amongst themselves and
# together with divers other talse traitors whose
# names are to the said jurors unknown un-
# lawfully wickedly and traitorously to sub-
# vert and alter and cause to be subverted and
# altered the legislature rule and government
# now duly and happily established in this king-
# dom and to depose and cause to be deposed our

# aforesaid in the county of Middlesex aforegaigsaid lord the king from the royal state title.

# power and government of this kingdom and
# further to fulfil perfect and bring to etiect their
# most evil and wicked treason and treasonable
# compassings and inayinations aforesaid and in

# order the more readily and ettectually to bringabout such subversion alterationand deposition

# as last aturesaid they the said Thomas Hardy
# John Horne Tooke John Augustus Bonney

# Stewart hyd Jeremiah Joyce ‘| bomas Wardle ;

# Thomas Holcrott. John Richter Matthew
# Moore John ‘Thelwall Richard Hodgson and
# John Baxter as such false traitors as afore-
# said together with divers other false traitors
# whose names arc to the Jurors aforesaid un-
# Known on the said first day of March in the
# thirty-third year aforesaid and on divers other
# days and times as well beture as after at the


# ‘and did then and there maliciously and trai-torously consent and agree to the procuring
# and providing arms and offensive weapons (to
# wit) guns muskets pikes and axes therewith
# to levy and wage war insurrection and rebel-"
# lion against our said lord the king within this
# Kingdom against the duty of the allegiance of
# them the said Thomas Hardy John Horne
# Tooke John Augustus Bonney Stewart Kyd
# Jeremiah Joyce Thomas Wardle Thomas
# ' Holeroft John Richter Matthew Moore John
# Thelwall Richard Hodgson and John Baxter
# ‘ against the peace of our said lord the nowking his crown and dignity and against the
# ‘ form of the statute in that case made andprovided.
# Mr. Attorney General stated to the Court,

# parish of St Giles aforesaid in the county of , that he had been informed by the counsel for

# Middlesex aforesaid with force and arms ma-
# liciously and traitorously did prepare aid com-
# pose and did then and there maliciously and
# traitorously cause and procure to he prepared
# and composed divers buoks pamphlets letters
# declarations instructions resolutions orders
# addresses and writings and did then and there
# maliciously and traitorously publish and dis-
# perse and did then and there maliciously and
# traitorously cause and procure to be published
# and dispersed divers other books pamphlets
# letters declarations instructions resolutions
# orders addresses and writings the said several
# books pamphlets letters declarations instruc-
# tions resolutions orders addresses and writings
# so respectively prepared composed published
# dispersed and caused to be prepared com-
# posed published and dispersed as last
# aforesaid purporting and containing therein

# (amongstother things) incitements encourage-
# ments and exhortations to move induce and
# persuade the subjects of our said lord the king

# to aid and assist in carrying into effect such ,

# traitorous subversion alteration and deposition
# as last aforesaid and also containing therein
# amongst other things information instructions
# and directions to the subjects of our said
# lord the king how when and upon what occa-
# sions the traitorous purposes last aforesaid
# should and might be carried into effect and fur-
# ther to fulfil perfect and bring to effect their
# most evil and wicked treason and treasonable
# compassings and imaginations aforesaid they
# the said Thomas Hardy Jolin Horne Tooke
# John Augustus Bonney Stewart Kyd Jere-
# miah Joyce Vhomas Wardle ‘Thomas Holcroft
# John Richter Matthew Moore John Thelwall
# Richard Hodgson and John Baxter as such
# false traitors as aforesaid together with divers
# other false traitors whose names are to the
# jurors aforesaid unknown on the said first day
# of March in the thirty-third year aforesaid
# and on divers other days and times as well
# before as alter at the parish of Saint Giles
# aforesaid in the county of Middlesex afore-
# said with force and arms maliciously and
# traitorously did procure and provide and
# did then and there maliciously and traitor-
# ously cause and procure to be provided

# the prisoners, it was their intention the pri-
# ''suners should be tricd separately. It was
# therefore his intention to proceed first on the
# ; trial of Thomas Hardy,At the request of the prisoners’ counsel,
# i the ‘a adjourned to Tuesday, October the
# 28th,""",
# #? Deleting the beginning (superfluous) of the trial (day 1)
# """Sessions House in the Old Builey, Tuesday, Oc
# tober 28th.

# Present,—Lord chief justice Eyre; lord
# chief baron Macdonald; Mr. baron Hotham ;
# Mr. justice Buller; Mr. justice Grose; and
# others his majesty’s justices, &c.

# Counsel for the Crown.—Mr. Attorney Ge-
# neral (Sir John Scott, afterwards lord ole
# —Mr. Solicitor General [Sir John Mitford,
# afterwards lord Redesdale],—Mr. Serjeant
# Adair,—Mr. Bearcrott,—Mr. Bower,—Mr.
# | Law [afterwards lord Ellenborough],—Mr.
# Garrow, [afterwards a baron of the court of
# i Exchequer],—Mr. Wood [afterwards a baron
# "of the court of Exchequer.

# Solicitor—Joseph White, esq. solicitor for
# the affairs of his majesty’s treasury.

# Counsel forthe Prisoner.—The hon. Thomas
# Frskine, {afterwards lord Erskine}, — Mr.
# Gibbs parents lord chief justice of the
# court of Common Pleas].

# Assistant Counsel, — Mr. Dampier, [after-
# wards a judge of the court of King’s-bench].
# —™Mr. Felix Vaughan.— Mr. Gurney.

# Solicitors.—Messrs. George and Romaine
# William Clarkson, of Essex strect.

# The court being opened and Thomas Hardy
# set to the har, the jurors returned by the she-
# tiff were called over.

# Major Rhode, esq. challenged by the prisoner.

# Thomas Martin, oilman, not a freeholder of
# the county of Middlesex.

# George Jctterys, jeweller, not a freeholder.

# Hugh French, esq. challenged by the prisoner.

# Robert Mellish, ship-builder, challenged by
# the prisoner.

# William Harwood, esq. challenged by the

# crown, a

# James Hagarth, esq. cltallenged ‘by the pri-

# soner.
# Robert Lewis, esq. excused on account of ill-

# ness.

# John Walker, esq. not a freeholder.

# George Wade, stock-broker, challenged b
# the crown,

# Thomas Buck, esq. sworn.

# ‘Thomas Aylifte, esq. challenged by the pri-
# soner.

# Thomas Wood, esq. sworn.

# Mark Hudson, esq. challenged by the prisoner.

# John Mandell, gent. challenged by the pri-

# soner.

# Henry Bullock, brewer, challenged by the
# crown. ;

# John Powsey, carpenter and surveyor, chal-
# lenged by the prisoner.

# George Capes, esq. challenged by the prisoner.

# Thomas Rhodes, cow-keeper, challenged by
# the prisoner.

# Edward Helme, esq. challenged by the pri-
# soner.

# Jeffery Holmes, esq. challenged by the crown.

# Wiliam Fraser, esq. sworn.

# Apsley Pellat, ironmonger, not a freeholder.

# Hugh Reyuelds, esq. challenged by the pri-
# soner.

# Thomas Harrison, cow-keeper, challenged by
# the prisoner.

# Daniel Gosset, esq. not a freeholder.

# Richard Meaus, esq. not a freeholder.

# Dicker Saunders, esq. one of the people called

# y

# uakers.
# Calvert Clapham, gent. not a freeholder.
# John Leader, gent. challenged by the prisoner.
# John Guest, esq. excused on account of illness.
# Charles Fourdrinier, stationer, nota freeholder.
# Adam Steinmetz, biscuit-baker.
# Mr. Attorney General.—Are you a natural
# born subject?
# Mr. Steinmets.—Y es.—Sworn.
# Alexander Baxter, esq. not a treeholder.
# Richard Child, distiller, not a freeholder.
# Jeremiah Blakeman, timber merchant, chal-
# lenged by the prisoner.
# Robert Kilby Cox, esq. challenged by the
# prisoner.
# Richard Hunt, esq. not a freeholder.
# James Payne, esq. challenged by the crown.
# Newell Connop, distiller, sworn.
# John Mercer, mealman, sworn.
# John Rixon, cooper, challenged by the crown.
# Thomas Sayer, esq. sworn,
# Richard Carter, esq. sworn.
# Edward Hale, gent. challenged by the pri-

# ~ soner.

# George Fillingham, esq. challenged by the
# prisoner.

# Samuel Rudge, esq. not a freeholder.

# William Perry, esq. challenged by the pri-
# soner.

# Richard Gough, esq. challenged by the pri-

# soner.

# Joshua Brookes, dealer in birds, not a free-
# holder.

# Thomas Lawrence, esq. not a freeholder.


# Thomas Skipp Dyott Bucknell, esq. ehalleng-
# _ ed by the prisoner.
# Jobn Blackburn, esq. challenged by the pri-
# soner.
# Samuel Mills, weaver.

# Mr. Miils — My father left in his will alt
# his estate to my brother and me, and a
# pointed trustees, and we are not by the will,
# to be of age till we are thirty-five,

# Joseph Bird, esq. not a freeholder of Middle-

# sex,

# Thomas Powell, esq. challenged by the priv
# soner.

# William Emerson, esq. not a fteeholder.

# James Cook, esq. not a freeholder.

# Nathaniel Stonard, brewer, sworn.

# Joseph Mawley, gent. nota freeholder.

# Thomas Allen, brewer, challenged by the pri-
# soner.

# John Baker, esq. challenged by the prisoner.

# William Row, esq. not a trecholder.

# James Smith, esq. challenged by the prisoner.

# Bryan Marshall, gent. challenged by the pri-
# soner.

# Joseph Nicoll, gentleman farmer, sworn.

# Thomas Bird, distiller, uot @ freeholder.

# Robert Vincent, esq. not a freeholder.

# David Roberts, esq. challenged by the priv
# soner.

# George Brooks, esq. not a freehulder.

# William Arnold, esq. not a freeholder,

# Thomas Nixon, esq. not a freeholder.

# Thomas Smith, esq. challenged by the pri-
# soner.

# John Charrington, esq. sworn.

# George Rigby, esq. not a freeholder.

# Thomas Allen, esq. challenged by the pri-
# soner.

# Andrew Burt, esq. challenged by the crown.

# Charles Smith, distiller, challenged by the
# prisoner.

# Archibald Paxton, wine merchant, challenged
# by the prisoner.

# Ralph Keddy, esq. not a freeholder.

# John Harsley, esq. not a freeholder.

# William Nicoll, farmer, challenged by the

# risoner.

# ward Franklin, farmer excused on account
# of illness.

# Michael Henley, coal merchant, challenged by
# the prisoner.

# John Thompson, brewer, challenged by the
# prisoner.

# Joseph Ainslie, esq. sworn.

# THE JURY.
# Thomas Buck, Thomas Sayer,
# Thomas Wood, Richard Carter,
# William Fraser, Nathaniel Stonard,
# Adam Steinmetz, Joseph Nichol, @

# Newell Connop, John Charrington,
# John Mercer, Joseph Ainslie."""

# ]

# # Opening new file for post passage deletion output
# with open("cleaned_with_Regex.txt", 'r', encoding='utf-8') as file:
#     original_text = file.read()

# processed_text = remove_specific_passages(original_text, passages_to_remove)

# with open("passage_deletion_test.txt", 'w', encoding='utf-8') as file:
#     file.write(processed_text)


print("     /✓\        PASSAGE DELETION COMPLETE")

