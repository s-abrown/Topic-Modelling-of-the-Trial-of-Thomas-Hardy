import re

# For sample data
#input_filename = 'Speech_extractor_Sample_Longer.txt' 
#output_filename = 'Extracted_Speech_Sample_Longer.txt'

# For actual data
input_filename = 'cleaned_with_Regex.txt' 
output_filename = 'data_for_MALLET_ENTIRE_TRIAL.txt'

WriteArray = []
#? Define the list of speakers
speakers = ["Lord Chief Justice Eyre", 
            "Lord Chief Baron Macdonald", 
            "Mr. Baron Hotham", 
            "Mr. Justice Buller", 
            "Mr. Justice Grose", 
            "Mr. Attorney General", 
            "Mr. Solicitor General", 
            "Mr. Serjeant Adair", 
            "Mr. Adair", 
            "Mr. Bearcroft", 
            "Mr. Bower", 
            "Mr. Law", 
            "Mr. Garrow", 
            "Mr. Wood", 
            "Mr. White", 
            "Mr. Erskine", 
            "Mr. Gibbs", 
            "Mr. Dampier", 
            "Mr. Felix Vaughan", 
            "Mr. Vaughan", 
            "Mr. Gurney", 
            "Clerk of the Arraigns", 
            "Mr. Shelton", 
            "Mr. Thomas Shelton", 
            "Foreman", 
            "Mr. Sheriff Eamer", 
            "Mr. Alderman Newman", 
            "One of the Jury",
            "Thomas Hardy",
            "Mr. Hardy",
            "Prisoner"
            ]

