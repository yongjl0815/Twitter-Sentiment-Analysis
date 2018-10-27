# usr/bin/python

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

#authentication                                                                                                                          
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


#prints tweets to file.                                                                   
class StdOL(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    #search keyword, can use multiple keywords                                          
    kword = 'movie'

    #Authetication, establish connection to Twitter Stream                                  
    x = StdOL()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, x)

    #This line filter Twitter stream by the keyword, add more keywords with ,               
    stream.filter(track=[kword])
    