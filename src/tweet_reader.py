__author__ = 'adrianwoalmeida'
"""
    This helper will read a file and return a iterable with all the words
"""
import sys
import logging

class TweetFile(object):
    """ Deals with file opening and line parsing, not loading all file in memory """

    def __init__(self, input_file=None):
        """
        Init the class
        :param input_file: input file where tweets should be. Each line a tweet
        :return:
        """
        if not input_file:
            logging.error('Input file must be defined')
            sys.exit(-1)

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
                words = line.lower().rstrip('\n\r').split(' ')
                yield words