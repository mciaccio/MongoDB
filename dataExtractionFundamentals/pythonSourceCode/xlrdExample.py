import os
import sys
import xlrd



DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"

def echoes():
    print("\tBegin echoes()")
    print ("\t\t{}".format(sys.version))
    print("\t\txlrd Version is {}".format(xlrd.__VERSION__))
    print("\t\tercot_xls.__class__.__name__ is {}".format(ercot_xls.__class__.__name__))
    print("\tEnd echoes()\n")
    
def parse_file(ercot_xls):
    print("\tBegin parse_file()\n")

    ercotWorkbook = xlrd.open_workbook(ercot_xls)
    print("\t\t\tercotWorkbook.__class__.__name__ is {}".format(ercotWorkbook.__class__.__name__)) # Book
    
    ercotSheet0 = ercotWorkbook.sheet_by_index(0)
    print("\t\t\tercotSheet0.__class__.__name__ is {}\n".format(ercotSheet0.__class__.__name__)) # Sheet
    
    print("\t\t\tercotSheet0.cell(0,0) is {}".format(ercotSheet0.cell(0,0))) # text:'Hour_End'
    print("\t\t\tercotSheet0.cell(0,0).__class__.__name__ is {}\n".format(ercotSheet0.cell(0,0).__class__.__name__)) # Cell
    
    print("\t\t\tercotSheet0.cell_value(0,0) is {}".format(ercotSheet0.cell_value(0,0))) # Hour End row, col
    print("\t\t\tercotSheet0.cell_value(0,0).__class__.__name__ is {}\n".format(ercotSheet0.cell_value(0,0).__class__.__name__)) # str
    
    print("\t\t\tercotSheet0.ncols is {}".format(ercotSheet0.ncols)) # 10
    print("\t\t\tercotSheet0.nrows is {}\n".format(ercotSheet0.nrows)) # 7296
    
    # (6, 7) six IS the ROW, 7 IS the column, row comes first 
    print("\t\t\tgrab a random cell_value (row-{},col-{}) is {}\n".format(6, 7, ercotSheet0.cell_value(6, 7)))
    
    # get a slice out of a column
    # col_values(colx, start_rowx=0, end_rowx=None)
    ercotSheet0.col_values(3, start_rowx=0, end_rowx=1)
    print("\t\t\tsliceOfColumn - ercotSheet0.col_values(3, start_rowx=0, end_rowx=3) is {}\n".format(ercotSheet0.col_values(3, start_rowx=0, end_rowx=3)))
    
    # get a slice out of a row
    # row_values(rowx, start_colx=0, end_colx=None)
    ercotSheet0.row_values(3, start_colx=0, end_colx=1)
    print("\t\t\tsliceOfRow - ercotSheet0.row_values(3, start_colx=0, end_colx=1) is {}\n".format(ercotSheet0.row_values(3, start_colx=1, end_colx=4)))    
    
    mySheetCopy = [[ercotSheet0.cell_value(row, col)
         for col in range(1, 2)] # second column only zero based indexing 
             for row in range(0,2)] # top two rows of the second column
    
    print("\t\t\tmySheetCopy.__class__.__name__ is {}".format(mySheetCopy.__class__.__name__)) # list
    print("\t\t\tmySheetCopy is {}\n".format(mySheetCopy))
    
    
    #col_values(colx, start_rowx=0, end_rowx=None) [#]
    #mySheetCopy.col_values(3, start_rowx=0, end_rowx=1)
    
    
    for col in range(0, 1):
        for row in range(0,3):
            # print("\t\t\tercotSheet0.cell_type(row, col) is {}".format(ercotSheet0.cell_type(row, col)))
            # print("\t\t\tercotSheet0.cell_value(row-{},col-{}) is {}\n".format(col, row, ercotSheet0.cell_value(row, col))) # Hour End 
            
            if ercotSheet0.cell_type(row, col) == 3:
                print("\t\t\tercotSheet0.cell_type(row-{},col-{}) is {}".format(row, col, ercotSheet0.cell_type(row, col)))
                print("\t\t\tdate field ercotSheet0.cell_value(row-{},col-{}) is {}".format(row, col, ercotSheet0.cell_value(row, col)))
                # xlrd.xldate_as_tuple(ercotSheet0.cell_value(row, col), 0) 
                print("\t\t\tGregorian (year, month, day, hour, minute, nearest_second)")
                print("\t\t\tdate field- formatted is {}\n".format(xlrd.xldate_as_tuple(ercotSheet0.cell_value(row, col), 0)))

            else:
                print("\t\t\tercotSheet0.cell_type(row-{}, col-{}) is {}".format(row, col, ercotSheet0.cell_type(row, col)))
                print("\t\t\tercotSheet0.cell_value(row-{}, col-{}) is {}\n".format(col, row, ercotSheet0.cell_value(row, col)))
 

    print("\tEnd parse_file()")
 
print("\nBegin Python Module\n")
ercot_xls = os.path.join(DATADIR, DATAFILE)
echoes()
parse_file(ercot_xls)
 
print("End Python Module")



