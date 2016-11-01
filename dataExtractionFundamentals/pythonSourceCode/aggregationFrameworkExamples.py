
# Aggregation Framework - MondoDB built-in analytics tool
# Pipeline - series of stages - the pipeline List 
# input to the first stage is the MongoDB Collection
#
# '$group', '$sort', '$sum', '$project', '$match', '$skip', '$limit', '$unwind'
# '$gt' inequality operator
# '$divide' divide operator

# Example of Aggregation Framework video
# '$group' aggregation operator
# '$sum' accumulator operator
# result = db.tweets.aagregate(
[{  '$group' : {  '_id' : '$user.screen_name',  'count' : {  '$sum' : 1  }  }  }  ,
{  '$sort' : {'count' : -1 }  }  ]
#)

# # Using group quiz
pipeline = []
pipeline.append ({  "$group" : {  "_id" : "$source",  "count" : {  "$sum" : 1  }  }  }  )      
pipeline.append (  {  "$sort" : {"count" : -1 }  }  )

# Match Operator Video
# Project Operator Video
# Match - Filtering
([{ '$match' : { 'user.friends_count' : { '$gt' :  0    } ,  'user.followers_count' :  { "$gt"   :  0    }  } },
{ '$project' : {  'ratio' : {  '$divide' : ['$user.followers_count',  '$user.friends_count']   }, 'screen_name' : '$user.screen_name'  } },
{  "$sort" : { "ratio" : -1  } } , {  "$limit" : 1 }])


# Using match and project quiz
pipeline.append({ '$match' : {'user.time_zone' : 'Brasilia', 'user.statuses_count' : {'$gte' : 100 } }  })
pipeline.append({ '$project' : { '_id' : 0,  'followers' : '$user.followers_count',
                                 'time_zone' : '$user.time_zone', 'tweets' : '$user.statuses_count',
                                 'screen_name' : '$user.screen_name'    } })
pipeline.append( {"$sort" : { "followers" : -1  } } )
pipeline.append( {'$limit' : 1  }  )

# Unwind operator video 
# {'$size' : 3}
# mentions array with three entries 
({'entities.user_mentions' : {'$size' : 3}})


# Unwind operator video 
# Count number of user.mentions for a user - '$user.scren_name'
# Who incuded the MOST user.mentions 
[{'$unwind' : '$entities.user.mentions'},
{'$group' : {'_id' : '$user.scren_name', 'count' : { '$sum' : 1 } } },
{"$sort" : { "ratio" : -1  } } , 
{"$limit" : 1 }
]


#Using unwind Quiz 
pipeline.append({'$match' : {'country' : 'India'} } )
pipeline.append({'$unwind' : '$isPartOf'}) # ****
pipeline.append({'$group' : {'_id' : '$isPartOf', 'count' : { '$sum' : 1 } } }) 
pipeline.append({ "$sort" : { "count" : -1  } })
# unwind the isPartOf Array
# Tally invividual elements of the isPartOf Array 
# "isPartOf" : [ "Jammu and Kashmir", "Udhampur district"]


# Group Accumulation Operators Video
# $group operators - '$sum', '$first' '$last', '$max', '$min', '$avg'

([{'unwind' : '$entities.hashtags'},
{'$group' : {'_id' : '$entities.hashtags.text', 'retweet_avg' : {'$avg' : '$retweet_count'} } },
{'$sort' : {'retweet_avg' : -1} }
])

# Group Accumulation Operators Video
'$push', '$addToSet'

([
{'$unwind' : '$entities.hashtags'},
{'$group' : {'_id' : '$user.screen_name', 'unique_hashtags' : {'$addToSet' : '$entities.hashtags.text'}}},
{'$sort' : {'_id' : -1}}
])


# Using Push video
pipeline = []
# Appended to the tweet_texts array, the text Field of each tweet  
pipeline.append({'$group' : {'_id' : '$user.screen_name', 'count' : {'$sum' : 1}, 'tweet_texts' : {'$push' : '$text'}}})
pipeline.append({"$sort" : { 'count' : -1}})
pipeline.append({'$limit' : 5 })

