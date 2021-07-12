#import nltk, scipy, numpy, matplotlib, pandas
import nltk
import re 
import string
import matplotlib.pyplot as plt
import random
from nltk import tokenize

from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

print(nltk.download('twitter_samples'))

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

print('Number os Positive tweets : ' ,len(all_positive_tweets))
print('Number os negative tweets : ' ,len(all_negative_tweets))

print('\nThe Type of All The Positive Tweets is : ', type(all_positive_tweets))
print('The Type of All Negative Tweets is : ', type(all_negative_tweets[0]))

#========================================================================================

# fig = plt.figure(figsize = (5,5))
# labels = 'ML-BSB-LAC','ML-HAP-LAC','ML-HAP-LAB'
# sizes =[40,35,25]

# plt.pie(sizes,labels=labels,autopct='%.2f%%',shadow=True,startangle=90)

# plt.axis('equal')

# plt.show()

#====================================================================================

# fig = plt.figure(figsize = (5,5))
# labels = 'Positive','Negative'
# sizes =[len(all_positive_tweets),len(all_negative_tweets)]

# plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)

# plt.axis('equal')

# plt.show()

#====================================================================================
#Looking at raw texts

#positive in green
print('\033[91m' + all_positive_tweets[random.randint(0,5000)])

#negatives are in red
print('\033[92m' + all_negative_tweets[random.randint(0,5000)])

tweet = all_positive_tweets[2277]
print(tweet)

print(nltk.download('stopwords'))

print('\033[92m' + tweet)
print('\033[94m')

tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

tweet2 = re.sub(r'#', '', tweet2)
print('tweet2 : ' + tweet2)
print()
print('\033[92m' + tweet2)
print('\033[94m')

tokenizer = TweetTokenizer(preserve_case=False)
tweet_tokens = tokenizer.tokenize(tweet2)

print()
print('Tokenized String:')
print(tweet_tokens)

stopwords_english = stopwords.words('english')
print('stop words \n')
print(stopwords_english)
print('\npunctuation\n')
print(string.punctuation)

print()
print('\033[92m')
print(tweet_tokens)
print('\033[94m')

tweets_clean = []

for word in tweet_tokens:
    if(word not in stopwords_english and word not in string.punctuation):
        tweets_clean.append(word)

print('removed stopwords and punctuations:')
print(tweets_clean)

print()
print('\033[92m')
print(tweets_clean)
print('\033[94m')

stemmer = PorterStemmer()
tweet_stem = []

for word in tweets_clean:
    stem_word = stemmer.stem(word)
    tweet_stem.append(stem_word)

print('stemmed words:')
print(tweet_stem)


print()
print('\033[92m')
print(tweets_clean)
print('\033[94m')

stemmer = PorterStemmer()
tweet_stem = []

for word in tweets_clean:
    stem_word = stemmer.stem(word)
    tweet_stem.append(stem_word)

print('stemmed words:')
print(tweet_stem)




