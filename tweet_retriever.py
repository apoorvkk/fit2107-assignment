import argparse
import datetime
import sys


def input_twitter_params():
	'''
	Collect parameters needed to retrieve and parse tweets from the user. 
	'''
	parser = argparse.ArgumentParser(description="Tweet retriever. We retrieve tweets and parse and sort data based on frequency excluding the given search string.")

	parser.add_argument("-s", help="Words retrieved from Twitter will be ignored if it is in the search string. This is required.", type=str)
	parser.add_argument("-m", help="Determines how many tweets will be retrieved. No more than 500 tweets can be retrieved.", type=int, default=100)
	parser.add_argument("-o", help="A Twitter application access token (required to access the Twitter API).", type=str)
	parser.add_argument("-p", help="The application access token secret (required to access the Twitter API).", type=str)
	parser.add_argument("-t", help="The user's application access token.", type=str)
	parser.add_argument("-x", help="The user's access token secret.", type=str)

	parser.add_argument("-a", help="Include results only from the given DATE. Specified as YYYY-MM-DD.", type=str, default=datetime.datetime.now().strftime("%Y-%m-%d"))
	parser.add_argument("-b", help="Include results only until the given DATE. Specified as YYYY-MM-DD.", type=str, default=datetime.datetime.now().strftime("%Y-%m-%d"))
	parser.add_argument("-i", help="An id of a specific twitter user to analyse. Should start with @ sign.", type=str)
	parser.add_argument("-T", help="List at most the top T words in the set.", type=int, default=10) # ASSUMPTION: argument is -T.
	parser.add_argument("-c", help="Only list words that occur the given minimum count or more times.", type=int)

	return parser.parse_args()

if __name__ == "__main__":
	args = input_twitter_params()
	
	search_text = args.s
	num_tweets = args.m
	app_access_token = args.o
	app_access_token_secret = args.p
	user_access_token = args.t
	user_access_token_secret = args.x
	from_date = args.a
	to_date = args.b
	twitter_user_id = args.i
	top_t_words = args.T
	min_word_count = args.c

	# Validate search string (-s).
	if not search_text: # ASSUMPTION: Search text cannot be empty. 
		print("Please provide a search text.")
		sys.exit()
	#if not search_text.is_alpha(): # ASSUMPTION: Search text cannot be empty. 




