# usr/bin/python

import json
import os
import tweepy

#load txt file                                                                              
data_path = './stream.txt'
tweet_data = []
tweet_file = open(data_path, "r")

print ('\n')
print ('============================================================')
print ('\n')
#Process the file and extract information                                                   
for line in tweet_file:
    try:
        tweet = json.loads(line)
        print ('Name : ' + tweet['user']['name'])
        print ('\n')
        print ('Created : ' + tweet['created_at'])
        print ('\n')
        print ('Description : ' + tweet['user']['description'])
        print ('\n')
        print ('Text : ' + tweet['text'])
        print ('\n')
        print ('\n')
        print ('============================================================')
        print ('\n')
        tweet_data.append(tweet)
    except:
        continue

print ('Total Tweet : ' + str(len(tweet_data)))
print ('\n')
print ('============================================================')