IDS - Coding Challenge
===========================================================

## Details of the basic implementation

- all in python
- uses the same structure of the original challenge.
- use only standard library.
- do not load the whole file in memory. Uses iterable to make a stream like processing of each line.
- uses logging to check execution.
- use default parameters.
- a base class works as a base processor for all processing that can be done with a tweet. so it is easilly expansible for other processing like sentiment analysis, 

## Details of the streaming implementation

- uses the processors word count and median from the basic implementation to calculate the stream values.
- uses tweepy as the connector to twitter's stream
- it saves the whole tweet or/and just the text part
- the src/config.yaml is a configuration file for:
  - the tags to be monitored
  - the output of the processing (no need to pass them when calling the python file)
  - logging level
  - Twitter key configuration
  - more info inside the file 

## Dependencies
tweepy

## Run Streaming
in the root directory of *this* repository, execute
`python src/stream.py`