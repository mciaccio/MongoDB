#!/usr/bin/env python3.5

# xlrd documentation
# http://www.lexicon.net/sjmachin/xlrd.html
'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.

An example output can be seen in the "example.csv" file.
'''

import xlrd
import os
import csv
# from zipfile import ZipFile

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "2013_ERCOT_Hourly_Load_Data.xls"
OUTFILE = "2013_Max_Loads.csv"

ercot_xls = os.path.join(DATADIR, DATAFILE)

ercot_csv = os.path.join(DATADIR, OUTFILE)

# def open_zip(datafile):
#     with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#         myzip.extractall()

def build_header():
        print("\tBegin build_header function")
        
        data = "Station|Year|Month|Day|Hour|Max Load"
        
        # data.rstrip() is Station|Year|Month|Day|Hour|Max Load
        print("\t\tdata.rstrip() is {}".format(data.rstrip()))
        print("\tEnd build_header function\n")
        return data
    
def get_StationName_MaxLoad_MaxTime(excelSheet, column_no):
        print("\tBegin get_StationName_MaxLoad_MaxTime function")
        # print("\t\tcolumn_no is {}".format(column_no))
        stationName = excelSheet.cell_value(0,column_no)
        # print("\t\tstationName is {}\n".format(stationName))

        stationLoadList = excelSheet.col_values(column_no,1,7296)
        
        # myMaxStationFloat is 2380.1654089999956
        myMaxStationFloat = max(stationLoadList)
        # print("\t\tmyMaxStationFloat is {}".format(myMaxStationFloat))
        
        myMaxStationIndex = stationLoadList.index(myMaxStationFloat)
        # print("\t\tmyMaxStationIndex is {}".format(myMaxStationIndex))
        
        # Verify max value at the index
        # ercotSheet0.cell_value(myMaxCOASTIndex + 1, 1)
        # print("\t\texcelSheet.cell_value(myMaxStationIndex + 1, column_no) is {}\n".format(excelSheet.cell_value(myMaxStationIndex + 1, column_no)))
        
        myMaxStationTime = xlrd.xldate_as_tuple(excelSheet.cell_value(myMaxStationIndex + 1, 0), 0)
        # Returns: Gregorian (year,         month,    day,    hour,    minute,    nearest_second).         
        # myMaxStationTime is (2013,        8,        5,      17,      0,         0)
        # print("\t\tmyMaxStationTime is {}".format(myMaxStationTime))
        
        # print("\t\tmyMaxStationTime.__class__.__name__ is {}".format(myMaxStationTime.__class__.__name__)) # tuple
        # print("\t\tlen(myMaxStationTime) is {}".format(len(myMaxStationTime)))
        # print("\t\tmyMaxStationTime[0] is {}\n".format(myMaxStationTime[0]))

        # unpack the tuple  
        (stationYear, stationMonth, stationDay, stationHour, stationMinute, stationNearest_second) = myMaxStationTime
        
        print("\t\tstationYear is {}, stationMonth is {}".format(stationYear, stationMonth))
        print("\t\tstationDay is {}, stationHour is {} ".format(stationDay, stationHour))
        print("\t\tstationMinute is {}, stationNearest_second is {} ".format(stationMinute, stationNearest_second))
        
        # data = stationName + "|" + stationYear + "|" + stationMonth + "|" + stationDay + "|" +  stationHour
        
        # print ("\t\tdata is {} ".format(data))
        # data = (stationName + "|"  + str(stationYear) + "|" + str(stationMonth) + "|" + str(stationDay) + "|" +  str(stationHour) + "|" + str(round(myMaxStationFloat, 1)) + "\n")
        # data = (stationName + ","  + str(stationYear) + "," + str(stationMonth) + "," + str(stationDay) + "," +  str(stationHour) + "," + str(round(myMaxStationFloat, 1)))
        #data = ('"'+stationName+'"' +","+ '"'+ str(stationYear)+'"'+"," + str(stationMonth) + "," + str(stationDay) + "," +  str(stationHour) + "," + str(round(myMaxStationFloat, 1)))
        data = (stationName +","+ str(stationYear) +","+ str(stationMonth) + "," + str(stationDay) + "," +  str(stationHour) + "," + str(round(myMaxStationFloat, 1)))
        # print ("\t\tdata is {} ".format(data).rstrip())
        
        print("\tEnd get_StationName_MaxLoad_MaxTime function\n")
        
        return data

def parse_file(datafile):
    
    print("\tBegin parse_file function\n")

    # print("\t\tercot_xls is {}".format(ercot_xls))
    # print("\t\tercot_xls.__classname__.__name__ is {}\n".format(ercot_xls.__class__.__name__)) # str
    # print("\t\tercot_csv is {}\n".format(ercot_csv))
    # print("\t\tercot_csv.__classname__.__name__ is {}\n".format(ercot_csv.__class__.__name__)) # str
    
    ercotWorkbook = xlrd.open_workbook(datafile)
    # print("\t\tercotWorkbook is {}".format(ercotWorkbook))
    # print("\t\tercotWorkbook.__classname__.__name__ is {}\n".format(ercotWorkbook.__class__.__name__)) # Book

    ercotSheet0 = ercotWorkbook.sheet_by_index(0)
    # print("\t\tercotSheet0 is {}\n".format(ercotSheet0))
    # print("\t\tercotSheet0.__class__.__name__ is {}\n".format(ercotSheet0.__class__.__name__)) # Sheet

    # print("\t\tercotSheet0.cell_value(1, 1) is {}".format(ercotSheet0.cell_value(1, 1))) # 7606.263544000012
    # print("\t\tercotSheet0.cell_value(1, 7295) is {}\n".format(ercotSheet0.cell_value(7295, 1))) # 8517.488200000013
    
    # print("\t\tnercotSheet0.nrows is {}".format(ercotSheet0.nrows)) #7296
    # print("\t\tercotSheet0.ncols is {}\n".format(ercotSheet0.ncols)) # 10
          
    # Get the column for the station  
    # Returns a slice of the values of the cells in the given column.
    # col_values(colx, start_rowx=0, end_rowx=None)   
    # myCOASTValuesList = ercotSheet0.col_values(1,1,7296)
    # myCOASTValuesList = ercotSheet0.col_values(1,1,7296)
    # print("\t\tmyCOASTValuesList.__class__.__name__ is {}".format(myCOASTValuesList.__class__.__name__)) #list
    # print("\t\tlen(myCOASTValuesList) is {}".format(len(myCOASTValuesList))) # 7296
    # print("\t\tmyCOASTValuesList[0] is {}".format(myCOASTValuesList[0])) # 7606.263544000012 AOK
    # print("\t\tmyCOASTValuesList[7294] is {}\n".format(myCOASTValuesList[7294])) # 8517.488200000013 AOK
    # print("\t\tmyCOASTValuesList[7294] is {}\n".format(myCOASTValuesList[7295])) # IndexError: list index out of range
    
    # Get the max load for that station
    # myMaxCOASTFloat = max(myCOASTValuesList)
    # print("\t\tmyMaxCOASTFloat is {}".format(myMaxCOASTFloat)) #18779.025510000003
    
    # Get the index of the max load 
    # myMaxCOASTIndex = myCOASTValuesList.index(myMaxCOASTFloat)
    # print("\t\tmyMaxCOASTIndex is {}\n".format(myMaxCOASTIndex)) # 5391
    
    # Verify max value at the index
    # ercotSheet0.cell_value(myMaxCOASTIndex + 1, 1) is 18779.025510000003
    # print("\t\tercotSheet0.cell_value(myMaxCOASTIndex + 1, 1) is {}".format(ercotSheet0.cell_value(myMaxCOASTIndex + 1, 1)))
     
    # Get and format the max value time 
    # cell_value(rowx, colx)
    # myMaxCOASTTime = xlrd.xldate_as_tuple(ercotSheet0.cell_value(myCOASTValuesList.index(max(myCOASTValuesList)) + 1, 0), 0)
    # print("\t\tmyMaxCOASTTime is {}".format(myMaxCOASTTime))
    
    #data = get_StationName_MaxLoad_MaxTime(ercotSheet0, 9)
    
    # iterate through the columns
    for column_no in range(1,ercotSheet0.ncols):
        # print("\tcolumn_no is {}...............................................".format(column_no))
        data = get_StationName_MaxLoad_MaxTime(ercotSheet0, column_no)
        save_file(data, ercot_csv)
        
    print("\tEnd parse_file function\n")

    return data


# def save_file(data, ercot_csvFile):
#     print("\tBegin save_file function")
#     # print("\t\tdata is {}".format(data.rstrip()))
#     # print("\t\tdata.rstrip().__class__.__name__ is {}".format(data.rstrip().__class__.__name__)) # str
#     # print("\tfilename is {}".format(ercot_csvFile))
#     
#     if "Station" in data:
#         outFile = open(ercot_csvFile, "w")
#     else:
#         outFile = open(ercot_csvFile, "a")
#         
#     outFile.write(data)
#     #outFile.write()
#     # outFile.write("and another line")
#     outFile.close()
#     print("\tEnd save_file function\n")
#     # YOUR CODE HERE

def save_file(data, ercot_csvFile): # csv.writer !!
    print("\tBegin save_file function")
    
    print("\t\tdata is {}".format(data))

    if "Station" in data:
        print("\t\tdata is {}".format(data))
        data = data.split('|')
        mycsvfile = open(ercot_csvFile, 'w')
    else:
        data = data.split(",") 
        mycsvfile = open(ercot_csvFile, 'a')       
    
    thedatawriter = csv.writer(mycsvfile, delimiter='|')
    thedatawriter.writerow(data)
 
    
    print("\tEnd save_file function\n")
    # YOUR CODE HERE

def test():
    print("\n\tBegin test function\n")
    
    data = build_header()
    # data is Station|Year|Month|Day|Hour|Max Load
    
    save_file(data,ercot_csv)

    parse_file(ercot_xls)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    
    # correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH', 'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH', 'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST', 'ERCOT'] # we did ERCOT too
    
    # hard coded fields list
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']
    print("\tEnd test function\n") 

    with open(ercot_csv) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            print("\n\t\tline is {}".format(line))
            station = line['Station']
            print("\t\tstation is {}".format(station))

            if station == 'FAR_WEST':
                for field in fields:
                    print("\n\t\t\tfield is {}".format(field))
                    # iterate through the hard coded fields list
                    # and dictionary lookup
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        print("\t\t\t\tmax_answer is {}".format(max_answer))

                        max_line = round(float(line[field]), 1)
                        print("\t\t\t\tmax_line is {}".format(max_line))
                        
                        assert max_answer == max_line
 
                    # Otherwise check for equality
                    else:
                        # echo hard coded ans FAR_WEST dictionary
                        # print("\t\t\tans[station] is {}".format(ans[station]))
                        print("\t\t\t\tans[station][field] is {}".format(ans[station][field]))
                        print("\t\t\t\tline[field] is {}".format(line[field]))
                        assert ans[station][field] == line[field]
 
            number_of_rows += 1
            print("\t\tnumber_of_rows is {}".format(number_of_rows))
            
            # populate list of stations
            stations.append(station)
            print("\t\tstations is {}".format(stations))
            
    assert number_of_rows == 9 # we did the last line ERCOT
    # assert number_of_rows == 8
    print("\nfinishing up number_of_rows is {}\n".format(number_of_rows))
    print("finishing up stations is {}".format(stations))
    print("finishing up set(stations) is {}\n".format(set(stations)))
    print("finishing up correct_stations is {}".format(correct_stations))
    print("finishing up set(correct_stations) is {}\n".format(set(correct_stations)))
    # print("finishing up set(correct_stations).__class__.__name__ is {}\n".format(set(correct_stations).__class__.__name__)) # set
    
    assert stations == correct_stations
    assert set(stations) == set(correct_stations)
 
print("\n\tBegin excelToCSV Python module")
test()
print("\tEnd excelToCSV Python module")

