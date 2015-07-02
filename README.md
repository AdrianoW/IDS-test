Insight Data Engineering - Coding Challenge
===========================================================

For this coding challenge, you will develop tools that could help analyze the community of Twitter users.  For simplicity, the features we will build are primitive, but you could easily build more complicated features on top of these.   

## Challenge Summary

This challenge is to implement two features:

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in. 

For example, suppose the following three tweets come in, one after the other

- is #bigdata finally the answer to end poverty? @lavanyarathnam http://ow.ly/o8gt3  #analytics  
- interview: xia wang, astrazeneca on #bigdata and the promise of effective healthcare #kdn http://ow.ly/ot2uj  
- big data is not just for big business. on how #bigdata is being deployed for small businesses: http://bddy.me/1bzukb3  @cxotodayalerts #smb  

The first feature would produce the following total count for each word:

	#analytics  				1
	#bigdata 					3
	#kdn 						1
	#smb 						1
	@cxotodayalerts 			1
	@lavanyarathnam 			1
	and 						1
	answer  					1
	astrazeneca 				1
	being 						1
	big 						2
	business. 					1 
	businesses: 				1
	data 						1
	deployed 					1
	effective 					1
	end 						1
	finally 					1
	for 						2
	healthcare 					1
	how 						1
	http://bddy.me/1bzukb3  	1
	http://ow.ly/o8gt3 	 		1
	http://ow.ly/ot2uj  		1
	interview: 					1
	is  						3
	just 						1
	not 						1
	of 							1
	on 							2
	poverty? 					1
	promise 					1
	small 						1
	the  						2
	to  						1
	wang,						1
	xia 						1

For the second feature, the number of unique words in each tweet is 11, 14, and 17 (since the words 'is', 'big', and 'for' appear twice in the third tweet).  This means that the set of unique words per tweet is {11} after the first tweet arrives, is {11, 14} after the second tweet arrives, and is {11, 14, 17} after all three tweets arrive.  Thus, the second feature would produce the following output:

	11
	12.5
	14

Recall that the median of a set with an even number of items is the mean of the two middle elements (e.g. the median of {11, 14} is 12.5). In this challenge we have made a few assumptions to make things simpler:

- Each tweet only contains lowercase letters, numbers, and ASCII characters like ':', '@', and '#'.
- A word is defined as anything separated by whitespace. 

Note that the output of the first feature is outputted in order, according to the [ASCII Code](http://www.ascii-code.com).   

## Details of Implementation

We'd like you to implement your own version of these two features.  However, we don't want this challenge to focus on the relatively uninteresting data cleaning and munging.  Normally, tweets can be obtained through Twitter's API in JSON format and the "payload" text is parsed, but you may assume that this has already been done and written to a file named 'tweets.txt' inside a directory named 'tweet_input'.  For simplicity, this file 'tweets.txt' will only contain lowercase letters, numbers, and ASCII characters (e.g. common punctuation and characters like '@', and '#').  Additionally, 'tweets.txt' will have the content of each tweet on a newline:

tweets.txt:

	Contents of first tweet  
	Contents of second tweet  
	Contents of third tweet  
	.
	.
	.
	Contents of last tweet  

Your program should output the results of this first feature to a text file named `ft1.txt` in a directory named `tweet_output`.  In order for your submission to be checked, it needs to output the results of your first feature in order, according to the [ASCII Code](http://www.ascii-code.com), as shown in the above example.  For simplicity, treat all punctuation as part of the word itself, so 'business.' would be counted as a different word than 'business' without the period.

Ideally, the second feature that updates the median as each tweet arrives would be connected to the Twitter streaming API and would add new tweets to the end of 'tweets.txt'.  However, connecting to the this API requires more system specific "dev ops" work, which isn't the primary focus for data engineers.  Instead, you should simply assume that each new line of the text file corresponds to a new tweet and design your program to handle a text file with a large number of tweets.  Your program should output the results of this second feature to a text file named `ft2.txt` in the `tweet_output` directory.

You may write your solution in any mainstream programming language such as C, C++, C#, Clojure, Erlang, Go, Haskell, Java, Python, Ruby, or Scala - then submit a link to a Github repo with your source code.  In addition to the source code, the top-most directory of your repo must include the `tweet_input` and `tweet_output` directories, and a shell script named `run.sh` that compiles and runs the program(s) that implement these features.  If your solution requires additional libraries, environments, or dependencies, you must specify these in your README documentation.  See the figure below for the required structure of the top-most directory in your repo, or simply clone this repo.

![Example Repo Structure](images/directory-pic.png)

Alternatively, here is example output of the 'tree' command:

	├── README.md  
	├── run.sh  
	├── src  
	│   ├── median_unique.py  
	│   └── words_tweeted.py  
	├── tweet_input  
	│   └── tweets.txt  
	└── tweet_output  
	    ├── ft1.txt  
	    └── ft2.txt  

As a data engineer, it’s important that you write clean, well-documented code that scales for large amounts of data.  For this reason, it’s important to ensure that your solution works well for a huge number of tweets, rather than just the simple examples above.  For example, your solution should be able to process a file containing every tweet from the last month without taking much longer than processing only the last hour of tweets.  For more details about the implementation, please refer to FAQ below or email us at info@insightdataengineering.com


## FAQ

Here are some common questions we've received.  If you have additional questions, feel free fork this repo, add them to the README.md, then issue a pull request.  Alternatively, you can email info@insightdataengineering.com and we'll add the answers.

* *Which Github link should I submit?*  
You should submit the URL for the top-level root of your repository.  For example, this repo would be submitted by copying the URL `https://github.com/InsightDataScience/cc-example` into the appropriate field on the application.  Please do NOT try to submit your coding challenge using a pull request, which will make your source code publicly available.  

* *May I use R or other analytics programming languages to solve the challenge?*  
While you may use any programming language to complete the challenge, it's important that your implementation scales to handle large amounts of data.  Many applicants have found that R is unable to process data in a scalable fashion, so it may be more practical to use another language.  