# Format: Mr. Firstname Lastname | Mr. Lastname | Firstname Lastname
witnesses = ["Mr. Alexander Gordon", 
             "Mr. Gordon", 
             "Alexander Gordon", 
            "Mr. Alexander Wills", 
            "Mr. Wills", 
            "Alexander Wills", 
            "Mr. Alexander Grant", 
            "Mr. Grant", 
            "Alexander Grant", 
            "Mr. Alexander Gregg", 
            "Mr. Gregg", 
            "Alexander Gregg", 
            "Mr. Alexander Fraser", 
            "Mr. Fraser", 
            "Alexander Fraser", 
            "Mr. Andrew Stirling", 
            "Mr. Stirling", 
            "Andrew Stirling", 
            "Mrs. Ann Evans", 
            "Mrs. Evans", 
            "Ann Evans", 
            "Mr. Archibald Hunter", 
            "Mr. Hunter", 
            "Archibald Hunter", 
            "Mr. Arthur McEwan", 
            "Mr. McEwan", 
            "Arthur McEwan", 
            "Mr. Charles Schaw", 
            "Mr. Shaw", 
            "Charles Schaw", 
            "Mr. Daniel Stuart", 
            "Mr. Stuart", 
            "Daniel Stuart", 
            "Mr. David Martin", 
            "Mr. Martin", 
            "David Martin", 
            "Mr. Edward Gosling", 
            "Mr. Gosling", 
            "Edward Gosling", 
            "Mr. Edward Hodson", 
            "Mr. Hodson", 
            "Edward Hodson", 
            "Mr. Edward Lauzun", 
            "Mr. Lauzun", 
            "Edward Lauzun", 
            "Mr. Edward Oakes", 
            "Mr. Oakes", 
            "Edward Oakes", 
            "Mr. Edward Smith", 
            "Mr. Smith", 
            "Edward Smith", 
            "Mr. Evan Evans", 
            "Mr. Evans", 
            "Evan Evans", 
            "Mr. Florimond Goddard", 
            "Mr. Goddard", 
            "Florimond Goddard", 
            "Mr. Francis Dowling", 
            "Mr. Dowling",
            "Francis Dowling", 
            "Mr. Frederic Polydore Nodder", 
            "Mr. Nodder", 
            "Frederic Polydore Nodder", 
            "Frederic Nodder", 
            "Mr. George Lynam", 
            "Mr. Lynam", 
            "George Lynam", 
            "Mr. George Ross", 
            "Mr. Ross", 
            "George Ross", 
            "Mr. George Sanderson", 
            "Mr. Sanderson", 
            "George Sanderson", 
            "Mr. George Widdison", 
            "Mr. Widdison",
            "George Widdison",  
            "Mr. Henry Alexander", 
            "Mr. Alexander", 
            "Henry Alexander", 
            "Mr. Henry Hill", 
            "Mr. Hill", 
            "Henry Hill", 
            "His Grace the Duke of Richmond", 
            #Doesn't seem to be any other variations for the Duke of Richmond
            "Mr. James Clerk", 
            "Mr. Clerk", 
            "James Clerk", 
            "Mr. James Davidson", 
            "Mr. Davidson", 
            "James Davidson", 
            "Mr. James Hardy", 
            #"Mr. Hardy", 
            "James Hardy", 
            "Mr. James Thornton", 
            "Mr. Thornton", 
            "James Thornton", 
            "Mr. James Walsh", 
            "Mr. Walsh", 
            "James Walsh", 
            "Mrs. Jane Rickman", 
            "Mrs. Rickman", 
            "Jane Rickman", 
            "Mr. Jeremiah Samuel Jordan", 
            "Mr. Samuel Jordan", 
            "Mr. Jordan", 
            "Jeremiah Samuel Jordan", 
            "Samuel Jordan", 
            "Mr. John Bogue", 
            "Mr. Bogue",
            "John Bogue",  
            "Mr. John Carr", 
            "Mr. Carr", 
            "John Carr", 
            "Mr. John Coates", 
            "Mr. Coates", 
            "John Coates", 
            "Mr. John Edwards", 
            "Mr. Edwards", 
            "John Edwards", 
            "Mr. John Gurnell", 
            "Mr. Gurnell", 
            "John Gurnell", 
            "John King, esq.", 
            "Mr. King", 
            "John King", 
            "Mr. John Nost", 
            "Mr. Nost", 
            "John Nost", 
            "Mr. John Stevenson", 
            "Mr. Stevenson", 
            "John Stevenson", 
            "Mr. John Thompson", 
            "Mr. Thompson", 
            "John Thompson", 
            "Mr. Joseph Strutt", 
            "Mr. Strutt", 
            "Joseph Strutt", 
            "Mr. Joseph Deboffe", 
            "Mr. Deboffe", 
            "Joseph Deboffe", 
            "Mr. Matthew Dickey", 
            "Mr. Dickey", 
            "Matthew Dickey", 
            "Mr. Bernard Bailey", 
            "Mr. Bailey", 
            "Bernard Bailey", 
            "Mr. Daniel Adams", 
            "Mr. Adams", 
            "Daniel Adams", 
            "Mr. Joseph Johnson", 
            "Mr. Johnson",
            "Joseph Johnson",  
            "Mr. Thomas Maclean", 
            "Mr. Maclean", 
            "Thomas Maclean", 
            "Mr. William Lockhart", 
            "Mr. Lockhart", 
            "William Lockhart", 
            "Mr. William Tims", 
            "Mr. Tims", 
            "William Tims", 
            "Mr. William Walker", 
            "Mr. Walker", 
            "William Walker", 
            "Mr. William Woodfall", 
            "Mr. Woodfall", 
            "William Woodfall", 
            "Mr. Peter Macbean", 
            "Mr. Macbean", 
            "Peter Macbean", 
            "Mr. Philip Francis", 
            "Mr. Francis", 
            "Philip Francis", 
            "Mr. Richard Brindsley Sheridan", 
            "Mr. Brindsley Sheridan", 
            "Mr. Sheridan", 
            "Richard Brindsley Sheridan", 
            "Mr. Robert Ferguson", 
            "Mr.Ferguson", 
            "Robert Ferguson", 
            "Mr. Robert Moody", 
            "Mr. Moody", 
            "Robert Moody", 
            "Mr. Samuel Williams", 
            "Mr. Williams", #! DOES THIS MATTER
            "Samuel Williams", 
            "The Rev. Richard Williams", 
            "Mr. Williams", #! DOES THIS MATTER
            "Richard Williams", 
            "Earl of Lauderdale", 
            # Doesn't seem to be any variations on the Earl of Lauderdale
            "The rev. Thomas Oliver", 
            "Mr. Oliver", 
            "Thomas Oliver", 
            "Mr. Thomas Chapman", 
            "Mr. Chapman", 
            "Thomas Chapman", 
            "Mr. Thomas Clio Rickman", 
            "Clio Rickman", 
            "Mr. Rickman", 
            "Mr. Thomas Green", 
            "Mr. Green", 
            "Thomas Green", 
            "Mr. Thomas Tourll", 
            "Mr. Tourll", 
            "Thomas Tourll", 
            "Mr. Thomas Whitehorn", 
            "Mr. Whitehorn", 
            "Thomas Whitehorn", 
            "Mr. Thomas Wood", 
            "Mr. Wood", #! DOES THIS MATTER
            "Thomas Wood", 
            "Mr. William Barclay", 
            "Mr. Barclay", 
            "William Barclay", 
            "Mr. William Broomhead", 
            "Mr. Broomhead", 
            "William Broomhead", 
            "Mr. William Dewsnap", 
            "Mr. Dewsnap", 
            "William Dewsnap", 
            "Mr. William Henderson", 
            "Mr. Henderson", 
            "William Henderson", 
            "Mr. William Huskisson", 
            "Mr. Huskisson", 
            "Mr. William Middleton", 
            "Mr. Middleton", 
            "William Middleton", 
            "Mr. William Scott",
            "Mr. Scott", 
            "William Scott"
            ]

