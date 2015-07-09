# -*- coding: utf-8 -*-
"""
   This will read a twitter stream and calculate the median and number of times a
   word appear
"""
from __future__ import unicode_literals # deal with strings as unicode
from tweet_reader import TweetFile
from median_unique import MedianFinder
from words_tweeted import WordsCounter

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from utils import get_error, setup_log
import logging
import argparse
import yaml

__author__ = 'adrianwoalmeida'


class Statistics(object):
    """
    Holds the statistics about the stream.
    """
    def __init__(self, cfg):
        logging.debug('Statistics initiated')
        self.wc = WordsCounter(cfg['output_count'])
        self.mf = MedianFinder(cfg['output_median'])
        self.num_processed = 0

    def median(self, line):
        """
        Call the median finder stats
        :param line: a list of words in the tweet
        """
        self.mf.process_tweet(line)
        self.mf.write_results()
        self.num_processed += 1

    def word_count(self, line):
        """
        Call the median finder stats
        :param line: number of unique words for the line
        """
        self.wc.process_tweet(line)

    def save_info(self):
        """
        Write the word count to file
        :return:
        """
        logging.info('Number of tweets processed %d' % self.num_processed)
        self.wc.write_results()


class Listener(StreamListener):
    """
    Class that will define what will be done on each tweeter received
    """
    def __init__(self, cfg, stats):
        """
        Open the files for output and connect to any database for tweet saving
        :param cfg: config structure with output file and any connections
        :param stats: statistics structure to save info to
        :return: None
        """
        # open the output file in append mode, not loosing previous tweets
        self.cache = cfg.get('twitter_cache', '')
        if self.cache:
            self.cache = open(self.cache, 'a')
        self.lines = cfg.get('twitter_lines', '')
        if self.lines:
            self.lines = open(self.lines, 'a')

        # save the statistic structure
        self.stats = stats

        # flush param
        self.flush_period = cfg.get('flush_period', -1)
        self.to_flush = 0
        super(Listener, self).__init__()

    def on_connect(self):
        """
        Log the connection
        :return:
        """
        logging.info('Starting to stream')

    def on_data(self, data):
        """
        This function is called when new data arrives. Once for each tweet
        :param data:
        :return:
        """
        # get the text removing line breaks
        low = json.loads(data).get('text', '').lower().replace('\n', '').replace('\r', '')
        self.to_flush +=1
        logging.debug(low)

        # if cache enabled
        if self.cache:
            self.cache.write(data)
            self.cache.write('\n')

            if self.to_flush == self.flush_period:
                self.cache.flush()


        # if line saving enabled
        if self.lines:
            self.lines.write(low.encode('utf-8'))
            self.lines.write('\n')

            if self.to_flush == self.flush_period:
                self.lines.flush()

        # reset flush counter and print progress
        if self.to_flush == self.flush_period:
            self.to_flush = 0
            logging.info('Nr tweets processed: %d' % self.stats.num_processed)

        # process the line
        line = TweetFile.process_tweet_text(low)
        self.stats.median(line)
        self.stats.word_count(line)

        return True

    def on_error(self, status):
        """
        Called on error
        :param status: of the call
        :return:
        """
        print status

    def on_event(self, status):
        """Called when a new event arrives"""
        print status


def main(cfg):

    logging.info('Starting')

    # will connect to the stream authenticating
    logging.debug('Connecting to the stream')
    auth = OAuthHandler(cfg['ckey'], cfg['csecret'])
    auth.set_access_token(cfg['atoken'], cfg['asecret'])

    # create the twitter stream listener using the configuration created
    stats = Statistics(cfg)
    twitter_stream = Stream(auth, Listener(cfg, stats))
    logging.debug('Authenticated')

    # start monitoring tags
    logging.info('Monitoring tags: %s' % cfg['monitored_tags'])
    try:
        twitter_stream.filter(track=cfg['monitored_tags'])
    except KeyboardInterrupt:
        # user finished
        logging.info('Program ended by user')
    finally:
        # save the stats
        stats.save_info()

if __name__ == '__main__':
    # single param, config file.
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('config_file', nargs='?',
                        help='a yaml file with the configuration for this process',
                        default='./src/config.yaml')
    args = parser.parse_args()
    
    # run logging any error
    try:
        # read the file, set the logging level and call the main program
        config = yaml.load(file(args.config_file))
        setup_log(config.get('logging_level'))

        main(config)
    except:
        logging.error(get_error())