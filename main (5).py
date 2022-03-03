import os
import pandas as pd
# import csv
import snscrape

tweet_count = 100
username = "lacroixwater"

# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --max-results {} twitter-search 'from:{}'> user-tweets-lacroixwater.json".format(tweet_count, username))
# Reads the json generated from the CLI command above and creates a pandas dataframe
tweets_df1 = pd.read_json('user-tweets-lacroixwater.json', lines=True)

# Displays first 5 entries from dataframe
tweets_df1.head()

tweets_df1.to_csv('user-tweets-lacroixwater.csv', sep=',', index=False)

import emoji
import re
import csv
import pandas

lacroixwater = pandas.read_csv('user-tweets-lacroixwater.csv', encoding = 'utf-8')
column = lacroixwater.renderedContent
content = column.tolist()

new_content = list(dict.fromkeys(content))
print(len(new_content))

sample_list = new_content
new_list = []
for element in sample_list:
  new_list.append(element.replace(":", ""))
# print(new_list)

holder = []
for element in new_list:
    holder.append(emoji.demojize(element))
holder2 = holder
print(len(holder2))
print(holder)

skim = []
for phrase in holder:
    if bool(re.findall(r'(:[^:]*:)', phrase)) == True:
        skim.append(phrase)
skim2 = skim
print(len(skim2))

complete = []
for part in skim:
    complete.append(emoji.emojize(part))
complete2 = complete
print(complete)
print(len(complete2))

tweetDataframe = pandas.DataFrame(complete)
tweetDataframe.to_csv('skimmed-tweets-lacroixwater.csv', header=["Tweets La Croix"], index=False)