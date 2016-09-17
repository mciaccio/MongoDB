#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
import os
import sys
import numpy
from numpy.distutils.system_info import numpy_info


from zipfile import ZipFile
from audioop import avg
from numpy.f2py.f2py2e import numpy_version
 
DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"
ercot_xls = os.path.join(DATADIR, DATAFILE)

def echoes():
        print("\tBegin echoes()")
        print ("\t\t{}".format(sys.version))
        print("\t\txlrd Version is {}".format(xlrd.__VERSION__))
        print("\t\tercot_xls.__class__.__name__ is {}".format(ercot_xls.__class__.__name__)) #str
        print(numpy_version)

        print("\tEnd echoes()\n")


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):

    print("\tBegin parse_file()")

    ercotWorkbook = xlrd.open_workbook(datafile)
    ercotSheet0 = ercotWorkbook.sheet_by_index(0)

    ### example on how you can get the data
    #sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:", 
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):", 
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):", 
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):", 
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    mySheetCopy = [[ercotSheet0.cell_value(row, col)
        for col in range(1, 2)] # second column only zero based indexing 
                   # for row in range(1, ercotSheet0.nrows-1 )] # 
                   for row in range(ercotSheet0.nrows-ercotSheet0.nrows+1, ercotSheet0.nrows-1 )] # 
    print("\t\tercotSheet0.nrows is {}".format(ercotSheet0.nrows))  
    print("\t\tercotSheet0.ncols is {}\n".format(ercotSheet0.ncols))  
    print("\t\tgrab last COAST column cell is {}\n".format(ercotSheet0.cell_value(ercotSheet0.nrows-1, 1)))
     
    print("\t\tmax(mySheetCopy) is max(mySheetCopy{}".format(max(mySheetCopy)))
    print("\t\tmySheetCopy.__class__.__name__ is {}\n".format(mySheetCopy.__class__.__name__)) # list
    
    myMaxFloatList = [float(i) for i in max(mySheetCopy)]
    print("\t\tmyMaxFloatList is {}".format(myMaxFloatList))  
    print("\t\tmyMaxFloatList.__class__.__name__ is {}\n".format(myMaxFloatList.__class__.__name__)) # list
    
    print("\t\tround(myMaxFloatList[0], 10) is {}".format((round(myMaxFloatList[0], 10)))) # float
    print("\t\tround(myMaxFloatList[0], 10).__class__.__name__ is {}\n".format((round(myMaxFloatList[0], 10).__class__.__name__))) # float
    
    myMinFloatList = [float(i) for i in min(mySheetCopy)]
    print("\t\tmyMinFloatList is {}".format(myMinFloatList))  
    print("\t\tmyMinFloatList.__class__.__name__ is {}\n".format(myMinFloatList.__class__.__name__)) # list
    
    print("\t\tround(myMinFloatList[0], 10) is {}".format((round(myMinFloatList[0], 10)))) # float
    print("\t\tround(myMinFloatList[0], 10).__class__.__name__ is {}\n".format((round(myMinFloatList[0], 10).__class__.__name__))) # float
    
    # print("\t\t\tgrab a random cell_value (row-{},col-{}) is {}\n".format(ercotSheet0.cell_value(ercotSheet0.nrows-ercotSheet0.nrows+1, ercotSheet0.nrows-1)))
    print("\t\tgrab last COAST column cell is {}".format(ercotSheet0.cell_value(ercotSheet0.nrows-1, ercotSheet0.ncols-9)))
    #nrows-ercotSheet0.nrows+1, ercotSheet0.nrows-1)

    
    
    
    
    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    
    data["maxvalue"] = round(myMaxFloatList[0], 10)
    data["minvalue"] = round(myMinFloatList[0], 10)
    
    print("\tEnd parse_file()\n")
    
    return data

def test():
    
    print("\tBegin test()\n")
    #open_zip(datafile)
    data = parse_file(ercot_xls)
    
    print("\t\t\tdata is {}\n".format(data)) 
    print("\t\t\tdata['maxvalue'] is {}".format(data['maxvalue'])) 
    print("\t\t\tdata['maxvalue'].__class__.__name__ is {}\n".format(data['maxvalue'].__class__.__name__)) # float
    
    print("\t\t\tdata['minvalue'] is {}".format(data['minvalue'])) 
    print("\t\t\tdata['minvalue'].__class__.__name__ is {}\n".format(data['minvalue'].__class__.__name__)) # float
    
    #assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    #assert round(data['maxvalue'], 10) == round(18779.02551, 10)
    
    print("\tEnd test()\n")



print("\nBegin Python Module\n")
ercot_xls = os.path.join(DATADIR, DATAFILE)
echoes()
#parse_file(ercot_xls)
test()



print("End Python Module")


