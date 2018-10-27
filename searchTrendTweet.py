# usr/bin/python3                                                                                                                        

import json
import os
import tweepy
from tweepy import OAuthHandler

#authentication                                                                                                                          
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tw = tweepy.API(auth)

print ("You want to search trending topics for your city?")
city = input("Please enter the name of your city (Don't for get Capitalization and Spacing) : ")
wid = ''

#get WOEID for desired city                                                                                                              
trend_a = tw.trends_available()

for a in trend_a:
    try:
        if (a['name'] == city):
            wid = a['woeid']
    except:
        print ("Error")


#Get data                                                                                                                                
trend_p = tw.trends_place(wid)

#Get data                                                                                                                                
trend_p = tw.trends_place(wid)

for a in trend_p:
    try:
        for b in a['trends']:
            print ("================================================================")
            print ('Name : ' + b['name'])
            print ('Query : ' + b['query'])
            print ('URL : ' + b['url'])
            print ('Tweets : ' + str(b['tweet_volume']))
            print ("================================================================")
            print ('\n')
    except:
        print ("Error")