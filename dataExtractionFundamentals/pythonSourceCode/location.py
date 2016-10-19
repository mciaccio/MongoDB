#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

If you look at the full city data, you will notice that there are couple of
values that seem to provide the same information in different formats: "point"
seems to be the combination of "wgs84_pos#lat" and "wgs84_pos#long". However,
we do not know if that is the case and should check if they are equivalent.

Finish the function check_loc(). It will recieve 3 strings: first, the combined
value of "point" followed by the separate "wgs84_pos#" values. You have to
extract the lat and long values from the "point" argument and compare them to
the "wgs84_pos# values, returning True or False.

Note that you do not have to fix the values, only determine if they are
consistent. To fix them in this case you would need more information. Feel free
to discuss possible strategies for fixing this on the discussion forum.

The rest of the code is just an example on how this function can be used.
Changes to "process_file" function will not be taken into account for grading.
"""

import os
import csv
import pprint

# CITIES = 'cities.csv'
DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "cities.csv"
CITIES = os.path.join(DATADIR, DATAFILE)


def check_loc(point, lat, longi):
    print("\t\tpoint\t\t- {}".format(point))
    mySplitPoint = point.split(' ')
    
    pointLat = mySplitPoint[0] 
    print("\t\tpointLat\t-> {}, lat\t-> {}".format(pointLat, lat))

    pointLong = mySplitPoint[1] 
    print("\t\tpointLat\t-> {}, longi\t-> {}\n".format(pointLong, longi))
    
    if (pointLat == lat) and (pointLong == longi):
        return True
    else:
        return False
        
    # print("\t\tpoint.__class__.__name__\t- {}".format(point.__class__.__name__)) # str
    # print("\t\tlat\t- {}".format(lat))
    # print("\t\tlongi\t- {}\n".format(longi))

    # YOUR CODE HERE

def process_file(filename):
    
    data = []
    
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        
        for i, row in enumerate(reader):
            if i > 2 :
                
                check_loc(row['point'], row['wgs84_pos#lat'], row['wgs84_pos#long'])
                
    return data


def test():
    data = process_file(CITIES)
    
    # point (33.08 75.28)
    assert check_loc("33.08 75.28", "33.08", "75.28") == True
    assert check_loc("44.57833333333333 -91.21833333333333", "44.5783", "-91.2183") == False
    #row35 - CK - point - 44.57833333333333 -91.21833333333333        CN - wgs84_pos_lat - 44.5783       CO - wgs84_pos_long - -91.2183      

if __name__ == "__main__":
    test()