
import os
import sys
import csv
import pprint

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "BeatlesDiscography.csv"


def parse_csv(datafile):
    print("\tBegin parse_csv Function")
    data = []
    
    with open (datafile) as csvFileBuffer:
        print("\tcsvFileBuffer class is {}".format(csvFileBuffer.__class__.__name__)) # BufferedReader
        dictReader = csv.DictReader(csvFileBuffer)
        print("\tdictReader class is {}".format(dictReader.__class__.__name__)) # DictReader
        
        for csvMusicDataLine in dictReader:
            #print("\t{}".format(csvMusicDataLine.__class__.__name__)) # dict
            #print("\tcsvMusicDataLine class is {}".format(csvMusicDataLine.__class__.__name__)) # dict
            #print("\tcsvMusicDataLine is {}".format(csvMusicDataLine)) # dict
            
            data.append(csvMusicDataLine)
            
            # print("\tdata class name is {}".format(data.__class__.__name__)) # list

        return data 
        
    print("\tEnd parse_csv Function")

print("Begin Python Module")
print (sys.version)

datafile = os.path.join (DATADIR, DATAFILE)

d = parse_csv(datafile)
print("\td is {}".format(d.__class__.__name__)) # list
print("\td is {}".format(d))
pprint.pprint(d)

print("End Python Module")
