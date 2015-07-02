#!/usr/bin/env bash

# example of the run script for running the word count

# I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python ./src/my_word_count.py ./wc_input ./wc_output/wc_result.txt
python ./src/my_running_median.py ./wc_input ./wc_output/med_result.txt



