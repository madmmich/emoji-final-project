import os
import pandas as pd
import csv
import snscrape

tweet_count = 100
username = "tinder"

# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets.json".format(tweet_count, username))
# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df1 = pd.read_json('user-tweets-tinder.json', lines=True)

# Displays first 5 entries from dataframe
tweets_df1.head()

tweets_df1.to_csv('user-tweets-tinder.csv', sep=',', index=False)