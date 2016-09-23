# To experiment with this code freely you will have to run this code locally.
# Take a look at the main() function for an example of how to use the code.
# We have provided example json output in the other code editor tabs for you to
# look at, but you will not be able to run any queries through our UI.
import json
import requests
from sqlite3.dbapi2 import paramstyle


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


#return query_site(url, params)
def query_site(url, params, uid="", fmt="json"):
    
    print("\n\tBegin query_site function")
    
    print("\t\t url BEFORE is {}".format(url)) # http://musicbrainz.org/ws/2/artist/
    print("\t\t params BEFORE is {}".format(params)) # params is {'query': 'artist:Nirvana'}
    print("\t\t uid is {}".format(uid)) #
    print("\t\t fmt is {}\n".format(fmt)) # json
    
    # This is the main function for making queries to the musicbrainz API.
    # A json document should be returned by the query.
    params["fmt"] = fmt
    print("\t\t params AFTER is {}\n".format(params)) # {'fmt': 'json', 'query': 'artist:Nirvana'}
    #params1={"fmt":"json"}
    #print("\t\tparams1 is {}".format(params1))


    #r = requests.get(url + uid, params=params)
    r = requests.get(url + uid, params=params)
    
    print("\t\tr is {}".format(r))
    print("\t\tr.__class__.__name__ is {}\n".format(r.__class__.__name__)) #Response
    
#                                                                                                   :
    print("\t\tr.url AFTER is {}".format(r.url)) # http://musicbrainz.org/ws/2/artist/?query=artist%3ANirvana&fmt=json
    print("\t\tr.url.__class__.__name__ is {}\n".format(r.url.__class__.__name__)) # str
    
    # print ("requesting", r.url)

    if r.status_code == requests.codes.ok:
        print("\t\trequests.codes.ok\t{}".format(requests.codes.ok)) # 200
        print("\t\trequests.codes.ok.__class__.__name__\t{}".format(requests.codes.ok.__class__.__name__)) # int
        
        #print("\t\tr.json() is {}".format(r.json())) # 
        print("\t\tr.json().__class__.__name__ is {}\n".format(r.json().__class__.__name__)) #dict
        print("\tEnd query_site function\n")

        return r.json()
    else:
        r.raise_for_status()
        
    # print("\tEnd query_site function\n")


#results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
def query_by_name(url, params, name):
    
    print("\n\tBegin query_by_name function")
    
    print("\t\turl is {}".format(url)) # url is http://musicbrainz.org/ws/2/artist/
    print("\t\tparams is {}".format(params)) # {}
    print("\t\tparams.__class__.__name__ is {}\n".format(params.__class__.__name__)) # dict 
    
    print("\t\tquery_type is {}".format(query_type)) # global see above 
    print("\t\tquery_type.__class__.__name__ is {}\n".format(query_type.__class__.__name__)) # dict
    
    print("\t\tname - Nirvana is {}".format(name))

    # This adds an artist name to the query parameters before making
    # an API call to the function above.
    params["query"] = "artist:" + name
    
    print("\t\turl - ARTIST_URL is {}".format(url)) # http://musicbrainz.org/ws/2/artist/
    print("\t\tparams is {}".format(params)) # params is {'query': 'artist:Nirvana'}
    print("\t\tparams.__class__.__name__ is {}".format(params.__class__.__name__)) # dict
   
    print("\tEnd query_by_name function\n")
    
    return query_site(url, params)


def pretty_print(data, indent=4):
    
    print("\tBegin pretty_print function")

    # After we get our output, we can format it to be more readable
    # by using this function.
    if type(data) == dict:
        #print (json.dumps(data, indent=indent, sort_keys=True))
        pass
    else:
        print (data)
        
    print("\tEnd pretty_print function")

