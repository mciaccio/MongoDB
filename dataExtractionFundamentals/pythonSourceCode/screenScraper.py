
import os
import bs4
import requests # Unresolved import: requests

def example1():
    print("\n\tBegin example1 function")
    r = requests.get('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2')
    print("\t\tr is {}".format(r)) # 
    print("\t\tr.__class__.__name__ is {}".format(r.__class__.__name__)) # 
    # print("\t\tr.text is {}".format(r.text)) # 
    print("\t\tr.text.__class__.__name__ is {}".format(r.text.__class__.__name__)) # 

    print("\n\tEnd example1 function")

    

# from bs4 import BeautifulSoup

# URL - http://www.transtats.bts.gov/Data_Elements.aspx?Data=2

def getCarrierList(mySoup):
    print("\n\tBegin getCarrierList function")

    carrierList = []
    
    # <select name="CarrierList" id="CarrierList" class="slcBox" style="width:450px;">
    # <option value="All">All U.S. and Foreign Carriers</option>
    carrier_list = mySoup.find(id="CarrierList")
    # <select name="CarrierList" id="CarrierList" 
    
    # carrier_list is 
    # <select class="slcBox" id="CarrierList" name="CarrierList" style="width:450px;">
    # <option value="UA">United Air Lines </option>
    # <option selected="selected" value="VX">Virgin America</option>
    # </select>
    
    # print("\t\tcarrier_list is {}\n".format(carrier_list))
    
    for carrier in carrier_list.find_all('option'):
        # carrier is <option value="NK">Spirit Air Lines</option>
        # print("\t\tcarrier.__class__.__name__ is {}".format(carrier.__class__.__name__)) # Tag
        # print("\t\tcarrier is {}".format(carrier))
        # print("\t\tcarrier.name is {}".format(carrier.name)) # option
        print("\t\tcarrier['value'] is {}".format(carrier['value']))
        carrierList.append(carrier['value']) # UA
        # print("\t\tcarrier.attrs is {}".format(carrier.attrs)) # {'value': 'UA'}
        print("\t\tcarrier.text is {}\n".format(carrier.text)) # United Air Lines
    
    print("\t\tcarrierList is {}".format(carrierList))
    
    print("\tEnd getCarrierList function")
    
    
def getAirportList(mySoup):
    print("\n\tBegin getAirportList function")

    airportList = []
    airport_list = mySoup.find(id="AirportList") 
    # <select name="AirportList" id="AirportList" 
    
    # print("\t\tairport_list is {}\n".format(airport_list))
    
    for airport in airport_list.find_all('option'):
        # print("\t\tairport.__class__.__name__ is {}".format(airport.__class__.__name__)) # Tag

        # <option value="AK8"> - Zips, AK: Zips Airport</option>
        print("\t\tairport['value'] is {}".format(airport['value']))
        airportList.append(airport['value']) # UA
        # print("\t\tcarrier.attrs is {}".format(carrier.attrs)) # {'value': 'UA'}
        print("\t\tairport.text is {}\n".format(airport.text)) # United Air Lines
    
    print("\t\tairportList is {}".format(airportList))
    
    print("\tEnd getAirportList function")

