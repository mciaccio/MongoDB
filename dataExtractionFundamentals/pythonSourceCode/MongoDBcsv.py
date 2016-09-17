#!/usr/bin/env python3.5

import os
import sys 
import csv

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "BeatlesDiscography.csv"
RECNO = 0

def myFunction():
    print('\tBegin myFunction')
    print('\tEnd myFunction\n')
    
def myParse_file(func_dataFile):
    print ('.')
    print('\tBegin myParse_file\n')
    #print ('\t\tdatafile is: %s.' % func_dataFile)
    #print(func_dataFile)
    with open(func_dataFile, "rb") as f:  
        for line in f:
            print("%r" % line)
    print('\n\tEnd myParse_file\n')

def myParse_file1(func_dataFile1):
    print('\tBegin myParse_file1\n')
    RECNO = 0
    
    with open(func_dataFile1) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(RECNO)
            print(row)
            RECNO += 1
            if RECNO > 9: break 
        
    print('\n\tEnd myParse_file1\n')

def myTest():
    print('\tBegin myTest')
    # print(datafile)
    print('\tEnd myTest\n')

print('\nBegin Python Module')
print (sys.version)

datafile = os.path.join(DATADIR,DATAFILE)

myParse_file1(datafile)

print('End Python Module')