#? adding witnesses on the end of the speakers list...
#! ... to get a megalist of speakers + witnesses
speakers += witnesses

current_speaker = "UNKNOWN"
current_witness = "UNKNOWN_WITNESS"
tag_number = 1
extracted_speech = ""
paragraph = ""
paragraphs = []

#? Defining a speaker dictionary a.k.a. Lookup table. [ID] for MALLET are store on the right of the col
#? This dict will contain BOTH main speakers AND witnesses
speaker_dict = {"Lord Chief Justice Eyre": "EYRE", 
                "Lord Chief Baron Macdonald": "MACDONALD", 
                "Mr. Baron Hotham": "HOTHAM", 
                "Mr. Justice Buller": "BULLER", 
                "Mr. Justice Grose": "GROSE", 
                "Mr. Attorney General": "ATTORNEYGENERAL", 
                "Mr. Solicitor General": "SOLICITORGENERAL", 
                "Mr. Serjeant Adair": "ADAIR", 
                "Mr. Adair": "ADAIR", 
                "Mr. Bearcroft": "BEARCROFT", 
                "Mr. Bower": "BOWER", 
                "Mr. Law": "LAW", 
                "Mr. Garrow": "GARROW", 
                "Mr. Wood": "WOOD", 
                "Mr. White": "WHITE", 
                "Mr. Erskine": "ERSKINE", 
                "Mr. Gibbs": "GIBBS", 
                "Mr. Dampier": "DAMPIER", 
                "Mr. Felix Vaughan": "VAUGHAN", 
                "Mr. Vaughan": "VAUGHAN", 
                "Mr. Gurney": "GURNEY", 
                "Clerk of the Arraigns": "ARRAIGNSCLERK", 
                "Mr. Thomas Shelton": "ARRAIGNSCLERK", 
                "Mr. Shelton": "ARRAIGNSCLERK",
                "Foreman": "FOREMAN", 
                "Mr. Sheriff Eamer": "EAMER", 
                "Mr. Alderman Newman": "NEWMAN", 
                "One of the Jury": "JURYMEMBER", 
                "Thomas Hardy": "THOMAS_HARDY",
                "Mr. Hardy": "THOMAS_HARDY",
                "Prisoner": "THOMAS_HARDY",
                #? Witnesses
                "Alexander Gordon": "GORDON", 
                "Mr. Gordon": "GORDON", 
                "Alexander Wills": "WILLS", 
                "Mr. Wills": "WILLS", 
                "Alexander Grant": "GRANT", 
                "Mr. Grant": "GRANT", 
                "Alexander Gregg": "GREGG", 
                "Mr. Gregg": "GREGG", 
                "Alexander Fraser": "FRASER", 
                "Mr. Fraser": "FRASER", 
                "Mr. Andrew Stirling": "STIRLING", 
                "Andrew Stirling": "STIRLING", 
                "Mr. Stirling": "STIRLING", 
                "Ann Evans": "MRS_EVANS", 
                "Mrs. Evans": "MRS_EVANS", 
                "Archibald Hunter": "HUNTER", 
                "Mr. Hunter": "HUNTER", 
                "Arthur McEwan": "MCEWAN", 
                "Mr. McEwan": "MCEWAN", 
                "Charles Schaw": "SCHAW", 
                "Mr. Shaw": "SCHAW", 
                "Daniel Stuart": "STUART", 
                "Mr. Daniel Stuart": "STUART", 
                "Mr. Stuart": "STUART", 
                "David Martin": "MARTIN", 
                "Mr. Martin": "MARTIN", 
                "Edward Gosling": "GOSLING", 
                "Mr. Gosling": "GOSLING", 
                "Edward Hodson": "HODSON", 
                "Mr. Hodson": "HODSON", 
                "Mr. Edward Lauzun": "LAUZUN", 
                "Edward Lauzun": "LAUZUN", 
                "Mr. Lauzun": "LAUZUN", 
                "Edward Oakes": "OAKES", 
                "Mr. Oakes": "OAKES", 
                "Edward Smith": "SMITH", 
                "Mr. Smith": "SMITH", 
                "Evan Evans": "MR_EVANS", 
                "Mr. Evans": "MR_EVANS", 
                "Florimond Goddard": "GODDARD", 
                "Mr. Goddard": "GODDARD", 
                "Francis Dowling": "DOWLING", 
                "Mr. Dowling": "DOWLING", 
                "Frederic Polydore Nodder": "NODDER", 
                "Mr. Nodder": "NODDER", 
                "George Lynam": "LYNAM", 
                "Mr. Lynam": "LYNAM", 
                "George Ross": "ROSS", 
                "Mr. Ross": "ROSS", 
                "George Sanderson": "SANDERSON", 
                "Mr. Sanderson": "SANDERSON", 
                "George Widdison": "WIDDISON", 
                "Mr. Widdison": "WIDDISON", 
                "Henry Alexander": "ALEXANDER", 
                "Mr. Alexander": "ALEXANDER", 
                "Henry Hill": "HILL", 
                "Mr. Hill": "HILL", 
                "His Grace the Duke of Richmond": "DUKEOFRICHMOND", 
                "James Clerk": "CLERK", 
                "Mr. Clerk": "CLERK", 
                "James Davidson": "DAVIDSON", 
                "Mr. Davidson": "DAVIDSON", 
                "James Hardy": "JAMES_HARDY", 
                "Mr. James Hardy": "JAMES_HARDY", 
                "James Thornton": "THORNTON", 
                "Mr. Thornton": "THORNTON", 
                "James Walsh": "WALSH", 
                "Mr. James Walsh": "WALSH",
                "Mr. Walsh": "WALSH", 
                "Jane Rickman": "MRS_RICKMAN", 
                "Mrs. Rickman": "MRS_RICKMAN", 
                "Jeremiah Samuel Jordan": "JORDAN", 
                "Mr. Samuel Jordan": "JORDAN", 
                "Mr. Jordan": "JORDAN", 
                "John Bogue": "BOGUE", 
                "Mr. Bogue": "BOGUE", 
                "John Carr": "CARR", 
                "Mr. Carr": "CARR", 
                "John Coates": "COATES", 
                "Mr. Coates": "COATES", 
                "John Edwards": "EDWARDS", 
                "Mr. Edwards": "EDWARDS", 
                'Mr. John Gurnell': "GURNELL", 
                "John Gurnell": "GURNELL", 
                "Mr. Gurnell": "GURNELL", 
                "John King, esq.": "KING", 
                "Mr. King": "KING", 
                "John Nost": "NOST", 
                "Mr. Nost": "NOST", 
                "John Stevenson": "STEVENSON", 
                "Mr. Stevenson": "STEVENSON", 
                "John Thompson": "THOMPSON", 
                "Mr. Thompson": "THOMPSON", 
                "Joseph Strutt": "STRUTT", 
                "Mr. Strutt": "STRUTT", 
                "Juseph Deboffe": "DEBOFFE", 
                "Mr. Deboffe": "DEBOFFE", 
                "Matthew Dickey": "DICKEY", 
                "Mr. Dickey": "DICKEY", 
                "Mr. Bernard Bailey": "BAILEY", 
                "Mr. Bailey": "BAILEY", 
                "Bernard Bailey": "BAILEY", 
                "Mr. Daniel Adams": "ADAMS", 
                "Mr. Adams": "ADAMS", 
                "Mr. Joseph Johnson": "JOHNSON", 
                "Mr. Johnson": "JOHNSON", 
                "Mr. Thomas Maclean": "MACLEAN", 
                "Mr. Maclean": "MACLEAN", 
                "Thomas Maclean": "MACLEAN", 
                "Mr. William Lockhart": "LOCKHART", 
                "Mr. Lockhart": "LOCKHART", 
                "Mr. William Tims": "TIMS", 
                "Mr. Tims": "TIMS", 
                "Mr. William Walker": "WALKER", 
                "Mr. Walker": "WALKER", 
                "Mr. William Woodfall": "WOODFALL", 
                "Mr. Woodfall": "WOODFALL", 
                "William Woodfall": "WOODFALL", 
                "Peter Macbean": "MACBEAN", 
                "Mr. Macbean": "MACBEAN", 
                "Philip Francis": "FRANCIS", 
                "Mr. Francis": "FRANCIS", 
                "Richard Brindsley Sheridan": "SHERIDAN", 
                "Mr. Sheridan": "SHERIDAN", 
                "Robert Ferguson": "FERGUSON", 
                "Mr.Ferguson": "FERGUSON", 
                "Robert Moody": "MOODY", 
                "Mr. Moody": "MOODY", 
                "Samuel Williams": "SAMUEL_WILLIAMS", 
                "Mr. Williams": "SAMUEL_WILLIAMS", 
                "The Rev. Richard Williams": "REV_WILLIAMS", 
                "Mr. Williams": "REV_WILLIAMS", 
                "Earl of Lauderdale": "LAUDERDALE", 
                "The rev. Thomas Oliver": "OLIVER", 
                "Mr. Oliver": "OLIVER", 
                "Thomas Oliver": "OLIVER", 
                "Thomas Chapman": "CHAPMAN", 
                "Mr. Chapman": "CHAPMAN", 
                "Thomas Clio Rickman": "MR_RICKMAN", 
                "Clio Rickman": "MR_RICKMAN", 
                "Mr. Rickman": "MR_RICKMAN", 
                "Thomas Green": "GREEN", 
                "Mr. Green": "GREEN", 
                "Thomas Tourll": "THOURLL", 
                "Mr. Tourll": "THOURLL", 
                "Thomas Whitehorn": "WHITEHORN", 
                "Mr. Whitehorn": "WHITEHORN", 
                "Thomas Wood": "THOMAS_WOOD", 
                # No entry for "Mr. Wood" because every insance of it refers to counsel for the crown Mr. Wood
                "William Barclay": "BARCLAY", 
                "Mr. Barclay": "BARCLAY", 
                "William Broomhead": "BROOMHEAD", 
                "Mr. Broomhead": "BROOMHEAD", 
                "William Dewsnap": "DEWSNAP", 
                "Mr. Dewsnap": "DEWSNAP", 
                "William Henderson": "HENDERSON", 
                "Mr. Henderson": "HENDERSON", 
                "William Huskisson": "HUSKISSON", 
                "Mr. Huskisson": "HUSKISSON", 
                "William Middleton": "MIDDLETON", 
                "Mr. Middleton": "MIDDLETON", 
                "Mr. William Scott": "SCOTT",
                "Mr. Scott": "SCOTT",
                "William Scott": "SCOTT"
            }

