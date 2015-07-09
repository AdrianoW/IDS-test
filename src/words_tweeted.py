# -*- coding: utf-8 -*-
# example of program that calculates the total number of times each word has been tweeted.
from __future__ import unicode_literals
from tweet_reader import TweetFile
import sys
from bisect import insort
from utils import parse_args, get_error, BaseProcessing, setup_log
import logging


class WordsCounter(BaseProcessing):
    """
    Holds the structure to count the words
    """
    def __init__(self, output_file):

        # structures used
        self.words_list = {}
        self.words_order = []
        self.output = output_file

    def process_tweet(self, tweet):
        """
        Count the words
        :param tweet: the list of words in the tweet
        """
        # for each word, count the number of times it appeared
        for word in tweet:
            # add one if exists, else add one to new key
            new_amt = self.words_list.get(word, 0) + 1
            self.words_list[word] = new_amt

            # new word, add to index
            if new_amt == 1:
                insort(self.words_order, word)

    def write_results(self):
        """
        Saves the counting to a file
        """
        with open(self.output, 'w') as out:
            # save the output file
            for word in self.words_order:
                # saves in ascii. some characters will be lost
                out.write('%-27s %d\n' % (word.encode('ascii', 'replace'), self.words_list[word]))


def main(args):
    """
    calulate the number of times the words show up
    :return:
    """
    logging.info('starting words_tweeted')
    if not args.output_file:
        logging.error('no output file defined')
        sys.exit(-1)

    # create the counting structure
    wc = WordsCounter(args.output_file)

    # read file bringing the word list
    tfile = TweetFile(args.input_file)
    for words in tfile.get_words():

        # add each word in the dictionary
        wc.process_tweet(words)

    # save the info to output
    wc.write_results()
    logging.debug('Finished writing to %s' % args.output_file)

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
