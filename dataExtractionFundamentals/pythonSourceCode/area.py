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



def fix_area(area):
    # print("\n\tBegin fix_area function")
    # print("\t\tarea - {}".format(area))
    # print("\t\ttype(area) - {}".format(type(area)))
    # print("\t\tarea.__class__.__name__ - {}".format(area.__class__.__name__)) #str
    
    if area == "NULL": # None
        pass
        # print("\t\tarea - {}".format(area)) # 8 NULL
    else:
        # print("\t\tarea - \t\t\t{}".format(area))
        if area[0] == '{':
            tempArea = area[1:-1]
            mySplitList = tempArea.split('|')
            first = mySplitList[0]
            second = mySplitList[1]
            # print("\t\tfirst - \t{}".format(first))
            # print("\t\tsecond - \t{}\n".format(second))
            if len(first) > len(second):
                return float(first)
            else:
                return float(second)
            
        elif area != "NULL":
            # print("\n\t\tlast else float(area)\t - {}".format(float(area))) # 3.58195e+07, 1.13e+07, 5.32e+07
            return float(area)
            
    # string[1:-1]

        

    
    # print("\tEnd fix_area function")


    # YOUR CODE HERE

    # return area



def process_file(filename):
    print("\n\tBegin process_file function")

    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    
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
                # print("\t\trow - {}".format(row))
                # print("\t\ti - {}, row['areaLand'] - {}".format(i, row['areaLand']))
                formatted_areaLand = fix_area(row["areaLand"])
                # print("\t\tformatted_areaLand\t - {}\n".format(formatted_areaLand))
                
                row['areaLand'] = formatted_areaLand
                
                # print("\t\trow['areaLand']\t - {}".format(row['areaLand']))

                
                data.append(row)


                
        print("\t\tEnd row for loop")
                    
        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                pass
                # line["areaLand"] = fix_area(line["areaLand"])
            # data.append(line)
            
    # print("\t\theader - {}".format(header))
    print("\tEnd process_file function")

    return data


def test():
    data = process_file(CITIES)

    print ("\nPrinting three example results:")
    
    # for n in range(5,8):
        # pprint.pprint(data[n]["areaLand"])

    print('\t\tdata[3]["areaLand"]\t - {}'.format(data[3]["areaLand"]))
    print('\t\tdata[8]["areaLand"]\t - {}'.format(data[8]["areaLand"]))
    print('\t\tdata[20]["areaLand"]\t - {}'.format(data[20]["areaLand"]))
    print('\t\tdata338]["areaLand"]\t - {}'.format(data[33]["areaLand"]))


    assert data[3]["areaLand"] == None
    
    #                               5.51667e+07
    assert data[8]["areaLand"] == 55166700.0 
    
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0    


if __name__ == "__main__":
    test()