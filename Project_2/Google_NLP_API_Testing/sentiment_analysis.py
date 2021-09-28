def run_quickstart():
 
    from google.cloud import language_v1

    # Instantiates a client. Input key file path on computer
    client = language_v1.LanguageServiceClient.from_service_account_json(r"C:\Users\212765608\Documents\Boston University\EC601\creds.json")

    # [END language_python_migration_client]

    # The text to analyze
    text = u"It is a wonderful day"
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    print("Text: {}".format(text))
    print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
    # [END language_quickstart]


if __name__ == "__main__":
    run_quickstart()
    
