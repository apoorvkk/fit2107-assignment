# FIT2107 Assignment 3 - Unit and Integration Testing

Apoorv Kansal - akan57, 27821455 <br>
Matthew Sturgeon - mjstu3, 27833380

## Overview
The project has been divided up into two parts:

**1.** Gathering and validating input parameters inside a class. <br>
**2.** Fetching tweet data and processing the tweet data to output a frequency table of words.

**Note:** We have made assumptions about various input variables. These have been outlined in the source code (see ```tweet_analyser.py```).

### Task 1 - Gathering and validating input parameters.
Across all of the input variables tested, we mainly used domain testing (blackbox) and branch/statement and mc/dc coverage testing. Domain testing was used because we wanted to ensure boundaries of all input data (eg. min word count, top t words etc.) were working as expected. The boundaries of any input domain is usually where most bugs are found. Statement coverage was used to ensure that the tests were hitting every single line of the source code written. Branch coverage was used to consider various decisions that the algorithm might go through and hence we should have test for each of those decisions to ensure they working as expected. MC/DC testing was used because we wanted to see how each variable can affect the overall outcome in each setter method. However, most input variables only had singular conditions in their conditional statements so mc/dc coverage turned out to not be as effective as standard branch and statement coverage. 

**search_text:** Divided the input domain into 3 equivalent partitions (non-empty alpha, non-empty non-alpha and empty)
and simply tested one input from each partition.

**max_num_tweets:** First divided input domain into 2 partitions (non-numbers of numbers). We tested for
non-number but then realised the numbers partition can be divided up further using domain testing.
So the numbers partition was broken down to valid numbers (0 <= max_num_tweets <= 500) and invalid numbers (<0 and >500).
We simply tested for 1 input from each of these partitions.

**all tokens:** Divided input domain into existence of tokens and non-existence of tokens (i.e null). We tested on each
partition with one input.

