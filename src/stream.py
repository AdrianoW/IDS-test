__author__ = 'adrianwoalmeida'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import utils
import logging
import argparse

# write to external file
f = open('tweet_input/tweet_stream_data.txt', 'a')

# class of the listenter
class listener(StreamListener):

   def __init__(self):
      # create the variable to connect to the memcache
      self.cache  = pylibmc.Client(["127.0.0.1"], binary=True,
        behaviors={"tcp_nodelay": True,
        "ketama": True})
      self.cache["cont_ambos"] = 0
      self.cache["cont_dilma"] = 0
      self.cache["cont_aecio"] = 0
      self.cache["cont_nenhum"] = 0
      self.cache["cont_total"] = 0

      # connect to mongo db
      self.db_client = MongoClient('mongodb://localhost:27017/')
      self.db = self.db_client.post_data
      self.coll = self.db.raw_post
      super(listener, self).__init__()

   def on_data(self, data):
      # check if the twitter has both or only one of them
      low = json.loads(data)['text'].lower()
      f.write(data)
      f.write(',\n')

      # save posts on db
      self.coll.insert(low)

      # write to the cache
      dilma = 1 if 'dilma' in low else 0
      aecio = 1 if 'aecio' in low else 0
      if dilma and aecio:
         self.cache.incr("cont_ambos")
      elif dilma:
         self.cache.incr("cont_dilma")
      elif aecio:
         self.cache.incr("cont_aecio")
      else:
         self.cache.incr("cont_nenhum")

      self.cache.incr("cont_total")
      #print self.cache["cont_total"],

      return True

   def on_error(self, status):
      print status

   def on_event(self, status):
      """Called when a new event arrives"""
      print status

# will connect on this one
print 'Starting'
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
print 'Authenticated'
twitterStream.filter(track=["#Aecio45PeloBrasil", "#SouAecio", "#TodosComDilma", "#13rasilTodoComDilma"])
print 'End'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('tweeter_key', nargs='?',
                        help='a yaml file with the info asecret, atoken, ckey, csecret',
                        default='twitter_keys.yaml')
    parser.add_argument('output_file', nargs='?',
                        help='output file of the program',
                        default='./tweet_output/out.txt')
    args = parser.parse_args()
    # run logging any error
    try:
        main(args)
    except:
        logging.error(get_error())
        logging.info('Exiting. Bye')