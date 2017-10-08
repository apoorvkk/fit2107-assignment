import unittest
import tweet_analyser
import datetime

class TestTweetAnalyserInputParams(unittest.TestCase):

    def test_search_text_empty(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                None, 10, "token", "token", "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_search_text_not_empty_and_alpha(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "a", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.search_text, "a")

    def test_search_text_not_empty_and_not_alpha(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "1", 10, "token", "token", "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_search_text_empty(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                None, 10, "token", "token", "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_max_num_tweets_invalid_num(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", "invalid_max_num_tweets", "token", "token", "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_max_num_tweets_out_of_lower_bounds(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", -1, "token", "token", "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_max_num_tweets_out_of_upper_bounds(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 501, "token", "token", "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_max_num_tweets_in_of_lower_bounds(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 0, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.max_num_tweets, 0)

    def test_max_num_tweets_in_of_upper_bounds(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 500, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.max_num_tweets, 500)
    
    def test_app_access_token_empty(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, None, "token", "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_app_access_token_not_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.app_access_token, "token")

    def test_app_access_token_secret_empty(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", None, "token", "token", 
                None, None, "@random_id", 10, 10)

    def test_app_access_token_secret_not_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.app_access_token_secret, "token")

    def test_user_access_token_empty(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", None, "token", 
                None, None, "@random_id", 10, 10)

    def test_user_access_token_not_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.user_access_token, "token")

    def test_user_access_token_secret_empty(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", None, 
                None, None, "@random_id", 10, 10)

    def test_user_access_token_secret_not_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.user_access_token_secret, "token")

    def test_to_date_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, None, 10, 10)
        self.assertEqual(t_analyser.to_date, None)

    def test_to_date_invalid_format(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                None, "invalid start date", None, 10, 10)

    def test_to_date_after_today_date(self):
        d = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                None, d, None, 10, 10)
    
    def test_to_date_today_date(self):
        d = (datetime.datetime.now().now()).strftime('%Y-%m-%d')
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, d, None, 10, 10)
        self.assertEqual(t_analyser.to_date, datetime.datetime.strptime(d, '%Y-%m-%d'))
    
    def test_to_date_equals_from_date(self):
        d = (datetime.datetime.now()).strftime('%Y-%m-%d')
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                d, d, None, 10, 10)

    def test_to_date_after_from_date(self):
        to_date = (datetime.datetime.now()).strftime('%Y-%m-%d')
        from_date = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime('%Y-%m-%d')
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            from_date, to_date, None, 10, 10)
        self.assertEqual(t_analyser.to_date, datetime.datetime.strptime(to_date, '%Y-%m-%d'))

    def test_from_date_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, None, 10, 10)
        self.assertEqual(t_analyser.from_date, None)

    def test_from_date_invalid_format(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                None, None, "invalid from date", 10, 10)

    def test_from_date_after_today_date(self):
        d = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                d, None, None, 10, 10)
    
    def test_from_date_today_date(self):
        d = (datetime.datetime.now().now()).strftime('%Y-%m-%d')
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            d, None, None, 10, 10)
        self.assertEqual(t_analyser.from_date, datetime.datetime.strptime(d, '%Y-%m-%d'))

    def test_twitter_user_id_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, None, 10, 10)
        self.assertEqual(t_analyser.twitter_user_id, None)

    def test_twitter_user_id_valid(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "a", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.twitter_user_id, "@random_id")
    
    def test_twitter_user_id_invalid(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "a", 10, "token", "token", "token", "token", 
                None, None, "random_id", 10, 10)

    def test_top_t_words_invalid_num(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                None, None, "@random_id", "invalid top t words", 10)

    def test_top_t_words_out_of_bounds(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                None, None, "@random_id", -1, 10)

    def test_top_t_words_in_of_bounds(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 1, 10)
        self.assertEqual(t_analyser.top_t_words, 1)

    def test_min_word_count_invalid_num(self):
        with self.assertRaises(TypeError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                None, None, "@random_id", 10, "invalid min count")

    def test_min_word_count_out_of_bounds(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                None, None, "@random_id", 10, -1)

    def test_min_word_count_in_of_bounds(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, "token", "token", "token", "token", 
            None, None, "@random_id", 1, 1)
        self.assertEqual(t_analyser.min_word_count, 1)


if __name__ == '__main__':
    unittest.main()