# Multiple Stages Using a Given Operator
{'$unwind' : '$entities.user_mentions'}
{'$group' : {'_id' : '$user.screen_name', 'mset' : {'$addToSet' : '$entities.user_mentions.screen_name'} }}
{'$unwind' : '$mset'}
{'$group' : {'_id' : '$_id', 'count' : {'$sum' : 1}}}
{ "$sort" : { "count" : -1  } }
{"$limit" : 10 }

#Same Operator Quiz     
pipeline.append({'$match' : {'country' : 'India'}}) 
pipeline.append({'$match' : {'population' : {'$gt' : 0}}}) 
pipeline.append({'$unwind' : '$isPartOf'})
pipeline.append({'$group' : {'_id' : '$isPartOf', 'regionPopAvg' : {'$avg' : '$population'}}})
pipeline.append({ '$group' : { '_id' : 'null', 'avg' : { '$avg' : '$regionPopAvg'}}})

# Most Common City Name
pipeline.append({ '$match' : {'name' : {'$exists' : 1}} })
pipeline.append({ '$group' : {  '_id' : '$name',  'count' : {  '$sum' : 1  }  }  })
pipeline.append({  '$sort' : {'count' : -1 }  })
pipeline.append({  "$limit" : 1 })


# Region Cities Quiz
pipeline.append({'$match' : {'country' : 'India'} } )
pipeline.append({ '$match' : {'name' : {'$exists' : 1}} })

# pipeline.append( {"$match": {'lon': {'$gt': 75, '$lt': 80} }} )
# BOTH WORK above and below 
pipeline.append({ '$match' : {'lon' : {'$gt' : 75}} })
pipeline.append({ '$match' : {'lon' : {'$lt' : 80}} })

pipeline.append({'$unwind' : '$isPartOf'})

pipeline.append({ '$group' : {  '_id' : '$isPartOf',  'count' : {  '$sum' : 1  } }  })
pipeline.append({  '$sort' : {'count' : -1 }  })
pipeline.append({'$limit' : 1 })

    
    
# Average Population 
# Make sure we have the fields populated that we need 
pipeline.append({ '$match' : {'country' : {'$exists' : 1}, } })
pipeline.append({ '$match' : {'population' : {'$exists' : 1}, } })
pipeline.append({ '$match' : {'name' : {'$exists' : 1}, } })
pipeline.append({ '$match' : {'isPartOf' : {'$exists' : 1}, } })

# get the array of interest unwound first 
pipeline.append({'$unwind' : '$isPartOf'})

# $group, more than one $group '_id' field, group by the 'isPartOf' filed WITHIN the country field - nested $group
pipeline.append({"$group":{"_id":{"country":"$country","isPartOf": "$isPartOf"},
                      "avg":{"$avg":"$population"},
                      # 'popArray' : {'$push' : '$population'}
                       }})
           
# use                        
pipeline.append({"$group":{'_id':'$_id.country','avgRegionalPopulation':{'$avg':'$avg'}}})