#? Making a function to detect/identify speakers
def speakerIdentifier(paragraph, speakers, speaker_dict):
    for speaker in speakers:
        #? Define the regex pattern which will allow to extract the text which follows "Mr. SPEAKER.—" up to BUT NOT INCLUDING responses given signaled with a — (em dash) + All cap word.
        pattern_template = speaker+r"\.—"
        match = re.search(pattern_template, paragraph)
        if match:
            # return speaker/who it is, and the text content/speech content
            return [speaker_dict[speaker], paragraph[match.end():]]
    # If gets this far none of speakers have matched, which means that the previous speaker is still speaking (no anchors to signal new speaker)
    return ["PREVIOUS_SPEAKER", paragraph]

#? Making a function to detect/identify witnesses
def witnessIdentifier(paragraph, speakers, speaker_dict):
    pattern_template = "examined\sby\sMr\.\s" #! check
    match = re.search(pattern_template, paragraph)
    # backupname if we fail to find a witness. IF appears, might be because the witness name does not appear in the dictionary and the witness list above.
    ID_of_speaker = "UNKNOWN_WITNESS"
    if match:
        # text_before_examined = is the text that comes before "(cross|re-)examined by Mr. " which will contained the names of the witnesses being questioned by the speakers.
        text_before_examined = paragraph[:match.start()]
        for speaker in speakers:
            pattern_template2 = speaker
            match2 = re.search(pattern_template2, text_before_examined)
            if match2:
                #if we match match2 we have a witness
                ID_of_speaker = speaker_dict[speaker]
            else:
                # Do nothing
                pass
        return [True, ID_of_speaker]
    else:
        return [False]


