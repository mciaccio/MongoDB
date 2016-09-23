#!/usr/bin/env python
"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os
#from test.final_a import x

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "745090.csv"


def parse_file(datafile):
    
    print('\n\t\tBegin parse_file function')
    data = []
    
    with open(datafile,'r') as f: 
        
        nrelReader = csv.reader(f)
        
        stationLine = next(nrelReader)
        print('\t\t\tstationLine is {}'.format(stationLine))
        # stationLine.__class__.__name__ is list
        # print('\t\t\tstationLine.__class__.__name__ is {}'.format(stationLine.__class__.__name__))
        
        name = stationLine[1]
        print('\t\t\tname is {}\n'.format(name))
        # name.__class__.__name__ is str
        #print('\t\t\tname.__class__.__name__ is {}'.format(name.__class__.__name__))
        
        next(nrelReader)

        for i in nrelReader:
            #print(i)
            data.append(i)
            print (data)
            print (len(data))
            
        print("\t\t\tdata[0][0] is {}".format(data[0][0]))
        print("\t\t\tdata[0][1] is {}".format(data[2][0]))
        print("\t\t\tdata[1][0] is {}".format(data[2][5]))
         
            
        """
        # print(nrelReader.__sizeof__())

        # csv.reader(datafile).__class__.__name__ is reader
        # print('\t\t\tcsv.reader(datafile).__class__.__name__ is {}'.format(csv.reader(datafile).__class__.__name__))
        """
        
    print('\t\tEnd parse_file function\n')

    # Do not change the line below
    return (name, data)


def test():
    
    print('\n\tBegin test function')

    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    # assert data[0][1] == "01:00"
    # assert data[2][0] == "01/01/2005"
    # assert data[2][5] == "2"
    
    print('\tEnd test function')


print('\nBegin Python Module')
test()
print('End Python Module')



# if __name__ == "__main__":
# test()