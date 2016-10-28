#!/usr/bin/env python
"""
Write an aggregation query to answer this question:

Of the users in the "Brasilia" timezone who have tweeted 100 times or more,
who has the largest number of followers?

The following hints will help you solve this problem:
- Time zone is found in the "time_zone" field of the user object in each tweet.
- The number of tweets for each user is found in the "statuses_count" field.
  To access these fields you will need to use dot notation (from Lesson 4)
- Your aggregation query should return something like the following:
{u'ok': 1.0,
 u'result': [{u'_id': ObjectId('52fd2490bac3fa1975477702'),
                  u'followers': 2597,
                  u'screen_name': u'marbles',
                  u'tweets': 12334}]}
Note that you will need to create the fields 'followers', 'screen_name' and 'tweets'.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation 
pipeline that can be passed to the MongoDB aggregate function. As in our examples in this lesson,
the aggregation pipeline should be a list of one or more dictionary objects. 
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code
locally on your machine, you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset used 
in examples in this lesson. If you attempt some of the same queries that we looked at in the lesson 
examples, your results will be different.
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    print()
 
    db = client[db_name]
       
    collection = db.collection_names(include_system_collections=True)
    
    
    # before mongoimport --db twitter  --type json --file ./twitter.json
    #        collection - []
    # print("collection - {}".format(collection))

# imported twitter database into MongoDB
# successfully imported file into MongoDB
# Menfi (master *) dataFiles $ mongoimport --db twitter  --type json --file ./twitter.json # ****************mongoimport 
# 2016-10-26T23:29:51.417-0500    no collection specified
# 2016-10-26T23:29:51.418-0500    using filename 'twitter' as collection
# 2016-10-26T23:29:51.420-0500    connected to: localhost
# 2016-10-26T23:29:54.420-0500    [#######.................] twitter.twitter    25.8MB/88.0MB (29.3%)
# 2016-10-26T23:29:57.420-0500    [################........] twitter.twitter    60.0MB/88.0MB (68.2%)
# 2016-10-26T23:29:59.654-0500    [########################] twitter.twitter    88.0MB/88.0MB (100.0%)
# 2016-10-26T23:29:59.654-0500    imported 51428 documents
    
    # after mongoimport --db twitter  --type json --file ./twitter.json
    #      collection - ['twitter']
    #print("collection - {}".format(collection))
    # print("type(collection) is {}\n".format(type(collection))) # list
    # print("len(collection) is {}\n".format(len(collection))) # 1
    
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ ] 
    
    pipeline.append({ '$match' : {'user.time_zone' : 'Brasilia', 'user.statuses_count' : {'$gte' : 100 } }  })
    
    pipeline.append({ '$project' : { '_id' : 0,  'followers' : '$user.followers_count',
                                 'time_zoneabc' : '$user.time_zone', 'tweets' : '$user.statuses_count',
                                 'screen_name' : '$user.screen_name'    } })
    
    pipeline.append( {"$sort" : { "followers" : -1  } } )
    pipeline.append( {'$limit' : 1  }  )
    
    return pipeline

def aggregate(db, pipeline):
 
    for doc in db.twitter.aggregate(pipeline):
        # print("doc - {}".format(doc))    
        print(doc)    
 
    
    return [doc for doc in db.twitter.aggregate(pipeline)]
    # 
    return [doc for doc in db.tweets.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    
    print()
    print("result is {}".format(result))
    print("len(result) is {}".format(len(result)))
    print("type(result) is {}\n".format(type(result)))
    
    import pprint
    pprint.pprint(result)
    assert len(result) == 1
    # assert result[0]["followers"] == 17209
