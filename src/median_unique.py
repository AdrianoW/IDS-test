# -*- coding: utf-8 -*-
# example of program that calculates the median number of unique words per tweet.
from tweet_reader import TweetFile
from bisect import insort
import sys
from utils import parse_args, get_error, BaseProcessing, setup_log
import logging


class MedianFinder(BaseProcessing):
    """
        Keeps the list, add values and calculate median value
    """
    def __init__(self, output):
        """ Init the structure """
        self.vals = []
        self.output = open(output, 'w')

    def process_tweet(self, tweet):
        """
        Add the element into the ordered list
        :param tweet: line with parsed words
        :return None
        """
        insort(self.vals, len(set(tweet)))

    def write_results(self):
        """
        Write current median to file
        :return:
        """
        self.output.write('%.2f\n' % self.print_partial())

    def print_partial(self):
        """
        Calculate the median
        :return the median
        """
        # save the middle position
        idx = int(len(self.vals)/2)
        size = len(self.vals)

        if size > 1 and (size % 2 == 0):
            # even number of elements. return the mean of the elements
            return (self.vals[idx-1]+self.vals[idx])/2.0
        else:
            # odd number. return the middle position
            return self.vals[idx]


def main(args):
    """
    Calculate the median of number of unique words
    :return:
    """
    logging.info('starting median_unique')
    if not args.output_file:
        logging.error('no output file defined')
        sys.exit(-1)

    # init vars
    mf = MedianFinder(args.output_file)

    # read file bringing the word list
    tfile = TweetFile(args.input_file)
    for words in tfile.get_words():
        # make an unique set of words and get its length
        mf.process_tweet(words)

        # save to file the current median
        mf.write_results()

    # log the program is finished
    logging.info('program finished')


if __name__ == '__main__':
    args = parse_args()
    # run logging any error
    try:
        setup_log()
        main(args)
    except:
        logging.error(get_error())
        logging.info('Exiting. Bye')