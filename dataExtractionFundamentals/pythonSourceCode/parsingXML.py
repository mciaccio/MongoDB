

import os
import xml.etree.ElementTree

# download the xml data file
# http://www.biomedcentral.com/2052-1847/5/9/abstract - website 
# http://www.biomedcentral.com/content/download/xml/2052-1847-5-9.xml - xml 

# python doc
# https://docs.python.org/3.5/library/xml.etree.elementtree.html

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "2052-1847-5-9.xml"

biomedCentralXML = os.path.join(DATADIR, DATAFILE)

def tellMe(variable, item):
    print("\tBegin tellMe function")
    print("\t\t{} is {}".format(variable, item))
    print("\t\t{}.__class__.__name__ is {}".format(variable, item.__class__.__name__))
    print("\t\t{}.tag is {}".format(variable, item.tag))
    if item.text is not None:
        print("\t\t{}.text is {}".format(variable, item.text.rstrip()))
 
    if item.tail is not None:
        print("\t\t{}.tail is {}".format(variable, item.tail.rstrip()))
        print("\t\t{}.tail.__class__.__name__ is {}".format(variable, item.tail.__class__.__name__))
        # print("\t\t{}.tail is {}".format(variable, item.tail.rstrip()))
    print("\t\t{}.attrib is {}".format(variable, item.attrib))
    print("\t\t{} keys is {}".format(variable, item.keys()))
    print("\t\t{} items is {}".format(variable, item.items()))
    
    print("\t\t{}.iter() is {}".format(variable, item.iter()))
    print("\t\t{}.iter.__class__.__name__ is {}".format(variable, item.iter.__class__.__name__))
    
    print("\t\t{}.itertext() is {}".format(variable, item.itertext()))
    print("\t\t{}.itertext().__class__.__name__ is {}".format(variable, item.itertext().__class__.__name__))
    
    print("\tEnd tellMe function\n")


print("\nBegin parseingXML module")

# print("\txml is {}".format(xml))
# print("\txml.__name__ from import is {}\n".format(xml.__name__)) # xml
# 
# print("\txml.etree is {}".format(xml.etree))
# print("\txml.etree.__name__ from import is {}\n".format(xml.etree.__name__)) # xml.etree

# print("\txml.etree is {}".format(xml.etree.ElementTree))
print("\txml.etree.__name__ from import is {}\n".format(xml.etree.ElementTree.__name__)) # ElementTree ElementTree

myTree = xml.etree.ElementTree.parse(biomedCentralXML)

# print("\tmyTree is {}".format(myTree))
print("\tmyTree.__class__.__name__ is {}\n".format(myTree.__class__.__name__)) # ElementTree ElementTree

#          myTree.findall('.') is [<Element 'art' at 0x101e15228>]
print("\tmyTree.findall('.') is {}".format(myTree.findall('.')))
# print("\tmyTree.findall('.').__class__.__name__ is {}\n".format(myTree.findall('.').__class__.__name__)) # list list

#         myTree.findall('./') is [<Element 'ui' at 0x101c1cb88>, <Element 'ji' at 0x101c1cbd8>, <Element 'fm' at 0x101c1cc28>, <Element 'bdy' at 0x101c277c8>, <Element 'bm' at 0x101c55638>]
print("\tmyTree.findall('./') is {}".format(myTree.findall('./')))
#vprint("\tmyTree.findall('./').__class__.__name__ is {}\n".format(myTree.findall('./').__class__.__name__)) # list list

print("\tmyTree.findall('./ui') is {}".format(myTree.findall('./ui')))
print("\tmyTree.findall('./ji') is {}".format(myTree.findall('./ji')))
print("\tmyTree.findall('./fm') is {}".format(myTree.findall('./fm')))
print("\tmyTree.findall('./fm/bibl') is {}".format(myTree.findall('./fm/bibl')))
print("\tmyTree.findall('./fm/bibl/title') is {}".format(myTree.findall('./fm/bibl/title')))
print("\tmyTree.findall('./fm/bibl/title/p') is {}".format(myTree.findall('./fm/bibl/title/p')))
print("\tmyTree.findall('./bdy') is {}".format(myTree.findall('./bdy')))
print("\tmyTree.findall('./bm') is {}".format(myTree.findall('./bm')))
print("\tmyTree.findall('./bm').__class__.__name__ is {}\n".format(myTree.findall('./bm').__class__.__name__)) # list list

myTreeRoot = myTree.getroot()
print("\tmyTreeRoot.tag is {}".format(myTreeRoot.tag)) # art


#        myTreeRoot is <Element 'art' at 0x101c223b8>
# print("\tmyTreeRoot is {}".format(myTreeRoot))
# print("\tmyTreeRoot.__class__.__name__ is {}\n".format(myTreeRoot.__class__.__name__)) # Element Element

