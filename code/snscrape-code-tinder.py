import os
import pandas as pd
import csv
import snscrape

tweet_count = 100
username = "tinder"

os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets.json".format(tweet_count, username))
tweets_df1 = pd.read_json('user-tweets-tinder.json', lines=True)

tweets_df1.head()

tweets_df1.to_csv('user-tweets-tinder.csv', sep=',', index=False)
