
import tweet_analyser
import datetime
import tweepy
import unittest
from unittest import mock

class TestInputParams(unittest.TestCase):
    '''
    The following tests are for input parameters and validating their data. These tests only check if data is being validated.
    '''

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
    
    def test_max_num_tweets_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "search", None, "token", "token", "token", "token", 
            None, None, "@random_id", 10, 10)
        self.assertEqual(t_analyser.max_num_tweets, 100)

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
        self.assertEqual(t_analyser.to_date.date(), datetime.datetime.now().date())

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
        self.assertEqual(t_analyser.from_date, datetime.datetime(2006, 3, 21)) # Default date is when Twitter was established.

    def test_from_date_invalid_format(self):
        with self.assertRaises(ValueError):
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, "token", "token", "token", "token", 
                "invalid from date", None, None, 10, 10)

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
        self.assertEqual(t_analyser.twitter_user_id, "random_id")
    
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

    def test_top_t_words_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "search", 100, "token", "token", "token", "token", 
            None, None, "@random_id", None, 10)
        self.assertEqual(t_analyser.top_t_words, 10)

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

    def test_min_word_count_empty(self):
        t_analyser = tweet_analyser.TweetAnalyser(
            "search", 100, "token", "token", "token", "token", 
            None, None, "@random_id", 10, None)
        self.assertEqual(t_analyser.min_word_count, 0)


# Used by test cases as EXAMPLE ONLY tokens (not real).
app_access_token = 'exp_token_5IPDWOouY8WrjRMLZVgC9XD9w'
app_access_token_secret = 'exp_token_pqyXj72rd6K0v6P6Kt38cRDGVMvcmevSk85r3aFbPxtIAzCMiR'
user_access_token = 'exp_token_3787840280-Wg6dj7ik8AgRTCVy1myE5uvx9YF7rUy1IJObEEV'
user_access_token_secret = 'exp_token_uTNYs4M7hyfv5IpV6Dz603xLDcveYQ12gAfNDFilx6u4S'


