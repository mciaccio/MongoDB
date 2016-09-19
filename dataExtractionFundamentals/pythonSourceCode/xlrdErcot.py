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
import pprint

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"
ercot_xls = os.path.join(DATADIR, DATAFILE)

def echoes():
        print("\tBegin echoes()")
        print ("\t\t{}".format(sys.version))
        print("\t\txlrd Version is {}".format(xlrd.__VERSION__))
        print("\t\tercot_xls.__class__.__name__ is {}".format(ercot_xls.__class__.__name__)) #str
        # print(numpy_version)

        print("\tEnd echoes()\n")

def parse_file(datafile):

    print("\tBegin parse_file()")

    ercotWorkbook = xlrd.open_workbook(datafile)
    ercotSheet0 = ercotWorkbook.sheet_by_index(0)
    print("\t\tercotSheet0.__class__.__name__) is {}".format(ercotSheet0.__class__.__name__)) # Sheet


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
    
    print("\t\tercotSheet0.nrows is {}".format(ercotSheet0.nrows))  
    print("\t\tercotSheet0.ncols is {}\n".format(ercotSheet0.ncols))  
    
    print("\t\tgrab first COAST column cell is {}".format(ercotSheet0.cell_value(1, 1)))
    print("\t\tgrab ercotSheet0.cell_value(1, 1).__class__.__name__) is {}".format(ercotSheet0.cell_value(1, 1).__class__.__name__)) # float

    print("\t\tgrab last  COAST column cell is {}\n".format(ercotSheet0.cell_value(ercotSheet0.nrows - 1, 1)))
        
    largestCOASTFloat = 0    
    smallestCOASTFloat = ercotSheet0.cell_value(1, 1)

    for dataRow in range(1, ercotSheet0.nrows):
        if largestCOASTFloat < ercotSheet0.cell_value(dataRow, 1):
            largestCOASTFloat = ercotSheet0.cell_value(dataRow, 1)
            largestDataRow = dataRow
        elif ercotSheet0.cell_value(dataRow, 1) < smallestCOASTFloat:
            smallestCOASTFloat = ercotSheet0.cell_value(dataRow, 1)
            smallestDataRow = dataRow
        else:
            pass
            
    print("..................................................................................................................")
    print("\t\tercotSheet0.cell_value(1, 1) is {}".format(ercotSheet0.cell_value(1, 1))) # 
    print("\t\tercotSheet0.cell_value(ercotSheet0.nrows - 1, 1) is {}\n".format(ercotSheet0.cell_value(ercotSheet0.nrows - 1, 1))) # 
    
    print("\t\tlargestCOASTFloat is {}".format(largestCOASTFloat)) # 
    print("\t\tercotSheet0.cell_value(largestDataRow, 1) is {}".format(ercotSheet0.cell_value(largestDataRow, 1)))
    print("\t\tercotSheet0.cell_value(largestDataRow, 1).__class__.__name__ is {}".format(ercotSheet0.cell_value(largestDataRow, 1).__class__.__name__))
    print("\t\tlargestDataRow is {}\n".format(largestDataRow)) # 
        
    print("\t\tsmallestCOASTFloat is {}".format(smallestCOASTFloat)) # 
    print("\t\tercotSheet0.cell_value(smallestDataRow, 1) is {}".format(ercotSheet0.cell_value(smallestDataRow, 1)))
    print("\t\tsmallestDataRow is {}".format(smallestDataRow)) # 
    print("..................................................................................................................\n") 
 
 
    # instructor way to get the max value (column 1) and corresponding date field (column 0)
    # build a list from the Sheet class
    myCOASTColumn = ercotSheet0.col_values(1, start_rowx=1, end_rowx=ercotSheet0.nrows)
    
    print("\t\tmyCOASTColumn.__class__.__name__ is {}\n".format(myCOASTColumn.__class__.__name__)) # list
    
    # max value in list 
    print("\t\tmax(myCOASTColumn is {}".format(max(myCOASTColumn))) #18779.025510000003
    #index of max value in list
    print("\t\tmyCOASTColumn.index(max(myCOASTColumn) is {}\n".format(myCOASTColumn.index(max(myCOASTColumn)))) # 5391
    
    # use list index to get the max row in the sheet - value - make sure in right row  
    print("\t\tercotSheet0.cell_value(myCOASTColumn.index(max(myCOASTColumn)) + 1, 1) is {}".format(ercotSheet0.cell_value(myCOASTColumn.index(max(myCOASTColumn)) + 1, 1))) 
    # get the date from the right row, column 0
    print("\t\tercotSheet0.cell_value(myCOASTColumn.index(max(myCOASTColumn)) + 1, 0) is {}\n".format(ercotSheet0.cell_value(myCOASTColumn.index(max(myCOASTColumn)) + 1, 0))) 
    
    # convert the time and priint it
    maxtime = xlrd.xldate_as_tuple(ercotSheet0.cell_value(myCOASTColumn.index(max(myCOASTColumn)) + 1, 0), 0)
    print("\t\tmaxtime is {} (2013, 8, 13, 17, 0, 0)\n".format(maxtime)) 
    # instructor way to get the max value (column 1) and corresponding date field (column 0)

    # calculate the average 
    print("\t\tlen(myCOASTColumn) is {}".format(len(myCOASTColumn))) # 7295
    print("\t\tmyCOASTColumn[0] is {}".format(myCOASTColumn[0])) 
    print("\t\tmyCOASTColumn[7294] is {}".format(myCOASTColumn[7294])) 
    print("\t\tnumpy.average(myCOASTColumn) is {}\n".format(numpy.average(myCOASTColumn))) # 10976.9334606798

    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    
    #print("\t\tdata['avgcoast'].__class__.__name__ is {}".format(data['avgcoast'].__class__.__name__)) # int

    data["maxtime"]  = xlrd.xldate_as_tuple(ercotSheet0.cell_value(largestDataRow, 0), 0)
    data["maxvalue"] = round(largestCOASTFloat, 10)
    data["mintime"]  = xlrd.xldate_as_tuple(ercotSheet0.cell_value(smallestDataRow, 0), 0)

    data["minvalue"] = round(smallestCOASTFloat, 10)
    data["avgcoast"] = round(numpy.average(myCOASTColumn), 10)
    
    print("\tEnd parse_file()\n")
    
    return data

