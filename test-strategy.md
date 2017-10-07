The project has been divided up into three parts:

	1. Gathering and validating input parameters.
	2. Fetching tweet data based on on input parameters.
	3. Processes the tweet data to output a frequency table of words.

1. Gathering and validating input parameters.
	
	Here, our testing strategies comprised of utilising domain testing, adhoc/exploratory testing and utilising
	branch/mcdc/path coverage testing. We will describe how we tested for each input parameter below:

		search_text: Divided the input domain into 3 equivalent partitions (non-empty alpha, non-empty non-alpha and empty)
		and simply tested one input from each partition.

		max_num_tweets: First divided input domain into 2 partitions (non-numbers of numbers). We tested for
		non-number but then realised the numbers partition can be divided up further using domain testing.
		So the numbers partition was broken down to valid numbers (0 <= max_num_tweets <= 500) and invalid numbers (<0 and >500).
		We simply tested for 1 input from each of these partitions.

		all tokens: Divided input domain into existence of tokens and non-existence of tokens (i.e null). We tested on each 
		parition with one input.

		top_t_words: First divided input domain into 2 partitions (non-numbers of numbers). We tested for
		non-number but then realised the numbers partition can be divided up further using domain testing.
		So the numbers partition was broken down to valid numbers (top_t_words >= 0) and invalid numbers (top_t_words < 0).
		We simply tested for 1 input from each of these partitions.

		min_word_count: First divided input domain into 2 partitions (non-numbers of numbers). We tested for
		non-number but then realised the numbers partition can be divided up further using domain testing.
		So the numbers partition was broken down to valid numbers (min_word_count >= 0) and invalid numbers (min_word_count < 0).
		We simply tested for 1 input from each of these partitions.



	All of the above aims to achieve 100% statement and branch coverage within each method of the setter methods.
		