
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
    
 









 



    