#%%

## Import libraries
import tweepy
import csv
from matplotlib import pyplot as plt
from google.cloud import language_v1

#### Twitter API ####

## Input your credentials here


def tweets(max_tweets, search_word):

    ck_file = open(r"C:\Users\bobby\Documents\Education\Boston University\EC601\Project 2\consumer_key.txt", "r")
    cs_file = open(r"C:\Users\bobby\Documents\Education\Boston University\EC601\Project 2\consumer_secret.txt", "r")
    at_file = open(r"C:\Users\bobby\Documents\Education\Boston University\EC601\Project 2\access_token.txt", "r")
    as_file = open(r"C:\Users\bobby\Documents\Education\Boston University\EC601\Project 2\access_token_secret.txt", "r")
    
    # Reads .txt files and saves them as strings
    consumer_key = ck_file.read()
    consumer_secret = cs_file.read()
    access_token = at_file.read()
    access_token_secret = as_file.read()
    
    # Close all key/token files
    ck_file.close()
    cs_file.close()
    at_file.close()
    as_file.close()
    
    # Takes the 4 keys to authorize user and connect to API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    

    # # Define columns for csv file
    # header = ['Username', 'Creation Date', 'Tweet Text']
    
    
    # # Open/Create a file to write data
    # csvFile = open(r'C:\Users\bobby\Documents\data.csv','w', encoding='utf-8')
    # csvwriter = csv.writer(csvFile)
    # csvwriter.writerow(header)
    
    
    max_n_tweets = max_tweets # Set the max number of tweets to pull
    tweet_list = [] # Create empty list for tweets
    search_term = search_word # Seperate search terms  with OR, multi-word search terms put in parentheses.
    filters = ' -filter:retweets AND -filter:links' #removes retweets and any tweets with links
    
    # Appends each tweet to a csv file for future viewing
    # Appends each tweet to a list for google NLP
    for tweet in tweepy.Cursor(api.search_tweets,q=search_term+filters, result_type = 'recent',tweet_mode = 'extended', count=15,lang="en").items(max_n_tweets):
        
        # Necessary to get full tweet text for retweeted texts
        if 'retweeted_status' in tweet._json:
            #print(tweet._json['retweeted_status']['full_text'])
            tweet_list.append(tweet._json['retweeted_status']['full_text'])
            #current_tweet = [tweet.user.screen_name, str(tweet.created_at), tweet._json['retweeted_status']['full_text']] 
        else:
            #print(tweet.full_text)
            tweet_list.append(tweet.full_text)
            #current_tweet = [tweet.user.screen_name, str(tweet.created_at), tweet.full_text] 
        
        #csvwriter.writerow(current_tweet)
       
    #csvFile.close()
    
    return tweet_list



#tweet_list = tweets(200, '#BTC')
#%%



#### Google NLP ####
def google(tweet_list):
    # Instantiates a client. Input key file path on computer
    client = language_v1.LanguageServiceClient.from_service_account_json(r"C:\Users\bobby\Documents\Education\Boston University\EC601\creds.json")
    
    sentiment_score = [] # Creates empty list to save sentiment score
    
    # Iterate through each tweet and get a sentiment score
    for i in tweet_list:
        text = i
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        
        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        sentiment_score.append(sentiment.score)
    
    avg_SS = sum(sentiment_score)/len(sentiment_score)
    color_line = '#fc4f30'
    plt.axvline(avg_SS, color = color_line, label = 'Mean Score',linestyle='--')
    
    plt.legend()
    # Plot sentiment score histogram
    bins = [-1,-0.875,-0.75,-0.625, -0.5, -0.375, -0.25,-0.125, 0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75,0.875, 1]
    plt.hist(sentiment_score, bins = bins, color = 'skyblue', edgecolor = 'black')
    
    plt.title('Sentiment Score Histogram')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    return sentiment_score


#google(tweet_list)