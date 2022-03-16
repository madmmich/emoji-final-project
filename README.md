# emoji-final-project
Ling-144 Final Project on brand emoji usage

This repository includes the code and datasets used for each company I skimmed tweets from.

The method used for skimming was **snscrape** and for filtering the tweets to contain only emoji's was **emoji** and **regex**.

The files are split into 2 folders, **code** and **data**:

1. **emoji-count-brand.py** which contains the code for counting emojis from each brand
2. **snscrape-filter-brand.py**, which contains the scraping and filter code for each brand that enabled me to look at tweets with only emojis
  a. the code for tinder is broken into two files, **filter-code-tinder.py** and **snscrape-code-tinder.py**
3. for the **data folder**, there are 2 separate .csv files for each brand, those being **brand-annotation.csv** and **brand-posneg-count.csv**
