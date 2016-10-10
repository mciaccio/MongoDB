#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import os
import xml.etree.ElementTree as ET

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "patent.data"

PATENTS = os.path.join(DATADIR, DATAFILE)

def get_root(fname):
    
    print('\tBegin get_root function')

    tree = ET.parse(fname)
    return tree.getroot()

    print('\tEnd get_root function')

def split_file(filename):
    
    print('\n\tBegin split_file function\n')
 
    """
    Split the input file into separate files, each containing a single patent.
    As a hint - each patent declaration starts with the same line that was
    causing the error found in the previous exercises.
    
    The new files should be saved with filename in the following format:
    "{}-{}".format(filename, n) where n is a counter, starting from 0.
    """

    tempOutFileName = 'patent.data-0'
    fileCounter = 0
    outerList =[]
    innerList =[]
    outerIndex = 0
    
    print('\t\tfilename is {}\n'.format(filename)) 
    
    with open(filename) as fIn:
        originalFile = fIn.readlines()
            
    # This works new line \n required 
    originalFile.index('<?xml version="1.0" encoding="UTF-8"?>\n')
    print('\t\toriginalFile.index <?xml version="1.0" encoding="UTF-8"?> is {}\n'.format(originalFile.index('<?xml version="1.0" encoding="UTF-8"?>\n')))
    
    # indices is [0, 656, 1070, 1724]
    indices = [i for i, x in enumerate(originalFile) if x == '<?xml version="1.0" encoding="UTF-8"?>\n']
    print('\t\tindices is {}\n'.format(indices))

    fn = 'patents.data'
    
    for i, xmlLine in enumerate(originalFile):
        #print("xmlLine is {} ".format(xmlLine))
        # print('\t\ti is {}'.format(i))

        if '<?xml version="1.0" encoding="UTF-8"?>' in xmlLine and i != 0:
            
            outerList.append(innerList)
            
            print('\t\touterIndex is {}'.format(outerIndex))
            print('\t\tlen(outerList) is {}'.format(len(outerList)))
            print('\t\tlen(outerList[outerIndex] is {}'.format(len(outerList[outerIndex])))
            print('\t\touterList[outerIndex][0].strip() is {}'.format(outerList[outerIndex][0].strip()))
            print('\t\touterList[outerIndex][len(innerList) - 1] is {}'.format(outerList[outerIndex][len(innerList) - 1]))
            
            outerIndex = outerIndex + 1
            
            innerList = []
            
        innerList.append(xmlLine)
        
    outerList.append(innerList)
    
    print('\t\touterIndex is {}'.format(outerIndex))
    print('\t\tlen(outerList) is {}'.format(len(outerList)))
    
    print('\t\tlen(outerList[outerIndex] is {}'.format(len(outerList[outerIndex])))
    print('\t\touterList[outerIndex][0].strip() is {}'.format(outerList[outerIndex][0].strip()))
    print('\t\touterList[outerIndex][len(innerList) - 2].strip() is {}'.format(outerList[outerIndex][len(innerList) - 2].strip()))


    for index in range(len(outerList)):
        print ('index', index)
        
        with open('patent.data-' + str(index), 'w') as file_handler:
            for item in outerList[index]:
                file_handler.write(item)
 
# print('\t\t is {}'.format())
# <?xml version="1.0" encoding="UTF-8"?>
# </us-patent-grant>
    
    print('\n\tEnd split_file function\n')

def test():
    
    print('\n\tBegin test function')
    
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print ("You have not split the file {} in the correct boundary!".format(fname))
            f.close()
        except:
            print("Could not find file {}. Check if the filename is correct!".format(fname))
            
    print('\n\tEnd test function\n')

print('\nBegin Python Module')

test()

print('End Python Module')

# FROM UDACITY BROWSER IDE
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # So, the problem is that the gigantic file is actually not a valid XML, because
# # it has several root elements, and XML declarations.
# # It is, a matter of fact, a collection of a lot of concatenated XML documents.
# # So, one solution would be to split the file into separate documents,
# # so that you can process the resulting files as valid XML documents.
# 
# import os
# import xml.etree.ElementTree as ET
# PATENTS = 'patent.data'
# 
# def get_root(fname):
#     tree = ET.parse(fname)
#     return tree.getroot()
# 
# 
# def split_file(filename):
#     """
#     Split the input file into separate files, each containing a single patent.
#     As a hint - each patent declaration starts with the same line that was
#     causing the error found in the previous exercises.
#     
#     The new files should be saved with filename in the following format:
#     "{}-{}".format(filename, n) where n is a counter, starting from 0.
#     """
#     
#     outerList =[]
#     outerIndex = 0
#     innerList =[]
# 
#     
#     with open(filename) as fIn:
#         originalFile = fIn.readlines()
#     
#     for i, xmlLine in enumerate(originalFile):
# 
#         if '<?xml version="1.0" encoding="UTF-8"?>' in xmlLine and i != 0:
#             
#             outerList.append(innerList)
#             
#             print('\t\touterIndex is {}'.format(outerIndex))
#             print('\t\tlen(outerList) is {}'.format(len(outerList)))
#             print('\t\tlen(outerList[outerIndex] is {}'.format(len(outerList[outerIndex])))
#             print('\t\touterList[outerIndex][0].strip() is {}'.format(outerList[outerIndex][0].strip()))
#             print('\t\touterList[outerIndex][len(innerList) - 1] is {}'.format(outerList[outerIndex][len(innerList) - 1]))
#             
#             outerIndex = outerIndex + 1
#             
#             innerList = []
#             
#         innerList.append(xmlLine)
#         
#     outerList.append(innerList)
#     
#     print('\t\touterIndex is {}'.format(outerIndex))
#     print('\t\tlen(outerList) is {}'.format(len(outerList)))
#     
#     print('\t\tlen(outerList[outerIndex] is {}'.format(len(outerList[outerIndex])))
#     print('\t\touterList[outerIndex][0].strip() is {}'.format(outerList[outerIndex][0].strip()))
#     print('\t\touterList[outerIndex][len(innerList) - 2].strip() is {}\n'.format(outerList[outerIndex][len(innerList) - 2].strip()))
# 
#     
#     for index in range(len(outerList)):
#         # print ('index', index)
#         # print ('filename', filename)
#         # print ('filename + "-" + str(index)', filename + "-" + str(index))
#         # print
#         
#         # with open('patent.data-1', 'w') as file_handler:
#         with open(filename + '-' + str(index), 'w') as file_handler:
#             for item in outerList[index]:
#                 file_handler.write(item)
#  
# def test():
#     split_file(PATENTS)
#     
#     # path = '.'
#     # for f in os.listdir(path):
#         # print f
#     
#     for n in range(4):
#         try:
#             fname = "{}-{}".format(PATENTS, n)
#             
#             f = open(fname, "r")
#             if not f.readline().startswith("<?xml"):
#                 print "You have not split the file {} in the correct boundary!".format(fname)
#             f.close()
#         except:
#             print "Could not find file {}. Check if the filename is correct!".format(fname)
# 
# test()