#? Making a function to capture the responses given by witnesses to speakers
def responseCapturer(input_list):
    # detect if a response exists
    # note: inputting 1th element of input list, aka the extracted spoken text, which atp still includes the speaker
    text = input_list[1]
    match = re.search("\?—", text)
    # in case need more, populate
    match2 = re.search("\.—", text)
    # If no response: do nothing
    # If response: split the list into 2: one for speaker, one for witness/answer.
    if match:
        before_text = text[:match.start()] # takes from text and takes everything until "start" aka em dash.
        after_text = text[match.end():] # takes from end of the em dash until the end.
        speaker_list = [input_list[0], before_text] # Taking original speaker ID and grouping it with the text before the response (aka only their speech)
        witness_list = ["WITNESS", after_text]
        return [True, speaker_list, witness_list]
    elif match2:
        before_text = text[:match2.start()] # takes from text and takes everything until "start" aka em dash.
        after_text = text[match2.end():] # takes from end of the em dash until the end.
        speaker_list = [input_list[0], before_text] # Taking original speaker ID and grouping it with the text before the response (aka only their speech)
        witness_list = ["WITNESS", after_text]
        return [True, speaker_list, witness_list]
    else :
        return [False, input_list]
    
#? Making a function to deal with instances of "SPEAKER to WITNESS" 
#? We're switchin'
def speakerWitnessSwap(paragraph, speakers):
    SPEAKER = ""
    WITNESS = ""
    for speaker in speakers:
        pattern_template = speaker+r"\.—"
        match = re.search(pattern_template, paragraph)
        if match:
            # means we found a witness being interrogated (& they're the ones with the .— stipulated in the pattern_template)
            WITNESS = speaker
            before_text = paragraph[:match.start()]
            match2 = re.search("\sto\s", before_text)
            if match2:
                for speaker2 in speakers:
                    match3 = re.search(speaker2, before_text)
                    if match3:
                        new_before_text = speaker + " examined by " + speaker2+".—"
                        paragraph = new_before_text + paragraph[match.end():]
                        return paragraph
            else:
                # If we found a speaker but with no matces wit the " to " template
                return paragraph
    return paragraph


    
