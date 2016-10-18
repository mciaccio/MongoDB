#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"areaLand" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint
import os 

# 39 total
 
# CITIES = 'cities.csv'

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "cities.csv"
CITIES = os.path.join(DATADIR, DATAFILE)

def fix_name(name):
    # print("\n\tBegin fix_area function")
    
    # tempName = ''
    myTempNameList = []
    
        
    if name == 'NULL':   
        # print("\t\tname - {}, myTempNameList - {}".format(name, myTempNameList))
        # return 'apple'
        return myTempNameList
    
    elif name[0] == '{' :
        tempName = name[1:-1]
        # print("46\t\tname - {}, tempName - {}".format(name, tempName))
        mySplitList = tempName.split('|')
        # print("\t\t\tname - {}, tempName - {}, mySplitList - {}".format(name, tempName, mySplitList))
        return mySplitList
    
    else:
        myTempNameList.append(name)
        # print("\t\tname - {}, myTempNameList - {}".format(name, myTempNameList))

        return myTempNameList
    
    # YOUR CODE HERE

def process_name(filename):
    print("\n\tBegin process_file function")
    
    # MGC
    totalRowCount = 0 
    # MGC
    
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        # print("\t\theader - {}".format(header))

        for i, row in enumerate(reader):
            if i > 2 :
                totalRowCount += 1
                
                formatted_name = fix_name(row["name"])
                row['name'] = formatted_name

                # print("\t\tformatted_name\t - {}".format(formatted_name))
                
                data.append(row) 
                
        print("\t\tEnd row for loop")
                        
    print("\tEnd process_file function")

    return data


def test():
    data = process_name(CITIES)

    print ("\nPrinting 20 results:")
    
    
    print("\t\tdata[14] - {}".format(data[14]['name']))
    print("\t\tdata[18] - {}".format(data[18]['name']))
    print("\t\tdata[9] - {}".format(data[9]['name']))
    print("\t\tdata[3] - {}".format(data[3]['name']))

    # for n in range(20):
        # pprint.pprint(data[n]["name"])

    assert data[14]["name"] == ['Negtemiut', 'Nightmute']
    assert data[9]["name"] == ['Pell City Alabama']
    assert data[3]["name"] == ['Kumhari'] 

if __name__ == "__main__":
    test()
    