 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
documentation
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#multi-valued-attributes
Let's assume that you combined the code from the previous 2 exercises with code
from the lesson on how to build requests, and downloaded all the data locally.
The files are in a directory "data", named after the carrier and airport:
"{}-{}.html".format(carrier, airport), for example "FL-ATL.html".

The table with flight info has a table class="dataTDRight". Your task is to
extract the flight data from that table as a list of dictionaries, each
dictionary containing relevant data from the file and table row. This is an
example of the data structure you should return:

data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}
]

Note - year, month, and the flight data should be integers.
You should skip the rows that contain the TOTAL data for a year.

There are couple of helper functions to deal with the data files.
Please do not change them for grading purposes.
All your changes should be in the 'process_file' function.
"""
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os

datadir = "data"


def open_zip(datadir):
    with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
        myzip.extractall()


def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    return:

    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]


    Note - year, month, and the flight data should be integers.
    You should skip the rows that contain the TOTAL data for a year.
    """
    # flights: dictionary data 
    flightTallies = {}
    
    # data list returned from the process_files function
    data = []
    
    # info dictionary used to populate the data list
    info = {}
    
    # capture courier and airport from file name 
    info['courier'], info['airport'] = f[:6].split("-")
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
    
    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html,"html.parser")
        # print("soup is {}".format(soup)) # 

        table = soup.find("table", { "class" : "dataTDRight" })
        for row in table.findAll("tr")[1:]:
            
            # print("\nlen(row) is {}".format(len(row))) # 7
            print("\nrow.contents[1].text is {}".format(row.contents[1].text)) # useful!!
            # print("rowCount is {}".format(rowCount)) 
            # print("row.__class__.__name__ is {}".format(row.__class__.__name__)) # Tag
            # print("type(row) is {}".format(type(row))) # <class 'bs4.element.Tag'>
            # print("row.name is {}".format(row.name)) # tr
            # print("row.attrs is {}".format(row.attrs)) # {u'class': [u'dataTDRight']}
            # print("row.attrs is {}".format(row.attrs)) # {u'style': u'background-color:#EFEFEF;', u'class': [u'dataTDRight']} 
            print("row.text is {}".format(row.text.strip())) # 200212782,17596,881879,056
            # print("row.descendants is {}".format(row.descendants)) # 
            # print("row.children is {}".format(row.children)) # 
            
            
            keeperRow = True
            tempRow = []
            
            # print("row is {}\n".format(row))
            cells = row.findAll("td")
            # print("len(cells) is {}".format(len(cells))) # 5

            for cell in cells:
                # print("cell.text is {}".format(cell.text))
            
                tempValue = cell.text.encode('ascii','ignore')
                # print("\ttempValue is (commas here) {}".format(tempValue))
                # print("tempValue.__class__.__name__ is {}".format(tempValue.__class__.__name__)) # str
                
                cleanTempValue = tempValue.replace(',', '')
                if cleanTempValue == 'TOTAL':
                    # tempRow.append(cleanTempValue)
                    keeperRow = False
                else:
                    myInt = int(cleanTempValue)
                    tempRow.append(myInt)
                    # print("myInt is {}".format(myInt))
                    # print("myInt.__class__.__name__ is {}".format(myInt.__class__.__name__)) # int
                    # print("type(myInt) is {}\n".format(type(myInt))) # int

            if keeperRow == False:
                pass
                # print
                # print("\tkeeperRow False - tempRow is {}".format(tempRow))
            else:
                # print("\n\tkeeperRow True - tempRow is {}".format(tempRow))
                # print("keeperRow True - tempRow is {}".format(tempRow[0:4]))
                
                flightTallies['domestic'] = tempRow[2]
                flightTallies['international'] = tempRow[3]
                # print("\tkeeperRow True - flightTallies is {}".format(flightTallies))

                info['year'] = tempRow[0]
                info['month'] = tempRow[1]
                info['flights'] = flightTallies
                # print("keeperRow True - info is {}".format(info))
                # print("\n{}".format(info)) 
                data.append(info)

    return data


def test():
    print "Running a simple test...\n"
    open_zip(datadir)
    files = process_all(datadir)
    data = []
    # Test will loop over three data files.
    for f in files:
        # pass
        data += process_file(f) # ORIG
    # data += process_file("FL-ATL.html")
    # print("\n{}".format(data)) 
        
    # print("\nlen(data) is {}".format(len(data))) 
    # print("\nlen(data[-1]) is {}".format(data[-1]))

    #assert len(data) == 399  # Total number of rows
    for entry in data[:3]:
        assert type(entry["year"]) == int
        assert type(entry["month"]) == int
        assert type(entry["flights"]["domestic"]) == int
        assert len(entry["airport"]) == 3
        assert len(entry["courier"]) == 2
    assert data[0]["courier"] == 'FL'
    assert data[0]["month"] == 10
    assert data[-1]["airport"] == "ATL"
    assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
    
    print "... success!"

if __name__ == "__main__":
    test()