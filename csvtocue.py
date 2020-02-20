import sys
import os
from os import path

# Export Settings
inputfile = "markers.csv"
outputfile = "markers.cue"
podcastgenre = "Podcast"
podcastcomment = "Created by CSVtoCUE by Dmitriy Zombak (Zavtracast)"
podcastperformer = "Podcast Name"
podcastdate = "2020"
podcasttitle = "Podcast Episode Title"
podcastfilename = "filename.mp3"

########################################################################################################################
#                              DO NOT TOUCH EVERYTHING BELOW THAT LINE
########################################################################################################################

# Open file
if path.exists(inputfile):
    print("Open file", inputfile, "to read")

    # With the open file we do this
    with open(inputfile) as f:
        # Read it line by line (and remove first symbol)
        array = [line.rstrip('\n') for line in f]

        # Delete first row (there is no need for this row)
        del array[0]

        # Count lines in file
        length = len(array)
        print("Found", length, "lines\n")

        # When we open a reading file, we also need a writing file
        with open(outputfile, 'w') as filetowrite:
            # Let's put a headers down there (tabs and spaces are important here!)
            firstcontent = """REM GENRE %s
REM DATE %s
REM COMMENT \"%s\"
PERFORMER \"%s\"
TITLE \"%s\"
FILE \"%s\"""" % (podcastgenre, podcastdate, podcastcomment, podcastperformer, podcasttitle, podcastfilename)
            filetowrite.write(firstcontent)

            # We created a list for every single line
            for linenumber, oneline in enumerate(array):
                # Split it by tabs
                newline = oneline.split("\t")
                # Get rid if milliseconds (no need of them) and convert time
                timearray = newline[1].split(".")
                time = timearray[0]
                # Oh, there is a fine chapter name
                chaptername = newline[0]
                # Get some linenumber and if it below 10, to format it with leading zero
                linenumber = linenumber+1
                if(linenumber<10):
                    linenumber = '%0*d' % (2, linenumber)
                # Let's write chapters in file (tabs and spacec are important here!)
                maincontent = """\n    TRACK %s AUDIO\n        TITLE \"%s\"\n        PERFORMER \"%s\"\n        INDEX 01 %s""" % (linenumber, chaptername, podcastperformer, time)
                filetowrite.write(maincontent)

        print("Everything done. Results are in output file", outputfile, "\n")

else:
    print("File", inputfile, "not found! Please double check the export settings!\n")