# iterate through, drill down,  the myTreeRoot child(ren) ui, ji, (fm - bib)l, bdy, bm
# fine the title
for child in myTreeRoot: 
    if child.tag == 'fm':
        for childL1 in child:
            # print("\nchildL1.tag is {}".format(childL1.tag))
            if childL1.tag == 'bibl':
                for childL2 in childL1: 
                    if childL2.tag == 'title':
                        for childL3 in childL2: 
                            if childL3.tag == 'p':
                                print("\tchild.tag is {}".format(child.tag))
                                print("\t\tchildL1.tag is {}".format(childL1.tag))
                                print("\t\t\tchildL2.tag is {}".format(childL2.tag))
                                print("\t\t\t\tchildL3.tag is {}".format(childL3.tag)) # p
#                                              childL3.text is Standardization of the functional syndesmosis widening by dynamic U.S examination
                                print("\t\t\t\tchildL3.text is {}".format(childL3.text))          
 
        
myTreeRootSlash = myTreeRoot.find('./')
# print("\nmyTreeRootSlash.__class__.__name__ is {}\n".format(myTreeRootSlash.__class__.__name__)) # Element

# tellMe("myTreeRootSlash", myTreeRootSlash)

# Nothing
for myTreeRootSlashElement in myTreeRootSlash:
    tellMe("myTreeRootSlashElement", myTreeRootSlashElement)
    
# drill down into xml <fm> tag  
myTreeRootSlash_FM = myTreeRoot.find('./fm')


for dochead in myTreeRootSlash_FM.iter('dochead'):
    print("\tdochead.tag is {}".format(dochead.tag))
    print("\tdochead.text is {}\n".format(dochead.text))

# tellMe("myTreeRootSlash_FM", myTreeRootSlash_FM)

for elementFM in myTreeRootSlash_FM:
    if elementFM.tag == 'bibl':
        print("\telementFM.tag is {}".format(elementFM.tag)) # bibl
        
        for element_FM_BIBL in elementFM:
            # print("125........................element_FM_BIBL.tag is {}".format(element_FM_BIBL.tag))
            if element_FM_BIBL.tag == 'title':
                print("\t\telement_FM_BIBL.tag is {}".format(element_FM_BIBL.tag)) # title
                for element_FM_BIBL_TITLE in element_FM_BIBL:
                    print("\t\t\telement_FM_BIBL_TITLE.tag is {}".format(element_FM_BIBL_TITLE.tag)) # p
                    print("\t\t\telement_FM_BIBL_TITLE.text is {}\n".format(element_FM_BIBL_TITLE.text.rstrip())) # Standardization of the functional ...

myTreeRootSlash_FM_BIBL = myTreeRoot.find('./fm/bibl')

for p in myTreeRootSlash_FM_BIBL.iter('p'): #WORKS
    # print("p is {}".format(p)) # Element
    # print("p.tag is {}".format(p.tag))
    print("p.text is {}".format(p.text))
    # print("WORKS")
    pass
print()

 
for elementFM_BIBL in myTreeRootSlash_FM_BIBL:
    # print("\telementFM_BIBL.tag is {}".format(elementFM_BIBL.tag))
    if  elementFM_BIBL.tag == 'title':
        print("\telementFM_BIBL.tag is {}".format(elementFM_BIBL.tag)) # title
        for element_FM_BIBL_Title in elementFM_BIBL:
            print("\t\ttelement_FM_BIBL_Title.tag is {}".format(element_FM_BIBL_Title.tag))
            print("\t\ttelement_FM_BIBL_Title.text is {}\n".format(element_FM_BIBL_Title.text))
      
myTreeRootSlash_FM_BIBL_Title = myTreeRoot.find('./fm/bibl/title')
 
for elementFM_BIBL_Title in myTreeRootSlash_FM_BIBL_Title:
    print("\telementFM_BIBL.tag is {}".format(elementFM_BIBL_Title.tag))
    print("\telementFM_BIBL.tag is {}\n".format(elementFM_BIBL_Title.text)) 