@mock.patch('tweepy.OAuthHandler')
@mock.patch('tweepy.OAuthHandler.set_access_token')
@mock.patch('tweepy.API')
@mock.patch("tweepy.Cursor")
class TestAnalyseTweets(unittest.TestCase):
    '''
    The following tests are used to actually test the bulk of the program that would actually access Twitter.
    We have mocked out network access and therefore, there is no real communication with Twitter. We have assumed
    what Twitter will return.
    '''

    def test_search_text_valid(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
                    [
                        mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                        mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
                    ],

                    [
                        mock.Mock(text = "Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                        mock.Mock(text = "Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
                    ]
            ]

        t_analyser = tweet_analyser.TweetAnalyser(
            "the", None, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, None, None)

        frequencies = t_analyser.analyse_tweets()

        found = False
        for item in frequencies:
            if item[0] == t_analyser.search_text:
                found = True
                break
        self.assertEqual(found, False)

    def test_search_text_match(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
                    [
                        mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                        mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
                    ],

                    [
                        mock.Mock(text = "Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                        mock.Mock(text = "Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
                    ]
            ]

        t_analyser = tweet_analyser.TweetAnalyser(
            "Hello", None, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, None, None)

        frequencies = t_analyser.analyse_tweets()
        found = False
        for item in frequencies:
            if item[0] == t_analyser.search_text:
                found = True
                break
        self.assertEqual(found, False)

    def test_max_num_tweets_zero(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
            [
                mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
            ],

            [
                mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
            ]
        ]
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 0, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, None, None)
        frequencies = t_analyser.analyse_tweets()
        self.assertEqual(frequencies, [])

    def test_tweets_matching(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
            [
                mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
            ] * 105
        ]
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 203, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, None, None)
        frequencies = t_analyser.analyse_tweets()
        matching = False
        expected = [('Hello', 102), ('my', 102), ('name', 102), ('is', 102), ('About', 101),
                             ('to', 101), ('blow', 101), ('up', 101), ('NK', 101), ('Donald', 101)]
        for i in range(len(frequencies)):
            matching = False
            for j in range(len(expected)):
                if frequencies[i][0] == expected[j][0]:
                    matching = True
                    del expected[j]
                    break
            if matching is False:
                break
        self.assertTrue(matching)

    def test_max_num_tweets_exceeded(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
            [
                mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
            ],

            [
                mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
            ]
        ]
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 1, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, None, None)
        frequencies = t_analyser.analyse_tweets()
        self.assertEqual(len(frequencies), 4)
        
    def test_tweets_ordered(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
            [
                mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
            ] * 105
        ]
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 203, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, None, None)
        frequencies = t_analyser.analyse_tweets()
        ordered = True
        for i in range(len(frequencies)-1):
            if frequencies[i][1] < frequencies[i+1][1]:
                ordered = False
        self.assertTrue(ordered)

    def test_app_access_token_invalid(self, cursor, api, access_token, oauth):
        with self.assertRaises(tweepy.error.TweepError):
            cursor.return_value.pages.return_value = pages = [
                [
                    mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
                ],

                [
                    mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
                ]
            ]
            api.side_effect = tweepy.error.TweepError(reason="access token invalid")
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, app_access_token, app_access_token_secret, user_access_token,
                user_access_token_secret, None, None, None, None, None)
            frequencies = t_analyser.analyse_tweets()

    def test_app_access_token_secret_invalid(self, cursor, api, access_token, oauth):
        with self.assertRaises(tweepy.error.TweepError):
            cursor.return_value.pages.return_value = pages = [
                [
                    mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
                ],

                [
                    mock.Mock(text="Dr. Merkel is awesome!",created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
                ]
            ]
            api.side_effect = tweepy.error.TweepError(reason="access token secret invalid")
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, app_access_token, app_access_token_secret, user_access_token,
                user_access_token_secret, None, None, None, None, None)
            frequencies = t_analyser.analyse_tweets()

    def test_user_access_token_invalid(self, cursor, api, access_token, oauth):
        with self.assertRaises(tweepy.error.TweepError):
            cursor.return_value.pages.return_value = pages = [
                [
                    mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
                ],

                [
                    mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
                ]
            ]
            api.side_effect = tweepy.error.TweepError(reason="user access token invalid")
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, app_access_token, app_access_token_secret, user_access_token,
                user_access_token_secret, None, None, None, None, None)
            frequencies = t_analyser.analyse_tweets()

    def test_user_access_token_secret_invalid(self, cursor, api, access_token, oauth):
        with self.assertRaises(tweepy.error.TweepError):
            cursor.return_value.pages.return_value = pages = [
                [
                    mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
                ],

                [
                    mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                    mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
                ]
            ]
            api.side_effect = tweepy.error.TweepError(reason="user access token secret invalid")
            t_analyser = tweet_analyser.TweetAnalyser(
                "searchtext", 10, app_access_token, app_access_token_secret, user_access_token,
                user_access_token_secret, None, None, None, None, None)
            frequencies = t_analyser.analyse_tweets()

    def test_twitter_user_id_given(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
            [
                mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
            ],

            [
                mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
            ]
        ]
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, "@Fred", None, None)
        frequencies = t_analyser.analyse_tweets()
        self.assertEqual(len(frequencies), 10)

    def test_top_t_words_zero(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
            [
                mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2016, 9, 9))
            ],

            [
                mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="Monash University 243546576879809", created_at=datetime.datetime(2016, 9, 9))
            ]
        ]
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, 0, None)
        frequencies = t_analyser.analyse_tweets()
        self.assertEqual(frequencies, [])

    def test_top_t_words_not_supplied(self, cursor, api, access_token, oauth):
        cursor.return_value.pages.return_value = pages = [
            [
                mock.Mock(text="Hello my name is Fred.", created_at=datetime.datetime(2012, 9, 9)),
                mock.Mock(text="About to blow up NK - Donald Trump.", created_at=datetime.datetime(2011, 1, 9))
            ],

            [
                mock.Mock(text="Dr. Merkel is awesome!", created_at=datetime.datetime(2016, 9, 9)),
                mock.Mock(text="Monash University 243546576879809",created_at=datetime.datetime(2014, 10, 9))
            ]
        ]
        t_analyser = tweet_analyser.TweetAnalyser(
            "searchtext", 10, app_access_token, app_access_token_secret, user_access_token, user_access_token_secret,
            None, None, None, None, None)
        frequencies = t_analyser.analyse_tweets()
        self.assertEqual(len(frequencies), 10)


if __name__ == '__main__':
    unittest.main()
