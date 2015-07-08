# example of program that calculates the total number of times each word has been tweeted.
from tweet_reader import TweetFile
import sys
from bisect import insort
from utils import parse_args, get_error
import logging


def main(args):
    """
    calulate the number of times the words show up
    :return:
    """
    logging.info('starting words_tweeted')
    if not args.output_file:
        logging.error('no output file defined')
        sys.exit(-1)

    # open the output file
    words_list = {}
    words_order = []
    with open(args.output_file, 'w') as out:

        # read file bringing the word list
        tfile = TweetFile(args.input_file)
        for words in tfile.get_words():

            # add each word in the dictionary
            for word in words:
                # count the number of times the word appeared
                new_amt = words_list.get(word, 0) + 1
                words_list[word] = new_amt

                # new word, add to index
                if new_amt == 1:
                    insort(words_order, word)

        # save the output file
        for word in words_order:
            out.write('%-28s%d\n' % (word, words_list[word]))
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
