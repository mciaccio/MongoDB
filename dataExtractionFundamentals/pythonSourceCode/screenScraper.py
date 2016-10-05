
import os
import bs4
# from bs4 import BeautifulSoup

def getCarrierList(mySoup):
    print("\n\tBegin getCarrierList function")

    carrierList = []
    carrier_list = mySoup.find(id='CarrierList')
    
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
    airport_list = mySoup.find(id='AirportList') 
    
    # print("\t\tairport_list is {}\n".format(airport_list))
    
    for airport in airport_list.find_all('option'):
        # <option value="AK8"> - Zips, AK: Zips Airport</option>
        print("\t\tairport['value'] is {}".format(airport['value']))
        airportList.append(airport['value']) # UA
        # print("\t\tcarrier.attrs is {}".format(carrier.attrs)) # {'value': 'UA'}
        print("\t\tairport.text is {}\n".format(airport.text)) # United Air Lines
    
    print("\t\tairportList is {}".format(airportList))
    
    print("\tEnd getAirportList function")


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
print("mySoup.__class__.__name__ is {}".format(mySoup.__class__.__name__))
getCarrierList(mySoup)
getAirportList(mySoup)


 


