import pandas
import csv
import emoji
import re

pos_emoji = pandas.read_csv('skimmed-tweets-lacroixwater.csv', encoding = 'utf-8')

pos_emoji = open("skimmed-tweets-lacroixwater.csv", "r")
emoji_tweets = csv.DictReader(pos_emoji)

tweet_content = []

for col in emoji_tweets:
    tweet_content.append(col['Tweets La Croix']) 
print('Tweet body:', tweet_content)

emoji_form = []
for element in tweet_content:
    emoji_form.append(emoji.demojize(element))


only_emoji = []
emojis_one = r'(:[^:]*:)'
for phrase in emoji_form:
  only_emoji.append(re.findall(emojis_one, phrase))

emoji_string2 = []
for element in only_emoji:
  emoji_string2.append(" ".join(element))

emoji_string2 = [y for x in emoji_string2 for y in x.split(' ')]

emoji_string_down = list(dict.fromkeys(emoji_string2))
print(emoji_string_down)



emoji_dict = {i:emoji_string2.count(i) for i in emoji_string2}
emoji_dict2 = emoji_dict
print(emoji_dict2)
emoji_count = []
for key in emoji_dict:
  emoji_count.append(emoji_dict[key])
print(emoji_dict)

full_file = open("emoji_count_lacroixwater.csv", "w")

writer = csv.writer(full_file)
for key, value in emoji_dict.items():
    writer.writerow([key, value])

full_file.close()

negative_emoji = '☹', '😷', '🤒', '🤕', '🤢', '🤮', '🤧', '🥵', '🥶', '🥴', '🤯', '😕', '😟', '🙁', '☹️', '😮', '😯', '😲', '😳', '🥺', '😦', '😧', '😨', '😰', '😥', '😢', '😭', '😱', '😖', '😣', '😞', '😓', '😩', '😫', '🥱', '😤', '😡', '😠', '🤬', '😈', '👿', '💀', '☠️', '😬', '😵'
neg_demojize = []  
for i in negative_emoji:
  neg_demojize.append(emoji.demojize(i))
print(neg_demojize)

maybe_new_count = []
count = 0
for y, k in emoji_dict.items():
  for element in neg_demojize:
    if element == y:
      count = count + k
    else:
      pass
maybe_new_count.append(count)
print(maybe_new_count)

maybe_new = []
for y, k in emoji_dict.items():
  for element in neg_demojize:
    if element == y:
      maybe_new.append([y, k])
  else:
    pass
print(maybe_new)


positive_emoji = '😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂', '🙂', '🙃', '😉', '😊', '😇', '🥰', '😍', '🤩', '😘', '😗', '☺️', '😚', '😙', '🥲', '😋', '😛', '😜', '🤪', '😝', '🤗', '🤑', '😎', '😌', '🤤', '☺'

pos_demojize = []
for p in positive_emoji:
  pos_demojize.append(emoji.demojize(p))
print(pos_demojize)

else_new_count = []
counter = 0
for y, k in emoji_dict.items():
  for element in pos_demojize:
    if element == y:
      counter = counter + k
    else:
      pass
else_new_count.append(counter)
print(else_new_count)

else_new = []
for y, k in emoji_dict.items():
  for element in pos_demojize:
    if element == y:
      else_new.append([y, k])
  else:
    pass
print(else_new)
else_new.append(else_new_count)
# else_list = else_new.split(" ")

print(else_new)


from csv import writer
from csv import reader
with open('emoji_count_lacroixwater.csv', 'r') as read_obj, \
        open('updated_emoji_lacroixwater.csv', 'w', newline='') as write_obj:
    csv_reader = reader(read_obj)
    csv_writer = writer(write_obj)
    for row in csv_reader:
        row.append(maybe_new)
        csv_writer.writerow(row)
        row.append(else_new)
        csv_writer.writerow(row)