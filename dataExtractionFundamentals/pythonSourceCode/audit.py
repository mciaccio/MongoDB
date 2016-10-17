#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}
The type() function returns a type object describing the argument given to the 
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""
# Dictionary code examples - Python
# Dictionary error handling 
# Python set code
# 39 total

import os
import codecs
import csv
import json
import pprint
import sys 

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "cities.csv"
CITIES = os.path.join(DATADIR, DATAFILE)

innerDictionary = {}
innerKeys = ['listCounter', 'zeroLengthStringCounter', 'NULLCounter', 'floatCounter', 'intCounter', 'intCounter', 'udacityStrCounter' ]

outerDictionary = {}

innerTypeDictionary = {}

# CITIES = 'cities.csv'
# 
FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal", "elevation",
"maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]

#FIELDS = ["areaLand", "areaMetro"]
# FIELDS = ["areaMetro"]
# FIELDS = ["areaLand"]

def initialize():
#     print("\n\tBegin initialize function") 

    global innerDictionary
    innerDictionary = dict.fromkeys(innerKeys, 0)
 
#     print("\tEnd initialize function\n") 
    
def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

def is_int(y):
    try:
        int(y)
    except ValueError:
        return False
    return True

def audit_file(filename, fields):
   
    print("\n\tBegin audit_file function\n") 
    global innerDictionary
    global outerDictionary
    totalRowCount = 0
 
    fieldtypes = {}
 
  
    # print("\t\tFIELDS- {}".format(FIELDS))
    for columnHeader in FIELDS:
        print("\t\tBegin outer columnHeader loop - columnHeader - {}".format(columnHeader))
        
        columnHeaderTypeSet = set()  
        
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
 
            header = reader.fieldnames
            # print("\t\theader - {}\n".format(header))
 
            for i, row in enumerate(reader):
                # print("\t\t\tBegin inner row loop - totalRowCount - {}".format(totalRowCount))

                if i > 2 :
                    # print("\t\ti - {}, columnHeader - {}, row[columnHeader]- {}".format(i, columnHeader, row[columnHeader]))
                    totalRowCount += 1 
                    #print("\t\ti - {}, totalRowCount - {}".format(i, totalRowCount))
                    
                    if row[columnHeader].startswith('{'):
                        innerDictionary['listCounter'] += 1
                        columnHeaderTypeSet.add(type([]))
                        
                    elif row[columnHeader] == "NULL": # None 
                        innerDictionary['NULLCounter'] += 1
                        columnHeaderTypeSet.add(type(None))
                        
                    elif len(row[columnHeader]) == 0: # None
                        innerDictionary['zeroLengthStringCounter'] += 1
                        columnHeaderTypeSet.add(type(None))
                        
                    # elif isinstance(float(row[columnHeader]), float): # float
                    # elif type (float (row[columnHeader]) ) == float:  # float
                    elif is_float(row[columnHeader]):  # float
                        innerDictionary['floatCounter'] += 1
                        columnHeaderTypeSet.add(type(1.1))
                        
                    # elif isinstance(int(row[columnHeader]), int): # int
                    elif is_int(row[columnHeader]) : # int  
                        innerDictionary['intCounter'] += 1
                        columnHeaderTypeSet.add(type(1))
                        print("\t\tINT row[columnHeader]- {}".format(row[columnHeader]))
                        
                    else:
                        innerDictionary['udacityStrCounter'] += 1
                        columnHeaderTypeSet.add(type("string"))

 
                if totalRowCount == 39:
 
                    totalCounter = innerDictionary['listCounter'] + innerDictionary['NULLCounter'] + innerDictionary['zeroLengthStringCounter'] + innerDictionary['floatCounter'] + innerDictionary['intCounter'] + innerDictionary['udacityStrCounter']
                    if totalCounter != 39:
                        sys.exit("sum is not 39 ")  
                    # print("\t\t\t\ttotalCounter - {}\n".format(totalCounter))

                    print("\t\t\tcolumnHeader - {} columnHeaderTypeSet - {}".format(columnHeader, columnHeaderTypeSet))
                    fieldtypes[columnHeader] = columnHeaderTypeSet
                    # print("\t\t\t\tfieldtypes- {}".format(fieldtypes))
                    print("\t\t\t\tlen(fieldtypes)- {}\n".format(len(fieldtypes)))

            print("\t\tEnd inner row loop")
            totalRowCount = 0

        outerDictionary.update({columnHeader:innerDictionary})
        #pprint.pprint(outerDictionary)