# Open the input file and read line by line
with open(input_filename, 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        #print(line)
        #? Grouping paragraphs which have been split into separate lines onto one single line.
        if line != "\n":
            #print(line=="\n")
            paragraph += line
        else:
            #print(paragraph)
            paragraph = paragraph.replace("-\n", "")
            paragraph = paragraph.replace("\n", " ")
            paragraph = paragraph.replace("  ", " ")
            paragraphs += [paragraph]
            paragraph = speakerWitnessSwap(paragraph, speakers)
            new_witness_list = witnessIdentifier(paragraph, speakers, speaker_dict)
            output_list = speakerIdentifier(paragraph, speakers, speaker_dict)
            output_list = responseCapturer(output_list)
            #? If statement to check if we have a previous speaker...
            #? if we do have a previous speaker...
            if output_list[1][0] == "PREVIOUS_SPEAKER":
                #? Copy the previous speaker name into the slot of the current speaker
                output_list[1][0] = current_speaker
            else:
                #? If we don't have a previous speaker, it must automatically mean there's a new speaker, being identified here
                #? copy the new speaker into the new variable current speaker
                current_speaker = output_list[1][0]
            # With this template: WriteArray += [[current_speaker + " " + str(tag_number) + " " + content_of_speech]]
            if output_list[0]:
                # if there is a response inside the paragraph being checked:
                # to identify the original speaker
                if output_list[1][1] != "":
                    WriteArray += [[output_list[1][0] + " " + str(tag_number) + " " + output_list[1][1]]]
                    tag_number += 1
                if new_witness_list[0]:
                    current_witness = new_witness_list[1]
                # to identify the witness speaking
                if output_list[2][1] != "":
                    WriteArray += [[current_witness + " " + str(tag_number) + " " + output_list[2][1]]]
                    tag_number += 1
            else:
                # if there is no response inside the paragraph being checked:
                if output_list[1][1] != "":
                    WriteArray += [[output_list[1][0] + " " + str(tag_number) + " " + output_list[1][1]]]
                    tag_number += 1
            # Tag == numbering the speaker so simple + 1
            #print(output_list)
            paragraph = ""
        



# One file, one instance per line:
#testWriteArray = [[ID] [TAG] [TEXT of the instance...]]
#testWriteArray = ["SPEAKERNAME 1 Today the cows went out to pasture.","SPEAKERNAME 2 Today the cows went out to pasture.", "SPEAKERNAME 3 Today the cows went out to pasture.", "SPEAKERNAME 4 Today the cows went out to pasture."]
# Writing the extracted speech into the file for MALLET to read (line by line)
with open(output_filename, 'w') as file:
# filtered_lines_
    for line in WriteArray:
        file.write(line[0]+"\n")
        #print(line)