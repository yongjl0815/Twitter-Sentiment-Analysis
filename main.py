
import nltk
import csvextract
import extractTestTweet


#make above lists to tuples in list
tweets = []
for (words, sentiment) in arrayC:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 4]
    tweets.append((words_filtered, sentiment))

#get words only into all_words
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

#get distinct words into word_features with most common ones first
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_order = wordlist.most_common()
    word_features = []
    for a in word_order:
        word_features.append(a[0])
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))

#feature extractor
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

def check():
    positive_number = 0
    negative_number = 0
    for i in tweet_data:
        if classifier.classify(extract_features(i.split())) == 'positive':
            positive_number = positive_number +1
        if classifier.classify(extract_features(i.split())) == 'negative':
            negative_number = negative_number +1
    print ('Positive : ' , positive_number)
    print ('Negative : ' , negative_number)

check()






