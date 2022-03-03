import pandas
import emoji
import re
import csv

tinder = pandas.read_csv('user-tweets-tinder.csv', encoding = 'utf-8')
column = tinder.renderedContent
content = column.tolist()

new_content = list(dict.fromkeys(content))
# print(len(new_content))

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
print(len(complete))

tweetDataframe = pandas.DataFrame(complete)
tweetDataframe.to_csv('skimmed-tweets-tinder.csv', header=["Tweets Tinder"], index=False)
