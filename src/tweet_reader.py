"""
   This helper will read a file and return a iterable with all the words
   The static method can be called for line processing
"""
import logging

__author__ = 'adrianwoalmeida'


class TweetFile(object):
    """ Deals with file opening and line parsing, not loading all file in memory """

    def __init__(self, input_file=None):
        """
        Init the class
        :param input_file: input file where tweets should be. Each line a tweet
        :return:
        """
        # save file name for later use
        self.input_file = input_file

    def get_words(self):
        """
        Will iterate over all lines, lowercasing the lines and splitting them based on spaces.
        :return: iterable of the words contained in a tweet line
        """
        logging.debug('Reading input file %s' % self.input_file)
        with open(self.input_file, 'r') as f:
            for line in f:
                words = self.process_tweet_text(line)
                yield words

    @staticmethod
    def process_tweet_text(tweet):
        """
        Will process the tweeter text. Simple parsing. This static method can be called without
        class loadinf
        :param tweet: just the tweet text
        :return a list of words
        """
        # lower, remove any and of line and split according to space
        return tweet.lower().rstrip('\n\r').split(' ')