def getExample(mySoup):
    print("\n\tBegin getExample function") 
    # mySoup static form a fle on the MAC - virgin_and_logan_airport.html
    # static 
    myEventValidation = mySoup.find(id="__EVENTVALIDATION") 
    print("\t\tmyEventValidation['value'][:15] is {}".format(myEventValidation['value'][:15])) # /wEdAMYJX3CuRnY
    # static
    myViewState = mySoup.find(id="__VIEWSTATE")
    print("\t\tmyViewState['value'] is {}".format(myViewState['value'][:11])) # /wEPDwULLTE
    # static
    myViewStateGenerator = mySoup.find(id="__VIEWSTATEGENERATOR")
    print("\t\tmyViewStateGenerator['value'] is {}\n".format(myViewStateGenerator['value'][:11]))  # 8E3A4798
    
    
    r = requests.get('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2')
    # real time current values
    realTimeSoup = bs4.BeautifulSoup(r.text,"html.parser")
    # real time current values
    myRTEventValidation = realTimeSoup.find(id="__EVENTVALIDATION") 
    myRTEventValidationValue = myRTEventValidation['value']  
    print("\t\tmyRTEventValidationValue is {}".format(myRTEventValidationValue[:15])) # /wEdAMYJX3CuRnY DIFFERENT /wEdAMYJCDMCT3a
    # real time current values
    myRTViewState = realTimeSoup.find(id="__VIEWSTATE") 
    myRTViewStateValue = myRTViewState['value']
    print("\t\tmyRTViewStateValue[:11] is {}".format(myRTViewStateValue[:11])) # /wEPDwULLTE DIFFERENT  /wEPDwULLTE
    # real time current values
    myRTViewStateGenerator = realTimeSoup.find(id="__VIEWSTATEGENERATOR") 
    myRTViewStateGeneratorValue = myRTViewStateGenerator['value']  
    print("\t\tmyRTViewStateGeneratorValue[:11] is {}\n".format(myRTViewStateGeneratorValue[:11])) # 8E3A4798  SAME 8E3A4798
    
    r = requests.post('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2',
                      data = {
                          'AirportList' : 'BOS',
                          'CarrierList' : 'VX',
                          'Submit' : 'Submit',
                          '__EVENTTARGET' : '', 
                          '__EVENTARGUMENT' : '',
                          '__EVENTVALIDATION' : myRTEventValidationValue, 
                          '__VIEWSTATE' : myRTViewStateValue,
                          '__VIEWSTATEGENERATOR' : myRTViewStateGeneratorValue
                          })
  
    print("\t\tr is {}".format(r))
    # print("\t\tr.__class__.__name__ is {}".format(r.__class__.__name__))
    # print("r.text is {}".format(r.text))
    # print("117\t\tr.text.__class__.__name__ is {}".format(r.text.__class__.__name__))
    fNo = open('noSession.html', 'w') # did not work 
    fNo.write(r.text) # did not work 
    
    # A syntax error has occurred.
    # The reason is probably that you have used a bookmarked URL with an invalid parameter.
    # Please click TranStats on the sidebar to start from the TranStats homepage.
    # If the problem persists, please contact ritainfo@dot.gov.
    
    # Finally the real work - Use this Example 
    # Fix the above error using session 
    # This time session - Maintain session state this worked
    # This time session get and session post
    # First use the generic URL - capture the parameter value pairs
    s = requests.Session()
    r = s.get('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2',)
    
    myRTSessionSoup = bs4.BeautifulSoup(r.text,"html.parser")
    
    myRTSessionEventValidation = myRTSessionSoup.find(id="__EVENTVALIDATION") 
    myRTSessionEventValidationValue = myRTSessionEventValidation['value']  
    print("\t\tmyRTSessionEventValidationValue is {}".format(myRTSessionEventValidationValue[:15])) # /wEdAMYJX3CuRnY DIFFERENT /wEdAMYJCDMCT3a

    myRTSessionViewState = myRTSessionSoup.find(id="__VIEWSTATE") 
    myRTSessionViewStateValue = myRTSessionViewState['value']  
    print("\t\tmyRTSessionViewStateValue is {}".format(myRTSessionViewStateValue[:11])) # /wEPDwULLTE SAME

    myRTSessionViewStateGenerator  = myRTSessionSoup.find(id="__VIEWSTATEGENERATOR") 
    myRTSessionViewStateGeneratorValue = myRTSessionViewStateGenerator['value']  
    print("\t\tmyRTSessionViewStateGeneratorValue is {}".format(myRTSessionViewStateGeneratorValue[:11])) # 

    # Now use the required captured parameter value pairs
    # This worked 
    r = s.post('http://www.transtats.bts.gov/Data_Elements.aspx?Data=2',
                      data = {
                          'AirportList' : 'BOS',
                          'CarrierList' : 'VX',
                          'Submit' : 'Submit',
                          '__EVENTTARGET' : '', 
                          '__EVENTARGUMENT' : '',
                          '__EVENTVALIDATION' : myRTSessionEventValidationValue, 
                          '__VIEWSTATE' : myRTSessionViewStateValue,
                          '__VIEWSTATEGENERATOR' : myRTSessionViewStateGeneratorValue
                          })
    
    # Open html in browser - correct data populated in browser
    fS = open('sessionOut.html', 'w') # Worked!! Session!!
    fS.write(r.text) # # Worked!! Session!!
    # how we knew it was a post request 
    # <form method="post" action="./Data_Elements.aspx?Data=2" id="form1">

    print("\tEnd getExample function")
    
    