# Average Population - nested $group
def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ ]

    # used for testing, developemnt 
    # pipeline.append( {"$match": {'country' : 'India'}  })  

    # used for testing, developemnt 
    # pipeline.append( {"$match": { '$or' : [{'country' : 'India'},
    # {'country' : 'Iran'}] }  })

    # used for testing, developemnt 
    # pipeline.append( {"$match": { '$or' : [{'isPartOf' : 'Urmia County'},
    # {'isPartOf' : 'Khordha district'}] }  })
    
    pipeline.append({ '$match' : {'country' : {'$exists' : 1}, } })
    pipeline.append({ '$match' : {'population' : {'$exists' : 1}, } })
    pipeline.append({ '$match' : {'name' : {'$exists' : 1}, } })
    pipeline.append({ '$match' : {'isPartOf' : {'$exists' : 1}, } })
    
    # used for testing, developemnt
    # pipeline.append( {"$match":{ 'isPartOf.2': { '$exists' : 1 } }})
    
    # associate the population field with EACH [region, district] in the isPartOf array 
    pipeline.append({'$unwind' : '$isPartOf'})
    
    # requirement -
    # first calculate the average city population for each [region, district] in a country
    #
    # first part of the assigment requires two $group
    # 1.) $group isPartOf field within 2.) $group country field 
    # $group by country, the outer grouping
    # $group isPartOf inner grouping
    # there are two and just as important only two required $group fields.
    # additional $group fields will break it
    # 
    # average the population field now associated with EACH [region, district] field
    #
    # output multiple documents for each country
    # one document per [region, district] with the associtaed population average
    #
    # *** Note multiple $group fields within the *** 
    # {"_id":{"country":"$country" .......}
    pipeline.append({"$group":{"_id":{"country":"$country","isPartOf": "$isPartOf"},
                          "avg":{"$avg":"$population"},
                          # 'popArray' : {'$push' : '$population'}
                           }})
                           
    # sample output documents   
    # Clear illustration - fields nested under the _id field 
    # hence "_id." prefix dot notation required
    # sample output
    # Multiple documents for each country - see the second $group below  
    # {u'_id': {u'country': u'Iran', u'isPartOf': u'Urmia County'}, u'avg': 255628.4},
    # {u'_id': {u'country': u'Iran', u'isPartOf': u'Sumay-ye Beradust District'}, u'avg': 1508.0}
    # {u'_id': {u'country': u'Iran', u'isPartOf': u'Silvaneh District'}, u'avg': 1350.0},
      
    # used for testing, developemnt
    # fails missing _id dot notation prefix                        
    # pipeline.append({'$match' : {'country' : 'India'}  }) 
    
    # used for testing, developemnt
    # works!!! _id dot notation prefix required         
    # pipeline.append({'$match' : {'_id.country' : 'India'}  })
    
    # used for testing, developemnt
    # fails generic xx does NOT work
    # pipeline.append({ '$project' : { 'xx' : '$_id.country'}})
    
    # used for testing, developemnt
    # works _id dot notation required
    # pipeline.append({ '$project' : { '_id.country' : '$_id.country'}})

    # used for testing, developemnt
    # works _id dot notation required
    # pipeline.append({ '$project' : { '_id.isPartOf' : '$_id.isPartOf'}})
    
    # used for testing, developemnt
    # works
    # dot notation required
    # pipeline.append({ '$project' : { '_id.country' : '$_id.country',
    # '_id.isPartOf' : '$_id.isPartOf'   }})
    
    # used for testing, developemnt
    # works
    # _id prefix required on the left
    # dot notation required
    # pipeline.append({ '$project' : { '_id.avg' : '$avg'}})
    
    # used for testing, developemnt
    # fails elevation NOT part of the $group above
    # pipeline.append({ '$project' : { '_id.isPartOf' : '$_id.elevation'}})
    
    # second part of the assignmnet 
    # requirement - 
    # then calculate the average of all the regional averages for a country
    #
    # sample input documents - note multiple documnets for each country
    # $group by country required to meet requiremnt 
    # {u'_id': {u'country': u'Iran', u'isPartOf': u'Urmia County'}, u'avg': 255628.4},
    # {u'_id': {u'country': u'Iran', u'isPartOf': u'Sumay-ye Beradust District'}, u'avg': 1508.0}
    # {u'_id': {u'country': u'Iran', u'isPartOf': u'Silvaneh District'}, u'avg': 1350.0},
    #
    # the first left $avg is the airthmetic operator - 'average'
    # the second right $avg is value that is $group by country then averaged
    # {'$avg':'$avg'}
    #
    # *** Only 1 $group field - country  *** 
    pipeline.append({"$group":{'_id':'$_id.country','avgRegionalPopulation':{'$avg':'$avg'}}})
    # sample output 1 document for each country  
    # {u'_id': u'Lithuania', u'avgRegionalPopulation': 14750.784447977203}
    # {u'_id': u'Iran', u'avgRegionalPopulation': 31174.275647889808}


# misc

# match equals 
pipeline.append({'$match' : {'country' : 'India'} } ) #gets many

# match not equals
pipeline.append({'$match' : { 'country' : { '$ne' : 'India'} }  }) # gets many

# match '$or'
pipeline.append( {"$match": { '$or' : [{'country' : 'Bolivia'}, {'country' : 'Sudan'}] }  })





 



    