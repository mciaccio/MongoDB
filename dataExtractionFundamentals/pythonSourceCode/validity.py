"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
# 46 total
# 4 with non compliant year

import os
import csv
import pprint

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "autos.csv"

PATENTS = os.path.join(DATADIR, DATAFILE)

INPUT_FILE = os.path.join(DATADIR, DATAFILE)
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):
    
    # recNo = 0
    YOURDATA = ''
    
    good_data = []
    bad_data = []
    
#     with open(input_file, 'r') as fIn:
#         originalFile = fIn.readlines()
#         print(originalFile)

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        
        # by pass the header row
        header = reader.fieldnames
        print("\nheader - {}\n".format(header))
        
        for i, row in enumerate(reader):
            # print("{}".format(i)) 
            
            # skip 2 nefarious rows
            if i > 2:
                # print("{}".format(i))

                # all seem to be from http://dbpedia.org
                myURI = row['URI']
                # print("{} - {}".format(myURI, myURI.__class__.__name__))
                if 'dbpedia.org' in myURI:
                    # print("{} - {}".format(myURI, myURI.__class__.__name__))

                    
                    # get the 'productionStartYear' from the current row
                    productionStartYear = row['productionStartYear']
                    
                    # print("{} - {} - {} - {}".format(i, productionStartYear, len(productionStartYear), productionStartYear.__class__.__name__))
                    # capture the year of the 'productionStartYear' filed of the current row
                    firstFourCharacters = productionStartYear[:4]
                    # print("{} - {}".format(firstFourCharacters, firstFourCharacters.__class__.__name__))
    
                    # identify compliant and non compliant year data 
                    if len(productionStartYear) != 25 or int(firstFourCharacters) < 1886 or int(firstFourCharacters) > 2014:
                        # print("70{} - {}".format(row['URI'], row['URI'].__class__.__name__))
                        # print("{} - {}".format(firstFourCharacters, firstFourCharacters.__class__.__name__))
    
                        bad_data.append(row)
                    else:
                        # print("83{}".format(row['productionStartYear']))
                        row['productionStartYear'] = firstFourCharacters
                        print("{}".format(row['productionStartYear']))
                        good_data.append(row)
     
        for i, badElement in enumerate(bad_data):
            pass
            #print("{} - {} - {} - {}".format(badElement['productionStartYear'], badElement['productionStartYear'].__class__.__name__, badElement.__class__.__name__, badElement['URI'])) 
            # print("{} - {}".format(badElement['URI'], badElement['URI'].__class__.__name__)) 
            
        for i, goodElement in enumerate(good_data):
            pass
            # print("{}".format(goodElement)) 
            # print("{}".format(goodElement['productionStartYear'])) 
            # print("{}".format(goodElement['productionStartYear'][:4]))   
            # print("{} - {} - {} - {}".format(goodElement['productionStartYear'], goodElement['productionStartYear'].__class__.__name__)) 
            # print("{} - {}".format(goodElement['URI'], badElement['URI'].__class__.__name__)) 

                    
        print("\nlen(bad_data) - {}".format(len(bad_data)))
        print("len(good_data) - {}".format(len(good_data)))
           
                

        
            
        #COMPLETE THIS FUNCTION



    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in good_data:
            writer.writerow(row)
            
    with open(output_bad, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in bad_data:
            writer.writerow(row)
            
            
            


            
            
    # print("recNo - {}".format(recNo))
    # print("recNo.__.class__.__name__ - {}".format(recNo.__.class__.__name__))



def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()
    
    
   
# instructor solution     
#     def process_file(input_file, output_good, output_bad):
#     # store data into lists for output
#     data_good = []
#     data_bad = []
#     with open(input_file, "r") as f:
#         reader = csv.DictReader(f)
#         header = reader.fieldnames
#         for row in reader:
#             # validate URI value
#             if row['URI'].find("dbpedia.org") < 0:
#                 continue
# 
#             ps_year = row['productionStartYear'][:4]
#             try: # use try/except to filter valid items
#                 ps_year = int(ps_year)
#                 row['productionStartYear'] = ps_year
#                 if (ps_year >= 1886) and (ps_year <= 2014):
#                     data_good.append(row)
#                 else:
#                     data_bad.append(row)
#             except ValueError: # non-numeric strings caught by exception
#                 if ps_year == 'NULL':
#                     data_bad.append(row)
# 
#     # Write processed data to output files
#     with open(output_good, "w") as good:
#         writer = csv.DictWriter(good, delimiter=",", fieldnames= header)
#         writer.writeheader()
#         for row in data_good:
#             writer.writerow(row)
# 
#     with open(output_bad, "w") as bad:
#         writer = csv.DictWriter(bad, delimiter=",", fieldnames= header)
#         writer.writeheader()
#         for row in data_bad:
#             writer.writerow(row)
