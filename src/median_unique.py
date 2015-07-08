# example of program that calculates the median number of unique words per tweet.
from tweet_reader import TweetFile
from bisect import insort
import sys
from utils import parse_args, get_error
import logging


class MedianFinder(object):
    """
        Keeps the list, add values and calculate median value
    """
    def __init__(self):
        """ Init the structure """
        self.vals = []

    def add(self, val):
        """
        Add the element into the ordered list
        :param val: value to be inserted
        :return None
        """
        insort(self.vals, val)

    def median(self):
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
    calulate the median of number of unique words
    :return:
    """
    logging.info('starting median_unique')
    if not args.output_file:
        logging.error('no output file defined')
        sys.exit(-1)

    # open the output file
    with open(args.output_file, 'w') as out:
        # init vars
        mf = MedianFinder()

        # read file bringing the word list
        tfile = TweetFile(args.input_file)
        for words in tfile.get_words():
            # make an unique set of words and get its length
            mf.add(len(set(words)))

            # save to file the current median
            out.write('%.2f\n' % mf.median())
        logging.debug('Finished writing to %s' % args.output_file)

    # log the program is finished
    logging.info('program finished')


if __name__ == '__main__':
    args = parse_args()
    # run logging any error
    try:
        main(args)
    except:
        logging.error(get_error())
        logging.info('Exiting. Bye')

