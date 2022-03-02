import csv

tinder-tweets = open('user-tweets-tinder.csv', 'r')
emoji-tweets = csv.DictReader(tinder-tweets)
tweet-content = []

for col in emoji-tweets:
    tweet-content.append(col['month_number']) 
print('Tweet body:', tweet-content)