#             print()
# 
#       initialize() the innerDirectory 
        initialize()
        
    print("\tEnd audit_file function\n")     
    # print("222\t\t\t\tfieldtypes - {}".format(fieldtypes))
       
                                            
# YOUR CODE HERE   

    return fieldtypes


def test():
    
    print("\tBegin test function")            

    fieldtypes = audit_file(CITIES, FIELDS)
    print("\t\t\tfieldtypes - {}".format(fieldtypes))
    
    print("\tEnd test function\n")            

    # print ("[type(1.1), type([]), type(None)] - {}".format([type(1.1), type([]), type(None)]))
    # print ("[type(1.1), type([]), type(None)].__class__.__name__ - {}\n".format([type(1.1), type([]), type(None)].__class__.__name__)) # list
    
    print ("set([type(1.1), type([]), type(None)]) - {}".format(set([type(1.1), type([]), type(None)])))

    # print ("set([type(1.1), type([]), type(None)]).__class__.__name__ - {}\n".format(set([type(1.1), type([]), type(None)]).__class__.__name__)) # set
    # pprint.pprint(fieldtypes)
    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
print("\nBegin audit Module\n")

initialize()
        
if __name__ == "__main__":
    test()
    
print("\nEnd audit Module\n")

#
# Browser based udacity.com IDE version 
# 
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# In this problem set you work with cities infobox data, audit it, come up with a
# cleaning idea and then clean it up. In the first exercise we want you to audit
# the datatypes that can be found in some particular fields in the dataset.
# The possible types of values can be:
# - NoneType if the value is a string "NULL" or an empty string ""
# - list, if the value starts with "{"
# - int, if the value can be cast to int
# - float, if the value can be cast to float, but CANNOT be cast to int.
#    For example, '3.23e+07' should be considered a float because it can be cast
#    as float but int('3.23e+07') will throw a ValueError
# - 'str', for all other values
# 
# The audit_file function should return a dictionary containing fieldnames and a 
# SET of the types that can be found in the field. e.g.
# {"field1": set([type(float()), type(int()), type(str())]),
#  "field2": set([type(str())]),
#   ....
# }
# The type() function returns a type object describing the argument given to the 
# function. You can also use examples of objects to create type objects, e.g.
# type(1.1) for a float: see the test function below for examples.
# 
# Note that the first three rows (after the header row) in the cities.csv file
# are not actual data points. The contents of these rows should note be included
# when processing data types. Be sure to include functionality in your code to
# skip over or detect these rows.
# """
# import codecs
# import csv
# import json
# import pprint
# 
# CITIES = 'cities.csv'
# 
# FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
#           "isPartOf_label", "areaCode", "populationTotal", "elevation",
#           "maximumElevation", "minimumElevation", "populationDensity",
#           "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]
# 
# innerDictionary = {}
# innerKeys = ['listCounter', 'zeroLengthStringCounter', 'NULLCounter', 'floatCounter', 'intCounter', 'intCounter', 'udacityStrCounter' ]
# 
# outerDictionary = {}
# 
# innerTypeDictionary = {}
# 
# def initialize():
# #     print("\n\tBegin initialize function") 
# 
#     global innerDictionary
#     innerDictionary = dict.fromkeys(innerKeys, 0)
#     print("\t\tinitialize func - innerDictionary - {}".format(innerDictionary))
# 
# def is_float(x):
#     try:
#         float(x)
#     except ValueError:
#         return False
#     return True
# 
# def is_int(y):
#     try:
#         int(y)
#     except ValueError:
#         return False
#     return True
# 
# def audit_file(filename, fields):
#    
#     print("\n\tBegin audit_file function\n") 
#     global innerDictionary
#     initialize()
# 
#     global outerDictionary
#     totalRowCount = 0
#  
#     fieldtypes = {}
#  
#   
#     # print("\t\tFIELDS- {}".format(FIELDS))
#     for columnHeader in FIELDS:
#         print("\t\tBegin outer columnHeader loop - columnHeader - {}".format(columnHeader))
#         
#         columnHeaderTypeSet = set()  
#         
#         with open(filename, "r") as f:
#             reader = csv.DictReader(f)
#  
#             header = reader.fieldnames
#             # print("\t\theader - {}\n".format(header))
#  
#             for i, row in enumerate(reader):
#                 # print("\t\t\tBegin inner row loop - totalRowCount - {}".format(totalRowCount))
# 
#                 if i > 2 :
#                     # print("\t\ti - {}, columnHeader - {}, row[columnHeader]- {}".format(i, columnHeader, row[columnHeader]))
#                     totalRowCount += 1 
#                     print("\t\tinnerDictionary - {}".format(innerDictionary))
#                     #print("\t\ti - {}, totalRowCount - {}".format(i, totalRowCount))
#                     
#                     if row[columnHeader].startswith('{'):
#                         innerDictionary['listCounter'] += 1
#                         columnHeaderTypeSet.add(type([]))
#                         
#                     elif row[columnHeader] == "NULL": # None 
#                         innerDictionary['NULLCounter'] += 1
#                         columnHeaderTypeSet.add(type(None))
#                         
#                     elif len(row[columnHeader]) == 0: # None
#                         innerDictionary['zeroLengthStringCounter'] += 1
#                         columnHeaderTypeSet.add(type(None))
#                         
#                     # elif isinstance(float(row[columnHeader]), float): # float
#                     # elif type (float (row[columnHeader]) ) == float:  # float
#                     elif is_float(row[columnHeader]):  # float
#                         innerDictionary['floatCounter'] += 1
#                         columnHeaderTypeSet.add(type(1.1))
#                         
#                     # elif isinstance(int(row[columnHeader]), int): # int
#                     elif is_int(row[columnHeader]) : # int  
#                         innerDictionary['intCounter'] += 1
#                         columnHeaderTypeSet.add(type(1))
#                         print("\t\tINT row[columnHeader]- {}".format(row[columnHeader]))
#                         
#                     else:
#                         innerDictionary['udacityStrCounter'] += 1
#                         columnHeaderTypeSet.add(type("string"))
# 
#  
#                 if totalRowCount == 39:
#  
#                     totalCounter = innerDictionary['listCounter'] + innerDictionary['NULLCounter'] + innerDictionary['zeroLengthStringCounter'] + innerDictionary['floatCounter'] + innerDictionary['intCounter'] + innerDictionary['udacityStrCounter']
#                     if totalCounter != 39:
#                         sys.exit("sum is not 39 ")  
#                     # print("\t\t\t\ttotalCounter - {}\n".format(totalCounter))
# 
#                     print("\t\t\tcolumnHeader - {} columnHeaderTypeSet - {}".format(columnHeader, columnHeaderTypeSet))
#                     fieldtypes[columnHeader] = columnHeaderTypeSet
#                     # print("\t\t\t\tfieldtypes- {}".format(fieldtypes))
#                     print("\t\t\t\tlen(fieldtypes)- {}\n".format(len(fieldtypes)))
# 
#             print("\t\tEnd inner row loop")
#             totalRowCount = 0
# 
#         outerDictionary.update({columnHeader:innerDictionary})
#         #pprint.pprint(outerDictionary)
# #             print()
# # 
# #       initialize() the innerDirectory 
#         initialize()
#         
#     print("\tEnd audit_file function\n")     
#     # print("222\t\t\t\tfieldtypes - {}".format(fieldtypes))
#        
#                                             
# # YOUR CODE HERE   
# 
#     return fieldtypes
# 
# def test():
#     fieldtypes = audit_file(CITIES, FIELDS)
# 
#     pprint.pprint(fieldtypes)
# 
#     assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
#     assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
#     
# if __name__ == "__main__":
#     test()
















