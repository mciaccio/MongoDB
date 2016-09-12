# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
import sys

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "beatles-diskography.csv"
RECNO = 0
data = []


def buildHeaderList(headerLine):
    print("Begin buildHeaderList function")
    print ("\theaderLine is -> {}".format(headerLine.strip()))
    #split the string return a list
    headerList = headerLine.strip().split(',')
    
    for index in range(len(headerList)):
        # print ("\theaderList[%s] is %s", index, headerList[index])
        print("\theaderList[{}] is {}".format(index, headerList[index]))

    print("End buildHeaderList function\n")
    return headerList 

def buildMusicList(musicLine):
    print("Begin buildMusicList function")
    print ("\tmusicLine is -> {}".format(musicLine.strip()))
    #split the string return a list
    musicList = musicLine.strip().split(',')
    
    for index in range(len(musicList)):
        print("\tmusicList[{}] is {}".format(index, musicList[index]))

    print("End buildMusicList function\n")
    return musicList

def buildDictionaryList(headerList, musicList):
    print("Begin buildDictionaryList function")
    keyValuePairList = []
    #Split Return a list of the words in the string
    
    for index in range(len(headerList)):
        pass
        # print("\theaderList[{}] is {}".format(index, headerList[index])) 
    # print()

    for index in range(len(musicList)):
        pass
        # print("\tmusicList[{}] is {}".format(index, musicList[index]))
    #print()
    
    for index in range(len(headerList)):
        #print ('\t\theaderList is ', headerList[index])
        #print ('\t\tmusicList  is ', musicList[index])
        keyValuePair = headerList[index] + ": " + musicList[index]
        print("\t\tkeyValuePair is {}".format(keyValuePair))
        
        keyValuePairList.append(keyValuePair)
        
    print("\t\tkeyValuePairList is {}".format(keyValuePairList))
    data.append(keyValuePairList)

    print("End buildDictionaryList function\n")

def parse_file(datafile):
    print("\nBegin parse_file(datafile) function\n")
    
    global RECNO

    #data = []
    with open(datafile, "r") as f:
        for line in f:
            #print (RECNO)
            RECNO += 1
            #print (RECNO)
            
            if RECNO == 1:
                # print ("\tfirst line is %s", line.strip(),"\n")
                headerList=buildHeaderList(line)
            elif RECNO < 12:
                musicList = buildMusicList(line)
                print("\theaderList is {}".format(headerList))
                print("\tmusicList is {}".format(musicList))
                print()
                buildDictionaryList(headerList,musicList)
                 
    print("End parse_file(datafile) function\n")

    return data


def test():
    # a simple test of your implemetation
    print("\nBegin test() function")

    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    #print("..........................{}".format(data[0]))
    #print("..........................{}".format(data[1]))
    
    print("..........................{}".format(d[0]))
    print("..........................{}".format(d[1]))
    print("..........................{}".format(d[2]))
    print("..........................{}".format(d[3]))
    print("..........................{}".format(d[4]))
    print("..........................{}".format(d[5]))
    print("..........................{}".format(d[6]))
    print("..........................{}".format(d[7]))
    print("..........................{}".format(d[8]))
    print("..........................{}".format(d[9]))
    #print("..........................{}".format(d)
    
    # firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    # tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    # assert d[0] == firstline
    # assert d[9] == tenthline
    
    print("End test() function")
    
print("\nBegin Udacity Parse Module\n")
print (sys.version)
test()
print("\nEnd Udacity Parse Module\n")