authors = []
data = {}
tempINSR = []

 
# looking for fnm, snm, email, one or more insr iid values
# position where the filed we are looking for is - <au
# <fm>
#   <dochead>Research</dochead>
#   <bibl>
#    <title>
#      <p>Standardization of the functional syndesmosis widening by dynamic U.S examination</p>
#    </title>
#    <aug>                                                   ***             ***
#      <au id="A6"><snm>Mann</snm><fnm>Gideon</fnm><insr iid="I3"/><insr iid="I5"/><email>gideon.mann.md@gmail.com</email></au>
#      
# note '<au'
#                                                     ***              ***
# position where the field we are looking for is 
# find all authors located right here, findall NOT find 
for author in myTreeRoot.findall('./fm/bibl/aug/au'):
    # print("\txx.tag is {}".format(xx.tag)) 
    # print("\txx.text is {}".format(xx.text)) 
 
    # find because there is only one first name per author
    fnm = author.find('fnm')
    if fnm is not None:
        print("\tfnm.text is {}".format(fnm.text))
        data['fnm'] = fnm.text

    snm = author.find('snm')
    if snm is not None:
        print("\tsnm.text is {}".format(snm.text))
        data['snm'] = snm.text
            
    # how to handle if there is more than one 
    # findall not find, then iterate through them with for loop <--------------------- findall example 
    email = author.findall('email')
    for anEmail in email:
        # print("\tanEmail is {}".format(anEmail))
        # print("\tanEmail.__class__.__name__ is {}".format(anEmail.__class__.__name__))
        # print("\tanEmail.tag is {}".format(anEmail.tag))
        print("\tanEmail.text is {}".format(anEmail.text))

    email = author.find('email') # <-------------------------------------find example
    if email is not None:
        print("\temail.text is {}".format(email.text))
        data['email'] = email.text

    # findall not find because there is more than one iid per insr
    # <insr iid="I3"/><insr iid="I5"/>
    # note attrib to get the attribute values of <insr iid="I3"/><insr iid="I5"/> 
    insr = author.findall('./insr') # Could be more than 1 - iterate through and find out <--------------------- findall example
    for institutionalRelationshipTag in insr: 
        # print("183\tinstitutionalRelationshipTag.tag is {}".format(institutionalRelationshipTag.tag)) #
        # it is a dictionary
        print("\t\tinstitutionalRelationshipTag.attrib is {}".format(institutionalRelationshipTag.attrib)) #
        # get the dictionary value from the dictionary key
        tempINSR.append(institutionalRelationshipTag.attrib['iid'])
        data['insr'] = tempINSR
        print("\t\tdata['insr'] is {}".format(data['insr'])) #

    tempINSR = []
        
    authors.append(data)
    data = {}
        
    print() 
        
# My method 
#     for authorElement in author:
#         # print("\tauthorElement is {}".format(authorElement)) 
#         # print("\tauthorElement.__class.__name__ is {}".format(authorElement.__class__.__name__)) 
#         print("\tauthorElement.tag is {}".format(authorElement.tag)) 
#         print("\tauthorElement.text is {}".format(authorElement.text)) 
#         
#         if authorElement.tag == 'fnm':
#             data['fnm'] = authorElement.text
#         
#         if authorElement.tag == 'snm':
#             data['snm'] = authorElement.text
#         
#         if authorElement.tag == 'email':
#             data['email'] = authorElement.text
#             
#         # print("data is {}\n".format(data))
#         authors.append(data)
#         data = {}

    
print("authors is {}".format(authors))
print("len(authors) is {}".format(len(authors)))
 
print("\nEnd parseingXML module")

 # BROWSER CODE udacity.com browser - make shift development environment
# def get_authors(root):
#     tempINSR = []
#     authors = []
#     
#     data = {
#             "fnm": None,
#             "snm": None,
#             "email": None,
#             "insr": []
#     }
# 
#     for author in root.findall('./fm/bibl/aug/au'):
#         fnm = author.find('fnm')
#         if fnm is not None:
#             print("\n\tfnm.text is {}".format(fnm.text))
#             data['fnm'] = fnm.text
# 
#         snm = author.find('snm')
#         if snm is not None:
#             #print("\tsnm.text is {}".format(snm.text))
#             data['snm'] = snm.text
#             
#         email = author.find('email')
#         if email is not None:
#             # print("\temail.text is {}".format(email.text))
#             data['email'] = email.text
# 
#         insr = author.findall('./insr') 
#     
#         for institutionalRelationshipTag in insr: 
#             # print("183\tinstitutionalRelationshipTag.tag is {}".format(institutionalRelationshipTag.tag)) #
#             # print("49institutionalRelationshipTag.attrib is {}".format(institutionalRelationshipTag.attrib)) #
#             tempINSR.append(institutionalRelationshipTag.attrib['iid'])
#             print ("51tempINSR is {}".format(tempINSR))
#             data['insr'] = tempINSR
#             
#         tempINSR = []
#         
#         # YOUR CODE HERE
#         print ("data is {}".format(data))
#         authors.append(data)
#         data = {}
#         # print ("authors[0] is {}\n".format(authors[0]))
#         print ("authors is {}\n".format(authors))
#         # assert 1 == 5
# 
# 
#     return authors

