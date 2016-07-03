#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "golang"
#-----------------------------------------------------------------------

from twitter import *
import json
import time

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

data = {"users":{}}
since_id = 1;
#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------

while (1):
    query = twitter.search.tweets(q = "golang", count = 100, since_id = since_id)


#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
    for result in query["statuses"]:
    #print "(%s) @%s %s" % (result["id"], result["user"]["screen_name"], result["text"])
        if result["id"]>since_id:
            since_id = result["id"]

        user = result["user"]["screen_name"] 

        if user in data["users"].keys():
            data["users"][user]+=1;
        else:
            data["users"][user]=1;

    print json.dumps(data)
    #print(len(data["users"].keys()))
    print(len(query["statuses"]))
    #print(data["users"].values())

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    
    time.sleep(2)

    
