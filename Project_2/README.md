# Project 2
Folder dedicated to all programs related to project 2 for EC601

# Objective
Use the Twitter API to gather tweets from the most popular stock trading Twitter users, as well as comments on these tweets. 
Then use the Google NLP to analyze the posts and comments to determine the sentiment towards the most popular stocks of the day/week/month.
If there is extra time, compare the sentiments on a given stock to the price change following the sentiment calculation.
How accurate was the sentiment? Is there a connection to the price of the stock?

# Twitter API Testing
For Phase 1a I tested 3 programs related to the twitter API:
(1) pull any users information such as account creation date, username, time since last tweet, etc
(2) get recent tweets from a user, the exact timeframe can be selected
(3) count the number of recent tweets from a user. timeframe can be selected

Next Steps: 
---> Learn how to gather tweets from a specific hashtags
---> Find most popular users related to stock trading and investing
---> Continue experimenting with filtering techniques
---> Determine how to export tweet and comment information into a format that can be used by the NLP API

# Google Natural Language API Testing
For Phase 1b I tested 2 programs related to the Google NLP API:
(1) Sentiment Analysis: Given a string of text analyze the overall sentiment of the message (is the message positive or negative?
(2) Entity Analysis: Given a string of text find the proper nouns (such as cities, names, addresses, etc) and determine how relevvant it is to the message.

Next Steps:
---> Learn how to import a text file to automatically give the NLP API a string of text to analyze
---> Update program to parse a large text file into individual sentences and return a sentiment score per sentence, rather than for entire text file.
---> Tweek program to only care about stock mentions