**to_date:** Utilised a combination of mc/dc/branch/statement coverage and domain testing. Essentially, we tested to cover all branches and made sure each variable in the conditional statements had an overall impact to the outcome of the method. Also, because we were using date ranges (eg. comparing against today's date and from_date), we used domain testing to test on and off boundaries. These two strategies fairly overlapped.

**from_date:** Similar to to_date except we did not compare date ranges with to_date.

**twitter_user_id:** We tested for empty twitter id (which is valid) and then for an invalid string (eg. does not start with @).
We also tested for a valid twitter id (starts with an @).

**top_t_words:** First divided input domain into 2 partitions (non-numbers of numbers). We tested for
non-number but then realised the numbers partition can be divided up further using domain testing.
So the numbers partition was broken down to valid numbers (top_t_words >= 0) and invalid numbers (top_t_words < 0).
We simply tested for 1 input from each of these partitions.

**min_word_count:** First divided input domain into 2 partitions (non-numbers of numbers). We tested for
non-number but then realised the numbers partition can be divided up further using domain testing.
So the numbers partition was broken down to valid numbers (min_word_count >= 0) and invalid numbers (min_word_count < 0).
We simply tested for 1 input from each of these partitions.

All of the above aims to achieve as close as possible to 100% statement and branch coverage within each method of the setter methods. This was considered when dividing up all the partitions as most partitions covered a particular branch and set of statements.

#### Digression: Looking at blackbox testing techniques
In addition to these whitebox testing techniques, we tried some blackbox techniques such as category partitioning with Jenny. We did this because we wanted to try a variety of testing strategies and see what worked best. Using category partitioning allowed us to think laterally and consider a wide number of test cases. To do this, we first defined our categories and choices as below:

**Note:** We have reduced the 4 token categories into 1 because we know that all tokens must be supplied for authentication to succeed. If even just 1 token is
incorrect or is missing, we know the program will not authenticate successfully with the Twitter API. In this way, the program will fail homogeneously over the 4 token categories. Reducing number of categories also helps us to test more parameters rigorously even with a limited set of test cases.

**1.** Search text: empty, valid alphabet string, invalid non-alphabet string <br>
**2.** Max results: empty, less than 0 , 0 <= m <= 500, >500, non-number <br>
**3.** Auth tokens: correct, incorrect <br>
**4.** From date: empty, invalid date form, > today’s date, <= today’s date <br>
**5.** To date: empty, invalid date form, >today’s date + no from date, <= today’s date + no from date,  <= from date, > from date <br>
**6.** Twitter user id: empty, valid string with @, invalid string with no @ <br>
**7.** Top t words: empty, <0, >=0, non-number <br>
**8.** Minimum word count: empty, <0, >=0, non-number

By utilising Jenny, we computed pairwise combinations with this command: <br>
```N2: ./jenny.out -n2 3 5 2 4 6 3 4 4```

This outputted this combinations (we have written the expected behaviour next to each one): <br>
1a 2a 3b 4d 5b 6b 7d 8c	- Error on search text  (empty) <br>
1b 2d 3a 4b 5e 6c 7b 8b - Error on max number of tweets (>500) <br>
1c 2e 3a 4a 5c 6a 7c 8d - Error on search text (invalid non-alphabet string) <br>
 1b 2b 3b 4c 5a 6a 7a 8a - Auth tokens incorrect <br>
 1a 2c 3a 4a 5d 6b 7a 8a - Error on search text (empty) <br>
 1c 2c 3b 4b 5f 6c 7d 8d - Error on search text (invalid non-alphabet string) <br>
 1a 2e 3b 4c 5e 6b 7c 8b - Error on search text (empty) <br>
 1b 2b 3a 4d 5f 6c 7c 8c - Error with twitter user id (invalid string with no @) <br>
 1a 2d 3b 4d 5d 6a 7b 8d - Error on search text (empty) <br>
 1b 2a 3a 4c 5c 6c 7d 8a - Error on from date (>today’s date) <br>
 1a 2e 3a 4b 5a 6c 7a 8c - Error on search text (empty) <br>
 1b 2b 3b 4a 5b 6b 7b 8d - Error on max_num_tweets (less than 0) <br />
 1c 2a 3b 4d 5e 6a 7a 8b - Error on search text (invalid non-alphabet string) <br>
 1c 2d 3b 4c 5c 6b 7b 8c - Error on search text (invalid non-alphabet string) <br>
 1c 2c 3a 4b 5b 6a 7c 8b - Error on search text (invalid non-alphabet string) <br>
 1c 2a 3b 4b 5a 6b 7c 8d - Error on search text (invalid non-alphabet string) <br>
 1b 2b 3a 4a 5d 6c 7d 8b - Error on max_num_tweets (less than 0) <br>
 1a 2e 3b 4d 5f 6b 7b 8a - Error on search text (empty) <br>
 1b 2c 3b 4a 5e 6a 7d 8c - Auth tokens incorrect <br>
 1c 2d 3a 4b 5b 6c 7a 8a - Error on search text (invalid non-alphabet string) <br>
 1b 2c 3a 4d 5a 6b 7b 8b - Error on negative minimum count <br>
 1a 2b 3a 4b 5c 6a 7a 8b - Error on search text (empty) <br>
 1c 2e 3a 4c 5d 6a 7c 8c - Error on search text (invalid non-alphabet string) <br>
 1b 2e 3b 4c 5f 6a 7a 8d - Error on maximum number of tweets - non-number <br>
 1c 2d 3b 4a 5a 6a 7d 8a - Error on search text (invalid non-alphabet string) <br>
 1b 2a 3a 4a 5f 6a 7b 8b - Empty max num tweets <br>
 1c 2b 3b 4a 5e 6c 7d 8d - Error on search text (invalid non-alphabet string) <br>
 1a 2c 3a 4d 5c 6a 7c 8a - Error on search text (empty) <br>
 1c 2d 3a 4b 5f 6b 7c 8d - Error on search text (invalid non-alphabet string) <br>
 1c 2e 3b 4c 5b 6a 7d 8b - Error on search text (invalid non-alphabet string) <br>
 1b 2a 3a 4b 5d 6b 7c 8a - Error on max number of tweets <br>
 1c 2c 3a 4c 5e 6c 7a 8a - Error on search text (invalid non-alphabet string) <br>

**Note: ** "1c" means Category 1 (Search text) and 3rd choice (invalid non-alphabet string). <br>

Because all of the above testcases have already been covered by the existing test cases that were produced via rigorous white box testing techniques (eg. Branch, statement coverage etc. and also with domain testing which is blackbox), we have decided to omit these test cases. These cases represent failed cases on specific parameters (where other parameters did not have any effect on the overall failure) which have already been created for each variable.


### Task 2 - Fetching tweet data and processing the tweet data to output a frequency table of words.
