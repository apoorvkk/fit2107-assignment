import operator
import datetime
class TweetAnalyser:
	'''
	This class is repsonsible for analysing tweet data based on user input data. The class will
	retrieve tweets from the Twitter API and process the data such that it will list most frequently 
	ocurring words in a set of tweets and exclude words that are inside the given search string.
	'''

	def __init__(self, search_text, max_num_tweets, app_access_token, 
		app_access_token_secret, user_access_token, user_access_token_secret, 
		from_date, to_date, twitter_user_id, top_t_words, min_word_count):
		
		self.search_text = search_text
		self.max_num_tweets = max_num_tweets
		self.app_access_token = app_access_token
		self.app_access_token_secret = app_access_token_secret
		self.user_access_token = user_access_token
		self.user_access_token_secret = user_access_token_secret
		self.from_date = from_date
		self.to_date = to_date
		self.twitter_user_id = twitter_user_id
		self.top_t_words = top_t_words
		self.min_word_count = min_word_count


	



	'''
	Simple setter and getter methods for the given input parameters.
	'''
	search_text = property(operator.attrgetter('_search_text')) 
	max_num_tweets = property(operator.attrgetter('_max_num_tweets')) 
	app_access_token = property(operator.attrgetter('_app_access_token')) 
	app_access_token_secret = property(operator.attrgetter('_app_access_token_secret')) 
	user_access_token= property(operator.attrgetter('_user_access_token')) 
	user_access_token_secret = property(operator.attrgetter('_user_access_token_secret')) 
	from_date = property(operator.attrgetter('_from_date')) 
	to_date = property(operator.attrgetter('_to_date')) 
	twitter_user_id = property(operator.attrgetter('_twitter_user_id')) 
	top_t_words = property(operator.attrgetter('_top_t_words')) 
	min_word_count = property(operator.attrgetter('_min_word_count')) 

	@search_text.setter
	def search_text(self, s):
		if s is None: # ASSUMPTION: Search text cannot be empty. 
			raise TypeError("Please provide a search text.")

		if not s.isalpha(): # ASSUMPTION: Search text cannot characters other than letters.
			raise ValueError("Please provide a search text that has letters only.")

		self._search_text = s

	@max_num_tweets.setter
	def max_num_tweets(self, m):
		if m is None: 
			m = 100
		try: 
			m = int(m)
		except (ValueError, TypeError):
			raise TypeError("Ensure that maximum number of tweets is an integer value.")

		if not 0 <= m <= 500: # ASSUMPTION: We are allowing the user to have 0 tweets specified.
			raise ValueError("Ensure that the maximum number of tweets is between 0 and 500 inclusively.")
		self._max_num_tweets = m

	@app_access_token.setter
	def app_access_token(self, a):
		if a is None: # ASSUMPTION: Token cannot be null.
			raise TypeError("Please provide an application access token for Twitter access.")
		self._app_access_token = str(a)

	@app_access_token_secret.setter
	def app_access_token_secret(self, a):
		if a is None: # ASSUMPTION: Token cannot be null.
			raise TypeError("Please provide an application access token secret for Twitter access.")
		self._app_access_token_secret = str(a)

	@user_access_token.setter
	def user_access_token(self, u):
		if u is None: # ASSUMPTION: Token cannot be null.
			raise TypeError("Please provide an user access token for Twitter access.")
		self._user_access_token = str(u)

	@user_access_token_secret.setter
	def user_access_token_secret(self, u):
		if u is None: # ASSUMPTION: Token cannot be null.
			raise TypeError("Please provide an user access token secret for Twitter access.")
		self._user_access_token_secret = str(u)

	@to_date.setter
	def to_date(self, d):
		if d is not None:
			try:
				d = datetime.datetime.strptime(d, '%Y-%m-%d')
			except ValueError:
				raise ValueError("Please input a valid date which is in the format of YYYY-MM-DD.")

		if d is not None and d > datetime.datetime.now():
			raise ValueError("Please input a from date that is not after today.")
		
		if d is not None and self.from_date and d <= self.from_date:
			raise ValueError("Please input a to date that is after the given from date.")
		self._to_date = d

	@from_date.setter
	def from_date(self, d):
		if d is not None:
			try:
				d = datetime.datetime.strptime(d, '%Y-%m-%d')
			except ValueError:
				raise ValueError("Please input a valid date which is in the format of YYYY-MM-DD.")
		if d is not None and d > datetime.datetime.now():
			raise ValueError("Please input a from date that is not after today.")
		self._from_date = d

	@twitter_user_id.setter
	def twitter_user_id(self, i):
		if i is not None:
			i = str(i)
			if i[0] != "@":
				raise ValueError("Please ensure the given twitter user id starts with '@'")
		self._twitter_user_id = i

	@top_t_words.setter
	def top_t_words(self, t):
		if t is None:
			t = 10
		try: 
			t = int(t)
		except (ValueError, TypeError):
			raise TypeError("Ensure that at most number of words is an integer value.")
			
		if t < 0: # ASSUMPTION: top t words must be non-negative integer.
			raise ValueError("Please ensure that that top most words provided is non-negative integer.")
		self._top_t_words = t

	@min_word_count.setter
	def min_word_count(self, c):
		if c is None:
			c = 10
		try: 
			c = int(c)
		except (ValueError, TypeError):
			raise TypeError("Ensure that minimum word count is an integer value.")
			
		if c < 0: # ASSUMPTION: min word count must be non-negative integer.
			raise ValueError("Please ensure minimum word count provided is non-negative integer.")
		self._min_word_count = c









