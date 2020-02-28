import sys
import os
from os import path

# Export Settings
inputfile = "markers.csv"
outputfile = "markers.cue"
podcastfilename = "file.mp3"
podcastperformer = "Podcast Name"
podcastdate = "2020"
podcasttitle = "Episode Title"

########################################################################################################################
#                              DO NOT TOUCH EVERYTHING BELOW THAT LINE
########################################################################################################################

# Function to convert timestamps
# If time markers is in hours, then convert hours:minutes:secs to minutes:secs and return a converted string
def convertTime(time):
    time = time.split(":")
    timearraylenght = len(time)
    if(timearraylenght>2):
        time[0]=int(time[0])*60
        time[0]=int(time[0])+int(time[1])
        del time[1]
        time[0] = str(time[0])
        time[1] = str(time[1])
        s = ":"
        s = s.join(time)
        time = s
    else:
        time[0] = str(time[0])
        time[1] = str(time[1])
        s = ":"
        s = s.join(time)
        time = s
    return time

# Open file
if path.exists(inputfile):
    print("Open file", inputfile, "to read")

    # With the open file we do this
    with open(inputfile, mode='r', encoding='utf-8') as f:
        # Read it line by line (and remove first symbol)
        array = [line.rstrip('\n') for line in f]

        # Delete first row (there is no need for this row)
        del array[0]

        length = len(array)
        print("Found", length, "lines\n")

        # When we open a reading file, we also need a writing file
        with open(outputfile, mode='w', encoding='utf-8') as filetowrite:
            # Let's put a headers down there (tabs and spaces are important here!)
            podcastgenre = "Podcast"
            podcastcomment = "Created by CSVtoCUE by Dmitriy Zombak (Zavtracast)"
            firstcontent = """REM GENRE %s
REM DATE %s
REM COMMENT \"%s\"
PERFORMER \"%s\"
TITLE \"%s\"
FILE \"%s\"""" % (podcastgenre, podcastdate, podcastcomment, podcastperformer, podcasttitle, podcastfilename)
            filetowrite.write(firstcontent)

            # We created a list for every single line
            for linenumber, oneline in enumerate(array):
                newline = oneline.split("\t")
                # Get rid if milliseconds (no need of them) and convert time
                timearray = newline[1].split(".")
                time = timearray[0]
                newtime = convertTime(time)
                chaptername = newline[0]
                # Get some linenumber and if it below 10, to format it with leading zero
                linenumber = linenumber+1
                if(linenumber<10):
                    linenumber = '%0*d' % (2, linenumber)
                # Let's write chapters in file (tabs and spacec are important here!)
                maincontent = """\n    TRACK %s AUDIO\n        TITLE \"%s\"\n        PERFORMER \"%s\"\n        INDEX 01 %s""" % (linenumber, chaptername, podcastperformer, newtime)
                filetowrite.write(maincontent)

        print("Everything done. Results are in output file", outputfile, "\n")

else:
    print("File", inputfile, "not found! Please double check the export settings!\n")