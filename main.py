import argparse
import datetime
import tweet_analyser

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Tweet retriever. We retrieve tweets and parse and sort data based on frequency excluding the given search string.")

	parser.add_argument("-s", help="Words retrieved from Twitter will be ignored if it is in the search string. This is required.", type=str)
	parser.add_argument("-m", help="Determines how many tweets will be retrieved. No more than 500 tweets can be retrieved.", type=int, default=100)
	parser.add_argument("-o", help="A Twitter application access token (required to access the Twitter API).", type=str)
	parser.add_argument("-p", help="The application access token secret (required to access the Twitter API).", type=str)
	parser.add_argument("-u", help="The user's application access token.", type=str)
	parser.add_argument("-x", help="The user's access token secret.", type=str)
	parser.add_argument("-a", help="Include results only from the given DATE. Specified as YYYY-MM-DD.", type=str)
	parser.add_argument("-b", help="Include results only until the given DATE. Specified as YYYY-MM-DD.", type=str)
	parser.add_argument("-i", help="An id of a specific twitter user to analyse. Should start with @ sign.", type=str)
	parser.add_argument("-t", help="List at most the top T words in the set.", type=int, default=10) # ASSUMPTION: argument is -T.
	parser.add_argument("-c", help="Only list words that occur the given minimum count or more times.", type=int)
	
	args = parser.parse_args()
	
	t_analyser = tweet_analyser.TweetAnalyser(args.s, args.m, args.o, args.p, args.u, args.x, args.a, args.b, args.i,
		args.t, args.c)

	frequency_table = t_analyser.analyse_tweets()

	for item in frequency_table:
		total = str(item[1])
		if len(total) == 1:
			total = "0" + total
		print(total + "    " + item[0])
	







