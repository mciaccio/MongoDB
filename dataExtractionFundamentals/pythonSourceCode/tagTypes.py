#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
Before you process the data and add it into your database, you should check the
"k" value for each "<tag>" and see if there are any potential problems.

We have provided you with 3 regular expressions to check for certain patterns
in the tags. As we saw in the quiz earlier, we would like to change the data
model and expand the "addr:street" type of keys to a dictionary like this:
{"address": {"street": "Some value"}}
So, we have to see if we have such tags, and if we have any tags with
problematic characters.

Please complete the function 'key_type', such that we have a count of each of
four tag categories in a dictionary:
  "lower", for tags that contain only lowercase letters and are valid,
  "lower_colon", for otherwise valid tags with a colon in their names,
  "problemchars", for tags with problematic characters, and
  "other", for other tags that do not fall into the other three categories.
See the 'process_map' and 'test' functions for examples of the expected format.
"""

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

def key_type(element, keys): 

    if element.tag == "tag":
        # print("element.attrib is {}".format(element.attrib)) # forum 
        # print("element.attrib['k'] is {}".format(element.attrib['k'])) # forum
        
        # print("element.get('k') is {}\n".format(element.get('k'))) 
        myK = element.get('k')

        if problemchars.search(myK):
            if 'problemchars' in keys:
                # print("problemchars - myK - {}".format(myK)) # 
                # print("problemchars.search(myK) is {}\n".format(problemchars.search(myK))) # 
                keys['problemchars'] += 1
            else:
                keys['problemchars'] = 1
                
        elif lower_colon.search(myK):
            if 'lower_colon' in keys:  
                # print("lower_colon - myK - {}".format(myK)) # 
                # print("lower_colon.search(myK) is {}\n".format(lower_colon.search(myK))) # 
                keys['lower_colon'] += 1
            else:
                keys['lower_colon'] = 1
                
        elif lower.search(myK):
            if 'lower' in keys:
                # print("lower_colon - myK - {}".format(myK)) # 
                # print("lower.search(myK) is {}\n".format(lower.search(myK)))
                keys['lower'] += 1
            else:
                keys['lower'] = 1
                
        else:
            # print("other - myK - {}".format(myK)) # 
            keys['other'] += 1
                    
        # YOUR CODE HERE
        
    return keys

def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map('example.osm')
    pprint.pprint(keys)
    # assert keys == {'lower': 5, 'lower_colon': 0, 'other': 1, 'problemchars': 1}

if __name__ == "__main__":
    test()