def myFunction():
    print("\tBegin myFunction function")
        
    s = requests.Session()

    r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    
    eventvalidation_value = soup.find(id = '__EVENTVALIDATION')['value']
    viewstate_value = soup.find(id = '__VIEWSTATE')['value']
    viewstategenerator_value = soup.find(id = '__VIEWSTATEGENERATOR')['value']
    
    print("\t\teventvalidation_value is {}".format(eventvalidation_value))
    print("\t\tviewstate_value is {}".format(viewstate_value))
    print("\t\tviewstategenerator_value is {}".format(viewstategenerator_value))

    
    r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                     data={'AirportList' : 'BOS',
                           'CarrierList' : 'VX',
                           'Submit' : 'Submit',
                           '__EVENTTARGET' : '',
                           '__EVENTARGUMENT' : '',
                           '__VIEWSTATEGENERATOR' : viewstategenerator_value,
                           '__EVENTVALIDATION' : eventvalidation_value,
                           '__VIEWSTATE' : viewstate_value})
    
    # f = open('carrier_test_request.html','w') # WORKED
    # f.write(r.text) # WORKED
    
        
    print("\tEnd myFunction function")
    
    
    
        
def myFunction1():
    print("\tBegin myFunction function")
        
    s = requests.Session()

    r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    
    eventvalidation_value = soup.find(id = '__EVENTVALIDATION')['value']
    viewstate_value = soup.find(id = '__VIEWSTATE')['value']
    viewstategenerator_value = soup.find(id = '__VIEWSTATEGENERATOR')['value']
    
    print("\t\teventvalidation_value is {}".format(eventvalidation_value))
    print("\t\tviewstate_value is {}".format(viewstate_value))
    print("\t\tviewstategenerator_value is {}".format(viewstategenerator_value))

    
    r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                     data={'AirportList' : 'BOS',
                           'CarrierList' : 'VX',
                           'Submit' : 'Submit',
                           '__EVENTTARGET' : '',
                           '__EVENTARGUMENT' : '',
                           '__VIEWSTATEGENERATOR' : viewstategenerator_value,
                           '__EVENTVALIDATION' : eventvalidation_value,
                           '__VIEWSTATE' : viewstate_value})
    
    # f = open('carrier_test_request.html','w')
    # f.write(r.text)
    
        
    print("\tEnd myFunction function")

DATADIR = "/Users/Menfi/Documents/gitBaseDirectory/MongoDB/dataExtractionFundamentals/dataFiles"
DATAFILE = "virgin_and_logan_airport.html"

virginLoganData = os.path.join(DATADIR, DATAFILE)

print("\nbs4 is {}".format(bs4))
print("bs4.__name__ is {}".format(bs4.__name__))
print("bs4.__version__ is {}".format(bs4.__version__))
print("bs4..__all__ is {}".format(bs4.__all__))
print("bs4.BeautifulSoup.__class__.__name__ is {}".format(bs4.BeautifulSoup.__class__.__name__))
print("virginLoganData.__class__.__name__ is {}".format(virginLoganData.__class__.__name__))

mySoup = bs4.BeautifulSoup(open(virginLoganData),"html.parser")
# mySoup = bs4.BeautifulSoup(open(virginLoganData),"lxml") # instructor used lxml note lxml
print("mySoup.__class__.__name__ is {}".format(mySoup.__class__.__name__))
getCarrierList(mySoup)
getAirportList(mySoup)
getExample(mySoup)
# myFunction()
# example1()



# My python code from the udacity browser environmnet
# instructor used mySoup = BeautifulSoup(open(html_page),"lxml") - note 'lxml'
# def extract_data(page):
#     data = {"eventvalidation": "",
#             "viewstate": ""}
#             
#     with open(page, "r") as html:
#         print("page is {}".format(page)) #
#         print("page.__class__.__name__ is {}".format(page.__class__.__name__)) # str 
#         
#         mySoup = BeautifulSoup(open(html_page),"html.parser")
#         
#         myEventValidation = mySoup.find(id="__EVENTVALIDATION")
#         # print("myEventValidation['value'] is {}".format(myEventValidation['value']))
#         print("myEventValidation['value'][:15] is {}".format(myEventValidation['value'][:15]))
#         data['eventvalidation'] = myEventValidation['value']
#         
#         myViewState = mySoup.find( id="__VIEWSTATE")
#         # print("myEventValidation['value'] is {}".format(myEventValidation['value']))
#         print("myViewState['value'][:15] is {}".format(myViewState['value'][:11]))
#         data['viewstate'] = myViewState['value']
#         
# 
#         # do something here to find the necessary values
#         pass
# 
#     return data
