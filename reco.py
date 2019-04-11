import boto3
client = boto3.client('comprehend')

ls = []

def sent():
    
    text = input('Please provide us with your feedback below\n\n')
    response = client.detect_sentiment(Text=text,LanguageCode='en')
    sentiment = response['Sentiment']
    ls.append({'sentiment': sentiment, 'text': text})
    if text == 'q':
        ls.pop()
        print('\n\t## Thank you, {} responses have been recorded ###\n'.format(str(len(ls))))
    else:
        sent()
sent()


for ratings in ('POSITIVE', 'NEUTRAL', 'NEGATIVE', 'MIXED'):
    print('=============\n{} reviews\n=============\n\n'.format(ratings.lower()))
    for reviews in range(0,len(ls)):
        if ls[reviews]['sentiment'] == ratings:
            print(ls[reviews]['text']+'\n')
    print('\n\n')
