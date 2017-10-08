The project has been divided up into two parts:

	1. Gathering and validating input parameters.
	2. Fetching tweet data and processing the tweet data to output a frequency table of words.

1. Gathering and validating input parameters.
	
	Here, our testing strategies comprised of utilising domain testing and
	branch/path coverage testing. We will describe how we tested for each input parameter below:

		search_text: Divided the input domain into 3 equivalent partitions (non-empty alpha, non-empty non-alpha and empty)
		and simply tested one input from each partition.

		max_num_tweets: First divided input domain into 2 partitions (non-numbers of numbers). We tested for
		non-number but then realised the numbers partition can be divided up further using domain testing.
		So the numbers partition was broken down to valid numbers (0 <= max_num_tweets <= 500) and invalid numbers (<0 and >500).
		We simply tested for 1 input from each of these partitions.

		all tokens: Divided input domain into existence of tokens and non-existence of tokens (i.e null). We tested on each 
		parition with one input.

		to_date: Utilised a combination of mc/dc coverage and domain testing here. Essentially, we tested to cover all branches
		and made sure each variable in the conditional statements had an overall impact to the outcome of the method. Also, because we 
		were using date ranges (eg. comparing against today's date and from_date), we used domain testing to test on and off boundaries.
		These two strategies fairly overlapped. 

		from_date: Similar to to_date except we did not compare date ranges with to_date.
		
		twitter_user_id: We tested for empty twitter id (which is valid) and then for an invalid string (eg. does not start with @).
		We also tested for a valid twitter id (starts with an @). 

		top_t_words: First divided input domain into 2 partitions (non-numbers of numbers). We tested for
		non-number but then realised the numbers partition can be divided up further using domain testing.
		So the numbers partition was broken down to valid numbers (top_t_words >= 0) and invalid numbers (top_t_words < 0).
		We simply tested for 1 input from each of these partitions.

		min_word_count: First divided input domain into 2 partitions (non-numbers of numbers). We tested for
		non-number but then realised the numbers partition can be divided up further using domain testing.
		So the numbers partition was broken down to valid numbers (min_word_count >= 0) and invalid numbers (min_word_count < 0).
		We simply tested for 1 input from each of these partitions.



	All of the above aims to achieve 100% statement and path coverage within each method of the setter methods. **** <- needs to be explained.
		