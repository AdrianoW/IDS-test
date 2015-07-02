Insight Data Engineering - Coding Challenge
===========================================================

For this coding challenge, you will develop tools that could help analyze the community of Twitter users.  For simplicity, the features we will build are primitive, but you could easily build more complicated features on top of these.   

## Challenge Summary

This challenge is to implement two features:

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of unique words per tweet, and update this median as tweets come in. 

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

while the second feature would produce the following output:

	11
	12.5
	14

since the number of unique words in each tweet is 11, 14, and 17 respectively.  In this challenge we have made a few assumptions to make things simpler:

- Each tweet only contains lowercase letters, numbers, and ASCII characters like ':', '@', and '#'.
- A word is defined as anything separated by whitespace. 

Note that the output of the first feature is outputted in order according to the [ASCII Code](http://www.ascii-code.com).  Also recall, that the median of a set with an even number of items is the mean of the two middle elements (e.g. the median of {11, 14} is 12.5).

## Details of Implementation

We'd like you to implement your own version of this running median that calculates the median number of words per line, for each line of the text files in the `wc_input` directory.  If there are multiple files in that directory, the files should be combined into a single stream and processed by your running median program in alphabetical order, so a file named `hello.txt` should be processed before a file named `world.txt`.  The resulting running median for each line should then be outputted to a text file named `med_result.txt` in the `wc_output` directory.

You may write your solution in any one of the following programming languages: C, C++, Clojure, Java, Python, Ruby, or Scala - then submit a link to a Github repo with your source code.  In addition to the source code, the top-most directory of your repo must include `wc_input` and `wc_output` directories, and a shell script named `run.sh` that compiles and runs the Word Count and Running Median programs.  If your solution requires additional libraries or dependencies, the shell script should load them first so that your programs can be run on any system just by running `run.sh`.  See the figure below for the required structure of the top-most directory in your repo, or simply clone this repo.

![Example Repo Structure](images/directory-pic.png)

As a data engineer, it’s important that you write clean, well-documented code that scales for large amounts of data.  For this reason, it’s important to ensure that your solution works well for small and large text files, rather than just the simple examples above.  For example, your solution should be able to process large files like the text of the book "War and Peace" without taking much longer than processing the small files.


## FAQ

Here are some common questions we've received.  If you have additional questions, feel free fork this repo, add them to the README.md, then issue a pull request.  Alternatively, you can email info@insightdataengineering.com and we'll add the answers.

* *Which Github link should I submit?*  
You should submit the URL for the top-level root of your repository.  For example, this repo would be submitted by copying the URL `https://github.com/InsightDataScience/cc-example` into the appropriate field on the application.  Please do NOT try to submit your coding challenge using a pull request, which will make your source code publicly available.  

* *Do I need to account for punctuation in the word count?*  
Yes, punctuation should be removed so `shout` and `shout.` should both be counted together.

* *Should I count capitalization differently in the word count?*  
No, both `Who` and `who` should be counted together.  For simplicity, the word count should return an alphabetical list of lowercase words (e.g. `who	2`).

* *What should the format of the word count be?*  
Please try to match the above example, by listing the words in **alphabetical** order, with a tab between the word and count, and each word separated by a newline.

* *How should hyphens be handled?*  
For simplicity, please remove hyphens so that `hi-lite` is counted as `hilite`.

* *Should words that are split onto two lines using hyphenation be counted as one word (or two separate words) for the word-counting program?*  
For simplicity, you may assume that all text files do not have any hyphens for splitting words across two different lines.  

* *How should conjunctions like `we're` or `haven't` be handled?*  
For simplicity, please remove apostrophes so that `we're` and `haven't` are counted as `were` and `havent`.

* *Do I need to account for digits (e.g 0-9)?*  
No, for simplicity you may assume that the text files do not contain any digits.  

* *Do I need to account for complicated Unicode characters?*  
No, you may assume that all of the characters are conventional, ASCII characters.

* *Should I check if the files in the input directory are text files or non text files(binary)?*
No, for simplicity you may assume that all of the files in the input directory are standard text files.  

* *Will our program need to look for text files in any subdirectories of the `wc_input` directory?*  
No, for simplicity you may assume that the `wc_input` directory only contains text files, with no subdirectories.  

* *What if I need to load a library or dependency for my program to run?*  
Make sure that your `run.sh` script loads all the dependencies for your program.  These dependencies should also be well documented in your Markdown README.

* *Do I need separate programs for WordCount and Running Median?*  
No, you may use a single combined program or several programs, as long as they are all executed by the `run.sh` script.

* *Does the `run.sh` script need to be a Bash script (i.e. on Linux or Mac OSX)?*  
Yes - Unix based systems like Linux and MacOSX are the standard in the field of Data Engineering - and the system needs to be compiled and tested on a Unix based system.  With that said, you can use emulators like [Cygwin](https://www.cygwin.com/) if you only have access to a Windows system.

* *Can I use an IDE like Eclipse to write my program?*  
Yes, you can use what ever tools you want -  as long as your `run.sh` script correctly runs the relevant target files and creates the `wc_result.txt` and `med_result.txt` files in the `wc_output` directory.

* *What should be in the `wc_input` directory?*  
You can put any text file you want in the directory.  In fact, this could be quite helpful for testing your solutions.

* *What should the output of the running median be?*  
For simplicity, please output the running median as a double with only 1 digit after the decimal (i.e. 2.0 instead of 2).  In the event that you need to round, simply truncate the answer (i.e. 2/3 should be 0.6).  The running median for each line of text should be separated by newlines as shown in the example above.

* *How should blank lines be handled in the running median?*  
Blank lines should be considered as lines with 0 words, so the runnning set for

> Hello world  
> 		  
> Brave new world  

should be {2, 0, 3} with a corresponding result of

	2  
	1  
	2

* *How does the running median work for multiple files?*  
All of the files should be processed as if they come from a single stream, ordered in alphabetical order as given by the ASCII code.  For example, if you had a file name `a.txt` with the following lines

> Hello world  
Hello brave new world

and another file named `b.txt` with the following

> Foo  
Bar

then the running median should process `a.txt` first, then `b.txt`.  As each line is read the running set will be

	{2}  
	{2, 4}  
	{1, 2, 4}  
	{1, 1, 2, 4}

to give a resulting running median of

	2.0
	3.0
	2.0  
	1.5  

This would continue in alphabetical order until the all the files in `wc_input` have been processed.  For simiplicity, you may assume that all the text files are lowercase.

* *Do I need to use MapReduce or Hadoop?*  
No, while you should make sure the algorithms you use scale for larger text files, you do not need to use Hadoop or the MapReduce programming paradigm.  






