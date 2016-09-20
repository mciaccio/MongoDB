# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import sys

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    RECNO = 0
    data = []
    
    with open(datafile, "r") as f:
        print("Working on the header line")
        headerLine = f.readline()
        print("headerLine ->{}".format(headerLine.strip()))
        # split returns a list
        headerFields = headerLine.strip().split(",")
        #headerFields = headerLine.split(",")
        print("headerFields ->{}".format(headerFields))

        for musicDataLine in f:
            #initialize new musicDataDictionary for this music data line  
            musicDataDictionary = {}
            FIELDNO = 0

            RECNO += 1
            print("\n\tMusic data record number is {}, music data is\t{}".format(RECNO,musicDataLine.strip()))
            
            musicDataFields = musicDataLine.split(",")
            
            #iterate through the list, enumerate the list 
            for fieldNumber, musicFieldData in enumerate (musicDataFields):
                # print("\tfieldNumber ->\t\t\t\t\t{}".format(fieldNumber))
                # print("\theaderFields[{}] ->\t\t\t\t{}".format(fieldNumber, headerFields[fieldNumber].strip()))
                print("\tfieldNumber -> {}, musicFieldData ->\t\t{}".format(fieldNumber, musicFieldData.strip()))
                
                #populate the musicDataDictionary for this music data line
                musicDataDictionary[headerFields[fieldNumber]] = musicFieldData.strip()
                if FIELDNO == 6:
                    print("\tmusicDataDictionary ->\t\t\t{}".format(musicDataDictionary))
                    
                FIELDNO += 1

            data.append(musicDataDictionary)
            if RECNO == 14:
                break

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
        
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    # order of key: value pairs did not impact assert test for equality
    assert d[0] == firstline
    assert d[9] == tenthline

print (sys.version)
test()
