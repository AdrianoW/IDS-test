# -*- coding: utf-8 -*-
"""
    Util functions to ease development
"""

import argparse
import traceback
import logging

__author__ = 'adrianwoalmeida'

def parse_args():
    """
    :return: parsed args
    """
    # check the arguments passed
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input_file', nargs='?',
                        help='input file where each line is a tweet',
                        default='./tweet_input/tweets.txt')
    parser.add_argument('output_file', nargs='?',
                        help='output file of the program',
                        default='./tweet_output/out.txt')
    args = parser.parse_args()
    return args


def get_error():
    """
    :return: formated trace
    """
    return traceback.format_exc().splitlines()[-2:]


def setup_log(logger_name="mylogger", log_filename=None):
    """
    Creates a logger instance printing on screen and in a file
    :param log_filename: the name of a log file. If None, will not create a log file
    :return: logger instance
    """

    logger = logging.getLogger(logger_name)

    # create a log file if a filename was specified
    if log_filename:
        # create file handler which logs even debug messages
        fh = logging.FileHandler(log_filename)
        fh.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)-8s - %(message)s'))
        # ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)-8s - \
        # [ %(filename)-20s:%(lineno)s - %(funcName)-10s() ] %(message)s'))

        # add the handlers to the logger
        logger.addHandler(fh)

    return logger

def setup_log(level=None):
    """
    Initiate logging according to param
    :param level: info or debug
    :return: None
    """
    # get logger instance with appropriate logging level
    if level == 'info':
        level = logging.INFO
    else:
        level = logging.DEBUG

    logging.basicConfig(level=level,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


class BaseProcessing(object):
    """
    This is the base class of the processor.
    This should be inherited and have the functions implemented
    """
    def process_tweet(self, tweet):
        """
        This should be implemented for processing a line of tweet.
        :param tweet: usually list with tweet words
        :return: none
        """
        raise NotImplementedError('You should implement process_tweet')

    def write_results(self):
        """
        This should write the output of the processing to a file
        :return:
        """
        raise NotImplementedError('You should implement write_results')

    def print_partial(self):
        """
        This should print a partial processing to the screen
        :return:
        """
        raise NotImplementedError('You should implement print_partial')