def main():
    
    print("\tBegin main function")
    
    '''
    Modify the function calls and indexing below to answer the questions on
    the next quiz. HINT: Note how the output we get from the site is a
    multi-level JSON document, so try making print statements to step through
    the structure one level at a time or copy the output to a separate output
    file.
    '''
    # {'fmt': 'json', 'query': 'artist:Nirvana'}
    # results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    #results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    #results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    # results = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")
    #print("results.__class__.__name__ is {}\n".format(results.__class__.__name__)) #dict
    
    print("xxxresults is {}".format(results))
    # dict_keys(['artists', 'offset', 'created', 'count'])
    print("xxxresults.keys() is {}\n".format(results.keys()))
    
    print("xxxresults['artists'] is {}".format(results['artists']))
    print("xxxresults['artists'].__class__.__name__ is {}".format(results['artists'].__class__.__name__)) # list
    print("xxxlen(results['artists']) is {}\n".format(len(results['artists']))) # 14
    
    print("xxxresults['artists'][0] is {}".format(results['artists'][0]))
    print("xxxlen(results['artists'][0]) is {}\n".format(len(results['artists'][0]))) # 12
    
    #dict_keys(['country', 'area', 'begin-area', 'aliases', 'sort-name', 'life-span', 'score', 'type', 'name', 'disambiguation', 'tags', 'id'])
    print("xxxresults['artists'][0].keys() is {}\n".format(results['artists'][0].keys())) # 12
    
    print("xxxlen(results['artists'][0]['disambiguation'] is {}\n".format(results['artists'][0]['disambiguation'])) # 12
    
    
    for i in range(len(results['artists'])):
        # print("aai is {}, results['artists'][i]['name'] is {}".format(i, results['artists'][i]['name']))
        if results['artists'][i]['name'] == "One Direction":
            print("bbi is {}, results['artists'][i]['name'] is {}".format(i, results['artists'][i]['name']))
            print("bbi is {}, results['artists'][i]['name'] is {}".format(i, results['artists'][i]['life-span']))
                
        # if 'disambiguation' in results['artists'][i]  and 'country' in results['artists'][i] and 'aliases' in results['artists'][i]:
        if 'disambiguation' in results['artists'][i]  and 'country' in results['artists'][i]:
            # print("i is {}, results['artists'][i]['name'] is {}".format(i, results['artists'][i]['name']))
            # print("i is {}, results['artists'][i]['country'] is {}".format(i, results['artists'][i]['country']))
            # print("i is {}, results['artists'][i]['aliases'] is {}".format(i, results['artists'][i]['aliases']))
            # print("i is {}, results['artists'][i]['disambiguation'] is {}\n".format(i, results['artists'][i]['disambiguation']))
            pass
    print()
    
    
    

    for i in range(len(results['artists'][0])):
        print("i is {}, results['artists'][i]['name'] is {}".format(i, results['artists'][i]['name']))
        if results['artists'][i]['name'] == "The Beatles":
            print("results['artists'][i].__class__.__name__ is {}".format(results['artists'][i].__class__.__name__)) # dict
            print("results['artists'][i].__class__.__name__ is {}".format(results['artists'][i].keys())) # dict
            print("results['artists'] is {}".format(results['artists']))
            if 'begin-area' in results['artists'][i]:
                print("results['results['artists'][i]['begin-area']['name'] is {}\n".format(results['artists'][i]['begin-area']['name'])) # dict


    print("\nxxxlen(results) is {}".format(len(results)))
    print("xxxlen(results['artists'] is {}".format(len(results['artists'])))
    print("xxxlen(results['artists'][0] is {}\n".format(len(results['artists'][0])))
    
    for i in range(len(results['artists'][0])):
        
        print("i is {}, results['artists'][i]['name'] is {}".format(i, results['artists'][i]['name']))
        if results['artists'][i]['name'] == "Queen":
            # print("results['artists'] is {}".format(results['artists']))
            print("results['artists'][i] is {}".format(results['artists'][i]))
            # ['type', 'area', 'score', 'aliases', 'tags', 'life-span', 'id', 'disambiguation', 'country', 'name', 'begin-area', 'sort-name']
            # print("\t\tresults['artists'][i].keys() is {}".format(results['artists'][i].keys()))
            if 'begin-area' in results['artists'][i]:
                print("results['results['artists'][i]['begin-area'] is {}\n".format(results['artists'][i]['begin-area'] ))
                # print("results['results['artists'][i]['begin-area']['name'] is {}\n".format(results['artists'][i]['begin-area']['name'])) # dict
                
    print()

    for i in range(len(results['artists'][0])):
        
        print("i is {}, results['artists'][i]['name'] is {}".format(i, results['artists'][i]['name']))
        if results['artists'][i]['name'] == "The Beatles":
            # print("results['artists'] is {}".format(results['artists']))
            # print("\tresults['artists'][i] is {}".format(results['artists'][i]))
            
            #['tags', 'score', 'name', 'type', 'id', 'area', 'life-span', 'aliases', 'country', 'begin-area', 'sort-name']
            # print("\tresults['artists'][i].keys() is {}".format(results['artists'][i].keys()))
            
            # print("results['artists'][i]['begin-area'] is {}".format(results['artists'][i]['begin-area']))
            #print("\tresults['artists'][i]['aliases'] is {}".format(results['artists'][i]['aliases']))  # list of dictionaries
            #print("\tlen(results['artists'][i]['aliases']) is {}".format(len(results['artists'][i]['aliases']))) # 13
            
            if 'aliases' in results['artists'][i]:
                # iterate through the list 
                for j in range(len(results['artists'][i]['aliases'])):
                    # print("j is {} results['artists'][i]['aliases'][j].keys() is {}".format(j, results['artists'][i]['aliases'][j].keys()))
                    # print("results['artists'][i]['aliases'][j] is {}".format(results['artists'][i]['aliases'][j]))
                    if results['artists'][i]['aliases'][j]['locale'] == 'es':
                        print("\tresults['artists'][i]['aliases'][j]['locale'] is {}".format(results['artists'][i]['aliases'][j]['locale']))
                        print("\tresults['artists'][i]['aliases'][j]['name'] is {}".format(results['artists'][i]['aliases'][j]['name']))
                    # print("\t\tresults['results['artists'][j]['aliases'] is {}".format(results['artists'][j]['aliases']))
                    # print("\t\tresults['len(results['artists'][j]['aliases']) is {}".format(len(results['artists'][j]['aliases'])))
                    #print("\t\tresults['results['artists'][j]['aliases'] is {}".format(results['artists'][j]['aliases']))

                


    
    
    nirvanaJsonKeys = results.keys()
    #dict_keys(['artists', 'offset', 'count', 'created'])
    # print("\nnirvanaJsonKeys is {}".format(nirvanaJsonKeys))
    # print("nirvanaJsonKeys.__class__.__name__ is {}\n".format(nirvanaJsonKeys.__class__.__name__)) #dict_keys
    
    #print("len(results[artists]) is {}".format(len(results['artists'])))
    #print("results[artists] is {}".format(results['artists']))
    #print("results[artists][0] is {}\n".format(results['artists'][0]))
    #print("results[artists][0]['name'] is {}\n".format(results['artists'][0]['name']))
    #print("results[artists][0]['name'] is {}\n".format(results['artists'][24]['name']))
    
    # for i in range(len(results['artists'][0])):
        # print("is {}".format(results['artists'][i]['name']))
        # if results['artists'][i]['name'] == "The Beatles":
            # print("results['artists'][i].__class__.__name__ is {}".format(results['artists'][i].__class__.__name__)) # dict
            # print("results['artists'][i].__class__.__name__ is {}".format(results['artists'][i].keys())) # dict
            #print("results['artists'] is {}".format(results['artists']))
            # if 'begin-area' in results['artists'][i]:
                # print("results['results['artists'][i]['begin-area']['name'] is {}\n".format(results['artists'][i]['begin-area']['name'])) # dict
    
    # print("results[artists] is {}\n".format(results['artists'])) # too long
    #print("results[artists].__class__.__name__ is {}".format(results['artists'].__class__.__name__)) #list
    # print("results[artists][0] is {}\n".format(results['artists'][0])) # too long
    #print("results[artists][0].__class__.__name__ is {}\n".format(results['artists'][0].__class__.__name__)) # dict
    
    # get the keys of the dict - nested in results['artists'][0]
    # (['life-span', 'begin-area', 'aliases', 'country', 'disambiguation', 'type', 'name', 'id', 'sort-name', 'score', 'area', 'tags'])
    # nirvanaJson_artistsListKeys = results['artists'][0].keys()
    #print("nirvanaJson_artistsListKeys is {}".format(nirvanaJson_artistsListKeys))
    # use on of the keys 
    #print("results['artists'][0]['country'] is {}\n".format(results['artists'][0]['country'])) # US
    
    #print("results['artists'][0] is {}".format(results['artists'][0]))
    # print("results['artists'][0]['aliases'] is {}".format(results['artists'][0]['aliases']))
    #print("results['artists'][0]['aliases'].__class__.__name__ is {}\n".format(results['artists'][0]['aliases'].__class__.__name__)) # list
    
    #{'begin-date': None, 'type': None, 'end-date': None, 'sort-name': 'Nirvana US', 'locale': None, 'primary': None, 'name': 'Nirvana US'}
    # print("results['artists'][0]['aliases'][0] is {}".format(results['artists'][0]['aliases'][0]))
    # print("results['artists'][0]['aliases'][0].__class__.__name__ is {}\n".format(results['artists'][0]['aliases'][0].__class__.__name__)) # dict
    
    # print("results['artists'][0]['aliases'][0]['sort-name'] is {}".format(results['artists'][0]['aliases'][0]['sort-name'])) # Nirvana US
    # print("results['artists'][0]['aliases'][0]['sort-name'].__class__.__name__ is {}\n".format(results['artists'][0]['aliases'][0]['sort-name'].__class__.__name__)) # str
    

    # print("results[offset] is {}".format(results['offset'])) # 0
    # print("results[offset].__class__.__name__ is {}\n".format(results['offset'].__class__.__name__)) #int
    
    # print("results[count] is {}".format(results['count'])) # 14
    # print("results[count].__class__.__name__ is {}\n".format(results['count'].__class__.__name__))
    
    # print("results[created] is {}".format(results['created'])) # 2016-09-21T13:56:44.947Z
    # print("results[created].__class__.__name__ is {}\n".format(results['created'].__class__.__name__)) # str

    #pretty_print(results)

    artist_id = results["artists"][1]["id"]
    # print("results[artists].__class__.__name__ is {}".format(results['artists'].__class__.__name__)) #list
    # print("results[artists][1] is {}".format(results['artists'][1])) # dict
    # print("results[artists][1][id] is {}".format(results['artists'][1]['id'])) #9282c8b4-ca0b-4c6b-b7e3-4f7762dfc4d6
    #print("results[artists][1][country] is {}\n".format(results['artists'][1]['country'])) # GB
    #print("results[artists][1][begin-area] is {}".format(results['artists'][1]['begin-area'])) # dict
    #print("results[artists][1][begin-area][id] is {}\n".format(results['artists'][1]['begin-area']['id'])) # f03d09b3-39dc-4083-afd6-159e3f0d462f
 

    #print ("\nARTIST:")
    #pretty_print(results["artists"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    json.dumps(artist_data, indent=4, sort_keys=True)

    # print("artist_data is {}".format(artist_data)) # too long dict
    print("artist_data.keys() is {}".format(artist_data.keys())) # dict_keys
    # print("artist_data['releases'] is {}".format(artist_data['releases'])) # list too long
    #print("len(artist_data['releases'][0]) is {}\n".format(len(artist_data['releases'][0]))) # 13
    # print("artist_data['releases'][0] is {}".format(artist_data['releases'][0])) # dict too long
    #len(artist_data['releases'][0])
    
    #print("artist_data['releases'][0] is {}".format(artist_data['releases'][0])) # dict too long
    #print("artist_data['releases'][0].__class__.__name__ is {}".format(artist_data['releases'][0].__class__.__name__)) # dict 
    #print("len(artist_data['releases'][0]) is {}".format(len(artist_data['releases'][0]))) # 13
    #print("artist_data['releases'][0]['title'] is {}\n".format(artist_data['releases'][0]['title'])) # To Markos III
    
    
    releases = artist_data["releases"]
    print("artist_data.__class__.__name__ is {}".format(artist_data.__class__.__name__)) # dict
    print("releases.__class__.__name__ is {}".format(releases.__class__.__name__)) # list
    print("release.__class__.__name__ is {}".format(releases)) #

    # print ("\nONE RELEASE:")
    # pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]
    print("release_titles is {}".format(release_titles)) # list
    print("release_titles.__class__.__name__ is {}".format(release_titles.__class__.__name__)) # list

    # print ("\nALL TITLES:")
    # for t in release_titles: # iterate through the list
        #print (t)
      #  pass
        
    print("\tEnd mainfunction\n")

print("\nBegin Python Module")
print("End Python Module\n")
if __name__ == '__main__':
    main()
