import re
import os
import glob


DefenceCounselSpeakers = ["ERSKINE", 
                        "GIBBS", 
                        "DAMPIER", 
                        "VAUGHAN", 
                        "GURNEY"]

ProsecutionSpeakers = ["EYRE", 
                        "MACDONALD", 
                        "HOTHAM", 
                        "GROSE", 
                        "ATTORNEYGENERAL", 
                        "SOLICITORGENERAL", 
                        "ADAIR", 
                        "BEARCROFT", 
                        "BOWER", 
                        "LAW", 
                        "GARROW", 
                        "WOOD", 
                        "WHITE", ]

# Path where the .txt files are located
path = 'separated_speakers/*.txt'

# Using glob to find all .txt files
txt_files = glob.glob(path)

# Loop through the list of .txt file paths
for file_path in txt_files:
    os.remove(file_path)  # Or perform any file operations

input_file = "data_for_MALLET_ENTIRE_TRIAL.txt"
defence_filename = "data_for_MALLET_DEFENCE_SPEAKERS.txt"
defence_text = []
pros_filename = "data_for_MALLET_PROS_SPEAKERS.txt"
pros_text = []

speaker_IDs = []
output_files = dict()

file = open(input_file, "r")
lines = file.readlines()
for line in lines:
    # extract the speaker ID
    pattern = r"(\b[A-Z]+_*[A-Z]+\b)\s"
    match = re.search(pattern, line)
    if match:
        current_speaker = line[match.start(): match.end()-1]
        #bulk_text = str(line[match.end():])
        #bulk_text = bulk_text.replace("\n","")
        #print(bulk_text)
        if current_speaker in speaker_IDs:
            pass
        else:
            speaker_IDs += [current_speaker]
            output_files.update({current_speaker : [str(current_speaker)+".txt",[]]})
        output_files[current_speaker][1] += [line]
        # extract the speaker tag
        # extract the speech content
        # if the speaker is new, add them to the speaker_IDs list
        # assign the text to each speaker+

        #? Creating the defence text list (AKA to make a model for the entire defence camp)
        if current_speaker in DefenceCounselSpeakers:
            defence_text += [line]
        #? Same for prosecution
        if current_speaker in ProsecutionSpeakers:
            pros_text += [line]
    else:
        break


for speaker in speaker_IDs:
    index = 0
    out_filename = output_files[speaker][0]
    save_file = open("separated_speakers/"+out_filename,"w")
    for line in output_files[speaker][1]:
        line = str(line)
        save_file.write(line)

# defence file save 
def_file = open("separated_speakers/"+defence_filename,"w")
for line in defence_text:
    def_file.write(str(line))

# pros file save 
def_file = open("separated_speakers/"+pros_filename,"w")
for line in pros_text:
    def_file.write(str(line))