def test():
    
    print("\tBegin test()\n")
    #open_zip(datafile)
    data = parse_file(ercot_xls)
    
    print("\t\tdata is {}\n".format(data)) 
    pprint.pprint(data) 
    print()
    print("\t\tdata['maxvalue'] is {} 18779.02551".format(data['maxvalue'])) 
    print("\t\tdata['maxvalue'].__class__.__name__ is {}\n".format(data['maxvalue'].__class__.__name__)) # float
    
    print("\t\tdata['maxtime'] is {} (2013, 8, 13, 17, 0, 0)".format(data['maxtime'])) 
    print("\t\tdata['maxtime'].__class__.__name__ is {}\n".format(data['maxtime'].__class__.__name__)) # tuple
    
    print("\t\tdata['minvalue'] is {} 6602.113899".format(data['minvalue'])) 
    print("\t\tdata['minvalue'].__class__.__name__ is {}\n".format(data['minvalue'].__class__.__name__)) # float
    
    print("\t\tdata['mintime'] is {} (2013, 2, 3, 4, 0, 0)".format(data['mintime'])) 
    print("\t\tdata['mintime'].__class__.__name__ is {}\n".format(data['mintime'].__class__.__name__)) # tuple
    
    print("\t\tdata['avgcoast'] is {} 10976.9334606798".format(data['avgcoast'])) 
    print("\t\tdata['avgcoast'].__class__.__name__ is {}".format(data['avgcoast'].__class__.__name__)) # float64
    
    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)
    
    print("\tEnd test()\n")

print("\nBegin Python Module\n")

ercot_xls = os.path.join(DATADIR, DATAFILE)
echoes()
#parse_file(ercot_xls)
test()

print("End Python Module")