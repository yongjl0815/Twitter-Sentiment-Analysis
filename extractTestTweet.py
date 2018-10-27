# usr/bin/python

import json
import os
import tweepy

#load txt file                                                                              
data_path = './stream.txt'
tweet_data = []
tweet_file = open(data_path, "r")


#Process the file and extract information, add text to tweet array                                                
for line in tweet_file:
    try:
        tweet = json.loads(line)
        temp = []
        temp = re.sub(r'[^a-zA-Z]', " ", tweet['text']).lstrip()
        tweet_data.append(temp)
        
    except:
        continue

#print (len(tweet_data))
