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

### Setup and dependencies
You need a twitter developer account to access the streamming api. Follow the steps below to get the info needed:

- Create a twitter account if you do not already have one.
- Go to https://apps.twitter.com/ and log in with your twitter credentials.
- Click "Create New App"
- Fill out the form, agree to the terms, and click "Create your Twitter application"
- In the next page, click on "API keys" tab, and copy your "API key" and "API secret".
- Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".
- fill the fields on src/config.yml 
  - ctkey, csecret: api key, api secret
  - atoken,asecret: acess token, access secret

The modules used by tweepy work better in Python2.7.9 (ssl part).
To install the dependencies, execute in the project base folder:

    pip install --upgrade pip
    pip install -r requirements.txt

### Run Streaming
On the base directory of *this* repository, execute
`python src/stream.py`. Stop with CTRL+C (keyboard)
